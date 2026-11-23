#!/usr/bin/env python3
"""dsa.py: tiny CLI that keeps progress.yaml, solutions and the README dashboard in sync.

Commands
  snapshot [FILE]   merge a pasted dsa-snapshot block (FILE or stdin) into progress.yaml
  export            print a dsa-snapshot block to paste into the Gemini skill next session
  new LC [opts]     scaffold a Java solution + JUnit test for a LeetCode problem
  solved LC [opts]  mark a problem solved
  due               list spaced reviews that are due or coming up
  status            short progress summary in the terminal
  dashboard         regenerate the README dashboard block, mistakes.md and docs/progress.json

Needs Python 3.10+ and PyYAML (pip install pyyaml). Set DSA_TODAY=YYYY-MM-DD to override "today".
"""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import json
import os
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
PROGRESS = ROOT / "progress.yaml"
CURRICULUM = ROOT / "curriculum" / "curriculum.json"
README = ROOT / "README.md"
DOCS_JSON = ROOT / "docs" / "progress.json"
MISTAKES_MD = ROOT / "mistakes.md"
START, END = "<!-- DASHBOARD:START -->", "<!-- DASHBOARD:END -->"
JAVA_KEYWORDS = {
    "abstract", "assert", "boolean", "break", "byte", "case", "catch", "char", "class", "const",
    "continue", "default", "do", "double", "else", "enum", "extends", "final", "finally", "float",
    "for", "goto", "if", "implements", "import", "instanceof", "int", "interface", "long", "native",
    "new", "package", "private", "protected", "public", "return", "short", "static", "strictfp",
    "super", "switch", "synchronized", "this", "throw", "throws", "transient", "try", "void",
    "volatile", "while", "true", "false", "null", "var", "record", "yield", "sealed", "permits",
}


# ----------------------------------------------------------------------------- helpers
def today() -> str:
    return os.environ.get("DSA_TODAY") or dt.date.today().isoformat()


def iso(value):
    if value is None:
        return None
    if isinstance(value, (dt.date, dt.datetime)):
        return value.strftime("%Y-%m-%d")
    return str(value)


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(text).lower()).strip()


def short_name(name: str) -> str:
    return re.sub(r"\s*\(.*?\)", "", name).strip()


def load_curriculum() -> dict:
    if not CURRICULUM.exists():
        sys.exit("curriculum/curriculum.json missing. Run: python scripts/build_curriculum.py")
    return json.loads(CURRICULUM.read_text(encoding="utf-8"))


DEFAULT_PROGRESS = {
    "meta": {"schema": 1, "created": None, "path": "syllabus"},
    "state": {},
    "topics": {},
    "patterns": {},
    "weak_areas": [],
    "reviews": [],
    "homework": [],
    "mistakes": [],
    "deviations": [],
    "problems": {},
    "history": [],
}


def load_progress() -> dict:
    data = {}
    if PROGRESS.exists():
        data = yaml.safe_load(PROGRESS.read_text(encoding="utf-8")) or {}
    for key, default in DEFAULT_PROGRESS.items():
        if key not in data or data[key] is None:
            data[key] = json.loads(json.dumps(default))
    return data


def save_progress(data: dict) -> None:
    header = ("# Source of truth for your DSA progress. Edited by scripts/dsa.py (and by hand if you must).\n"
              "# Dates are YYYY-MM-DD strings. The README dashboard is generated from this file.\n")
    body = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100)
    PROGRESS.write_text(header + body, encoding="utf-8", newline="\n")


class TopicIndex:
    """Maps free-text topic names (as the mentor writes them) to canonical syllabus topics."""

    def __init__(self, cur: dict):
        self.by_norm: dict[str, tuple[int, str]] = {}
        for m in cur["modules"]:
            for t in m["topics"]:
                for key in {norm(t["name"]), norm(short_name(t["name"]))}:
                    self.by_norm.setdefault(key, (m["number"], t["name"]))

    def match(self, name: str):
        n = norm(name)
        if n in self.by_norm:
            return self.by_norm[n]
        contained = [k for k in self.by_norm if len(n) >= 4 and (n in k or k in n)]
        if len(contained) == 1:
            return self.by_norm[contained[0]]
        close = difflib.get_close_matches(n, list(self.by_norm), n=1, cutoff=0.72)
        return self.by_norm[close[0]] if close else None


# ----------------------------------------------------------------------------- snapshot
def extract_snapshot(text: str):
    marker = "```dsa-snapshot"
    idx = text.rfind(marker)
    if idx >= 0:
        rest = text[idx + len(marker):]
        end = rest.find("```")
        body = rest[:end] if end >= 0 else rest
    else:
        fences = re.findall(r"```[ \t]*[\w-]*[ \t]*\n(.*?)```", text, re.S)
        body = fences[-1] if fences else text
    body = "\n".join(l for l in body.splitlines() if not l.strip().startswith("```"))
    try:
        data = yaml.safe_load(body)
    except yaml.YAMLError as exc:
        sys.exit(f"Could not parse the snapshot as YAML: {exc}")
    if not isinstance(data, dict):
        sys.exit("Snapshot is empty or not a YAML mapping. Paste the whole dsa-snapshot block.")
    return data.get("SESSION_STATE", data)


def stage_of(status: str):
    m = re.search(r"stage\s*(\d)", status or "", re.I)
    return int(m.group(1)) if m else None


def merge_snapshot(prog: dict, snap: dict, idx: TopicIndex, cur: dict, day: str) -> list[str]:
    log: list[str] = []
    day = iso(snap.get("last_updated")) or day
    module_no = snap.get("module_number")

    state = prog["state"]
    for key in ("module_number", "module_name", "current_topic", "topic_status"):
        if snap.get(key) is not None:
            state[key] = snap[key]
    state["last_updated"] = day
    if snap.get("path"):
        prog["meta"]["path"] = snap["path"]

    def topic_entry(name: str):
        hit = idx.match(name)
        if hit:
            return hit[1], hit[0]
        log.append(f"  ! topic not in syllabus table, stored as written: {name!r}")
        return str(name), module_no

    for n in snap.get("modules_completed") or []:
        module = next((m for m in cur["modules"] if m["number"] == n), None)
        for t in (module["topics"] if module else []):
            entry = prog["topics"].setdefault(t["name"], {})
            entry.update({"module": n, "status": "completed"})
            entry.setdefault("completed_on", day)

    for name in snap.get("topics_completed_in_module") or []:
        canon, mod = topic_entry(name)
        entry = prog["topics"].setdefault(canon, {})
        entry.update({"module": mod, "status": "completed"})
        entry.setdefault("completed_on", day)
    if snap.get("current_topic"):
        canon, mod = topic_entry(snap["current_topic"])
        status = str(snap.get("topic_status") or "IN_PROGRESS")
        entry = prog["topics"].setdefault(canon, {})
        entry["module"] = mod
        if status.upper().startswith("COMPLETED"):
            entry["status"] = "completed"
            entry.setdefault("completed_on", day)
        else:
            if entry.get("status") != "completed":
                entry["status"] = "in_progress"
            stage = stage_of(status)
            if stage:
                entry["stage"] = stage
        state["current_topic"] = canon

    for p in snap.get("pattern_mastery") or []:
        if isinstance(p, dict) and p.get("pattern"):
            prog["patterns"][str(p["pattern"])] = {
                "questions_solved": p.get("questions_solved", 0),
                "confidence": p.get("confidence"),
            }

    if "weak_areas_to_reinforce" in snap:
        prog["weak_areas"] = [str(x) for x in snap["weak_areas_to_reinforce"] or []]
    if "homework_assigned" in snap:
        prog["homework"] = [str(x) for x in snap["homework_assigned"] or []]
    if "reviews_due" in snap:
        reviews = []
        for r in snap["reviews_due"] or []:
            if isinstance(r, dict):
                reviews.append({"topic": str(r.get("topic")), "due": iso(r.get("due")),
                                "type": str(r.get("type") or "review")})
        prog["reviews"] = reviews

    known = {m["text"] for m in prog["mistakes"]}
    for item in snap.get("mistakes_log") or []:
        text = item.get("text") if isinstance(item, dict) else str(item)
        if text and text not in known:
            prog["mistakes"].append({"date": day, "text": text})
            known.add(text)
    for item in snap.get("deviations") or []:
        text = str(item)
        if text and text not in {d["text"] for d in prog["deviations"]}:
            prog["deviations"].append({"date": day, "text": text})

    row = {"date": day, "module": module_no, "topic": state.get("current_topic"),
           "status": state.get("topic_status")}
    if not prog["history"] or prog["history"][-1] != row:
        prog["history"].append(row)

    log.insert(0, f"Merged snapshot dated {day}: module {module_no}, topic {state.get('current_topic')!r}, "
                  f"{len(prog['reviews'])} review(s) scheduled.")
    return log


def cmd_snapshot(args):
    text = Path(args.file).read_text(encoding="utf-8") if args.file else sys.stdin.read()
    if not text.strip():
        sys.exit("Nothing to read. Paste the snapshot, then press Ctrl-D (Ctrl-Z then Enter on Windows),"
                 " or pass a file: python scripts/dsa.py snapshot snap.txt")
    cur = load_curriculum()
    prog = load_progress()
    prog["meta"]["created"] = prog["meta"].get("created") or today()
    for line in merge_snapshot(prog, extract_snapshot(text), TopicIndex(cur), cur, today()):
        print(line)
    save_progress(prog)
    build_outputs(prog, cur)
    print("progress.yaml, README dashboard, mistakes.md and docs/progress.json updated.")


# ----------------------------------------------------------------------------- export
def completed_topics_by_module(prog: dict) -> dict[int, list[str]]:
    out: dict[int, list[str]] = {}
    for name, t in prog["topics"].items():
        if t.get("status") == "completed" and t.get("module") is not None:
            out.setdefault(int(t["module"]), []).append(name)
    return out


def modules_completed(prog: dict, cur: dict) -> list[int]:
    done = completed_topics_by_module(prog)
    return [m["number"] for m in cur["modules"]
            if m["topics"] and {t["name"] for t in m["topics"]} <= set(done.get(m["number"], []))]


def cmd_export(_args):
    cur, prog = load_curriculum(), load_progress()
    st = prog["state"]
    if not st:
        print("No progress recorded yet. Start the skill without a snapshot.")
        return
    mod = st.get("module_number")
    done = completed_topics_by_module(prog).get(mod, [])
    module = next((m for m in cur["modules"] if m["number"] == mod), None)
    pending = [t["name"] for t in module["topics"] if t["name"] not in done] if module else []
    snap = {"SESSION_STATE": {
        "last_updated": st.get("last_updated"),
        "path": prog["meta"].get("path", "syllabus"),
        "modules_completed": modules_completed(prog, cur),
        "module_number": mod,
        "module_name": st.get("module_name"),
        "current_topic": st.get("current_topic"),
        "topic_status": st.get("topic_status"),
        "topics_completed_in_module": done,
        "topics_pending_in_module": pending,
        "pattern_mastery": [{"pattern": k, **v} for k, v in prog["patterns"].items()],
        "weak_areas_to_reinforce": prog["weak_areas"],
        "homework_assigned": prog["homework"],
        "reviews_due": prog["reviews"],
        "mistakes_log": [m["text"] for m in prog["mistakes"][-8:]],
        "deviations": [d["text"] for d in prog["deviations"][-5:]],
    }}
    print("```dsa-snapshot")
    print(yaml.safe_dump(snap, sort_keys=False, allow_unicode=True, width=100).rstrip())
    print("```")


# ----------------------------------------------------------------------------- problems
def java_slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_") or "misc"
    if s[0].isdigit() or s in JAVA_KEYWORDS:
        s = "p_" + s
    return s


def pascal(text: str) -> str:
    return "".join(w[0].upper() + w[1:] for w in re.findall(r"[A-Za-z0-9]+", text))


SOLUTION_TEMPLATE = """package {pkg};

/**
 * LeetCode {num}: {title} ({difficulty})
 * Module {module} | Group: {group}
 *
 * Pattern:
 * Invariant:
 * Time: O(?)   Space: O(?)
 * Gotchas (edge cases, int overflow, recursion depth):
 */
public final class {cls} {{

    private {cls}() {{}}

    /** Paste your accepted LeetCode solution here. Keep the class name Solution. */
    public static class Solution {{
        // TODO
    }}
}}
"""

TEST_TEMPLATE = """package {pkg};

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class {cls}Test {{

    private final {cls}.Solution solution = new {cls}.Solution();

    @Test
    void examplesFromStatement() {{
        // assertEquals(expected, solution.method(args));
    }}

    @Test
    void edgeCases() {{
        // empty input, single element, duplicates, negatives, max constraints (int overflow?)
    }}
}}
"""


def cmd_new(args):
    cur, prog = load_curriculum(), load_progress()
    bank = {b["lc"]: b for b in cur["bank"]}
    num = args.lc
    entry = bank.get(num)
    title = args.title or (entry["title"] if entry else None)
    if not title:
        sys.exit(f"LC {num} is not in the Core Practice Bank, so pass --title \"...\".")
    difficulty = (entry or {}).get("difficulty", "?")
    group = args.topic or (entry or {}).get("group") or "Misc"
    module = args.module if args.module is not None else (entry["module"] if entry else None)
    pkg = f"dsa.m{module:02d}.{java_slug(group)}" if module is not None else f"dsa.extra.{java_slug(group)}"
    cls = f"Lc{num:04d}{pascal(title)}"
    rel = Path(*pkg.split("."))
    main_file = ROOT / "src" / "main" / "java" / rel / f"{cls}.java"
    test_file = ROOT / "src" / "test" / "java" / rel / f"{cls}Test.java"
    if main_file.exists() and not args.force:
        sys.exit(f"{main_file.relative_to(ROOT)} already exists (use --force to overwrite).")
    fields = dict(pkg=pkg, cls=cls, num=num, title=title, difficulty=difficulty,
                  module=module if module is not None else "-", group=group)
    for path, tpl in ((main_file, SOLUTION_TEMPLATE), (test_file, TEST_TEMPLATE)):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(tpl.format(**fields), encoding="utf-8", newline="\n")
    key = f"LC{num}"
    p = prog["problems"].setdefault(key, {})
    p.setdefault("title", title)
    p.setdefault("difficulty", difficulty)
    p.setdefault("group", group)
    p.setdefault("module", module)
    p.setdefault("in_bank", entry is not None)
    p.setdefault("status", "attempting")
    p.setdefault("attempts", 0)
    p.setdefault("hints", 0)
    p.setdefault("first_touched", today())
    p["last_touched"] = today()
    p["path"] = str(main_file.relative_to(ROOT)).replace("\\", "/")
    save_progress(prog)
    print(f"Created {p['path']}\nCreated {test_file.relative_to(ROOT)}".replace("\\", "/"))


def cmd_solved(args):
    cur, prog = load_curriculum(), load_progress()
    bank = {b["lc"]: b for b in cur["bank"]}
    key = f"LC{args.lc}"
    p = prog["problems"].setdefault(key, {})
    entry = bank.get(args.lc)
    title = args.title or p.get("title") or (entry["title"] if entry else None)
    if not title:
        sys.exit(f"Unknown title for LC {args.lc}: pass --title \"...\".")
    p.update({"title": title, "status": "solved", "last_touched": today(),
              "in_bank": entry is not None})
    p.setdefault("difficulty", (entry or {}).get("difficulty", "?"))
    p.setdefault("group", (entry or {}).get("group"))
    p.setdefault("module", (entry or {}).get("module"))
    p.setdefault("first_touched", today())
    p.setdefault("first_solved", today())
    if args.attempts is not None:
        p["attempts"] = args.attempts
    if args.hints is not None:
        p["hints"] = args.hints
    p.setdefault("attempts", 0)
    p.setdefault("hints", 0)
    prog["homework"] = [h for h in prog["homework"]
                        if not re.match(rf"^\s*LC\s*{args.lc}\b", h, re.I)]
    save_progress(prog)
    print(f"Marked {key}: {title} as solved ({p['first_solved']}).")


# ----------------------------------------------------------------------------- dashboard
def bar(done: int, total: int, width: int = 10) -> str:
    filled = round(width * done / total) if total else 0
    return "▓" * filled + "░" * (width - filled)


def compute(prog: dict, cur: dict) -> dict:
    day = dt.date.fromisoformat(today())
    done_by_mod = completed_topics_by_module(prog)
    modules = []
    for m in cur["modules"]:
        names = [t["name"] for t in m["topics"]]
        done = [n for n in names if n in done_by_mod.get(m["number"], [])]
        wip = [n for n in names if prog["topics"].get(n, {}).get("status") == "in_progress"]
        modules.append({"number": m["number"], "name": m["name"], "topics_total": len(names),
                        "topics_done": len(done), "topics_in_progress": len(wip),
                        "topics": [{"name": n, "status": prog["topics"].get(n, {}).get("status", "todo")}
                                   for n in names]})
    bank_ids = {b["lc"] for b in cur["bank"]}
    solved = {k: v for k, v in prog["problems"].items() if v.get("status") == "solved"}
    bank_solved = sum(1 for k in solved if int(k[2:]) in bank_ids)

    due, upcoming = [], []
    for r in prog["reviews"]:
        d = r.get("due")
        if not d:
            continue
        delta = (dt.date.fromisoformat(d) - day).days
        if delta <= 0:
            due.append({**r, "days_overdue": -delta})
        elif delta <= 7:
            upcoming.append({**r, "in_days": delta})
    due.sort(key=lambda r: r["due"])
    upcoming.sort(key=lambda r: r["due"])

    activity: dict[str, int] = {}

    def tick(d):
        if d:
            activity[d] = activity.get(d, 0) + 1

    for h in prog["history"]:
        tick(h.get("date"))
    for v in prog["problems"].values():
        tick(v.get("first_touched"))
        if v.get("first_solved") != v.get("first_touched"):
            tick(v.get("first_solved"))
    streak, cursor = 0, day
    if cursor.isoformat() not in activity:
        cursor -= dt.timedelta(days=1)
    while cursor.isoformat() in activity:
        streak += 1
        cursor -= dt.timedelta(days=1)

    recent = sorted(solved.items(), key=lambda kv: (kv[1].get("first_solved") or "", kv[0]), reverse=True)[:10]
    topics_total = sum(m["topics_total"] for m in modules)
    topics_done = sum(m["topics_done"] for m in modules)
    return {
        "generated_for": day.isoformat(),
        "overall": {"topics_done": topics_done, "topics_total": topics_total,
                    "bank_solved": bank_solved, "bank_total": len(bank_ids),
                    "problems_solved_total": len(solved), "streak_days": streak,
                    "active_days": len(activity)},
        "state": prog["state"],
        "modules": modules,
        "reviews_due": due,
        "reviews_upcoming": upcoming,
        "weak_areas": prog["weak_areas"],
        "homework": prog["homework"],
        "patterns": prog["patterns"],
        "recent_solved": [{"id": k, **v} for k, v in recent],
        "mistakes_recent": prog["mistakes"][-20:],
        "activity": dict(sorted(activity.items())),
    }


def render_markdown(c: dict) -> str:
    o, st = c["overall"], c["state"]
    pct = lambda a, b: f"{round(100 * a / b)}%" if b else "0%"
    lines = [START, "### Progress", "",
             f"**Topics** {bar(o['topics_done'], o['topics_total'], 20)} {o['topics_done']}/{o['topics_total']} "
             f"({pct(o['topics_done'], o['topics_total'])})  ",
             f"**Practice bank** {bar(o['bank_solved'], o['bank_total'], 20)} {o['bank_solved']}/{o['bank_total']} "
             f"({pct(o['bank_solved'], o['bank_total'])})  ",
             f"**Streak** {o['streak_days']} day(s) · **Active days** {o['active_days']} · "
             f"**Problems solved** {o['problems_solved_total']}", ""]
    if st.get("current_topic"):
        lines.append(f"Last session ({st.get('last_updated')}): Module {st.get('module_number')}, "
                     f"{st['current_topic']} ({st.get('topic_status')})")
        lines.append("")
    lines += ["| # | Module | Progress | Topics |", "|---|---|---|---|"]
    for m in c["modules"]:
        wip = f" (+{m['topics_in_progress']} in progress)" if m["topics_in_progress"] else ""
        lines.append(f"| {m['number']} | {m['name']} | {bar(m['topics_done'], m['topics_total'])} | "
                     f"{m['topics_done']}/{m['topics_total']}{wip} |")
    lines.append("")
    lines.append(f"**Reviews due now ({len(c['reviews_due'])})**")
    lines += [f"- {r['topic']} · {r['type']} · due {r['due']}"
              f"{' (overdue ' + str(r['days_overdue']) + 'd)' if r['days_overdue'] else ''}"
              for r in c["reviews_due"]] or ["- nothing due"]
    lines += ["", "**Next 7 days**"]
    lines += [f"- {r['topic']} · {r['type']} · {r['due']}" for r in c["reviews_upcoming"]] or ["- nothing scheduled"]
    lines += ["", "**Weak areas**"] + ([f"- {w}" for w in c["weak_areas"]] or ["- none recorded"])
    lines += ["", "**Homework**"] + ([f"- {h}" for h in c["homework"]] or ["- none assigned"])
    lines += ["", "**Recently solved**"]
    lines += [f"- LC {r['id'][2:]}: {r.get('title')} ({r.get('difficulty')}) · {r.get('first_solved')}"
              for r in c["recent_solved"]] or ["- nothing yet"]
    lines += ["", f"_Generated by `scripts/dsa.py dashboard` for {c['generated_for']}. Do not edit between the markers._", END]
    return "\n".join(lines)


def render_mistakes(prog: dict) -> str:
    out = ["# Mistakes log", "",
           "Generated from `progress.yaml` by `scripts/dsa.py dashboard`. Add mistakes by telling the mentor,"
           " pasting its snapshot, and running `python scripts/dsa.py snapshot`.", ""]
    if not prog["mistakes"]:
        out.append("_Nothing logged yet._")
    for m in reversed(prog["mistakes"]):
        out.append(f"- {m['date']}: {m['text']}")
    return "\n".join(out) + "\n"


def build_outputs(prog: dict, cur: dict) -> None:
    c = compute(prog, cur)
    block = render_markdown(c)
    text = README.read_text(encoding="utf-8") if README.exists() else ""
    if START in text and END in text:
        text = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _m: block, text, flags=re.S)
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    README.write_text(text, encoding="utf-8", newline="\n")
    MISTAKES_MD.write_text(render_mistakes(prog), encoding="utf-8", newline="\n")
    DOCS_JSON.parent.mkdir(parents=True, exist_ok=True)
    DOCS_JSON.write_text(json.dumps(c, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def cmd_dashboard(_args):
    build_outputs(load_progress(), load_curriculum())
    print("README dashboard, mistakes.md and docs/progress.json regenerated.")


def cmd_due(_args):
    c = compute(load_progress(), load_curriculum())
    print(f"Due now ({len(c['reviews_due'])}):")
    for r in c["reviews_due"] or [None]:
        print("  nothing due" if r is None else f"  {r['topic']} | {r['type']} | {r['due']}")
    print(f"Next 7 days ({len(c['reviews_upcoming'])}):")
    for r in c["reviews_upcoming"]:
        print(f"  {r['topic']} | {r['type']} | {r['due']}")


def cmd_status(_args):
    c = compute(load_progress(), load_curriculum())
    o, st = c["overall"], c["state"]
    print(f"Topics {o['topics_done']}/{o['topics_total']} | bank {o['bank_solved']}/{o['bank_total']} | "
          f"solved {o['problems_solved_total']} | streak {o['streak_days']}d | due now {len(c['reviews_due'])}")
    if st.get("current_topic"):
        print(f"Last: module {st.get('module_number')}, {st['current_topic']} ({st.get('topic_status')})")


# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--today", help="override today's date (YYYY-MM-DD)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("snapshot"); s.add_argument("file", nargs="?"); s.set_defaults(fn=cmd_snapshot)
    sub.add_parser("export").set_defaults(fn=cmd_export)
    n = sub.add_parser("new")
    n.add_argument("lc", type=int); n.add_argument("--title"); n.add_argument("--module", type=int)
    n.add_argument("--topic"); n.add_argument("--force", action="store_true"); n.set_defaults(fn=cmd_new)
    v = sub.add_parser("solved")
    v.add_argument("lc", type=int); v.add_argument("--title")
    v.add_argument("--attempts", type=int); v.add_argument("--hints", type=int); v.set_defaults(fn=cmd_solved)
    sub.add_parser("due").set_defaults(fn=cmd_due)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    sub.add_parser("dashboard").set_defaults(fn=cmd_dashboard)
    args = ap.parse_args()
    if args.today:
        os.environ["DSA_TODAY"] = args.today
    args.fn(args)


if __name__ == "__main__":
    main()
