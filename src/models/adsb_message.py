from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class ADSBMessage:
    """
    Représente un message ADS-B émis par un avion.
    Correspond exactement à ce que retourne l'API OpenSky.
    """
    
    icao24: str                      # Identifiant unique matériel de l'avion
    callsign: Optional[str]          # Indicatif de vol (ex: AFR123) — peut être vide
    origin_country: str              # Pays d'origine (ex: France)
    latitude: Optional[float]        # Position GPS
    longitude: Optional[float]       # Position GPS
    altitude: Optional[float]        # Altitude en mètres
    velocity: Optional[float]        # Vitesse en m/s
    heading: Optional[float]         # Cap (direction) en degrés
    on_ground: bool                  # Est-il au sol ?
    timestamp: datetime              # Moment de la capture