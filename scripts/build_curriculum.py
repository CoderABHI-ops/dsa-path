#!/usr/bin/env python3
"""Build curriculum/curriculum.json from the skill's module reference files.

Source of truth: skill/dsa-mentor/references/mNN-*.md (Part A: topic table + Core Practice Bank).
Run this again whenever you edit those files:  python scripts/build_curriculum.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "skill" / "dsa-mentor" / "references"
OUT = ROOT / "curriculum" / "curriculum.json"

PROBLEM = re.compile(
    r"^- LC (\d+) — (.+?) \((Easy|Medium|Hard)\)(?: — (https?://\S+))?(?: — (.*))?$"
)


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def first_number(text: str, default=None):
    m = re.search(r"(\d+(?:\.\d+)?)", text or "")
    return float(m.group(1)) if m else default


def parse_topics(part_a: str):
    head = part_a.split("### Core Practice Bank")[0]
    topics = []
    for line in head.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells[0] == "Topic" or set(cells[0]) <= set("-: "):
            continue
        if len(cells) < 7:
            continue
        name_raw = cells[0]
        # the Purpose cell may itself contain "|" characters, so index from both ends
        purpose = " | ".join(cells[1:-5])
        difficulty, prereqs, why, effort, freq = cells[-5:]
        note_match = re.search(r"\*\((.+?)\)\*", name_raw)
        name = re.sub(r"\s*\*\(.+?\)\*", "", name_raw).strip()
        topics.append({
            "id": slug(name),
            "name": name,
            "note": note_match.group(1) if note_match else None,
            "purpose": purpose,
            "difficulty": difficulty,
            "prereqs": prereqs,
            "effort_days": first_number(effort),
            "freq_pct": first_number(freq),
        })
    return topics


def parse_bank(part_a: str, module_no: int):
    if "### Core Practice Bank" not in part_a:
        return []
    bank = part_a.split("### Core Practice Bank")[1]
    group, items = "General", []
    for line in bank.splitlines():
        g = re.match(r"^\*\*(.+?)\*\*\s*$", line)
        if g:
            group = g.group(1).strip()
            continue
        m = PROBLEM.match(line.strip())
        if m:
            items.append({
                "lc": int(m.group(1)),
                "title": m.group(2).strip(),
                "difficulty": m.group(3),
                "group": group,
                "module": module_no,
                "url": m.group(4),
                "note": (m.group(5) or "").strip() or None,
            })
    return items


def main():
    modules, bank = [], {}
    for f in sorted(REF.glob("m[0-9][0-9]-*.md")):
        text = f.read_text(encoding="utf-8")
        head = re.match(r"# Module (\d+) of \d+: (.+)", text)
        if not head:
            raise SystemExit(f"Unexpected header in {f.name}")
        n, name = int(head.group(1)), head.group(2).strip()
        part_a = text.split("## PART A")[1].split("## PART B")[0]
        topics = parse_topics(part_a)
        items = parse_bank(part_a, n)
        for it in items:
            if it["lc"] in bank:
                bank[it["lc"]]["also_in_modules"].append(n)
            else:
                it["also_in_modules"] = []
                bank[it["lc"]] = it
        modules.append({"number": n, "name": name, "file": f.name,
                        "topics": topics,
                        "bank_size": len({i["lc"] for i in items})})
    data = {
        "totals": {"modules": len(modules),
                   "topics": sum(len(m["topics"]) for m in modules),
                   "bank_problems": len(bank)},
        "modules": modules,
        "bank": [bank[k] for k in sorted(bank)],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    t = data["totals"]
    print(f"Wrote {OUT.relative_to(ROOT)}: {t['modules']} modules, {t['topics']} topics, "
          f"{t['bank_problems']} unique bank problems")


if __name__ == "__main__":
    main()
