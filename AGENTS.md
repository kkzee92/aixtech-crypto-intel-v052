# Agent rules for AIxTech crypto intel v0.52

This repository follows secure AI-agent practices inspired by zeekiankok92/aixtech-agent-harness-demo.

## Core rules

- **Paper-only**: Never implement or enable live order placement, withdrawals, or trade API key handling. Raise PermissionError on any live mode attempt.
- **No secrets**: Do not commit, log, or process real exchange keys, private keys, seeds, or personal data. Use synthetic fixtures only.
- **Human review required**: All changes must pass CI gates and human review before merge. Definition of Done = green CI + human approval.
- **Disclosure**: Mark AI-assisted commits with `AI-Assisted: yes` trailer.
- **Security first**: Expand redaction, maintain lineage, enforce risk gates. Prefer fail-closed.

## Task process

1. Write a task brief with acceptance criteria.
2. Agent proposes changes under AGENTS.md constraints.
3. Run local CI (lint, tests, secret scan, PDPA check).
4. Human reviews using checklist.
5. Merge only if DoD met.

See CONTRIBUTING.md and harness templates for more.
