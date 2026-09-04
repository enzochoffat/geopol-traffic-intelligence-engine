import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


import time
import pandas as pd
from datetime import datetime
from pathlib import Path

from ingestion.adsb_ingestor import fetch_flights
from storage.data_store import save_flights
from utils.regions import Region, get_all_regions

# Délai entre chaque région pour respecter le rate limit OpenSky
INTER_REGION_DELAY = 6   # secondes


def fetch_global_snapshot(
    regions: list[Region] = None,
    delay: int = INTER_REGION_DELAY,
) -> dict[str, pd.DataFrame]:
    """
    Récupère un snapshot de trafic pour chaque région mondiale.

    Pourquoi région par région et pas tout d'un coup ?
    OpenSky limite la taille des bounding boxes et le nombre
    de requêtes. On découpe pour rester dans les limites.

    Args:
        regions : liste de régions (défaut = toutes)
        delay   : pause entre régions (secondes)

    Returns:
        Dict {code_région: DataFrame}
    """

    if regions is None:
        regions = get_all_regions()

    results  = {}
    total    = len(regions)

    print(f"[Global] Démarrage snapshot mondial — {total} régions")
    print(f"[Global] Durée estimée : ~{total * delay}s")
    print("─" * 50)

    for i, region in enumerate(regions, 1):
        print(f"[{i}/{total}] {region.name} ({region.code})...")

        try:
            messages = fetch_flights(
                lat_min=region.lat_min,
                lon_min=region.lon_min,
                lat_max=region.lat_max,
                lon_max=region.lon_max,
            )

            if messages:
                # Sauvegarde avec le code région dans le nom de fichier
                save_flights(messages, suffix=region.code)

                # Convertit en DataFrame pour le retour
                df = pd.DataFrame([vars(m) for m in messages])
                df["region"] = region.code
                results[region.code] = df

                print(f"  ✓ {len(messages)} avions")
            else:
                print(f"  ─ Aucun avion")
                results[region.code] = pd.DataFrame()

        except Exception as e:
            print(f"  ✗ Erreur : {e}")
            results[region.code] = pd.DataFrame()

        # Pause sauf pour la dernière région
        if i < total:
            time.sleep(delay)

    total_aircraft = sum(len(df) for df in results.values())
    print("─" * 50)
    print(f"[Global] ✓ Snapshot terminé — {total_aircraft} avions au total")

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