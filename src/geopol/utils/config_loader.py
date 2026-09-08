import yaml
import logging

from pathlib import Path

logger = logging.getLogger(__name__)

def load_config(config_path: str) -> dict:
    """
    Charge le fichier de configuration YAML.

    Returns:
        Dictionnaire de configuration
    """
    path = Path(config_path)

    if not path.exists():
        logger.error(f"[Config] Fichier introuvable : {path.resolve()}", extra={"bbox": True, "color": "red"})
        raise FileNotFoundError(f"[Config] Fichier introuvable : {path.resolve()}")

    with open(path, "r") as f:
        config = yaml.safe_load(f)

    logger.info(f"[Config] Configuration chargée depuis {path}", extra={"bbox": True, "color": "green"})
    return config