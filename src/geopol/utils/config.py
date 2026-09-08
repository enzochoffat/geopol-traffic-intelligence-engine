from pydantic import BaseModel, Field
import yaml
from pathlib import Path
from src.geopol.utils.paths import CONFIG_PATH

class Zone(BaseModel):
    name: str
    lat_min: float = Field(ge=-90, le=90)
    lon_min: float = Field(ge=-180, le=180)
    lat_max: float
    lon_max: float
    def model_post_init(self, __ctx):
        assert self.lat_min < self.lat_min and self.lon_min < self.lon_max

class Settings(BaseModel):
    zone: Zone
    collection: dict
    paths: dict

def load_config(config_path: Path = CONFIG_PATH) -> Settings:
    """
    Load the configuration from a YAML file.
    """
    return Settings(**yaml.safe_load(config_path.read_text()))