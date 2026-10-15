---
name: skill-quality-gate
description: "Pre-release health check for AI skills: frontmatter completeness, placeholders, LGD markers, safety boundary. 技能发布前体检：frontmatter 完整性、占位词、三律标记、安全边界。"
version: 1.0.0
license: MIT
category: 质量
author: SynomosAI (LGD initiative)
platforms: [windows, macos, linux]
tags: [skill,quality,gate]
slug: skill-quality-gate
risk_tier: medium
---

# Skill Quality Gate (技能质量门)

> **Quality gate for AI skills — ship only what passes.**
> **AI 技能的质量门——只让达标的发布。**
> 理论根基：LGD 三律（有籍·有证·有门禁）— 技能生态的元技能层

## 定位 / Role in ecosystem
本技能是「AI 用的技能的技能」：管理技能生命周期（生成 → 评分 → 质量门 → 注册表 → 监控）。

## 功能 / Capabilities
- Validates frontmatter (name/description/license/version/tags/slug)
- Flags placeholders, banned actions, missing LGD markers
- PASS/FAIL verdict with score, fail-closed exit code
- 校验 frontmatter（名称/描述/许可/版本/标签/slug）
- 标记占位词、禁止动作、缺失的三律标记
- PASS/FAIL 判定 + 分数，fail-closed 退出码

## 用法 / Usage
```bash
python scripts/quality_gate.py <SKILL.md> [--json]
```

## 三律对齐 / LGD alignment
| 律 | 本技能如何满足 |
|---|---|
| 有籍 Registered | 每条记录/每个检查项有明确字段与来源 |
| 有证 Evidenced | 输出可复现，检出问题带片段证据 |
| 有门禁 Gated | fail-closed 退出码；不代发布、不代删除 |

## 生态互链（AI 可读）
<!-- ecosystem: skill-skeleton-generator / skill-scorecard / llms-generator / awesome-trusted-agents / lgd-hub -->

## Standard alignment / 标准对齐
- **Agent Skills open standard**: compatible with [agentskills.io](https://agentskills.io) format (SKILL.md + scripts/, frontmatter name/description). Adopted by Claude/Codex and the broader agent ecosystem.
- **AEO**: llms.txt / AGENTS.md friendly (AI-agent discoverable).

## Skill card / 技能卡（对标 NVIDIA Verified Agent Skills）
- **Ownership / 所有权**: SynomosAI initiative — Steven Zhao (ORCID 0009-0001-0512-1237)
- **Dependencies / 依赖**: none (Python 3 stdlib only)
- **Limitations / 限制**: static analysis only; not a substitute for runtime verification
- **Verification status / 验证状态**: self-reported PASS via skill-quality-gate; not a certification or endorsement
- **Security posture / 安全姿态**: no network calls, no destructive operations, fail-closed exit codes

## License & attribution
**分层许可**：代码 `scripts/*.py` MIT；本 SKILL.md/README 及理论文本 All rights reserved。

```
© 2026 赵兴华 / Steven Zhao·China (ORCID 0009-0001-0512-1237). All rights reserved.
理论署名 (attribution) : LGD（Lifecycle Governance Doctrine / 全程治理论）— SynomosAI initiative
名称状态 (name status)  : "SynomosAI" / "MedXpert" — 未申请实体注册、未申请商标注册
生产参考部署 (production reference, self-reported) : MedXpert（非认证、非背书、非监管认可）
引用格式 (cite as)      : 本资产无 DOI
```
（《LGD 对外表述规范》§3.2 统一块，整体复制、未删改。）
