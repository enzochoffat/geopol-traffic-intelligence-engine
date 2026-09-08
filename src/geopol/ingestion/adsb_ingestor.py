import requests
import logging
import tenacity
import time

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

from datetime import datetime
from typing import Optional
from src.geopol.models.adsb_message import ADSBMessage

logger = logging.getLogger(__name__)

# URL de base de l'API OpenSky
OPENSKY_URL = "https://opensky-network.org/api/states/all"

@retry(stop=stop_after_attempt(3),
       wait=wait_exponential(2, 10),
       retry=retry_if_exception_type(requests.exceptions.RequestException))

def fetch_flights(
    lat_min: float,
    lon_min: float,
    lat_max: float,
    lon_max: float
) -> list[ADSBMessage]:
    """
    Interroge l'API OpenSky et retourne une liste d'avions
    sur la zone géographique demandée.
    
    Args:
        lat_min, lon_min : coin bas-gauche de la zone
        lat_max, lon_max : coin haut-droite de la zone
    
    Returns:
        Liste d'objets ADSBMessage
    """

    # Construction des paramètres de la requête
    params = {
        "lamin": lat_min,
        "lomin": lon_min,
        "lamax": lat_max,
        "lomax": lon_max,
    }

    logger.info(f"[OpenSky] Appel API sur la zone : {lat_min},{lon_min} → {lat_max},{lon_max}", extra={"bbox": True, "color": "green"})

    # Appel HTTP
    response = requests.Session()
    response.mount("https://", requests.adapters.HTTPAdapter(max_retries=3))
    response = response.get(OPENSKY_URL, params=params, timeout=10)

    if response.status_code == 429:
        wait = int(response.headers.get("Retry-After", 10))
        logger.warning(f"[OpenSky] Trop de requêtes. Attente de {wait} secondes.", extra={"bbox": True, "color": "yellow"})
        time.sleep(wait)

    # Si l'API répond avec une erreur, on lève une exception
    response.raise_for_status()

    data = response.json()

    # Si aucun avion dans la zone
    if not data.get("states"):
        logger.info("[OpenSky] Aucun avion détecté sur cette zone.", extra={"bbox": True, "color": "yellow"})
        return []

    # Timestamp de la capture (fourni par OpenSky)
    capture_time = datetime.fromtimestamp(data["time"])

    messages = []

    for state in data["states"]:
        message = _parse_state(state, capture_time)
        if message:
            messages.append(message)

    logger.info(f"[OpenSky] {len(messages)} avions récupérés.", extra={"bbox": True, "color": "green"})
    return messages


def _parse_state(state: list, timestamp: datetime) -> Optional[ADSBMessage]:
    """
    Convertit une ligne brute OpenSky en objet ADSBMessage.
    Retourne None si les données sont trop incomplètes.
    """

    # On ignore les avions sans position GPS
    if state[6] is None or state[5] is None:
        return None

    return ADSBMessage(
        icao24=state[0],
        callsign=state[1].strip() if state[1] else None,
        origin_country=state[2],
        latitude=state[6],
        longitude=state[5],
        altitude=state[7],
        velocity=state[9],
        heading=state[10],
        on_ground=state[8],
        timestamp=timestamp,
    )