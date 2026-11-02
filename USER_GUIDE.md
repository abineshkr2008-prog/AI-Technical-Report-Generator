# User Guide

## Purpose
Turn genuine ECE lab notes into a structured report outline and use AI responsibly to draft supporting documentation.

## Steps
1. Copy `lab_notes_template.txt` and fill every field you know. Leave unknowns clearly marked.
2. Save your completed notes as `my_lab_notes.txt`.
3. Open a terminal in this folder and run:
   `python generate_outline.py my_lab_notes.txt`
4. The script creates `report_outline.md`. Review it for missing fields.
5. Copy relevant notes into a prompt from `PROMPT_LIBRARY.md`.
6. Generate one section at a time. Do not ask AI to invent readings, values or references.
7. Check circuit details against your schematic and component datasheets.
8. Enter actual measurements into `observations.csv`; enter actual timings into `time_quality_comparison.csv`.
9. Record all corrections in `error_log.csv`.
10. Update the PDF report and slides, then rehearse the demonstration.

## Troubleshooting
- If Python is not installed, install Python 3 and rerun the command.
- If the notes file is not found, check the filename and current folder.
- If the generated outline contains placeholders, fill them using your notebook.
- If an AI answer contains an unsupported value, remove it or verify it from a reliable datasheet.
