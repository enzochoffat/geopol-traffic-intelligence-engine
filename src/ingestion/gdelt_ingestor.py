import requests
import pandas as pd
import zipfile
import io
from datetime import datetime, timedelta
from pathlib import Path

# Colonnes GDELT qui nous intéressent
# GDELT a 61 colonnes — on garde les utiles
GDELT_ALL_COLUMNS = [
    "GlobalEventID", "Day", "MonthYear", "Year", "FractionDate",
    "Actor1Code", "Actor1Name", "Actor1CountryCode", "Actor1KnownGroupCode",
    "Actor1EthnicCode", "Actor1Religion1Code", "Actor1Religion2Code",
    "Actor1Type1Code", "Actor1Type2Code", "Actor1Type3Code",
    "Actor2Code", "Actor2Name", "Actor2CountryCode", "Actor2KnownGroupCode",
    "Actor2EthnicCode", "Actor2Religion1Code", "Actor2Religion2Code",
    "Actor2Type1Code", "Actor2Type2Code", "Actor2Type3Code",
    "IsRootEvent", "EventCode", "EventBaseCode", "EventRootCode",
    "QuadClass", "GoldsteinScale", "NumMentions", "NumSources", "NumArticles",
    "AvgTone",
    "Actor1Geo_Type", "Actor1Geo_FullName", "Actor1Geo_CountryCode",
    "Actor1Geo_ADM1Code", "Actor1Geo_ADM2Code", "Actor1Geo_Lat", "Actor1Geo_Long",
    "Actor1Geo_FeatureID",
    "Actor2Geo_Type", "Actor2Geo_FullName", "Actor2Geo_CountryCode",
    "Actor2Geo_ADM1Code", "Actor2Geo_ADM2Code", "Actor2Geo_Lat", "Actor2Geo_Long",
    "Actor2Geo_FeatureID",
    "ActionGeo_Type", "ActionGeo_FullName", "ActionGeo_CountryCode",
    "ActionGeo_ADM1Code", "ActionGeo_ADM2Code", "ActionGeo_Lat", "ActionGeo_Long",
    "ActionGeo_FeatureID",
    "DATEADDED", "SOURCEURL",
]

GDELT_DATA_DIR = Path("data/gdelt")


def _round_to_15min(dt: datetime) -> datetime:
    """
    GDELT publie un fichier toutes les 15 minutes.
    On arrondit au quart d'heure inférieur le plus proche.
    """
    minutes = (dt.minute // 15) * 15
    return dt.replace(minute=minutes, second=0, microsecond=0)


def _build_gdelt_url(dt: datetime) -> str:
    """
    Construit l'URL du fichier GDELT pour un datetime donné.
    """
    rounded = _round_to_15min(dt)
    timestamp = rounded.strftime("%Y%m%d%H%M%S")
    return f"http://data.gdeltproject.org/gdeltv2/{timestamp}.export.CSV.zip"


def fetch_gdelt_events(dt: datetime = None) -> pd.DataFrame:
    """
    Télécharge et parse le fichier GDELT pour un moment donné.

    Args:
        dt : datetime cible (défaut = maintenant - 30min pour éviter
             les fichiers pas encore publiés)

    Returns:
        DataFrame des événements géopolitiques
    """

    if dt is None:
        # GDELT a ~15-30min de délai — on prend il y a 30 min
        dt = datetime.utcnow() - timedelta(minutes=30)

    url = _build_gdelt_url(dt)
    print(f"[GDELT] Téléchargement : {url}")

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f"[GDELT] ⚠ Fichier indisponible : {e}")
        return pd.DataFrame()

    # Le fichier est un ZIP contenant un CSV
    # On le dézippe en mémoire sans écrire sur disque
    try:
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            csv_filename = z.namelist()[0]
            with z.open(csv_filename) as f:
                df = pd.read_csv(
                    f,
                    sep="\t",
                    header=None,
                    names=GDELT_ALL_COLUMNS,  # ← 61 colonnes complètes
                    on_bad_lines="skip",
                    low_memory=False,
                )
    except Exception as e:
        print(f"[GDELT] ⚠ Erreur parsing : {e}")
        return pd.DataFrame()

    print(f"[GDELT] {len(df)} événements récupérés.")
    return df


def filter_events_by_zone(
    df: pd.DataFrame,
    lat_min: float,
    lon_min: float,
    lat_max: float,
    lon_max: float,
) -> pd.DataFrame:
    """
    Filtre les événements GDELT dans une zone géographique.

    Args:
        df                    : DataFrame GDELT complet
        lat_min/max, lon_min/max : bounding box de ta zone

    Returns:
        Événements dans la zone uniquement
    """

    if df.empty:
        return df

    # Convertit les coordonnées en numérique
    # (GDELT peut avoir des valeurs manquantes)
    df["ActionGeo_Lat"]  = pd.to_numeric(df["ActionGeo_Lat"],  errors="coerce")
    df["ActionGeo_Long"] = pd.to_numeric(df["ActionGeo_Long"], errors="coerce")

    mask = (
        (df["ActionGeo_Lat"]  >= lat_min) &
        (df["ActionGeo_Lat"]  <= lat_max) &
        (df["ActionGeo_Long"] >= lon_min) &
        (df["ActionGeo_Long"] <= lon_max)
    )

    filtered = df[mask].copy()
    print(f"[GDELT] {len(filtered)} événements dans la zone.")
    return filtered


def save_gdelt_events(df: pd.DataFrame, label: str = "") -> Path:
    """
    Sauvegarde les événements GDELT en CSV local.
    """
    GDELT_DATA_DIR.mkdir(parents=True, exist_ok=True)

    now      = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    suffix   = f"_{label}" if label else ""
    filepath = GDELT_DATA_DIR / f"events{suffix}_{now}.csv"

    df.to_csv(filepath, index=False)
    print(f"[GDELT] Événements sauvegardés → {filepath}")
    return filepath