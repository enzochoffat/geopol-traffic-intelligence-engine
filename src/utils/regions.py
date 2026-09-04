from dataclasses import dataclass


@dataclass
class Region:
    """
    Définit une zone géographique d'analyse.

    lat_min/max : latitude  sud → nord
    lon_min/max : longitude ouest → est
    """
    name     : str
    code     : str       # identifiant court pour les fichiers
    lat_min  : float
    lon_min  : float
    lat_max  : float
    lon_max  : float
    color    : str = "#58a6ff"   # couleur sur le dashboard


# ══════════════════════════════════════════════
# RÉGIONS MONDIALES
# ══════════════════════════════════════════════

REGIONS: dict[str, Region] = {

    # ── Europe ──
    "europe_west": Region(
        name="Europe Occidentale", code="EU_W",
        lat_min=36.0, lon_min=-10.0,
        lat_max=55.0, lon_max=20.0,
        color="#58a6ff",
    ),
    "europe_east": Region(
        name="Europe Orientale", code="EU_E",
        lat_min=45.0, lon_min=20.0,
        lat_max=60.0, lon_max=40.0,
        color="#3498db",
    ),
    "russia": Region(
        name="Russie / Asie Centrale", code="RU",
        lat_min=50.0, lon_min=40.0,
        lat_max=72.0, lon_max=130.0,
        color="#e74c3c",
    ),

    # ── Moyen-Orient ──
    "middle_east": Region(
        name="Moyen-Orient", code="ME",
        lat_min=12.0, lon_min=30.0,
        lat_max=42.0, lon_max=65.0,
        color="#e67e22",
    ),

    # ── Asie ──
    "asia_south": Region(
        name="Asie du Sud", code="AS_S",
        lat_min=5.0,  lon_min=60.0,
        lat_max=35.0, lon_max=90.0,
        color="#9b59b6",
    ),
    "asia_east": Region(
        name="Asie de l'Est", code="AS_E",
        lat_min=20.0, lon_min=100.0,
        lat_max=50.0, lon_max=145.0,
        color="#8e44ad",
    ),

    # ── Amériques ──
    "north_america": Region(
        name="Amérique du Nord", code="NA",
        lat_min=25.0, lon_min=-130.0,
        lat_max=60.0, lon_max=-60.0,
        color="#2ecc71",
    ),
    "south_america": Region(
        name="Amérique du Sud", code="SA",
        lat_min=-55.0, lon_min=-80.0,
        lat_max=15.0,  lon_max=-35.0,
        color="#27ae60",
    ),

    # ── Afrique ──
    "africa": Region(
        name="Afrique", code="AF",
        lat_min=-35.0, lon_min=-20.0,
        lat_max=37.0,  lon_max=50.0,
        color="#f39c12",
    ),

    # ── Zones de tension spécifiques ──
    "ukraine_zone": Region(
        name="Zone Ukraine / Mer Noire", code="UKR",
        lat_min=43.0, lon_min=22.0,
        lat_max=52.0, lon_max=40.0,
        color="#e74c3c",
    ),
    "taiwan_strait": Region(
        name="Détroit de Taïwan", code="TWN",
        lat_min=20.0, lon_min=115.0,
        lat_max=30.0, lon_max=125.0,
        color="#e74c3c",
    ),
    "persian_gulf": Region(
        name="Golfe Persique", code="PG",
        lat_min=22.0, lon_min=48.0,
        lat_max=30.0, lon_max=60.0,
        color="#e67e22",
    ),
}


def get_region(code: str) -> Region:
    """Retourne une région par son code."""
    for r in REGIONS.values():
        if r.code == code:
            return r
    raise KeyError(f"Région inconnue : {code}")


def get_all_regions() -> list[Region]:
    return list(REGIONS.values())