# CAPSTONE 10 — AI Technical Report and Documentation Generator
## ECE case study: Automatic Street Light Using LDR

This package demonstrates an AI-assisted documentation workflow. It does **not** claim that the circuit has been physically built or tested. Fill in the observation, timing and quality tables using your own work.

## Files
- `Capstone10_Final_Report.pdf` — report framework and documentation workflow
- `README.md` — this file
- `USER_GUIDE.md` — operating instructions
- `PROMPT_LIBRARY.md` — reusable prompts
- `lab_notes_template.txt` — notes template
- `generate_outline.py` — automation: lab notes to Markdown outline
- `time_quality_comparison.csv` — record your measured comparison
- `observations.csv` — record actual experiment readings
- `error_log.csv` — record AI errors and corrections
- `verification_checklist.md` — verification evidence checklist
- `presentation.pptx` — 7-slide presentation outline

## Project overview
An LDR senses ambient light. A threshold circuit/controller switches a low-voltage LED lamp ON in darkness and OFF in bright conditions. The exact circuit topology and sensor voltage polarity depend on the design; document the circuit you actually build.

## Suggested components
LDR, resistor/potentiometer, comparator or microcontroller, suitable transistor/driver, LED with current-limiting resistor, regulated low-voltage DC supply, breadboard and wires. Confirm all ratings and pinouts from datasheets.

## How to use
1. Build/simulate the low-voltage circuit under instructor guidance.
2. Fill `lab_notes_template.txt` with actual connections, component values and observations.
3. Run `python generate_outline.py lab_notes_template.txt`.
4. Use the prompts in `PROMPT_LIBRARY.md` with your notes in an AI tool.
5. Verify every technical statement against the schematic, datasheets and raw readings.
6. Complete the report tables and update the error log.
7. Edit the presentation with your actual results and photographs.

## Safety
Use a low-voltage LED demonstration. Do not connect mains voltage without qualified supervision, isolation and proper protection.

## Academic integrity
AI-generated content is a draft. Disclose AI assistance as required, cite sources, check copyright/licensing, and never invent results or references.
