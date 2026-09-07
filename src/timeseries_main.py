from pathlib import Path
from storage.data_store import load_all_flights
from analysis.timeseries_analyzer import build_timeseries, detect_anomalies, print_timeseries_report
from visualization.timeseries_plotter import plot_timeseries
from utils.paths import DATA_RAW, DATA_REPORTS


def main():
    print("=" * 55)
    print("  GeoPol — Analyse Série Temporelle")
    print("=" * 55)

    # ── Charge tous les snapshots ──
    df = load_all_flights(DATA_RAW)

    # ── Construit la série temporelle ──
    ts = build_timeseries(df)

    # ── Détecte les anomalies ──
    anomalies = detect_anomalies(ts)

    # ── Rapport terminal ──
    print_timeseries_report(ts)

    # ── Graphe interactif ──             
    plot_timeseries(ts, anomalies)

    # ── Sauvegarde CSV ──
    out = DATA_REPORTS
    out.mkdir(parents=True, exist_ok=True)
    ts.to_csv(out / "timeseries.csv", index=False)
    print(f"\n[Main] Série temporelle sauvegardée → {DATA_REPORTS}/timeseries.csv")


if __name__ == "__main__":
    main()