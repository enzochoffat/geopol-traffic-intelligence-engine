import time
import signal
import sys
from pathlib import Path
from datetime import datetime
import logging
import requests

from src.geopol.ingestion.adsb_ingestor import fetch_flights
from src.geopol.analysis.air_traffic_analyser import compute_basic_metrics
from src.geopol.utils.config_loader import load_config
from src.geopol.utils.paths import CONFIG_PATH
from src.geopol.utils.exceptions import GeopolError, FetchError, ParseError
from src.geopol.storage.csv_store import CsvStore

logger = logging.getLogger(__name__)

# ── Gestion propre du Ctrl+C ──
# Sans ça, Ctrl+C affiche une stacktrace moche
def _handle_exit(sig, frame):
    print("\n[Collector] Arrêt propre. À bientôt.")
    sys.exit(0)

signal.signal(signal.SIGINT, _handle_exit)


def run_collector(config_path: str = CONFIG_PATH):
    """
    Boucle principale de collecte.
    Interroge OpenSky toutes les X secondes et sauvegarde chaque snapshot.
    """
    config   = load_config(config_path)
    zone     = config["zone"]
    interval = config["collection"]["interval_seconds"]
    max_snap = config["collection"]["max_snapshots"]

    print("=" * 50)
    print("  GeoPol — Collecteur temps réel")
    print(f"  Zone     : {zone['name']}")
    print(f"  Intervalle : {interval}s ({interval//60} min)")
    print(f"  Max snapshots : {max_snap}")
    print("  Ctrl+C pour arrêter proprement")
    print("=" * 50)

    store = CsvStore()  # Utilise le stockage CSV par défaut

    snapshot_count = 0
    consecutive_failures = 0
    MAX_FAILURES = 5

    while snapshot_count < max_snap:
        snapshot_count += 1
        now = datetime.now().strftime("%H:%M:%S")

        print(f"\n[{now}] Snapshot #{snapshot_count}/{max_snap}")

        try:
            # ── Collecte ──
            flights = fetch_flights(
                lat_min=zone["lat_min"],
                lon_min=zone["lon_min"],
                lat_max=zone["lat_max"],
                lon_max=zone["lon_max"],
            )

            if not flights:
                logger.info("[Collector] Snapshot vide, on continue.", extra={"bbox": True, "color": "yellow"})
                consecutive_failures = 0  # Reset on success
            else:
                # ── Sauvegarde ──
                filepath = store.save_flights(flights)

                try:
                    # ── Métriques rapides ──
                    df      = store.load_flights(filepath)
                    metrics = compute_basic_metrics(df)

                    print(
                        f"  ✈  {metrics['in_flight']} en vol | "
                        f"🅿  {metrics['on_ground']} au sol | "
                        f"🌍 {metrics['unique_countries']} pays | "
                        f"↑  {metrics['altitude_mean']:.0f}m moy"
                    )
                    consecutive_failures = 0  # Reset on success

                except Exception as parse_err:
                    logger.error(f"[Collector] Erreur parsing snapshot #{snapshot_count} : {parse_err}", extra={"bbox": True, "color": "red"})
                    consecutive_failures += 1
                    raise ParseError(f"Échec parsing snapshot #{snapshot_count}") from parse_err

        except requests.RequestException as e:
            # Erreur réseau : on logge avec exc_info pour la stack trace complète
            logger.error(f"[Collector] ⚠ Erreur réseau snapshot #{snapshot_count} : {e}", exc_info=True)
            consecutive_failures += 1
            print(f"[Collector] Échec réseau ({consecutive_failures}/{MAX_FAILURES}). On continue...")

        except ParseError as e:
            # Erreur de parsing explicite
            logger.error(f"[Collector] ⚠ Erreur de parsing snapshot #{snapshot_count} : {e}", exc_info=True)
            consecutive_failures += 1
            print(f"[Collector] Échec parsing ({consecutive_failures}/{MAX_FAILURES}).")

        except GeopolError as e:
            # Autre erreur métier géopol
            logger.error(f"[Collector] ⚠ Erreur métier snapshot #{snapshot_count} : {e}", exc_info=True)
            consecutive_failures += 1

        # ── Gestion du seuil d'échecs ──
        if consecutive_failures >= MAX_FAILURES:
            logger.critical(f"[Collector] {MAX_FAILURES} échecs consécutifs. Arrêt de la collecte pour éviter une boucle infinie.")
            print(f"\n[Collector] ERREUR CRITIQUE : {MAX_FAILURES} échecs consécutifs. Arrêt du script.")
            break

        # ── Attente ──
        if snapshot_count < max_snap and consecutive_failures < MAX_FAILURES:
            logger.info(f"[Collector] Prochain snapshot dans {interval}s...", extra={"bbox": True, "color": "green"})
            time.sleep(interval)

    if consecutive_failures >= MAX_FAILURES:
        sys.exit(1) # Code de sortie erreur pour alerter les superviseurs
        
    print("\n[Collector] Collecte terminée.")


if __name__ == "__main__":
    run_collector()