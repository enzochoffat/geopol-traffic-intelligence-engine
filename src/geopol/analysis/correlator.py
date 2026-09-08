import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path


def correlate_event_with_traffic(
    event: dict,
    ts: pd.DataFrame,
    window_hours: int = 24,
) -> dict:
    """
    Corrèle un événement géopolitique avec la série temporelle
    de trafic aérien.

    Args:
        event        : dict avec clés {name, lat, lon, timestamp, goldstein}
        ts           : série temporelle (output de build_timeseries)
        window_hours : fenêtre d'analyse en heures (avant ET après)

    Returns:
        Dictionnaire de corrélation avec scores
    """

    event_time = pd.to_datetime(event["timestamp"])

    # ── Découpe la fenêtre temporelle ──
    before_mask = (
        (ts["timestamp"] >= event_time - timedelta(hours=window_hours)) &
        (ts["timestamp"] <  event_time)
    )
    after_mask = (
        (ts["timestamp"] >  event_time) &
        (ts["timestamp"] <= event_time + timedelta(hours=window_hours))
    )

    before = ts[before_mask]
    after  = ts[after_mask]

    # ── Calcule les moyennes avant / après ──
    avg_before = before["total_aircraft"].mean() if len(before) > 0 else None
    avg_after  = after["total_aircraft"].mean()  if len(after)  > 0 else None

    # ── Calcule la variation ──
    if avg_before is not None and avg_after is not None and avg_before > 0:
        delta_pct = ((avg_after - avg_before) / avg_before) * 100
    else:
        delta_pct = None

    # ── Calcule l'altitude avant / après ──
    alt_before = before["altitude_mean"].mean() if len(before) > 0 else None
    alt_after  = after["altitude_mean"].mean()  if len(after)  > 0 else None

    if alt_before is not None and alt_after is not None and alt_before > 0:
        alt_delta_pct = ((alt_after - alt_before) / alt_before) * 100
    else:
        alt_delta_pct = None

    # ── Score de corrélation simple ──
    # On combine variation trafic + score Goldstein
    # Goldstein négatif + trafic en baisse = signal fort
    correlation_signal = _compute_signal(
        delta_pct=delta_pct,
        goldstein=event.get("goldstein", 0),
        alt_delta_pct=alt_delta_pct,
    )

    return {
        # Infos événement
        "event_name"       : event["name"],
        "event_time"       : event_time,
        "event_goldstein"  : event.get("goldstein", 0),
        "event_lat"        : event.get("lat"),
        "event_lon"        : event.get("lon"),

        # Snapshots analysés
        "snapshots_before" : len(before),
        "snapshots_after"  : len(after),

        # Trafic
        "avg_traffic_before" : avg_before,
        "avg_traffic_after"  : avg_after,
        "traffic_delta_pct"  : delta_pct,

        # Altitude
        "avg_altitude_before" : alt_before,
        "avg_altitude_after"  : alt_after,
        "altitude_delta_pct"  : alt_delta_pct,

        # Signal final
        "correlation_signal"  : correlation_signal,
        "signal_label"        : _signal_label(correlation_signal),
    }


def _compute_signal(
    delta_pct: float,
    goldstein: float,
    alt_delta_pct: float,
) -> float:
    """
    Calcule un score de signal de corrélation entre 0 et 1.

    Logique :
    - Goldstein très négatif + trafic en baisse = signal fort
    - Goldstein positif + trafic stable          = signal faible

    Returns:
        Score entre 0.0 (aucune corrélation) et 1.0 (forte corrélation)
    """

    if delta_pct is None or goldstein is None:
        return 0.0

    # Normalise Goldstein : [-10, +10] → [1, 0]
    # Plus c'est conflictuel (négatif), plus le poids est fort
    goldstein_weight = max(0.0, min(1.0, (10 - goldstein) / 20))

    # Normalise la variation trafic
    # Une chute de 20%+ = signal max
    traffic_signal = min(abs(delta_pct) / 20.0, 1.0)

    # Bonus si l'altitude aussi varie (contournement de zone)
    alt_bonus = 0.0
    if alt_delta_pct is not None and abs(alt_delta_pct) > 5:
        alt_bonus = 0.1

    # Score pondéré
    score = (goldstein_weight * 0.4) + (traffic_signal * 0.5) + alt_bonus
    return round(min(score, 1.0), 3)


def _signal_label(score: float) -> str:
    """Traduit un score numérique en étiquette lisible."""
    if score >= 0.7:
        return "🔴 SIGNAL FORT"
    elif score >= 0.4:
        return "🟡 SIGNAL MODÉRÉ"
    elif score >= 0.2:
        return "🟢 SIGNAL FAIBLE"
    else:
        return "⚪ PAS DE SIGNAL"


def correlate_multiple_events(
    events: list[dict],
    ts: pd.DataFrame,
    window_hours: int = 24,
) -> pd.DataFrame:
    """
    Corrèle une liste d'événements avec la série temporelle.

    Returns:
        DataFrame trié par force du signal
    """

    results = []
    for event in events:
        result = correlate_event_with_traffic(event, ts, window_hours)
        results.append(result)

    df = pd.DataFrame(results)

    if not df.empty:
        df = df.sort_values("correlation_signal", ascending=False)

    return df


def print_correlation_report(correlations: pd.DataFrame) -> None:
    """
    Affiche le rapport de corrélation dans le terminal.
    """

    print("\n" + "═" * 60)
    print("  RAPPORT DE CORRÉLATION — Trafic ↔ Géopolitique")
    print("═" * 60)

    if correlations.empty:
        print("  Aucune corrélation calculée.")
        return

    for _, row in correlations.iterrows():
        print(f"\n  {row['signal_label']}")
        print(f"  Événement  : {row['event_name']}")
        print(f"  Date       : {row['event_time']}")
        print(f"  Goldstein  : {row['event_goldstein']}")
        print(f"  ─────────────────────────────")

        if row['avg_traffic_before']:
            print(f"  Trafic avant   : {row['avg_traffic_before']:.0f} avions")
            print(f"  Trafic après   : {row['avg_traffic_after']:.0f} avions")
            print(f"  Variation      : {row['traffic_delta_pct']:+.1f}%")

        if row['avg_altitude_before']:
            print(f"  Altitude avant : {row['avg_altitude_before']:.0f} m")
            print(f"  Altitude après : {row['avg_altitude_after']:.0f} m")
            print(f"  Var. altitude  : {row['altitude_delta_pct']:+.1f}%")

        print(f"  Score signal   : {row['correlation_signal']}")