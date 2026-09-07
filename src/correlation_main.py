from pathlib import Path
from storage.data_store import load_all_flights
from analysis.timeseries_analyzer import build_timeseries
from analysis.correlator import print_correlation_report
from analysis.gdelt_correlator import run_gdelt_correlation
from utils.paths import DATA_RAW, DATA_REPORTS

# ── Zone France ──
LAT_MIN, LON_MIN = 2.0, 45.0
LAT_MAX, LON_MAX = 22.0, 83.0


def main():
    print("=" * 60)
    print("  GeoPol — Corrélation GDELT Automatique")
    print("=" * 60)

    # ── Série temporelle ──
    df  = load_all_flights(DATA_RAW)
    ts  = build_timeseries(df)

    print(f"\n[Main] Série temporelle : {len(ts)} snapshots")
    print(f"[Main] Période : {ts['timestamp'].min()} → {ts['timestamp'].max()}")

    # ── Pipeline GDELT → Corrélation ──
    correlations = run_gdelt_correlation(
        ts=ts,
        lat_min=LAT_MIN,
        lon_min=LON_MIN,
        lat_max=LAT_MAX,
        lon_max=LON_MAX,
        window_hours=6,
        lookback_hours=2,
    )

    # ── Rapport terminal ──
    print_correlation_report(correlations)

    # ── Sauvegarde ──
    if not correlations.empty:
        out = DATA_REPORTS
        out.mkdir(parents=True, exist_ok=True)
        correlations.to_csv(out / "correlations.csv", index=False)
        print(f"\n[Main] Rapport sauvegardé → {DATA_REPORTS}/correlations.csv")


if __name__ == "__main__":
    main()