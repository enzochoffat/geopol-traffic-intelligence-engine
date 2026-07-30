import pandas as pd
import numpy as np
from pathlib import Path


def build_timeseries(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrège le DataFrame combiné en une série temporelle.
    Une ligne par snapshot = évolution dans le temps.

    Args:
        df : DataFrame combiné (tous les snapshots)

    Returns:
        DataFrame avec une ligne par timestamp
    """

    # groupby("timestamp") → groupe toutes les lignes du même snapshot
    # puis on calcule les métriques pour chaque groupe
    ts = (
        df.groupby("timestamp")
        .agg(
            total_aircraft   = ("icao24",    "count"),
            in_flight        = ("on_ground", lambda x: (~x).sum()),
            on_ground        = ("on_ground", "sum"),
            unique_countries = ("origin_country", "nunique"),
            altitude_mean    = ("altitude",  "mean"),
            velocity_mean    = ("velocity",  "mean"),
        )
        .reset_index()
        .sort_values("timestamp")
    )

    # Calcule le ratio avions au sol
    ts["ground_ratio"] = ts["on_ground"] / ts["total_aircraft"]

    # Calcule la variation absolue entre chaque snapshot
    # diff() = valeur[t] - valeur[t-1]
    ts["delta_total"]    = ts["total_aircraft"].diff()
    ts["delta_inflight"] = ts["in_flight"].diff()

    # Calcule la variation en % entre chaque snapshot
    ts["pct_change"] = ts["total_aircraft"].pct_change() * 100

    return ts


def detect_anomalies(ts: pd.DataFrame, z_threshold: float = 2.0) -> pd.DataFrame:
    """
    Détecte les snapshots anormaux via Z-score.

    Le Z-score mesure combien d'écarts-types une valeur
    est éloignée de la moyenne.

    Z > 2.0  → valeur inhabituellement haute
    Z < -2.0 → valeur inhabituellement basse

    Args:
        ts           : série temporelle (output de build_timeseries)
        z_threshold  : seuil de détection (2.0 = top/bottom 5%)

    Returns:
        DataFrame des snapshots anormaux uniquement
    """

    mean = ts["total_aircraft"].mean()
    std  = ts["total_aircraft"].std()

    # Évite la division par zéro si std = 0
    if std == 0:
        print("[Anomaly] Pas assez de variance pour détecter des anomalies.")
        return pd.DataFrame()

    # Calcule le Z-score pour chaque snapshot
    ts["z_score"] = (ts["total_aircraft"] - mean) / std

    # Filtre les snapshots au-delà du seuil
    anomalies = ts[ts["z_score"].abs() > z_threshold].copy()

    # Ajoute une étiquette lisible
    anomalies["anomaly_type"] = anomalies["z_score"].apply(
        lambda z: "📈 PIC ANORMAL" if z > 0 else "📉 CHUTE ANORMALE"
    )

    return anomalies


def print_timeseries_report(ts: pd.DataFrame) -> None:
    """
    Affiche un rapport de la série temporelle dans le terminal.
    """

    anomalies = detect_anomalies(ts)

    print("\n" + "═" * 55)
    print("  RAPPORT SÉRIE TEMPORELLE")
    print("═" * 55)
    print(f"\n  Snapshots analysés : {len(ts)}")
    print(f"  Période            : {ts['timestamp'].min()} → {ts['timestamp'].max()}")
    print(f"\n── Statistiques globales ──")
    print(f"  Avions moyen       : {ts['total_aircraft'].mean():.0f}")
    print(f"  Avions min         : {ts['total_aircraft'].min()} ({ts.loc[ts['total_aircraft'].idxmin(), 'timestamp']})")
    print(f"  Avions max         : {ts['total_aircraft'].max()} ({ts.loc[ts['total_aircraft'].idxmax(), 'timestamp']})")
    print(f"  Écart-type         : {ts['total_aircraft'].std():.1f}")

    print(f"\n── Évolution snapshot par snapshot ──")
    for _, row in ts.iterrows():
        # Flèche selon variation
        if pd.isna(row["delta_total"]):
            arrow = "  "
        elif row["delta_total"] > 0:
            arrow = "↑ "
        elif row["delta_total"] < 0:
            arrow = "↓ "
        else:
            arrow = "→ "

        delta_str = f"({row['delta_total']:+.0f})" if not pd.isna(row["delta_total"]) else "     "

        print(
            f"  {str(row['timestamp'])[11:16]}  "
            f"{arrow}{row['total_aircraft']:4.0f} avions {delta_str:8}  "
            f"alt: {row['altitude_mean']:.0f}m  "
            f"pays: {row['unique_countries']:.0f}"
        )

    if len(anomalies) > 0:
        print(f"\n── ⚠  Anomalies détectées ──")
        for _, row in anomalies.iterrows():
            print(
                f"  {row['anomaly_type']}  "
                f"{str(row['timestamp'])[11:16]}  "
                f"{row['total_aircraft']:.0f} avions  "
                f"Z={row['z_score']:.2f}"
            )
    else:
        print(f"\n  ✅ Aucune anomalie détectée sur cette période.")