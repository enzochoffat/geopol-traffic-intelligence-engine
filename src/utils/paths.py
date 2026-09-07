from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_ROOT = PROJECT_ROOT / "data"
DATA_RAW = DATA_ROOT / "raw"
DATA_GDELT = DATA_ROOT / "gdelt"
DATA_REPORTS = DATA_ROOT / "reports"
MAPS_DIR = DATA_ROOT / "maps"
CONFIG_PATH = PROJECT_ROOT / "config" / "config.yaml"