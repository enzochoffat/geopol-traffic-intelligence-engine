import sys
import logging
from pathlib import Path
import pandas as pd
from pathlib import Path
from flask import Flask, request, jsonify, Response, stream_with_context
from flask_limiter import Limiter
from flask_cors import CORS

from src.geopol.storage.csv_store import CsvStore
from src.geopol.storage.protocol import DataStoreProtocol
from src.geopol.analysis.timeseries_analyzer import build_timeseries, detect_anomalies
from src.geopol.analysis.air_traffic_analyser import compute_basic_metrics, compute_country_breakdown
from src.geopol.agent.llm_analyst import ask, _build_context
from src.geopol.utils.paths import DATA_RAW as _DATA_RAW
from src.geopol.utils.paths import DATA_REPORTS as _DATA_REPORTS

logger = logging.getLogger(__name__)

def create_app(store: DataStoreProtocol | None = None) -> Flask:
    """
    Crée l'application Flask avec les routes API.
    Permet d'injecter un DataStore pour les tests.
    """
    if store is None:
        store = CsvStore()  # Utilise le stockage CSV par défaut

    app = Flask(__name__)
    app.config["MAX_CONTENT_LENGTH"] = 2*1024
    app.config["JSON_SORT_KEYS"] = False
    app.config["store"] = store

    # CORS = autorise le dashboard HTML (fichier local) à appeler l'API
    # Sans ça le navigateur bloque les requêtes cross-origin
    CORS(app, origins=app.config.get("CORS_ALLOWED_ORIGINS", []), supports_credentials=False)

    # ── Cache en mémoire ──
    # On charge les données une fois au démarrage
    # pour ne pas relire les CSV à chaque requête
    _cache = {
        "df_latest"    : None,
        "ts"           : None,
        "correlations" : None,
        "loaded"       : False,
    }

    def _load_data():
        if _cache["loaded"]:
            return True

        current_store = app.config["store"]

        try:
            all_data = current_store.load_all()

            if all_data.empty:
                logger.warning("[API] Aucun fichier CSV trouvé dans le dossier de données", extra={"bbox": True, "color": "yellow"})
                return False

            all_data = all_data.sort_values("timestamp")

            last_ts = all_data["timestamp"].max()
            _cache["df_latest"] = all_data[all_data["timestamp"] == last_ts].copy()

            _cache["ts"] = build_timeseries(all_data)

            from src.geopol.utils.paths import DATA_REPORTS
            corr_path = DATA_REPORTS / "correlations.csv"
            if corr_path.exists():
                _cache["correlations"] = pd.read_csv(corr_path)

            _cache["loaded"] = True
            logger.info("[API] Données chargées en mémoire", extra={"bbox": True, "color": "green"})
            return True

        except Exception as e:
            logger.error(f"[API] Erreur lors du chargement des données : {e}", extra={"bbox": True, "color": "red"}, exc_info=True)
            return False


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

    limiter = Limiter(
        app,
        key_func=lambda: request.remote_addr,
        default_limits=["5 per minute"]
    )

    @app.route("/api/ask", methods=["POST"])
    @limiter.limit("5 per minute")  # Limite à 5 requêtes par minute par IP
    def ask_agent():
        """
        Reçoit une question, la passe à l'agent LLM,
        retourne la réponse en streaming (Server-Sent Events).

        SSE = Server-Sent Events : le serveur envoie des tokens
        au fur et à mesure, le navigateur les affiche en temps réel.
        C'est exactement comme ChatGPT.
        """


        body = request.get_json(force=True, silent=False)
        if not body:
            return jsonify({"error": "Requête invalide"}), 400
        question = body.get("question", "").strip()[:500] # Limite à 500 caractères

        if len(question) < 3:
            return jsonify({"error": "Question trop courte"}), 400

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
            full_prompt = f"<DATA>{context}</DATA>\n<QUESTION>{question}</QUESTION>"

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

    @app.after_request
    def add_security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        return response

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

    app = create_app()

    with app.app_context():
        pass
    
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
    )