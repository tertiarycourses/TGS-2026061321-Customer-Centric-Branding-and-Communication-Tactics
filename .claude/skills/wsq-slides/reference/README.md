# WSQ courseware reference pipeline (PPT + LP + LG, single source)

This is the **canonical reference implementation** for Tertiary Infotech Academy WSQ
courseware. One content module drives **all three** artifacts so the slide deck, Lesson
Plan and Learner Guide can never drift apart. It is the reference the `wsq-slides`,
`wsq-lesson-plan` and `wsq-learner-guide` skills point to.

Origin: the Customer-Centric Branding and Communication Tactics course
(`TGS-2026061321`). Treat that content as an **example** — copy this folder into a new
course repo and swap in that course's content.

## Files

| File | Role |
|------|------|
| `course_data.py` | **Single source of truth** — metadata, version + version date, TSC details, learning outcomes, topics + concept bullets, day themes, assessment strings. Edit this first. |
| `data_domain1.py … data_domain4.py` | Per-topic activity data (title, desc, objective, build/deliverable, duration, workflow steps). One module per topic; add/remove modules to match the course. |
| `data_brandtrust.py` | **Concept-enrichment module** — extra insight slides per topic as `(kind, spec)` pairs rendered by `render_insight`: `pillars`, `table` (compare_table), `stats` (stat_band), `image` (img_slide), `quote` (big_statement), `flow` (flow_h), `playbook`, `twocol`. Rename per course; keep the pattern. |
| `prodoc.py` | Shared DOCX helpers: WSQ cover page, Document Version Control Record, TOC field, "Page X of Y" footer. Used by the LP and LG builders. |
| `build_slides.py` | **The slide deck** (python-pptx, all-white house style). Contains the full **visual component library**: `cover` (WSQ badge + Version on cover), `section`, `content` (renders numbered tile cards — never a bullet wall), `two_col`, `cards3` (auto-fits 2–3 cards), `tile_grid`, `flow_h` (optional `intro`/`note`), `trainer_slide`, `big_statement`, `lead`, `callout`, `compare_table`, `stat_band`, `playbook`, `img_slide`, `activity_slide` (**one workflow slide per activity** — scenario + numbered workflow strip + deliverable band), `lms_slide` (visual LMS portal card), `brk`. Applies a uniform fade transition to every slide and writes `slide_map.json` (anchor → deck page) for the Lesson Plan builder. |
| `build_lesson_plan.py` | **The Lesson Plan** DOCX (cover, version control, TOC, colour-coded day schedule tables; cites deck pages via `slide_map.json`). |
| `build_learner_guide.py` | **The Learner Guide** as a Markdown mirror + DOCX from one source. |
| `inject_toc.py` | Post-processes the DOCX TOC field into a page-numbered TOC. |
| `render_pdfs.py` | Headless LibreOffice PDF rendering helper. |
| `build_courseware.sh` | Builds all artifacts in order (derives filenames from `course_data.py`). |

## The visual + structural rules this pipeline encodes

`build_slides.py` is the reference for the `wsq-slides` **hard rules**:

- **Always visual** — every content slide is a component: `content` itself renders
  numbered tile cards; concept / outcome / process / trainer slides use `tile_grid`,
  `flow_h`, `cards3`, `compare_table`, `stat_band`, `playbook` or `trainer_slide` —
  never plain bullet walls (`bullets()` survives only inside `two_col`/`cards3` panels).
- **One workflow slide per activity** — `activity_slide(...)`: ACTIVITY tag + scenario +
  compact numbered workflow strip (≤6 chips; overflow points to the Learner Guide) +
  "You'll produce" deliverable band + duration. Never one-step-per-slide runs.
- **About the Trainer ×2** — `trainer_slide(...)` profile cards: a blank *General Trainer*
  template and the *named trainer*.
- **Assessment Flow** — `flow_h(...)` horizontal numbered flow diagram.
- **LMS slide is visual** — `lms_slide()`: dark portal card + numbered steps, never a
  bare text link.
- **TRAQOM · SSG Digital Attendance** page present at the front and again at the end.
- **Assessment admin pages repeated at the END** before *Thank You*:
  Assessment → Assessment Flow → Digital Attendance (Mandatory).
- **Concept enrichment** — each topic gets Key Concepts (`tile_grid`) plus the
  insight slides from the enrichment module via `render_insight`.
- Cover shows the WSQ badge, course code, org + UEN and **Version vNN + date**.
- Palette cycles blue → teal → violet → amber; footer carries course · code · © · page;
  uniform fade transition on every slide.

## How to build a new course

1. Copy this `reference/` folder into the new course repo (e.g. `courseware/build/`).
2. Put the Tertiary logo (and any course logo) in `courseware/assets/`.
3. Edit `course_data.py` (title, TGS code, version, outcomes, topics, concepts, day
   themes) and the `data_domainN.py` modules (activities). Add/remove domain modules to
   match the number of topics — update the `import`s at the top of each builder
   accordingly. Rework the concept-enrichment module (`data_brandtrust.py` pattern) with
   that course's insight slides.
4. Build:
   ```bash
   python3 build_slides.py          # -> courseware/<Short Title>-<ver>.pptx + slide_map.json
   python3 build_lesson_plan.py     # -> courseware/LP-<Short Title>.docx
   python3 build_learner_guide.py   # -> LG mirror (.md) + courseware/LG-<Short Title>.docx
   # or: ./build_courseware.sh
   ```
5. Run visual QA on the deck (render slides to images, inspect) before delivering.
   Move superseded versioned outputs to `courseware/archive/`.

> Assessments (WA + PP/CS) are produced by the separate **wsq-assessment** skill, not
> this pipeline.
