import pandas as pd
import numpy as np
from pathlib import Path

def compute_basic_metrics(df: pd.DataFrame) -> dict:
    """
    Calcule les métriques de base sur un snapshot de trafic.

    Args:
        df : DataFrame chargé depuis le CSV

    Returns:
        Dictionnaire de métriques
    """

    in_flight = df[df["on_ground"] == False]
    on_ground = df[df["on_ground"] == True]

    metrics = {
        # ── Comptages ──
        "total_aircraft"     : len(df),
        "in_flight"          : len(in_flight),
        "on_ground"          : len(on_ground),
        "ground_ratio"       : len(on_ground) / len(df) if len(df) > 0 else 0,

        # ── Altitude (seulement ceux en vol) ──
        "altitude_mean"      : in_flight["altitude"].mean(),
        "altitude_median"    : in_flight["altitude"].median(),
        "altitude_std"       : in_flight["altitude"].std(),

        # ── Vitesse ──
        "velocity_mean"      : in_flight["velocity"].mean(),
        "velocity_median"    : in_flight["velocity"].median(),

        # ── Diversité ──
        "unique_countries"   : df["origin_country"].nunique(),
        "unique_flights"     : df["icao24"].nunique(),

        # ── Timestamp ──
        "captured_at"        : df["timestamp"].iloc[0],
    }

    return metrics


def compute_country_breakdown(df: pd.DataFrame) -> pd.DataFrame:
    """
    Retourne un tableau de métriques par pays.

    Utile pour détecter : un pays qui disparaît soudainement.
    """

    breakdown = (
        df.groupby("origin_country")
        .agg(
            total        = ("icao24",    "count"),
            in_flight    = ("on_ground", lambda x: (~x).sum()),
            on_ground    = ("on_ground", "sum"),
            alt_mean     = ("altitude",  "mean"),
            vel_mean     = ("velocity",  "mean"),
        )
        .sort_values("total", ascending=False)
        .reset_index()
    )

    return breakdown


def compute_altitude_distribution(df: pd.DataFrame) -> pd.DataFrame:
    """
    Distribue les avions en tranches d'altitude.

    Tranche       | Signification
    0 - 1000 m    | Décollage / atterrissage
    1000 - 5000 m | Vol court courrier / hélicos
    5000 - 9000 m | Croisière court/moyen courrier
    9000 m+       | Long courrier / haute altitude
    """

    bins   = [0, 1000, 5000, 9000, 15000]
    labels = ["0-1000m", "1000-5000m", "5000-9000m", "9000m+"]

    in_flight = df[df["on_ground"] == False].copy()

    # pd.cut() découpe une colonne continue en catégories
    in_flight["alt_band"] = pd.cut(
        in_flight["altitude"],
        bins=bins,
        labels=labels,
        right=True
    )

    distribution = (
        in_flight["alt_band"]
        .value_counts()
        .sort_index()
        .reset_index()
    )
    distribution.columns = ["altitude_band", "count"]

    return distribution


def print_report(df: pd.DataFrame) -> None:
    """
    Affiche un rapport complet dans le terminal.
    """

    metrics   = compute_basic_metrics(df)
    countries = compute_country_breakdown(df)
    altitudes = compute_altitude_distribution(df)

    print("\n" + "═" * 50)
    print("  RAPPORT D'ANALYSE — TRAFIC AÉRIEN")
    print("═" * 50)

    print(f"\n📅 Capture        : {metrics['captured_at']}")
    print(f"✈  Total avions   : {metrics['total_aircraft']}")
    print(f"🛫 En vol         : {metrics['in_flight']}")
    print(f"🅿  Au sol         : {metrics['on_ground']} ({metrics['ground_ratio']:.1%})")
    print(f"🌍 Pays           : {metrics['unique_countries']}")

    print(f"\n── Altitude (avions en vol) ──")
    print(f"   Moyenne  : {metrics['altitude_mean']:.0f} m")
    print(f"   Médiane  : {metrics['altitude_median']:.0f} m")
    print(f"   Écart-type : {metrics['altitude_std']:.0f} m")

    print(f"\n── Vitesse ──")
    print(f"   Moyenne  : {metrics['velocity_mean']:.0f} m/s")
    print(f"   Médiane  : {metrics['velocity_median']:.0f} m/s")

    print(f"\n── Distribution altitude ──")
    for _, row in altitudes.iterrows():
        bar = "█" * int(row["count"] / metrics["in_flight"] * 30)
        print(f"   {row['altitude_band']:12} {bar} {row['count']}")

    print(f"\n── Top 10 pays ──")
    for _, row in countries.head(10).iterrows():
        print(f"   {row['origin_country']:25} {row['total']:4} avions  "
              f"alt moy: {row['alt_mean']:.0f}m")