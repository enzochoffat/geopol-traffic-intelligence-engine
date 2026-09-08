"""
Snapshot mondial — collecte toutes les régions
et affiche un résumé global.
"""

from pathlib import Path
from src.geopol.ingestion.global_ingestor import fetch_global_snapshot, build_global_summary
from src.geopol.utils.regions import REGIONS, get_all_regions
from src.geopol.utils.paths import DATA_RAW, DATA_REPORTS


def main():
    print("=" * 60)
    print("  GeoPol — Snapshot Mondial")
    print("=" * 60)

    # ── Snapshot complet ──
    snapshots = fetch_global_snapshot()

    # ── Résumé par région ──
    summary = build_global_summary(snapshots)

    print("\n" + "═" * 60)
    print("  RÉSUMÉ MONDIAL")
    print("═" * 60)
    print(f"\n{'Région':<30} {'Avions':>7} {'En vol':>7} {'Pays':>5}")
    print("─" * 55)

    for _, row in summary.iterrows():
        region_name = REGIONS.get(
            next((k for k, v in REGIONS.items()
                  if v.code == row['region_code']), ""),
        )
        name = region_name.name if region_name else row['region_code']
        print(
            f"{name:<30} "
            f"{int(row['total_aircraft']):>7} "
            f"{int(row['in_flight']):>7} "
            f"{int(row['unique_countries']):>5}"
        )

    print("─" * 55)
    print(f"{'TOTAL':<30} {summary['total_aircraft'].sum():>7}")

    # ── Sauvegarde résumé ──
    out = DATA_REPORTS
    out.mkdir(parents=True, exist_ok=True)
    summary.to_csv(out / "global_summary.csv", index=False)
    print(f"\n[Main] Résumé sauvegardé → {DATA_REPORTS}/global_summary.csv")


if __name__ == "__main__":
    main()