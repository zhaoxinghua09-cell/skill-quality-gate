# AGENTS.md — skill-quality-gate

Machine-readable entry for AI agents.

## Purpose
Quality gate for AI skills — ship only what passes.

## Invocation
```bash
python scripts/quality_gate.py <SKILL.md> [--json]
```

## Output contract
- Structured JSON via `--json`; exit 0 = PASS, 1 = FAIL (fail-closed).
- Never publishes or deletes; analysis only.

## Rules
- No placeholders in outputs.

## Skill Marketplace
- lgd-skill-marketplace: https://github.com/zhaoxinghua09-cell/lgd-skill-marketplace — full skill catalog (enter from any skill).
