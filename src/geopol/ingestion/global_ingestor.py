import sys
from pathlib import Path
import time
from typing import Dict
import pandas as pd
import logging

from datetime import datetime
from pathlib import Path

from src.geopol.ingestion.adsb_ingestor import fetch_flights
from src.geopol.storage.csv_store import CsvStore
from src.geopol.storage.protocol import DataStoreProtocol
from src.geopol.utils.regions import Region, get_all_regions
from src.geopol.models.adsb_message import ADSBMessage

logger = logging.getLogger(__name__)

# Délai entre chaque région pour respecter le rate limit OpenSky
INTER_REGION_DELAY = 6   # secondes


def fetch_global_snapshot(
    store: DataStoreProtocol,
    regions: list[Region] = None,
    delay: int = INTER_REGION_DELAY,
) -> dict[str, pd.DataFrame]:
    """
    Récupère un snapshot de trafic pour chaque région mondiale.

    Pourquoi région par région et pas tout d'un coup ?
    OpenSky limite la taille des bounding boxes et le nombre
    de requêtes. On découpe pour rester dans les limites.

    Args:
        store   : instance de DataStoreProtocol pour sauvegarder les données
        regions : liste de régions (défaut = toutes)
        delay   : pause entre régions (secondes)

    Returns:
        Dict {code_région: DataFrame}
    """

    if regions is None:
        regions = get_all_regions()

    results: Dict[str, pd.DataFrame] = {}
    total = len(regions)

    logger.info(f"[Global] Démarrage snapshot mondial — {total} régions", extra={"bbox": True, "color": "green"})
    logger.info(f"[Global] Durée estimée : ~{total * delay}s", extra={"bbox": True, "color": "green"})
    logger.info("─" * 50, extra={"bbox": True, "color": "green"})

    for i, region in enumerate(regions, 1):
        logger.info(f"[{i}/{total}] {region.name} ({region.code})...", extra={"bbox": True, "color": "green"})

        try:
            messages = fetch_flights(
                lat_min=region.lat_min,
                lon_min=region.lon_min,
                lat_max=region.lat_max,
                lon_max=region.lon_max,
            )

            if messages:
                # Sauvegarde avec le code région dans le nom de fichier
                filepath = store.save_flights(messages, region_code=region.code)

                # Convertit en DataFrame pour le retour
                df = pd.DataFrame([vars(m) for m in messages])
                df["region"] = region.code
                results[region.code] = df

                logger.info(f"[{region.code}] {len(messages)} avions récupérés.", extra={"bbox": True, "color": "green"})
            else:
                logger.info(f"[{region.code}] Aucun avion détecté.", extra={"bbox": True, "color": "yellow"})
                results[region.code] = pd.DataFrame()

        except Exception as e:
            logger.error(f"[Global] Erreur lors de la récupération pour {region.code}: {e}", extra={"bbox": True, "color": "red"}, exc_info=True)
            print(f"  ✗ Erreur : {e}")
            results[region.code] = pd.DataFrame()

        # Pause sauf pour la dernière région
        if i < total:
            time.sleep(delay)

    total_aircraft = sum(len(df) for df in results.values())
    logger.info(f"[Global] ✓ Snapshot terminé — {total_aircraft} avions au total", extra={"bbox": True, "color": "green"})

    return results


def build_global_summary(snapshots: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """
    Construit un résumé par région à partir des snapshots.

    Returns:
        DataFrame avec une ligne par région et ses métriques
    """

    rows = []
    for code, df in snapshots.items():
        if df.empty:
            rows.append({
                "region_code"     : code,
                "total_aircraft"  : 0,
                "in_flight"       : 0,
                "on_ground"       : 0,
                "altitude_mean"   : 0,
                "velocity_mean"   : 0,
                "unique_countries": 0,
            })
            continue

        rows.append({
            "region_code"      : code,
            "total_aircraft"   : len(df),
            "in_flight"        : int((~df["on_ground"]).sum()),
            "on_ground"        : int(df["on_ground"].sum()),
            "altitude_mean"    : round(df["altitude"].mean(), 0),
            "velocity_mean"    : round(df["velocity"].mean(), 0),
            "unique_countries" : int(df["origin_country"].nunique()),
            "timestamp"        : datetime.utcnow().isoformat(),
        })

    return pd.DataFrame(rows).sort_values("total_aircraft", ascending=False)