import folium
import pandas as pd
import logging

from pathlib import Path
from src.geopol.utils.paths import MAPS_DIR

logger = logging.getLogger(__name__)


def build_flight_map(df: pd.DataFrame, output_name: str = "flights_map") -> Path:
    """
    Génère une carte HTML interactive avec les avions en vol.

    Args:
        df          : DataFrame chargé depuis le CSV
        output_name : nom du fichier HTML de sortie

    Returns:
        Chemin vers le fichier HTML généré
    """

    MAPS_DIR.mkdir(parents=True, exist_ok=True)

    # ── Centre de la carte = moyenne des positions ──
    center_lat = df["latitude"].mean()
    center_lon = df["longitude"].mean()

    # Crée la carte centrée sur la zone
    # zoom_start : 1=monde, 5=pays, 10=ville
    m = folium.Map(location=[center_lat, center_lon], zoom_start=5)

    # ── Sépare avions en vol / au sol ──
    in_flight = df[df["on_ground"] == False]
    on_ground = df[df["on_ground"] == True]

    # ── Ajoute les avions EN VOL (bleu) ──
    for _, row in in_flight.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=4,
            color="#3498db",
            fill=True,
            fill_opacity=0.7,
            tooltip=_build_tooltip(row),
        ).add_to(m)

    # ── Ajoute les avions AU SOL (orange) ──
    for _, row in on_ground.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=5,
            color="#e67e22",
            fill=True,
            fill_opacity=0.8,
            tooltip=_build_tooltip(row),
        ).add_to(m)

    # ── Légende simple en haut à droite ──
    legend_html = """
    <div style="position:fixed; top:10px; right:10px; z-index:1000;
                background:white; padding:10px; border-radius:8px;
                border:1px solid #ccc; font-size:13px;">
        <b>Trafic aérien</b><br>
        <span style="color:#3498db;">●</span> En vol ({in_flight})<br>
        <span style="color:#e67e22;">●</span> Au sol ({on_ground})<br>
        <span style="font-size:11px; color:#888;">{timestamp}</span>
    </div>
    """.format(
        in_flight=len(in_flight),
        on_ground=len(on_ground),
        timestamp=df["timestamp"].iloc[0].strftime("%Y-%m-%d %H:%M UTC")
    )
    m.get_root().html.add_child(folium.Element(legend_html))

    # ── Sauvegarde la carte ──
    filepath = MAPS_DIR / f"{output_name}.html"
    m.save(str(filepath))

    logger.info(f"[MapViewer] Carte générée → {filepath}", extra={"bbox": True, "color": "green"})
    print(f"[MapViewer] Ouvre dans ton navigateur : file://{filepath.resolve()}")
    return filepath


def _build_tooltip(row: pd.Series) -> str:
    """
    Construit le texte affiché au survol d'un avion.
    """
    callsign  = row["callsign"] if pd.notna(row["callsign"]) else "Inconnu"
    altitude  = f"{row['altitude']:.0f} m" if pd.notna(row["altitude"]) else "N/A"
    velocity  = f"{row['velocity']:.0f} m/s" if pd.notna(row["velocity"]) else "N/A"
    heading   = f"{row['heading']:.0f}°" if pd.notna(row["heading"]) else "N/A"

    return (
        f"✈ {callsign} ({row['icao24']})\n"
        f"Pays : {row['origin_country']}\n"
        f"Altitude : {altitude}\n"
        f"Vitesse  : {velocity}\n"
        f"Cap      : {heading}"
    )