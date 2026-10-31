"""Asset-class specific research strategies (paper-only). v0.52 refinements."""

ASSET_CLASSES = {
    "major": {"risk_cap": 0.08, "cost_bps": 8, "confidence_floor": 0.55},
    "large_alt": {"risk_cap": 0.04, "cost_bps": 14, "confidence_floor": 0.60},
    "stable": {"risk_cap": 0.0, "cost_bps": 0, "confidence_floor": 0.0},
    "defi": {"risk_cap": 0.02, "cost_bps": 22, "confidence_floor": 0.65},
    "meme": {"risk_cap": 0.005, "cost_bps": 45, "confidence_floor": 0.70},
    "l2": {"risk_cap": 0.03, "cost_bps": 16, "confidence_floor": 0.58},
    "rwa": {"risk_cap": 0.02, "cost_bps": 12, "confidence_floor": 0.60},
    "perp": {"risk_cap": 0.02, "cost_bps": 10, "confidence_floor": 0.55},
    "ai_token": {"risk_cap": 0.01, "cost_bps": 30, "confidence_floor": 0.68},
}

def score_signal(asset_class: str, regime: str, factors: dict) -> float:
    """Multi-factor score with vol/anomaly/correlation/isolation adjustments. Research only."""
    if regime == "stress" or factors.get("anomaly", 0) > 0.75 or factors.get("isolation", 0) > 0.8:
        return 0.0
    base = factors.get("strength", 0.5)
    # Volatility scaling
    vol = factors.get("vol_tier", 0.5)
    if vol > 0.7:
        base *= 0.6
    # Correlation penalty for alts/meme
    if asset_class in ("large_alt", "meme", "ai_token") and factors.get("correlation", 0) > 0.6:
        base *= 0.7
    # Isolation forest-style
    if factors.get("isolation", 0) > 0.5:
        base *= 0.75
    cfg = ASSET_CLASSES.get(asset_class, {})
    score = min(base, cfg.get("risk_cap", 0.0))
    if score < cfg.get("confidence_floor", 0.0):
        return 0.0
    return round(score, 4)
