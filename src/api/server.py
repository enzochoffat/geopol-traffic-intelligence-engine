import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
from pathlib import Path
from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS

from storage.data_store import load_all_flights, load_flights
from analysis.timeseries_analyzer import build_timeseries, detect_anomalies
from analysis.air_traffic_analyser import compute_basic_metrics, compute_country_breakdown
from agent.llm_analyst import ask, _build_context

app = Flask(__name__)

# CORS = autorise le dashboard HTML (fichier local) à appeler l'API
# Sans ça le navigateur bloque les requêtes cross-origin
CORS(app)

# ── Cache en mémoire ──
# On charge les données une fois au démarrage
# pour ne pas relire les CSV à chaque requête
_cache = {
    "df_latest"    : None,
    "ts"           : None,
    "correlations" : None,
}

_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
_DATA_RAW     = _PROJECT_ROOT / "data" / "raw"

if not _DATA_RAW.exists():
    _DATA_RAW = Path("data/raw")


def _load_data():
    csv_files = sorted(_DATA_RAW.glob("flights_*.csv"))
    if not csv_files:
        return False

    _cache["df_latest"] = load_flights(csv_files[-1])
    df_all              = load_all_flights(_DATA_RAW)
    _cache["ts"]        = build_timeseries(df_all)

    corr_path = _PROJECT_ROOT / "data" / "reports" / "correlations.csv"
    if corr_path.exists():
        import pandas as pd
        _cache["correlations"] = pd.read_csv(corr_path)

    return True


# ════════════════════════════════════════
# ROUTES — Données
# ════════════════════════════════════════

@app.route("/api/status", methods=["GET"])
def status():
    """
    Route de santé — vérifie que l'API tourne.
    Le dashboard l'appelle au démarrage.
    """
    loaded = _load_data()
    if not loaded:
        return jsonify({"status": "no_data", "message": "Aucune donnée disponible"}), 404

    ts  = _cache["ts"]
    df  = _cache["df_latest"]

    return jsonify({
        "status"          : "ok",
        "snapshots"       : len(ts),
        "latest_aircraft" : len(df),
        "in_flight"       : int((~df["on_ground"]).sum()),
        "on_ground"       : int(df["on_ground"].sum()),
        "countries"       : int(df["origin_country"].nunique()),
        "altitude_mean"   : round(float(df["altitude"].mean()), 0),
        "velocity_mean"   : round(float(df["velocity"].mean()), 0),
        "period_start"    : str(ts["timestamp"].min()),
        "period_end"      : str(ts["timestamp"].max()),
    })


@app.route("/api/metrics", methods=["GET"])
def metrics():
    """Retourne les métriques complètes du dernier snapshot."""

    _load_data()
    df = _cache["df_latest"]
    if df is None:
        return jsonify({"error": "Aucune donnée"}), 404

    m = compute_basic_metrics(df)

    # Convertit les types numpy en types Python natifs pour JSON
    return jsonify({k: _serialize(v) for k, v in m.items()})


@app.route("/api/countries", methods=["GET"])
def countries():
    """Retourne la répartition par pays."""

    _load_data()
    df = _cache["df_latest"]
    if df is None:
        return jsonify({"error": "Aucune donnée"}), 404

    breakdown = compute_country_breakdown(df)

    return jsonify(breakdown.head(20).to_dict(orient="records"))


@app.route("/api/timeseries", methods=["GET"])
def timeseries():
    """Retourne la série temporelle complète."""

    _load_data()
    ts = _cache["ts"]
    if ts is None:
        return jsonify({"error": "Aucune donnée"}), 404

    return jsonify(ts.to_dict(orient="records"))


@app.route("/api/correlations", methods=["GET"])
def correlations():
    """Retourne les corrélations géopolitiques."""

    _load_data()
    corr = _cache["correlations"]
    if corr is None:
        return jsonify([])

    return jsonify(corr.head(10).to_dict(orient="records"))


@app.route("/api/anomalies", methods=["GET"])
def anomalies():
    """Retourne les anomalies détectées."""

    _load_data()
    ts = _cache["ts"]
    if ts is None:
        return jsonify([])

    anom = detect_anomalies(ts)
    if anom.empty:
        return jsonify([])

    return jsonify(anom.to_dict(orient="records"))


# ════════════════════════════════════════
# ROUTE — Agent LLM
# ════════════════════════════════════════

@app.route("/api/ask", methods=["POST"])
def ask_agent():
    """
    Reçoit une question, la passe à l'agent LLM,
    retourne la réponse en streaming (Server-Sent Events).

    SSE = Server-Sent Events : le serveur envoie des tokens
    au fur et à mesure, le navigateur les affiche en temps réel.
    C'est exactement comme ChatGPT.
    """

    body     = request.get_json()
    question = body.get("question", "").strip()

    if not question:
        return jsonify({"error": "Question vide"}), 400

    _load_data()
    df   = _cache["df_latest"]
    ts   = _cache["ts"]
    corr = _cache["correlations"]

    if df is None:
        return jsonify({"error": "Aucune donnée disponible"}), 404

    def generate():
        """Générateur SSE — envoie les tokens un par un."""
        import ollama

        context       = _build_context(ts, df, corr)
        system_prompt = (
            "Tu es un analyste OSINT spécialisé en trafic aérien et géopolitique. "
            "Réponds en français, de façon concise et factuelle. "
            "Cite toujours les chiffres précis des données fournies."
        )
        full_prompt = f"{context}\n\nQuestion : {question}"

        try:
            stream = ollama.chat(
                model="mistral",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user",   "content": full_prompt},
                ],
                stream=True,
            )
            for chunk in stream:
                token = chunk["message"]["content"]
                # Format SSE : "data: <token>\n\n"
                yield f"data: {token}\n\n"

        except Exception as e:
            yield f"data: [Erreur agent : {e}]\n\n"

        # Signal de fin
        yield "data: [DONE]\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={
            "Cache-Control"  : "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


@app.route("/api/reload", methods=["POST"])
def reload_data():
    """Force le rechargement des données depuis les CSV."""
    success = _load_data()
    return jsonify({"success": success})


# ════════════════════════════════════════
# UTILITAIRES
# ════════════════════════════════════════

def _serialize(val):
    """Convertit les types numpy/pandas en types JSON-compatibles."""
    import numpy as np
    if isinstance(val, (pd.Timestamp,)):
        return str(val)
    if isinstance(val, (np.integer,)):
        return int(val)
    if isinstance(val, (np.floating,)):
        return float(val)
    if pd.isna(val):
        return None
    return val


if __name__ == "__main__":
    print("=" * 50)
    print("  GeoPol API — Démarrage")
    print("  http://localhost:5000")
    print("=" * 50)

    loaded = _load_data()
    print(f"[API] Données {'chargées' if loaded else 'non disponibles au démarrage'}")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
    )