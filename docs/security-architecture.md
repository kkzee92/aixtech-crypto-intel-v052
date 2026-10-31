# Security architecture (v0.52)

Version 0.52 extends the zero-trust control plane. Research design only; not a certified product or legal advice.

## Trust boundaries

Synthetic fixture or injected public ticker → Source attestation → Strategy research rules + regime/vol/correlation/cluster/isolation overlay → Multi-gate risk (class caps, confidence, correlation, anomaly, isolation, drawdown, kill switch, vol scaling) → Paper fill only → Hash-chained audit with multi-hash sealed lineage (SHA-256 + SHA3 + BLAKE2b), timestamps, residency, consecutive counter, continuous verification.

Trade/withdrawal keys refused. No order router. assert_paper_only. refuse_trade_secret.

## Roles

| Role | Allowed | Denied |
|---|---|---|
| Researcher | scan, backtest, read audit | place order, withdraw, enable live |
| Auditor | read audit, verify chain, scan | place order, withdraw, enable live |
| Operator | scan, kill switch, read audit | place order, withdraw, enable live |

No trader role.

## Data classes & redaction

Expanded patterns: BIP39, WIF, PEM, AWS keys, GitHub PATs, high-entropy strings, Solana base58, session cookies/tokens, hardware wallet exports, partial seed fragments, quantum-resistant algorithm mentions, exchange API key patterns, JWT, private key hex. Wallet addresses, personal data tripwired.

## Feed integrity & lineage

feed_status for jumps/staleness. attest_source + integrity_digest. Sealed multi-hash lineage. Entropy scoring, isolation forest-style anomaly detection, continuous verification proxies, ATR-percentile vol tier.

## Threats and controls

| Threat | Control |
|---|---|
| Secret committed | gitleaks + expanded redaction |
| Trade key paste | refuse_trade_secret |
| Fixture injection | SYNTHETIC label + attestation |
| Stale/jumped feed | feed_status |
| Oversized risk | Class caps, confidence, correlation, anomaly, isolation, vol scaling |
| Runaway loss | Drawdown halt + kill switch |
| Audit tamper | Hash chain + multi-hash seal |
| Live-order mistake | Mode guard + RBAC |
| Personal data | PDPA tripwire |

## Incident handling

1. Engage kill switch.
2. Freeze audit chain and record digests.
3. Rotate any pasted secret outside repo.
4. Human review before clearing kill switch.

## Operating rules

- Read-only market credentials only if ever added; never trade keys.
- Logs pass through redact.
- Default is research. Promotion to broker is separate human-approved system.
