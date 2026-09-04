import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path

from ingestion.gdelt_ingestor import (
    fetch_gdelt_events,
    filter_events_by_zone,
    save_gdelt_events,
)
from analysis.correlator import correlate_multiple_events


# ── Codes CAMEO importants pour l'OSINT aérien ──
# CAMEO = système de classification des événements géopolitiques
# Source : https://www.gdeltproject.org/data/documentation/CAMEO.Manual.1.1b3.pdf
CAMEO_CODES_OF_INTEREST = {
    "13"  : "🚫 Menace / ultimatum",
    "14"  : "💣 Protestation",
    "15"  : "⚔️  Conflit armé",
    "16"  : "💥 Attaque",
    "17"  : "🔒 Coercition",
    "18"  : "🚨 Attentat",
    "19"  : "☢️  Guerre",
    "20"  : "🛑 Sanction / embargo",
}


def gdelt_to_events(df: pd.DataFrame) -> list[dict]:
    """
    Convertit un DataFrame GDELT en liste d'événements
    compatibles avec le corrélateur.

    On garde uniquement les événements :
    - Avec coordonnées GPS valides
    - Avec un score Goldstein négatif (conflictuels)
    - Avec au moins 3 mentions médias (filtre le bruit)

    Args:
        df : DataFrame GDELT filtré par zone

    Returns:
        Liste de dicts {name, timestamp, lat, lon, goldstein, ...}
    """

    if df.empty:
        return []

    # ── Nettoyage ──
    df = df.copy()
    df["ActionGeo_Lat"]   = pd.to_numeric(df["ActionGeo_Lat"],   errors="coerce")
    df["ActionGeo_Long"]  = pd.to_numeric(df["ActionGeo_Long"],  errors="coerce")
    df["GoldsteinScale"]  = pd.to_numeric(df["GoldsteinScale"],  errors="coerce")
    df["NumMentions"]     = pd.to_numeric(df["NumMentions"],      errors="coerce")

    # ── Filtres qualité ──
    df = df.dropna(subset=["ActionGeo_Lat", "ActionGeo_Long", "GoldsteinScale"])
    df = df[df["NumMentions"] >= 3]          # au moins 3 mentions
    df = df[df["GoldsteinScale"] <= -1.0]    # événements conflictuels uniquement

    if df.empty:
        print("[GDELTCorrelator] Aucun événement conflictuel significatif.")
        return []

    # ── Déduplique par lieu ──
    # GDELT peut avoir 50 lignes pour le même événement
    # On garde le plus mentionné par lieu
    df = (
        df.sort_values("NumMentions", ascending=False)
          .drop_duplicates(subset=["ActionGeo_FullName"])
          .head(20)   # max 20 événements pour ne pas surcharger
    )

    # ── Construit le timestamp ──
    # GDELT stocke la date en YYYYMMDDHHMMSS dans DATEADDED
    def parse_gdelt_timestamp(val) -> datetime:
        try:
            return datetime.strptime(str(int(val)), "%Y%m%d%H%M%S")
        except Exception:
            return datetime.utcnow()

    events = []
    for _, row in df.iterrows():
        # Code CAMEO → label lisible
        event_code = str(row.get("EventBaseCode", ""))
        code_label = CAMEO_CODES_OF_INTEREST.get(
            event_code[:2],
            f"Événement {event_code}"
        )

        events.append({
            "name"       : f"{code_label} — {row['ActionGeo_FullName']}",
            "timestamp"  : parse_gdelt_timestamp(row["DATEADDED"]),
            "lat"        : row["ActionGeo_Lat"],
            "lon"        : row["ActionGeo_Long"],
            "goldstein"  : row["GoldsteinScale"],
            "mentions"   : row["NumMentions"],
            "source_url" : row.get("SOURCEURL", ""),
            "avg_tone"   : row.get("AvgTone", 0),
        })

    print(f"[GDELTCorrelator] {len(events)} événements convertis.")
    return events


def run_gdelt_correlation(
    ts: pd.DataFrame,
    lat_min: float,
    lon_min: float,
    lat_max: float,
    lon_max: float,
    window_hours: int = 6,
    lookback_hours: int = 2,
) -> pd.DataFrame:
    """
    Pipeline complet : GDELT → filtrage → corrélation.

    Args:
        ts            : série temporelle de trafic
        lat/lon       : bounding box de la zone
        window_hours  : fenêtre de corrélation avant/après
        lookback_hours: combien d'heures en arrière chercher dans GDELT

    Returns:
        DataFrame de corrélations trié par signal
    """

    print("\n[GDELTCorrelator] Démarrage pipeline GDELT → Corrélation")
    print("─" * 50)

    all_correlations = []

    # ── Télécharge les fichiers GDELT des X dernières heures ──
    # GDELT publie un fichier toutes les 15 min
    # On itère sur les créneaux
    now = datetime.utcnow()
    slots = []
    current = now - timedelta(hours=lookback_hours)

    while current <= now:
        slots.append(current)
        current += timedelta(minutes=15)

    print(f"[GDELTCorrelator] {len(slots)} créneaux GDELT à analyser...")

    seen_events = set()   # évite les doublons entre fichiers

    for slot in slots:
        # ── Télécharge ──
        df_gdelt = fetch_gdelt_events(dt=slot)

        if df_gdelt.empty:
            continue

        # ── Filtre zone ──
        df_zone = filter_events_by_zone(df_gdelt, lat_min, lon_min, lat_max, lon_max)

        if df_zone.empty:
            continue

        # ── Convertit ──
        events = gdelt_to_events(df_zone)

        # ── Déduplique par nom d'événement ──
        new_events = []
        for e in events:
            key = e["name"]
            if key not in seen_events:
                seen_events.add(key)
                new_events.append(e)

        if not new_events:
            continue

        # ── Corrèle ──
        correlations = correlate_multiple_events(
            new_events, ts, window_hours=window_hours
        )
        all_correlations.append(correlations)

    # ── Fusionne tous les résultats ──
    if not all_correlations:
        print("[GDELTCorrelator] Aucune corrélation trouvée sur la période.")
        return pd.DataFrame()

    import pandas as pd
    final = pd.concat(all_correlations, ignore_index=True)
    final = final.sort_values("correlation_signal", ascending=False)

    print(f"\n[GDELTCorrelator] {len(final)} corrélations calculées.")
    return final