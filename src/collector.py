import time
import signal
import sys
from pathlib import Path
from datetime import datetime

from ingestion.adsb_ingestor import fetch_flights
from storage.data_store import save_flights, load_flights
from analysis.air_traffic_analyser import compute_basic_metrics
from utils.config_loader import load_config
from utils.paths import CONFIG_PATH

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

    snapshot_count = 0

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
                print("[Collector] Snapshot vide, on continue.")
            else:
                # ── Sauvegarde ──
                filepath = save_flights(flights)

                # ── Métriques rapides ──
                df      = load_flights(filepath)
                metrics = compute_basic_metrics(df)

                print(
                    f"  ✈  {metrics['in_flight']} en vol | "
                    f"🅿  {metrics['on_ground']} au sol | "
                    f"🌍 {metrics['unique_countries']} pays | "
                    f"↑  {metrics['altitude_mean']:.0f}m moy"
                )

        except Exception as e:
            # On ne plante pas sur une erreur réseau passagère
            print(f"[Collector] ⚠ Erreur snapshot #{snapshot_count} : {e}")
            print("[Collector] On continue au prochain intervalle...")

        # ── Attente ──
        if snapshot_count < max_snap:
            print(f"[Collector] Prochain snapshot dans {interval}s...")
            time.sleep(interval)

    print("\n[Collector] Collecte terminée.")


if __name__ == "__main__":
    run_collector()