import yaml
from pathlib import Path


def load_config(config_path: str = "config/settings.yaml") -> dict:
    """
    Charge le fichier de configuration YAML.

    Returns:
        Dictionnaire de configuration
    """
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"[Config] Fichier introuvable : {path.resolve()}")

    with open(path, "r") as f:
        config = yaml.safe_load(f)

    print(f"[Config] Configuration chargée depuis {path}")
    return config