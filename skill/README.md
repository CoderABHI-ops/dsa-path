# Skill source

`dsa-mentor/` is the Gemini skill (SKILL.md plus references/). It is the single source of truth for HOW the mentor
teaches (SKILL.md) and WHAT it teaches (references/).

## Update the skill in Gemini
1. Edit `dsa-mentor/SKILL.md` or `dsa-mentor/references/*.md` here and commit.
2. In Gemini: Settings, Skills, upload the `dsa-mentor` folder again (or paste `SKILL.md` and re-attach the
   reference files). Delete the old version so only one copy is active.
3. If you edited a module file's topic table or practice bank, run `python scripts/build_curriculum.py` so the
   tracker's `curriculum/curriculum.json` stays in sync.

## Rules that keep the tracker working
- Keep the snapshot format in `SKILL.md` compatible with `scripts/dsa.py` (see AGENTS.md for the key list).
- Keep each `references/mNN-*.md` header as `# Module N of 11: <name>` and the sections `## PART A` / `## PART B`.
- Practice-bank lines must look like `- LC 3 — Title (Medium) — https://...` under a `**Group**` heading.
