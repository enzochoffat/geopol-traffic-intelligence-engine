from pathlib import Path
import re
import logging

from src.geopol.storage.data_store import load_all_flights, load_flights
from src.geopol.analysis.timeseries_analyzer import build_timeseries, detect_anomalies
from src.geopol.visualization.dashboard import build_dashboard
from src.geopol.api.server import PROJECT_ROOT
from src.geopol.utils.paths import DATA_RAW, DATA_REPORTS
import os
import subprocess
import sys

logger = logging.getLogger(__name__)

def main():
    print("=" * 55)
    print("  GeoPol — Dashboard Unifié")
    print("=" * 55)

    # ── Dernier snapshot pour la carte ──
    csv_files = sorted(DATA_RAW.glob("flights_*.csv"))
    if not csv_files:
        logger.error("[Main] Aucune donnée. Lance d'abord : python main.py", extra={"bbox": True, "color": "red"})
        return

    df_latest = load_flights(csv_files[-1])
    logger.info(f"[Main] Snapshot carte : {csv_files[-1].name}", extra={"bbox": True, "color": "green"})

    # ── Série temporelle complète ──
    df_all = load_all_flights(DATA_RAW)
    ts     = build_timeseries(df_all)
    anomalies = detect_anomalies(ts)

    # ── Corrélations si disponibles ──
    corr_path = DATA_REPORTS / "correlations.csv"
    correlations = None
    if corr_path.exists():
        import pandas as pd
        correlations = pd.read_csv(corr_path)
        logger.info(f"[Main] Corrélations chargées : {len(correlations)} événements", extra={"bbox": True, "color": "green"})

    # ── Génère le dashboard ──
    filepath = build_dashboard(
        df_flights=df_latest,
        ts=ts,
        correlations=correlations,
        anomalies=anomalies,
    )
    logger.info(f"[Main] Dashboard généré : {filepath}", extra={"bbox": True, "color": "green"})

    # ── Lance l'API en arrière-plan ──
    print("\n[Main] Démarrage de l'API Flask...")
    subprocess.Popen(
        [sys.executable, "api/server.py"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        cwd=PROJECT_ROOT,
    )
    print("[Main] API disponible sur http://localhost:5000")
    
    # ── Ouvre dans le navigateur ──
    subprocess.run(["xdg-open", filepath])


if __name__ == "__main__":
    main()