import ollama
import pandas as pd
from pathlib import Path
from datetime import datetime


# Modèle Ollama à utiliser
LLM_MODEL = "mistral"


def _build_context(
    ts: pd.DataFrame,
    df_latest: pd.DataFrame,
    correlations: pd.DataFrame = None,
) -> str:
    """
    Construit le contexte de données à injecter dans le prompt.
    Le LLM n'a pas accès aux fichiers — on lui résume les données
    sous forme de texte structuré.

    C'est le principe du RAG (Retrieval Augmented Generation) :
    on enrichit le prompt avec les vraies données.
    """

    # ── Résumé snapshot ──
    in_flight = int((~df_latest["on_ground"]).sum())
    on_ground = int(df_latest["on_ground"].sum())
    countries = df_latest["origin_country"].value_counts().head(5).to_dict()
    alt_mean  = df_latest["altitude"].mean()
    vel_mean  = df_latest["velocity"].mean()
    top_countries = "\n".join([f"  - {k}: {v} avions" for k, v in countries.items()])

    # ── Résumé série temporelle ──
    ts_summary = ""
    if not ts.empty:
        ts_summary = f"""
SÉRIE TEMPORELLE ({len(ts)} snapshots) :
- Période : {ts['timestamp'].min()} → {ts['timestamp'].max()}
- Avions moyen : {ts['total_aircraft'].mean():.0f}
- Min : {ts['total_aircraft'].min():.0f} ({ts.loc[ts['total_aircraft'].idxmin(), 'timestamp']})
- Max : {ts['total_aircraft'].max():.0f} ({ts.loc[ts['total_aircraft'].idxmax(), 'timestamp']})
- Dernière variation : {ts['delta_total'].iloc[-1]:+.0f} avions
- Dernière variation % : {ts['pct_change'].iloc[-1]:+.1f}%
"""

    # ── Résumé corrélations ──
    corr_summary = ""
    if correlations is not None and not correlations.empty:
        top_corr = correlations.head(3)
        lines = []
        for _, row in top_corr.iterrows():
            lines.append(
                f"  - {row.get('signal_label','?')} | "
                f"{row.get('event_name','?')} | "
                f"Δ trafic: {row.get('traffic_delta_pct', 0):+.1f}% | "
                f"Score: {row.get('correlation_signal', 0)}"
            )
        corr_summary = "CORRÉLATIONS GÉOPOLITIQUES :\n" + "\n".join(lines)

    return f"""
=== DONNÉES TRAFIC AÉRIEN — {datetime.now().strftime('%Y-%m-%d %H:%M')} ===

SNAPSHOT ACTUEL :
- Total avions     : {len(df_latest)}
- En vol           : {in_flight}
- Au sol           : {on_ground}
- Ratio sol/air    : {on_ground/len(df_latest):.1%}
- Altitude moyenne : {alt_mean:.0f} m
- Vitesse moyenne  : {vel_mean:.0f} m/s
- Pays représentés : {df_latest['origin_country'].nunique()}

TOP 5 PAYS :
{top_countries}

{ts_summary}
{corr_summary}
=== FIN DES DONNÉES ===
"""


def _build_system_prompt() -> str:
    """
    Le system prompt définit le rôle et le comportement du LLM.
    C'est la 'personnalité' de l'agent.
    """
    return """Tu es un analyste OSINT spécialisé dans le trafic aérien et la géopolitique.

Tu reçois des données de trafic aérien en temps réel et des corrélations
avec des événements géopolitiques.

Tes règles :
- Réponds toujours en français
- Sois concis et factuel — pas de remplissage
- Cite toujours les chiffres précis des données fournies
- Si une anomalie est visible, explique-la clairement
- Si les données sont insuffisantes pour conclure, dis-le explicitement
- Ne fabrique pas de données — utilise uniquement ce qui est fourni
- Format : bullet points quand c'est pertinent
"""


def ask(
    question: str,
    ts: pd.DataFrame,
    df_latest: pd.DataFrame,
    correlations: pd.DataFrame = None,
    stream: bool = True,
) -> str:
    """
    Pose une question à l'agent LLM avec le contexte des données.

    Args:
        question     : question en langage naturel
        ts           : série temporelle
        df_latest    : dernier snapshot
        correlations : corrélations GDELT
        stream       : affiche la réponse au fur et à mesure

    Returns:
        Réponse complète du LLM
    """

    context      = _build_context(ts, df_latest, correlations)
    system_prompt = _build_system_prompt()

    # Le prompt final = system + contexte + question
    full_prompt = f"{context}\n\nQuestion : {question}"

    print(f"\n[Agent] Question : {question}")
    print("[Agent] Analyse en cours...\n")
    print("─" * 50)

    if stream:
        # Mode streaming — affiche token par token comme ChatGPT
        response_text = ""
        stream_response = ollama.chat(
            model=LLM_MODEL,
            messages=[
                {"role": "system",  "content": system_prompt},
                {"role": "user",    "content": full_prompt},
            ],
            stream=True,
        )
        for chunk in stream_response:
            token = chunk["message"]["content"]
            print(token, end="", flush=True)
            response_text += token

        print("\n" + "─" * 50)
        return response_text

    else:
        # Mode normal — attend la réponse complète
        response = ollama.chat(
            model=LLM_MODEL,
            messages=[
                {"role": "system",  "content": system_prompt},
                {"role": "user",    "content": full_prompt},
            ],
        )
        answer = response["message"]["content"]
        print(answer)
        print("─" * 50)
        return answer