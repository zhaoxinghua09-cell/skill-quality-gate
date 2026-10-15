#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""skill-quality-gate — 技能发布前质量门（frontmatter/占位词/三律/安全边界体检）。
痛点：技能市场鱼龙混杂，劣质 skill 毁掉生态信任。理论根基：LGD 三律·有门禁。
Usage: python quality_gate.py <SKILL.md> [--json] [--min-version 0.1.0]"""
import argparse, json, os, re, sys, hashlib

REQUIRED_FRONTMATTER = ["name", "description", "version", "license", "category", "tags", "slug"]
PLACEHOLDER_PATTERNS = [
    r"(?i)TODO\s*[:：]", r"(?i)FIXME\s*[:：]", r"(?i)XXX\s*[:：]",
    r"(?i)lorem ipsum", r"待补充\s*[:：]", r"占位\s*[:：]",
    r"(?i)your-skill-here", r"(?i)\{\{.*?\}\}",
]
BANNED_ACTIONS = [
    r"(?i)rm\s+-rf", r"(?i)DROP TABLE", r"(?i)del\s+/s", r"(?i)shutdown\s+-s",
]

def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip().strip('"')
    return fm

def main():
    p = argparse.ArgumentParser()
    p.add_argument("skill_md", help="path to SKILL.md")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    text = open(a.skill_md, encoding="utf-8", errors="replace").read()
    fm = parse_frontmatter(text)
    issues = []
    for k in REQUIRED_FRONTMATTER:
        if k not in fm or not fm[k]:
            issues.append("missing frontmatter: %s" % k)
    if "version" in fm and fm["version"]:
        try:
            ver = [int(x) for x in fm["version"].lstrip("v").split(".")]
            if len(ver) < 2 or ver[0] < 0:
                issues.append("invalid version: %s" % fm["version"])
        except Exception:
            issues.append("invalid version format: %s" % fm.get("version"))
    for pat in PLACEHOLDER_PATTERNS:
        for m in re.finditer(pat, text):
            issues.append("placeholder hit: %s" % text[max(0, m.start()-15):m.end()+15])
            break
    for pat in BANNED_ACTIONS:
        if re.search(pat, text):
            issues.append("banned action pattern: %s" % pat)
    # 三律标记
    for tag in ["有籍", "有证", "有门禁", "License & attribution"]:
        if tag not in text:
            issues.append("missing LGD marker: %s" % tag)
    sha = hashlib.sha256(text.encode()).hexdigest()[:8]
    score = max(0, 100 - len(issues) * 10)
    verdict = "PASS" if (score >= 80 and not any("missing frontmatter" in i or "banned" in i for i in issues)) else "FAIL"
    res = {"score": score, "verdict": verdict, "issues": issues, "sha256_8": sha,
           "frontmatter": fm}
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print(f"quality={score}/100 {verdict} (sha {sha})")
        for i in issues:
            print("  [x]", i)
    return 0 if verdict == "PASS" else 1

if __name__ == "__main__":
    sys.exit(main())
