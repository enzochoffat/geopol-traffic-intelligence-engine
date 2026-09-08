import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from pathlib import Path
from src.geopol.utils.paths import MAPS_DIR


def plot_timeseries(ts: pd.DataFrame, anomalies: pd.DataFrame = None) -> Path:
    """
    Génère un graphe HTML interactif de la série temporelle.

    Contient 3 sous-graphes :
      1. Nombre d'avions total + anomalies marquées
      2. Altitude moyenne
      3. Nombre de pays représentés

    Args:
        ts        : série temporelle (output de build_timeseries)
        anomalies : DataFrame des anomalies détectées (peut être None)

    Returns:
        Chemin vers le fichier HTML généré
    """

    MAPS_DIR.mkdir(parents=True, exist_ok=True)

    # ── Crée une figure avec 3 graphes empilés verticalement ──
    # shared_xaxes = ils partagent tous le même axe X (temps)
    fig = make_subplots(
        rows=3, cols=1,
        shared_xaxes=True,
        subplot_titles=(
            "Nombre d'avions total",
            "Altitude moyenne (m)",
            "Pays représentés"
        ),
        vertical_spacing=0.08
    )

    # ════════════════════════════════════════
    # GRAPHE 1 — Nombre d'avions
    # ════════════════════════════════════════

    # Courbe principale
    fig.add_trace(
        go.Scatter(
            x=ts["timestamp"],
            y=ts["total_aircraft"],
            mode="lines+markers",
            name="Total avions",
            line=dict(color="#3498db", width=2),
            marker=dict(size=6),
            # Texte au survol
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Total : %{y} avions<br>"
                "<extra></extra>"
            ),
        ),
        row=1, col=1
    )

    # Zone colorée sous la courbe (effet visuel)
    fig.add_trace(
        go.Scatter(
            x=ts["timestamp"],
            y=ts["total_aircraft"],
            fill="tozeroy",
            fillcolor="rgba(52, 152, 219, 0.1)",
            line=dict(width=0),
            showlegend=False,
            hoverinfo="skip",
        ),
        row=1, col=1
    )

    # ── Marque les anomalies en rouge ──
    if anomalies is not None and len(anomalies) > 0:
        fig.add_trace(
            go.Scatter(
                x=anomalies["timestamp"],
                y=anomalies["total_aircraft"],
                mode="markers",
                name="⚠ Anomalie",
                marker=dict(
                    color="#e74c3c",
                    size=14,
                    symbol="x",
                    line=dict(width=2)
                ),
                hovertemplate=(
                    "<b>⚠ ANOMALIE</b><br>"
                    "%{x}<br>"
                    "Total : %{y} avions<br>"
                    "Z-score : %{customdata:.2f}<br>"
                    "<extra></extra>"
                ),
                customdata=anomalies["z_score"],
            ),
            row=1, col=1
        )

    # ════════════════════════════════════════
    # GRAPHE 2 — Altitude moyenne
    # ════════════════════════════════════════

    fig.add_trace(
        go.Scatter(
            x=ts["timestamp"],
            y=ts["altitude_mean"],
            mode="lines+markers",
            name="Altitude moy.",
            line=dict(color="#2ecc71", width=2),
            marker=dict(size=5),
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Altitude : %{y:.0f} m<br>"
                "<extra></extra>"
            ),
        ),
        row=2, col=1
    )

    # ════════════════════════════════════════
    # GRAPHE 3 — Nombre de pays
    # ════════════════════════════════════════

    fig.add_trace(
        go.Bar(
            x=ts["timestamp"],
            y=ts["unique_countries"],
            name="Pays",
            marker_color="#9b59b6",
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Pays : %{y}<br>"
                "<extra></extra>"
            ),
        ),
        row=3, col=1
    )

    # ════════════════════════════════════════
    # MISE EN PAGE GLOBALE
    # ════════════════════════════════════════

    fig.update_layout(
        title=dict(
            text="GeoPol Traffic Intelligence — Série Temporelle",
            font=dict(size=20)
        ),
        height=800,
        template="plotly_dark",
        hovermode="x unified",       # affiche toutes les valeurs au même x
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
    )

    # Labels axes Y
    fig.update_yaxes(title_text="Avions",  row=1, col=1)
    fig.update_yaxes(title_text="Mètres",  row=2, col=1)
    fig.update_yaxes(title_text="Pays",    row=3, col=1)
    fig.update_xaxes(title_text="Heure",   row=3, col=1)

    # ── Sauvegarde ──
    filepath = MAPS_DIR / "timeseries.html"
    fig.write_html(str(filepath))

    print(f"[Plotter] Graphe généré → {filepath}")
    print(f"[Plotter] Ouvre : file://{filepath.resolve()}")
    return filepath