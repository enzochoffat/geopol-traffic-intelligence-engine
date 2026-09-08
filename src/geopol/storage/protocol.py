import pandas as pd

from typing import Protocol
from pathlib import Path

from src.geopol.models.adsb_message import ADSBMessage

class DataStoreProtocol(Protocol):

    def save_flights(self, messages: list[ADSBMessage], region_code: str|None) -> Path:
        """
        Sauvegarde une liste d'ADSBMessage dans un fichier CSV horodaté.
        
        Args:
            messages : liste d'avions récupérés depuis OpenSky
            region_code : code de la région

        Returns:
            Le chemin du fichier créé
        """
        ...

    def load_flights(self, filepath: Path) -> pd.DataFrame:
        """
        Charge un fichier CSV d'avions et retourne un DataFrame pandas.
        
        Args:
            filepath : chemin vers le fichier CSV
        
        Returns:
            DataFrame pandas contenant les données des avions
        """
        ...

    def load_all(self, data_dir: Path | None = None) -> pd.DataFrame:
        """
        Charge tous les fichiers CSV d'avions dans un dossier et retourne un DataFrame pandas.
        
        Args:
            data_dir : chemin vers le dossier contenant les fichiers CSV
        
        Returns:
            DataFrame pandas contenant toutes les données des avions
        """
        ...

    def load_latest_per_region(self, data_dir: Path | None = None) -> dict[str, pd.DataFrame]:
        """
        Charge le dernier fichier CSV d'avions par région dans un dossier et retourne un DataFrame pandas.
        
        Args:
            data_dir : chemin vers le dossier contenant les fichiers CSV
        
        Returns:
            DataFrame pandas contenant les données des avions du dernier fichier par région
        """
        ...