from pathlib import Path
from storage.data_store import load_all_flights, load_flights
from analysis.timeseries_analyzer import build_timeseries, detect_anomalies
from visualization.dashboard import build_dashboard
import os
import subprocess
import sys


def main():
    print("=" * 55)
    print("  GeoPol — Dashboard Unifié")
    print("=" * 55)

    # ── Dernier snapshot pour la carte ──
    csv_files = sorted(Path("data/raw").glob("flights_*.csv"))
    if not csv_files:
        print("[Main] Aucune donnée. Lance d'abord : python main.py")
        return

    df_latest = load_flights(csv_files[-1])
    print(f"[Main] Snapshot carte : {csv_files[-1].name}")

    # ── Série temporelle complète ──
    df_all = load_all_flights(Path("data/raw"))
    ts     = build_timeseries(df_all)
    anomalies = detect_anomalies(ts)

    # ── Corrélations si disponibles ──
    corr_path = Path("data/reports/correlations.csv")
    correlations = None
    if corr_path.exists():
        import pandas as pd
        correlations = pd.read_csv(corr_path)
        print(f"[Main] Corrélations chargées : {len(correlations)} événements")

    # ── Génère le dashboard ──
    filepath = build_dashboard(
        df_flights=df_latest,
        ts=ts,
        correlations=correlations,
        anomalies=anomalies,
    )

    # ── Lance l'API en arrière-plan ──
    print("\n[Main] Démarrage de l'API Flask...")
    subprocess.Popen(
        [sys.executable, "api/server.py"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print("[Main] API disponible sur http://localhost:5000")
    
    # ── Ouvre dans le navigateur ──
    subprocess.run(["xdg-open", filepath])


if __name__ == "__main__":
    main()