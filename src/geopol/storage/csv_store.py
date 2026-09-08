import re
import pandas as pd
import logging

from pathlib import Path
from datetime import datetime
from typing import List

from src.geopol.models.adsb_message import ADSBMessage
from src.geopol.storage.protocol import DataStoreProtocol
from src.geopol.utils.paths import DATA_RAW as DATA_DIR

logger = logging.getLogger(__name__)

FLIGHT_RE = re.compile(r"^flights_(?P<ts>\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})(?:__(?P<code>[A-Z_]+))?\.csv$")

class CsvStore:
    """Store data in CSV files, implementing the DataStoreProtocol."""

    def __init__(self, root_dir: Path | None = None):
        self.root_dir = root_dir if root_dir else DATA_DIR

    def save_flights(self, messages: list[ADSBMessage], region_code: str | None = None) -> Path:
        """
        Sauvegarde une liste d'ADSBMessage dans un fichier CSV horodaté.
        
        Args:
            messages : liste d'avions récupérés depuis OpenSky
        
        Returns:
            Le chemin du fichier créé
        """
        self.root_dir.mkdir(parents=True, exist_ok=True)

        # Convertit les objets en liste de dictionnaires
        # dataclasses.asdict() transforme un ADSBMessage → dict Python
        records = []
        if not messages:
            logger.warning("[DataStore] Aucun message à sauvegarder", extra={"bbox": True, "color": "yellow"})
            raise ValueError("[DataStore] Aucun message à sauvegarder")
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
        region_code = re.match(r"^[A-Z_]{2,10}$", region_code) if region_code else None
        suffix_ = f"_{region_code}" if region_code else ""
        filepath = DATA_DIR / f"flights_{now}{suffix_}.csv"

        # Sauvegarde en CSV sans l'index pandas (colonne 0,1,2...)
        df.to_csv(filepath, index=False)

        logger.info(f"[DataStore] {len(df)} avions sauvegardés → {filepath}", extra={"bbox": True, "color": "green"})
        return filepath


    def load_flights(self, filepath: Path) -> pd.DataFrame:
        """
        Charge un fichier CSV de vols et retourne un DataFrame.
        
        Args:
            filepath : chemin vers le fichier CSV
        
        Returns:
            DataFrame pandas avec les données de vols
        """

        df = pd.read_csv(filepath, parse_dates=["timestamp"])

        logger.info(f"[DataStore] {len(df)} avions chargés depuis {filepath}", extra={"bbox": True, "color": "green"})
        return df

    def load_all_flights(self,data_dir: Path | None = None) -> pd.DataFrame:
        """
        Charge TOUS les fichiers CSV du dossier et les fusionne.
        Chaque fichier = un snapshot = un moment dans le temps.

        Returns:
            DataFrame combiné, trié par timestamp
        """
        target_dir = data_dir if data_dir else self.root_dir
        csv_files = sorted(target_dir.glob("flights_*.csv"))

        if not csv_files:
            logger.error(f"[DataStore] Aucun fichier CSV dans {target_dir}", extra={"bbox": True, "color": "red"})
            raise FileNotFoundError(f"[DataStore] Aucun fichier CSV dans {target_dir}")

        logger.info(f"[DataStore] {len(csv_files)} snapshots trouvés...", extra={"bbox": True, "color": "green"})

        # Charge chaque fichier et les empile verticalement
        # pd.concat() fusionne une liste de DataFrames
        frames = []
        for f in csv_files:
            df = pd.read_csv(f, parse_dates=["timestamp"])
            frames.append(df)

        combined = pd.concat(frames, ignore_index=True, verify_integrity=True)
        set(df.columns)
        combined = combined.sort_values("timestamp").reset_index(drop=True)

        logger.info(f"[DataStore] {len(combined)} lignes totales sur {combined['timestamp'].nunique()} snapshots", extra={"bbox": True, "color": "green"})
        return combined

    def load_latest_global(self, data_dir: Path | None = None) -> dict[str, pd.DataFrame]:
        """
        Charge le dernier snapshot de chaque région mondiale.

        Pour chaque code région (EU_W, ME, RU...) on prend
        le fichier le plus récent.

        Returns:
            Dict {code_région: DataFrame}
        """
        target_dir = data_dir if data_dir else self.root_dir
        region_files: dict[str, Path] = {}

        for f in sorted(target_dir.glob("flights_*_*.csv")):
            # Le nom contient le code région après le dernier "_"
            # ex: flights_2026-03-11_17-14-01__EU_E.csv → EU_E
            match = FLIGHT_RE.match(f.name)
            if not match:
                continue
            groups = match.groups()
            if len(groups) < 2 or not groups[1]:
                continue
            code = re.match(r"^[A-Z_]{2,10}$", groups[-1])
            if not code:
                continue
            code = groups[-1]
            # On garde toujours le plus récent (sorted garantit l'ordre)
            region_files[code] = f

        result = {}
        for code, filepath in region_files.items():
            df = pd.read_csv(filepath, parse_dates=["timestamp"])
            if not df.empty:
                df["region"] = code
            result[code] = df

        logger.info(f"[DataStore] {len(result)} régions chargées depuis {target_dir}", extra={"bbox": True, "color": "green"})
        return result



    def load_latest_snapshot(self, data_dir: Path | None = None) -> pd.DataFrame:
        """
        Fusionne tous les derniers snapshots régionaux
        en un seul DataFrame mondial.

        Returns:
            DataFrame avec colonne 'region' ajoutée
        """
        target_dir = data_dir if data_dir else self.root_dir
        regional = self.load_latest_global(target_dir)

        if not regional:
            return pd.DataFrame()

        frames = [df for df in regional.values() if not df.empty]
        if not frames:
            return pd.DataFrame()

        combined = pd.concat(frames, ignore_index=True, verify_integrity=True)
        logger.info(f"[DataStore] Total mondial : {len(combined)} avions", extra={"bbox": True, "color": "green"})
        return combined