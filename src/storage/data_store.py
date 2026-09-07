import pandas as pd
from pathlib import Path
from datetime import datetime
from models.adsb_message import ADSBMessage
from utils.paths import DATA_RAW as DATA_DIR


def save_flights(messages: list[ADSBMessage], suffix: str = "") -> Path:
    """
    Sauvegarde une liste d'ADSBMessage dans un fichier CSV horodaté.
    
    Args:
        messages : liste d'avions récupérés depuis OpenSky
    
    Returns:
        Le chemin du fichier créé
    """

    # Crée le dossier data/raw/ s'il n'existe pas
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Convertit les objets en liste de dictionnaires
    # dataclasses.asdict() transforme un ADSBMessage → dict Python
    records = []
    for msg in messages:
        records.append({
            "icao24":         msg.icao24,
            "callsign":       msg.callsign,
            "origin_country": msg.origin_country,
            "latitude":       msg.latitude,
            "longitude":      msg.longitude,
            "altitude":       msg.altitude,
            "velocity":       msg.velocity,
            "heading":        msg.heading,
            "on_ground":      msg.on_ground,
            "timestamp":      msg.timestamp,
        })

    # Crée le DataFrame pandas
    df = pd.DataFrame(records)

    # Nom du fichier avec timestamp pour ne pas écraser les précédents
    # Exemple : flights_2026-03-03_14-30-00.csv
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    suffix_ = f"_{suffix}" if suffix else ""
    filepath = DATA_DIR / f"flights_{now}_{suffix_}.csv"

    # Sauvegarde en CSV sans l'index pandas (colonne 0,1,2...)
    df.to_csv(filepath, index=False)

    print(f"[DataStore] {len(df)} avions sauvegardés → {filepath}")
    return filepath


def load_flights(filepath: Path) -> pd.DataFrame:
    """
    Charge un fichier CSV de vols et retourne un DataFrame.
    
    Args:
        filepath : chemin vers le fichier CSV
    
    Returns:
        DataFrame pandas avec les données de vols
    """

    df = pd.read_csv(filepath, parse_dates=["timestamp"])

    print(f"[DataStore] {len(df)} avions chargés depuis {filepath}")
    return df

def load_all_flights(data_dir: Path = DATA_DIR) -> pd.DataFrame:
    """
    Charge TOUS les fichiers CSV du dossier et les fusionne.
    Chaque fichier = un snapshot = un moment dans le temps.

    Returns:
        DataFrame combiné, trié par timestamp
    """

    csv_files = sorted(data_dir.glob("flights_*.csv"))

    if not csv_files:
        raise FileNotFoundError(f"[DataStore] Aucun fichier CSV dans {data_dir}")

    print(f"[DataStore] {len(csv_files)} snapshots trouvés...")

    # Charge chaque fichier et les empile verticalement
    # pd.concat() fusionne une liste de DataFrames
    frames = []
    for f in csv_files:
        df = pd.read_csv(f, parse_dates=["timestamp"])
        frames.append(df)

    combined = pd.concat(frames, ignore_index=True)
    combined = combined.sort_values("timestamp").reset_index(drop=True)

    print(f"[DataStore] {len(combined)} lignes totales sur {combined['timestamp'].nunique()} snapshots")
    return combined

def load_latest_global(data_dir: Path = DATA_DIR) -> dict[str, pd.DataFrame]:
    """
    Charge le dernier snapshot de chaque région mondiale.

    Pour chaque code région (EU_W, ME, RU...) on prend
    le fichier le plus récent.

    Returns:
        Dict {code_région: DataFrame}
    """

    region_files: dict[str, Path] = {}

    for f in sorted(data_dir.glob("flights_*_*.csv")):
        # Le nom contient le code région après le dernier "_"
        # ex: flights_2026-03-11_17-14-01__EU_E.csv → EU_E
        parts = f.stem.split("__")
        if len(parts) < 2:
            continue
        code = parts[-1]
        # On garde toujours le plus récent (sorted garantit l'ordre)
        region_files[code] = f

    result = {}
    for code, filepath in region_files.items():
        df = pd.read_csv(filepath, parse_dates=["timestamp"])
        if not df.empty:
            df["region"] = code
        result[code] = df

    print(f"[DataStore] {len(result)} régions chargées depuis {data_dir}")
    return result


def load_latest_snapshot(data_dir: Path = DATA_DIR) -> pd.DataFrame:
    """
    Fusionne tous les derniers snapshots régionaux
    en un seul DataFrame mondial.

    Returns:
        DataFrame avec colonne 'region' ajoutée
    """

    regional = load_latest_global(data_dir)

    if not regional:
        return pd.DataFrame()

    frames = [df for df in regional.values() if not df.empty]
    if not frames:
        return pd.DataFrame()

    combined = pd.concat(frames, ignore_index=True)
    print(f"[DataStore] Total mondial : {len(combined)} avions")
    return combined