#!/usr/bin/env python3
"""Convert student lab notes into a Markdown report outline. No AI calls; no fabricated data."""
import sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("Usage: python generate_outline.py <lab_notes.txt>")

source = Path(sys.argv[1])
if not source.is_file():
    raise SystemExit(f"Notes file not found: {source}")

notes = source.read_text(encoding="utf-8")
sections = [
    ("Abstract", "Summarize problem, objective, method and verified outcome. Do not invent results."),
    ("Introduction", "Explain background, problem, need and objectives. Cite reliable sources."),
    ("Components and circuit", "List exact component ratings and pin-to-pin connections from the notes."),
    ("Methodology", "Convert the actual build and test procedure into numbered steps."),
    ("Results", "Use only the raw readings and observations supplied in the notes."),
    ("Conclusion", "Conclude only what the verified evidence supports; state limitations."),
]
out = ["# AI-assisted technical report outline", "",
       "> Draft outline generated from student notes. Verify every technical claim.", "",
       "## Source lab notes", "```text", notes, "```", ""]
for title, instruction in sections:
    out += [f"## {title}", f"_{instruction}_", "", "[Add verified content from the lab notes. Mark missing information as TO BE PROVIDED.]", ""]
Path("report_outline.md").write_text("\n".join(out), encoding="utf-8")
print("Created report_outline.md. Review it and verify all content before submission.")
