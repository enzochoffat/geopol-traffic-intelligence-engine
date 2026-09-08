"""
Shell interactif — pose des questions en boucle à l'agent.
Tape 'exit' pour quitter.
"""

import sys
from pathlib import Path
import logging

import pandas as pd
from src.geopol.agent.llm_analyst import ask
from src.geopol.storage.data_store import load_all_flights, load_flights
from src.geopol.analysis.timeseries_analyzer import build_timeseries
from src.geopol.utils.paths import DATA_RAW, DATA_REPORTS

logger =logging.getLogger(__name__)

# Questions prédéfinies accessibles par numéro
QUICK_QUESTIONS = {
    "1": "Résume la situation du trafic aérien actuel.",
    "2": "Y a-t-il des anomalies visibles dans les données ?",
    "3": "Quels pays dominent le trafic et pourquoi est-ce significatif ?",
    "4": "Analyse les variations de la série temporelle.",
    "5": "Y a-t-il une corrélation entre les événements géopolitiques et le trafic ?",
    "6": "Quel est le niveau de tension géopolitique actuel selon ces données ?",
}


def run_shell():
    print("=" * 60)
    print("  GeoPol — Agent LLM Interactif")
    print("=" * 60)

    # ── Charge les données ──
    print("\n[Shell] Chargement des données...")

    csv_files = sorted(DATA_RAW.glob("flights_*.csv"))
    if not csv_files:
        print("[Shell] Aucune donnée. Lance d'abord : python main.py")
        return

    df_latest = load_flights(csv_files[-1])
    df_all    = load_all_flights(DATA_RAW)
    ts        = build_timeseries(df_all)

    # Corrélations si disponibles
    correlations = None
    corr_path    = DATA_REPORTS / "correlations.csv"
    if corr_path.exists():
        correlations = pd.read_csv(corr_path)

    logger.info(f"Chargement des données : {len(df_latest)} avions | {len(ts)} snapshots | {len(correlations) if correlations is not None else 0} corrélations", 
                extra={"bbox": {"color": "green"}})

    # ── Menu questions rapides ──
    print("\n── Questions rapides ──")
    for num, question in QUICK_QUESTIONS.items():
        print(f"  {num}. {question}")
    print("\n  Tape un numéro, ou écris ta propre question.")
    print("  'exit' pour quitter.\n")

    # ── Boucle interactive ──
    while True:
        try:
            user_input = input("❯ ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n[Shell] À bientôt.")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit", "q"):
            print("[Shell] À bientôt.")
            break

        # Résout les raccourcis numériques
        question = QUICK_QUESTIONS.get(user_input, user_input)

        ask(
            question=question,
            ts=ts,
            df_latest=df_latest,
            correlations=correlations,
            stream=True,
        )

        print()


if __name__ == "__main__":
    run_shell()