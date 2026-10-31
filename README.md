# AIxTech crypto intel v0.52: paper-only trading information system

Research harness for automated cryptocurrency **information** and paper strategy evaluation. Does not place live orders, does not store exchange secrets, and is not financial advice.

Builds on [zeekiankok92/aixtech-agent-harness-demo](https://github.com/zeekiankok92/aixtech-agent-harness-demo) secure AI-agent practices and prior kkzee92 versions (up to v0.51).

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![version](https://img.shields.io/badge/version-0.52.0-blue)
![mode](https://img.shields.io/badge/execution-paper%20only-orange)
![Licence](https://img.shields.io/badge/licence-MIT-green)

## Enhancements in v0.52

- Refined multi-factor strategies per asset class: adaptive EMA/ATR/Supertrend/Ichimoku/BB/Keltner/VWAP/MACD/Stochastic/Heikin-Ashi/Parabolic SAR/Donchian proxies, funding-rate and expanded on-chain (volume-flow, active-address, whale, smart-money, exchange inflow) proxies, volatility clustering (GARCH-style + ATR percentile), multi-horizon consistency, RSI/MACD/Stoch/Heikin divergence, regime clustering simulation, volume profile/delta, relative strength z-score.
- Portfolio-level adaptive correlation + isolation risk gate with dynamic vol-scaled sizing under high vol/anomaly/correlation/isolation/cluster regimes.
- Strengthened zero-trust cyber/data security architecture: expanded redaction (BIP39, WIF, PEM, AWS, GitHub PATs, high-entropy, Solana, session tokens, hardware wallet exports, partial seeds, quantum mentions, exchange API key patterns, JWT, private key hex), sealed multi-hash lineage (SHA-256 + SHA3-256 + BLAKE2b), entropy scoring, isolation forest-style anomaly, residency stamps, consecutive-action counters, source attestation, continuous verification proxies, PDPA-style tripwire, feed integrity checks.
- Nine asset classes with refined playbooks, risk caps, and class-specific cost models + confidence floors.
- Research only; synthetic fixtures recommended. AI-agent harness friendly with CI gates (lint, tests, secret scan style).

See [docs/asset-class-strategies.md](docs/asset-class-strategies.md) and [docs/security-architecture.md](docs/security-architecture.md).

## What it does

- Classifies into nine asset classes with enhanced multi-factor research rules.
- Labels regime (trend/range/stress) + volatility tier + anomaly score + correlation regime + cluster + isolation + relative strength.
- Scores signal then multi-gate risk (class caps, confidence, correlation, anomaly, isolation, drawdown, kill switch, vol scaling).
- Paper fills with class costs; hash-chained audit with multi-hash sealed lineage.
- No live execution, no secret storage.

| Asset class | Enhanced research rule | Risk cap | Cost |
|---|---|---|---|
| Major | Adaptive multi-factor EMA + Supertrend + Ichimoku + BB + Keltner + VWAP + MACD + Heikin-Ashi + SAR + Donchian + funding/on-chain proxies + correlation-adjusted outside stress | 8% | 8 bps |
| Large-cap alt | Volume-profile breakout + VWAP + MACD + multi-TF + relative strength z-score vs major + correlation filter + regime cluster + volume delta | 4% | 14 bps |
| Stablecoin | Adaptive peg deviation (15-50 bps) with volume confirmation | 0% | n/a |
| DeFi | Calm multi-scale + low anomaly + Supertrend + ADX + on-chain activity proxy + isolation check | 2% | 22 bps |
| Meme | Qualified burst + StochRSI + consistency + hard horizon + volume-flow decay + anomaly filter | 0.5% | 45 bps |
| L2 | Relative strength + MACD vs benchmark + adaptive MTF + correlation confirmation + cluster | 3% | 16 bps |
| RWA | Slow multi-scale + gap/anomaly halt + volume filter + isolation | 2% | 12 bps |
| Perpetual | Negative funding carry + contained drift + low anomaly + funding flip alert + correlation | 2% | 10 bps |
| AI-token | Hybrid burst + activity proxy + divergence + low isolation; strict horizon | 1% | 30 bps |

## Run

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src python -m crypto_intel.demo
PYTHONPATH=src pytest tests/ -q
```

## Controls

Paper-only mode guard. No trade keys. Class caps, confidence floors, kill switch, drawdown, correlation, anomaly, isolation gates. Hash-chained audit + sealed multi-hash lineage. Expanded redaction. PDPA-style tripwire. gitleaks and lint in CI recommended.

## Honesty

No live connector included. Strategy scores describe synthetic data. Not financial, legal, or compliance advice. Research only.
