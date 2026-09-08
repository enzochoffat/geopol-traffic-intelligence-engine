from src.geopol.ingestion.adsb_ingestor import fetch_flights
from src.geopol.storage.data_store import save_flights, load_flights
from src.geopol.visualization.map_viewer import build_flight_map
from src.geopol.analysis.air_traffic_analyser import print_report

# ─────────────────────────────────────────────
# ZONE GÉOGRAPHIQUE : France métropolitaine
# ─────────────────────────────────────────────
# C'est une "bounding box" (rectangle GPS)
# lat_min, lon_min = coin bas-gauche  (sud-ouest)
# lat_max, lon_max = coin haut-droite (nord-est)
LAT_MIN = 41.0
LON_MIN = -5.5
LAT_MAX = 51.5
LON_MAX = 10.0


def main():
    print("=" * 50)
    print("  GeoPol Traffic Intelligence Engine")
    print("  Phase 1 — Ingestion aérienne")
    print("=" * 50)

    # ── Étape 1 : Récupérer les avions en vol ──
    flights = fetch_flights(
        lat_min=LAT_MIN,
        lon_min=LON_MIN,
        lat_max=LAT_MAX,
        lon_max=LON_MAX
    )

    if not flights:
        print("[Main] Aucune donnée à sauvegarder.")
        return

    # ── Étape 2 : Sauvegarder en CSV ──
    filepath = save_flights(flights)

    # ── Étape 3 : Recharger et afficher un résumé ──
    df = load_flights(filepath)

    print("\n── Résumé ──")
    print(f"  Avions total       : {len(df)}")
    print(f"  Au sol             : {df['on_ground'].sum()}")
    print(f"  En vol             : {(~df['on_ground']).sum()}")
    print(f"  Pays représentés   : {df['origin_country'].nunique()}")
    print(f"  Altitude moyenne   : {df['altitude'].mean():.0f} m")
    print(f"  Vitesse moyenne    : {df['velocity'].mean():.0f} m/s")
    print("\n── Top 5 pays ──")
    print(df['origin_country'].value_counts().head())
    print(f"\n  Fichier sauvegardé : {filepath}")

    # ── Étape 4 : Afficher un rapport détaillé ──
    print_report(df)

    # ── Étape 5 : Générer une carte interactive ──
    build_flight_map(df)


if __name__ == "__main__":
    main()