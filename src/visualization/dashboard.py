import pandas as pd
import folium
from folium.plugins import MarkerCluster, HeatMap
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path
from datetime import datetime

from utils.regions import REGIONS, get_all_regions

DASHBOARD_DIR = Path("data/maps")


def build_dashboard(
    df_flights: pd.DataFrame,
    ts: pd.DataFrame,
    correlations: pd.DataFrame = None,
    anomalies: pd.DataFrame = None,
    regional_data: dict = None,       # ← nouveau
    output_name: str = "dashboard",
) -> Path:
    """
    Génère le dashboard HTML unifié.

    Args:
        df_flights    : snapshot fusionné (tous avions)
        ts            : série temporelle
        correlations  : corrélations GDELT
        anomalies     : anomalies détectées
        regional_data : dict {code: DataFrame} par région
        output_name   : nom du fichier HTML
    """

    DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)

    map_html     = _build_world_map(df_flights, regional_data)
    chart_html   = _build_chart_fragment(ts, anomalies)
    table_html   = _build_correlation_table(correlations)
    metrics_html = _build_metrics_banner(df_flights, ts, regional_data)
    region_html  = _build_region_panel(regional_data)
    chat_html    = _build_chat_block()

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>GeoPol — Dashboard Mondial</title>
    <style>
        * {{ margin:0; padding:0; box-sizing:border-box; }}
        body {{
            font-family: 'Segoe UI', sans-serif;
            background: #0d1117;
            color: #c9d1d9;
        }}
        .header {{
            background: linear-gradient(135deg, #1a1f2e, #16213e);
            border-bottom: 1px solid #30363d;
            padding: 20px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .header h1 {{ font-size:22px; color:#58a6ff; letter-spacing:1px; }}
        .api-status {{
            display:flex; align-items:center; gap:8px; font-size:12px; color:#8b949e;
        }}
        .api-dot {{
            width:8px; height:8px; border-radius:50%;
            background:#e74c3c; transition:background 0.3s;
        }}
        .api-dot.online {{ background:#2ecc71; }}

        /* ── Métriques ── */
        .metrics-bar {{
            display:flex; gap:12px; padding:15px 30px;
            background:#161b22; border-bottom:1px solid #30363d;
            flex-wrap:wrap; align-items:center;
        }}
        .metric-card {{
            background:#1c2128; border:1px solid #30363d;
            border-radius:8px; padding:10px 18px;
            min-width:120px; text-align:center;
        }}
        .metric-card .value {{
            font-size:22px; font-weight:bold; color:#58a6ff;
        }}
        .metric-card .label {{
            font-size:10px; color:#8b949e; margin-top:3px;
            text-transform:uppercase; letter-spacing:0.5px;
        }}
        .metric-card.alert .value {{ color:#e74c3c; }}
        .metric-card.warn  .value {{ color:#e67e22; }}
        .metric-card.ok    .value {{ color:#2ecc71; }}

        /* ── Layout ── */
        .main-grid {{
            display:grid;
            grid-template-columns: 2fr 1fr;
            height: 520px;
        }}
        .panel {{ border:1px solid #30363d; overflow:hidden; }}
        .panel-title {{
            background:#161b22; padding:10px 20px;
            font-size:12px; color:#8b949e;
            border-bottom:1px solid #30363d;
            text-transform:uppercase; letter-spacing:1px;
            display:flex; justify-content:space-between;
            align-items:center;
        }}
        .panel-content {{ height:calc(100% - 38px); overflow:hidden; }}
        .panel-content > div,
        .panel-content iframe {{ width:100%; height:100%; border:none; }}

        /* ── Panneau régions ── */
        .region-panel {{
            overflow-y:auto;
            padding:10px;
            height:calc(100% - 38px);
        }}
        .region-row {{
            display:flex; align-items:center; gap:10px;
            padding:8px 10px; border-radius:6px;
            margin-bottom:4px; cursor:pointer;
            transition:background 0.2s;
            border:1px solid transparent;
        }}
        .region-row:hover {{ background:#1c2128; border-color:#30363d; }}
        .region-dot {{
            width:10px; height:10px; border-radius:50%; flex-shrink:0;
        }}
        .region-name {{ font-size:12px; flex:1; }}
        .region-count {{
            font-size:14px; font-weight:bold;
            color:#58a6ff; min-width:45px; text-align:right;
        }}
        .region-bar-wrap {{
            width:60px; background:#21262d;
            border-radius:3px; height:6px;
        }}
        .region-bar {{
            height:6px; border-radius:3px;
            background:#58a6ff; transition:width 0.3s;
        }}

        /* ── Sections basses ── */
        .bottom-grid {{
            display:grid;
            grid-template-columns: 1fr 1fr;
        }}
        .section {{
            padding:20px 30px;
            border-top:1px solid #30363d;
            border-right:1px solid #30363d;
        }}
        .section-title {{
            font-size:13px; color:#58a6ff;
            text-transform:uppercase; letter-spacing:1px;
            margin-bottom:15px;
        }}
        table {{ width:100%; border-collapse:collapse; font-size:12px; }}
        th {{
            background:#161b22; color:#8b949e; padding:8px 12px;
            text-align:left; border-bottom:1px solid #30363d;
            font-weight:normal; text-transform:uppercase; font-size:10px;
        }}
        td {{ padding:8px 12px; border-bottom:1px solid #21262d; }}
        tr:hover td {{ background:#161b22; }}

        /* ── Chat ── */
        .chat-section {{
            padding:20px 30px 30px;
            border-top:2px solid #58a6ff22;
        }}
        .chat-container {{ max-width:100%; }}
        .chat-messages {{
            background:#161b22; border:1px solid #30363d;
            border-radius:10px; padding:20px;
            min-height:150px; max-height:320px;
            overflow-y:auto; margin-bottom:15px;
            font-size:13px; line-height:1.6;
        }}
        .msg-user {{
            background:#1f3a5f; border-left:3px solid #58a6ff;
            padding:10px 15px; border-radius:6px;
            margin-bottom:12px; color:#90caf9;
        }}
        .msg-agent {{
            background:#1a2332; border-left:3px solid #2ecc71;
            padding:10px 15px; border-radius:6px;
            margin-bottom:12px; color:#c9d1d9; white-space:pre-wrap;
        }}
        .msg-agent .agent-label {{
            font-size:10px; color:#2ecc71;
            text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;
        }}
        .cursor {{
            display:inline-block; width:8px; height:14px;
            background:#2ecc71; animation:blink 0.8s infinite;
            vertical-align:middle; margin-left:2px;
        }}
        @keyframes blink {{ 0%,100%{{opacity:1}} 50%{{opacity:0}} }}
        .quick-questions {{
            display:flex; flex-wrap:wrap; gap:8px; margin-bottom:15px;
        }}
        .quick-btn {{
            background:#1c2128; border:1px solid #30363d;
            color:#8b949e; padding:5px 12px; border-radius:20px;
            font-size:11px; cursor:pointer; transition:all 0.2s;
        }}
        .quick-btn:hover {{ border-color:#58a6ff; color:#58a6ff; }}
        .chat-input-row {{ display:flex; gap:10px; }}
        .chat-input {{
            flex:1; background:#161b22; border:1px solid #30363d;
            border-radius:8px; padding:11px 16px; color:#c9d1d9;
            font-size:13px; outline:none; transition:border-color 0.2s;
        }}
        .chat-input:focus {{ border-color:#58a6ff; }}
        .chat-input::placeholder {{ color:#484f58; }}
        .send-btn {{
            background:#238636; border:none; border-radius:8px;
            color:white; padding:11px 22px; font-size:13px;
            cursor:pointer; transition:background 0.2s;
        }}
        .send-btn:hover {{ background:#2ea043; }}
        .send-btn:disabled {{
            background:#21262d; color:#484f58; cursor:not-allowed;
        }}
    </style>
</head>
<body>

<div class="header">
    <h1>🌍 GeoPol Traffic Intelligence — Vue Mondiale</h1>
    <div style="display:flex;align-items:center;gap:20px;">
        <div class="api-status">
            <div class="api-dot" id="apiDot"></div>
            <span id="apiLabel">API...</span>
        </div>
        <span style="font-size:12px;color:#8b949e;">
            Mise à jour : {now} UTC
        </span>
    </div>
</div>

{metrics_html}

<div class="main-grid">
    <div class="panel">
        <div class="panel-title">
            <span>🗺 Trafic mondial en temps réel</span>
            <span style="font-size:11px;">
                🔵 En vol &nbsp; 🟠 Au sol &nbsp; 🔴 Zone de tension
            </span>
        </div>
        <div class="panel-content">{map_html}</div>
    </div>
    <div class="panel">
        <div class="panel-title">
            <span>📡 Régions</span>
        </div>
        <div class="region-panel">{region_html}</div>
    </div>
</div>

<div class="bottom-grid">
    <div class="section">
        <div class="section-title">📈 Série temporelle</div>
        {chart_html}
    </div>
    <div class="section">
        {table_html}
    </div>
</div>

{chat_html}

<script>
// ── Vérifie l'API ──
async function checkApi() {{
    try {{
        const r = await fetch("http://localhost:5000/api/status");
        if (r.ok) {{
            document.getElementById("apiDot").classList.add("online");
            document.getElementById("apiLabel").textContent = "API en ligne";
        }}
    }} catch(e) {{
        document.getElementById("apiLabel").textContent = "API hors ligne";
    }}
}}
checkApi();

// ── Chat ──
const messagesDiv = document.getElementById("chatMessages");
const input       = document.getElementById("chatInput");
const sendBtn     = document.getElementById("sendBtn");

function scrollBottom() {{ messagesDiv.scrollTop = messagesDiv.scrollHeight; }}

function addUserMessage(text) {{
    const div = document.createElement("div");
    div.className = "msg-user";
    div.textContent = "❯ " + text;
    messagesDiv.appendChild(div);
    scrollBottom();
}}

function createAgentMessage() {{
    const div = document.createElement("div");
    div.className = "msg-agent";
    const label = document.createElement("div");
    label.className = "agent-label";
    label.textContent = "Agent OSINT";
    const content = document.createElement("span");
    content.id = "streamContent";
    const cursor = document.createElement("span");
    cursor.className = "cursor";
    cursor.id = "streamCursor";
    div.appendChild(label);
    div.appendChild(content);
    div.appendChild(cursor);
    messagesDiv.appendChild(div);
    scrollBottom();
    return content;
}}

async function sendQuestion(question) {{
    if (!question.trim()) return;
    sendBtn.disabled = true;
    input.value = "";
    addUserMessage(question);
    const contentEl = createAgentMessage();
    try {{
        const response = await fetch("http://localhost:5000/api/ask", {{
            method:"POST",
            headers:{{"Content-Type":"application/json"}},
            body: JSON.stringify({{question}}),
        }});
        const reader  = response.body.getReader();
        const decoder = new TextDecoder();
        let buffer = "";
        while (true) {{
            const {{done, value}} = await reader.read();
            if (done) break;
            buffer += decoder.decode(value, {{stream:true}});
            const lines = buffer.split("\\n");
            buffer = lines.pop();
            for (const line of lines) {{
                if (!line.startsWith("data: ")) continue;
                const token = line.slice(6);
                if (token === "[DONE]") break;
                contentEl.textContent += token;
                scrollBottom();
            }}
        }}
    }} catch(e) {{
        contentEl.textContent = "Erreur : " + e.message;
    }}
    const cursor = document.getElementById("streamCursor");
    if (cursor) cursor.remove();
    sendBtn.disabled = false;
    input.focus();
}}

sendBtn.addEventListener("click", () => sendQuestion(input.value));
input.addEventListener("keydown", e => {{
    if (e.key === "Enter" && !e.shiftKey) {{
        e.preventDefault();
        sendQuestion(input.value);
    }}
}});
document.querySelectorAll(".quick-btn").forEach(btn => {{
    btn.addEventListener("click", () => sendQuestion(btn.dataset.question));
}});
</script>
</body>
</html>"""

    filepath = DASHBOARD_DIR / f"{output_name}.html"
    filepath.write_text(full_html, encoding="utf-8")
    print(f"[Dashboard] Généré → {filepath}")
    return filepath


# ════════════════════════════════════════════════
# FONCTIONS INTERNES
# ════════════════════════════════════════════════

def _build_chart_fragment(ts: pd.DataFrame, anomalies: pd.DataFrame) -> str:
    """Génère le graphe Plotly et retourne son HTML."""

    fig = make_subplots(
        rows=2, cols=1,
        shared_xaxes=True,
        subplot_titles=("Nombre d'avions", "Altitude moyenne (m)"),
        vertical_spacing=0.12,
    )

    fig.add_trace(
        go.Scatter(
            x=ts["timestamp"], y=ts["total_aircraft"],
            mode="lines+markers",
            name="Total avions",
            line=dict(color="#58a6ff", width=2),
            hovertemplate="<b>%{x}</b><br>%{y} avions<extra></extra>",
        ),
        row=1, col=1
    )

    if anomalies is not None and len(anomalies) > 0:
        fig.add_trace(
            go.Scatter(
                x=anomalies["timestamp"], y=anomalies["total_aircraft"],
                mode="markers", name="⚠ Anomalie",
                marker=dict(color="#e74c3c", size=12, symbol="x"),
            ),
            row=1, col=1
        )

    fig.add_trace(
        go.Scatter(
            x=ts["timestamp"], y=ts["altitude_mean"],
            mode="lines", name="Altitude",
            line=dict(color="#2ecc71", width=2),
        ),
        row=2, col=1
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#1c2128",
        plot_bgcolor="#1c2128",
        margin=dict(l=50, r=20, t=40, b=30),
        height=None,
        autosize=True,
        legend=dict(orientation="h", y=1.08),
    )

    return fig.to_html(
        full_html=False,
        include_plotlyjs="cdn",
        config={"responsive": True},
    )

def _build_correlation_table(correlations: pd.DataFrame) -> str:
    """Génère le tableau HTML des corrélations."""

    if correlations is None or correlations.empty:
        return """
        <div class="correlations-section">
            <div class="section-title">⚡ Corrélations géopolitiques</div>
            <p style="color:#8b949e; font-size:13px;">
                Aucune corrélation disponible.
                Lance <code>correlation_main.py</code> pour en générer.
            </p>
        </div>"""

    rows_html = ""
    for _, row in correlations.iterrows():
        delta = f"{row['traffic_delta_pct']:+.1f}%" if pd.notna(row.get('traffic_delta_pct')) else "N/A"
        rows_html += f"""
        <tr>
            <td>{row.get('signal_label','—')}</td>
            <td>{row.get('event_name','—')}</td>
            <td>{str(row.get('event_time','—'))[:16]}</td>
            <td>{row.get('event_goldstein','—')}</td>
            <td>{delta}</td>
            <td>{row.get('correlation_signal','—')}</td>
        </tr>"""

    return f"""
    <div class="correlations-section">
        <div class="section-title">⚡ Corrélations géopolitiques</div>
        <table>
            <thead>
                <tr>
                    <th>Signal</th>
                    <th>Événement</th>
                    <th>Date</th>
                    <th>Goldstein</th>
                    <th>Δ Trafic</th>
                    <th>Score</th>
                </tr>
            </thead>
            <tbody>{rows_html}</tbody>
        </table>
    </div>"""
    
def _build_chat_block() -> str:
    """Génère le bloc chat HTML + questions rapides."""

    quick = [
        ("Résume la situation",          "Résume la situation du trafic aérien actuel."),
        ("Anomalies ?",                   "Y a-t-il des anomalies visibles dans les données ?"),
        ("Top pays",                      "Quels pays dominent le trafic et pourquoi ?"),
        ("Analyse temporelle",            "Analyse les variations de la série temporelle."),
        ("Corrélation géopolitique ?",    "Y a-t-il une corrélation entre les événements géopolitiques et le trafic ?"),
        ("Niveau de tension ?",           "Quel est le niveau de tension géopolitique actuel selon ces données ?"),
    ]

    quick_btns = "".join([
        f'<button class="quick-btn" data-question="{q}">{label}</button>'
        for label, q in quick
    ])

    return f"""
    <div class="chat-section">
        <div class="chat-container">
            <div class="section-title">💬 Agent OSINT — Analyse en langage naturel</div>

            <div class="quick-questions">
                {quick_btns}
            </div>

            <div class="chat-messages" id="chatMessages">
                <div class="msg-agent">
                    <div class="agent-label">Agent OSINT</div>
                    Bonjour. Je suis connecté aux données de trafic aérien en temps réel.
                    Pose-moi une question ou clique sur un raccourci ci-dessus.
                </div>
            </div>

            <div class="chat-input-row">
                <input
                    type="text"
                    class="chat-input"
                    id="chatInput"
                    placeholder="Ex: Y a-t-il une chute de trafic inhabituelle ?"
                    autocomplete="off"
                />
                <button class="send-btn" id="sendBtn">Envoyer ↵</button>
            </div>
        </div>
    </div>"""
    
def _build_world_map(
    df: pd.DataFrame,
    regional_data: dict = None,
) -> str:
    """
    Carte mondiale Folium avec :
    - Points avions en vol / au sol
    - Rectangles de régions colorés par densité
    - Heatmap de densité de trafic
    """

    m = folium.Map(
        location=[30.0, 15.0],
        zoom_start=2,
        tiles="CartoDB dark_matter",   # fond sombre style OSINT
    )

    # ── Calque : rectangles de régions ──
    if regional_data:
        max_count = max(
            (len(df) for df in regional_data.values() if not df.empty),
            default=1
        )
        for code, region_df in regional_data.items():
            region = next((r for r in REGIONS.values() if r.code == code), None)
            if not region:
                continue

            count   = len(region_df)
            # Opacité proportionnelle à la densité de trafic
            opacity = 0.05 + 0.25 * (count / max(max_count, 1))

            folium.Rectangle(
                bounds=[
                    [region.lat_min, region.lon_min],
                    [region.lat_max, region.lon_max],
                ],
                color=region.color,
                fill=True,
                fill_opacity=opacity,
                weight=1,
                tooltip=f"{region.name} — {count} avions",
            ).add_to(m)

    if df.empty:
        return m._repr_html_()

    # ── Calque : heatmap densité ──
    heat_data = [
        [row["latitude"], row["longitude"], 1]
        for _, row in df.iterrows()
        if pd.notna(row["latitude"]) and pd.notna(row["longitude"])
    ]
    if heat_data:
        HeatMap(
            heat_data,
            radius=4,
            blur=6,
            min_opacity=0.2,
            gradient={"0.4":"blue","0.65":"lime","1":"red"},
        ).add_to(m)

    # ── Calque : avions (clustérisés pour les performances) ──
    cluster = MarkerCluster(
        options={"maxClusterRadius": 30, "disableClusteringAtZoom": 6}
    )

    in_flight = df[df["on_ground"] == False]
    on_ground = df[df["on_ground"] == True]

    for _, row in in_flight.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=2,
            color="#3498db",
            fill=True,
            fill_opacity=0.7,
            tooltip=(
                f"✈ {row.get('callsign','?')} | "
                f"{row['origin_country']} | "
                f"{row['altitude']:.0f}m | "
                f"{row.get('region','?')}"
            ),
        ).add_to(cluster)

    for _, row in on_ground.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=3,
            color="#e67e22",
            fill=True,
            fill_opacity=0.8,
            tooltip=f"🅿 {row.get('callsign','?')} | {row['origin_country']}",
        ).add_to(cluster)

    cluster.add_to(m)
    return m._repr_html_()

def _build_region_panel(regional_data: dict = None) -> str:
    """Génère le panneau latéral avec la liste des régions."""

    if not regional_data:
        return "<p style='color:#8b949e;font-size:12px;padding:10px;'>Lance make global pour charger les régions.</p>"

    # Trie par nombre d'avions décroissant
    sorted_regions = sorted(
        regional_data.items(),
        key=lambda x: len(x[1]),
        reverse=True,
    )
    max_count = max((len(df) for _, df in sorted_regions), default=1)

    rows = ""
    for code, df in sorted_regions:
        region = next((r for r in REGIONS.values() if r.code == code), None)
        if not region:
            continue

        count    = len(df)
        bar_pct  = int((count / max(max_count, 1)) * 100)
        in_fl    = int((~df["on_ground"]).sum()) if not df.empty else 0

        rows += f"""
        <div class="region-row">
            <div class="region-dot" style="background:{region.color}"></div>
            <div class="region-name">{region.name}</div>
            <div>
                <div class="region-bar-wrap">
                    <div class="region-bar"
                         style="width:{bar_pct}%;background:{region.color}">
                    </div>
                </div>
            </div>
            <div class="region-count">{count}</div>
        </div>"""

    return rows


def _build_metrics_banner(
    df: pd.DataFrame,
    ts: pd.DataFrame,
    regional_data: dict = None,
) -> str:
    """Génère la barre de métriques globales."""

    total     = len(df) if df is not None else 0
    in_flight = int((~df["on_ground"]).sum()) if not df.empty else 0
    on_ground = total - in_flight
    countries = int(df["origin_country"].nunique()) if not df.empty else 0
    regions   = len(regional_data) if regional_data else 0
    snapshots = len(ts) if ts is not None else 0

    # Détecte les régions avec peu de trafic (signal potentiel)
    alert_regions = []
    if regional_data:
        counts = {c: len(d) for c, d in regional_data.items() if not d.empty}
        if counts:
            avg = sum(counts.values()) / len(counts)
            alert_regions = [c for c, n in counts.items() if n < avg * 0.3]

    alert_class = "alert" if alert_regions else "ok"
    alert_label = f"⚠ {','.join(alert_regions)}" if alert_regions else "Normal"

    cards = [
        (f"{total:,}",    "Avions mondial",   ""),
        (str(in_flight),  "En vol",           "ok"),
        (str(on_ground),  "Au sol",           ""),
        (str(countries),  "Pays",             ""),
        (str(regions),    "Régions actives",  ""),
        (str(snapshots),  "Snapshots",        ""),
        (alert_label,     "Signal trafic",    alert_class),
    ]

    cards_html = ""
    for value, label, cls in cards:
        cards_html += f"""
        <div class="metric-card {cls}">
            <div class="value">{value}</div>
            <div class="label">{label}</div>
        </div>"""

    return f'<div class="metrics-bar">{cards_html}</div>'