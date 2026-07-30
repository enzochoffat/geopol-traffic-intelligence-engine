from datetime import datetime
from ingestion.gdelt_ingestor import (
    fetch_gdelt_events,
    filter_events_by_zone,
    save_gdelt_events,
)

# Zone France
LAT_MIN, LON_MIN = 12.0, 25.0
LAT_MAX, LON_MAX = 42.0, 63.0

def main():
    print("=" * 55)
    print("  GeoPol — Ingestion GDELT")
    print("=" * 55)

    # ── Récupère les événements ──
    df = fetch_gdelt_events()

    if df.empty:
        print("[Main] Aucun événement récupéré.")
        return

    # ── Filtre sur la zone France ──
    zone_df = filter_events_by_zone(df, LAT_MIN, LON_MIN, LAT_MAX, LON_MAX)

    # ── Résumé dans le terminal ──
    print(f"\n── Résumé événements zone France ──")
    print(f"  Total événements     : {len(zone_df)}")

    if not zone_df.empty:
        print(f"  Score Goldstein moy  : {zone_df['GoldsteinScale'].mean():.2f}")
        print(f"  Événement le + cité  : {zone_df.nlargest(1, 'NumMentions')['ActionGeo_FullName'].values[0]}")
        print(f"\n── Top 5 événements (par mentions médias) ──")

        top5 = zone_df.nlargest(5, "NumMentions")[
            ["ActionGeo_FullName", "GoldsteinScale", "NumMentions", "AvgTone", "SOURCEURL"]
        ]
        for _, row in top5.iterrows():
            print(f"\n  📍 {row['ActionGeo_FullName']}")
            print(f"     Goldstein : {row['GoldsteinScale']} | Mentions : {row['NumMentions']}")
            print(f"     Ton       : {row['AvgTone']:.1f}")
            print(f"     Source    : {row['SOURCEURL'][:60]}...")

    # ── Sauvegarde ──
    save_gdelt_events(zone_df, label="france")


if __name__ == "__main__":
    main()