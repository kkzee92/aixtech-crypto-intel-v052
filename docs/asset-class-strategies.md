# Asset-class strategy notes (v0.52)

These rules are research heuristics. Each class has an edge hypothesis, entry, invalidation, horizon, and size cap. They are not a promise of return. Version 0.52 adds Keltner/Donchian proxies, relative strength z-score, exchange-inflow on-chain, ATR-percentile vol, refined isolation, and vol-scaled sizing.

Regime labels:
- **trend**: multi-horizon move of at least 2.5% with controlled range and cluster alignment
- **range**: neither stress nor trend
- **stress**: elevated average bar range or volatility clustering; directional ideas stand aside

## Major (BTC, ETH)

Hypothesis: liquid majors trend with multi-factor confirmation. Adaptive EMA (period scaled by ATR), Supertrend, Ichimoku cloud, Bollinger + Keltner width, VWAP, MACD histogram, Heikin-Ashi consistency, Parabolic SAR, Donchian channel, funding-rate correlation proxy, on-chain volume-flow, active-address, whale, and exchange-inflow proxies, and cross-asset correlation filter. Mean reversion only in range with BB/Keltner squeeze and divergence. Cap 8%. Horizon 8-20 bars. Cost 8 bps. Confidence floor 0.55.

## Large-cap alt

Hypothesis: breakouts need volume profile and relative strength. Entry: close above prior high with volume ≥1.3x avg, VWAP confirmation, MACD, multi-TF consistency, relative strength z-score vs major, non-elevated correlation, regime cluster match, and volume delta. Cap 4%. Cost 14 bps.

## Stablecoin

Hypothesis: peg integrity. Adaptive deviation watch at 15 bps, depeg alert at 50 bps with volume confirmation. Risk gate forces size to zero.

## DeFi

Hypothesis: trend only in calm regimes. Stand aside if volatility clustering high, anomaly elevated, isolation score high, or ADX weak. Prefer Supertrend + on-chain activity proxy. Cap 2%. Cost 22 bps.

## Meme

Hypothesis: most bursts untradeable. Qualified long after ≥15% burst, rising volume-flow, StochRSI, consistency, extension <40%, and low isolation anomaly. Horizon 3 bars. Cap 0.5%. Cost 45 bps.

## L2

Hypothesis: relative strength vs benchmark. Requires non-stress benchmark, MACD confirmation, adaptive MTF, correlation filter, and cluster alignment. Cap 3%. Cost 16 bps.

## RWA

Hypothesis: slow trends. Halt on ≥8% gap or stress/anomaly/isolation. Volume filter preferred. Cap 2%, horizon 24 bars. Cost 12 bps.

## Perpetual

Hypothesis: negative funding with contained drift is carry. Funding ≥10 bps or flip is alert. Drift outside 4% blocks. Low anomaly and isolation required. Cap 2%. Cost 10 bps. Does not model liquidation or exchange risk.

## AI-token (hybrid)

Hypothesis: activity-driven bursts with meme filters. Requires on-chain activity proxy elevation + divergence + low isolation. Strict 4-bar horizon. Cap 1%. Cost 30 bps.

## Still out of scope

- Live order routing, withdrawal, and trade API keys.
- Broker adapter (separate human-approved system).
- Claims about future returns.
