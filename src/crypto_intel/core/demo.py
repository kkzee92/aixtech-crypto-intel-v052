"""Simple demo runner for paper-only research."""
from crypto_intel.strategies.asset_class import score_signal, ASSET_CLASSES
from crypto_intel.security.audit import seal_event
from crypto_intel.security.redact import redact

def run_demo():
    print("AIxTech crypto intel v0.52 demo (paper-only)")
    print("Synthetic data only. No live execution. Builds on zeekiankok92 harness.")
    # Sample synthetic factors
    factors = {"strength": 0.72, "anomaly": 0.15, "correlation": 0.3, "isolation": 0.1, "vol_tier": 0.4}
    for cls in ["major", "large_alt", "meme", "ai_token"]:
        score = score_signal(cls, "trend", factors)
        print(f"{cls}: score={score:.3f} (cap={ASSET_CLASSES[cls]['risk_cap']})")
    event = seal_event({"action": "paper_scan", "asset": "BTC", "score": 0.6})
    print("Sealed audit:", redact(str(event)))
    print("Regime clustering, multi-factor strategies, zero-trust security active.")
