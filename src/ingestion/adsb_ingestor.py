import requests
from datetime import datetime
from typing import Optional
from models.adsb_message import ADSBMessage

# URL de base de l'API OpenSky
OPENSKY_URL = "https://opensky-network.org/api/states/all"


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

    print(f"[OpenSky] Appel API sur la zone : {lat_min},{lon_min} → {lat_max},{lon_max}")

    # Appel HTTP
    response = requests.get(OPENSKY_URL, params=params, timeout=10)

    # Si l'API répond avec une erreur, on lève une exception
    response.raise_for_status()

    data = response.json()

    # Si aucun avion dans la zone
    if not data.get("states"):
        print("[OpenSky] Aucun avion détecté sur cette zone.")
        return []

    # Timestamp de la capture (fourni par OpenSky)
    capture_time = datetime.fromtimestamp(data["time"])

    messages = []

    for state in data["states"]:
        message = _parse_state(state, capture_time)
        if message:
            messages.append(message)

    print(f"[OpenSky] {len(messages)} avions récupérés.")
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