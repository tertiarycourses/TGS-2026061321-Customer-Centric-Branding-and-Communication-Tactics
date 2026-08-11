---
name: tertiary-softskills-ppt-design
description: Design system and activity pattern for Tertiary Infotech WSQ SOFT-SKILLS course decks (branding, communication, leadership, service-excellence type courses) — case-study/role-play activities instead of step-by-step, an expanded native-shape diagram library (pyramids, icon-grid cards, pros/cons arrows, journey maps with emotion curves, service blueprints, funnels, empathy maps, decision trees, KPI dashboards, persona cards, ecosystem/stakeholder maps, real-world case-study callouts, dark "impact" quote/playbook slides), soft vector icons and drop shadows for real depth, and a research-grounding rule. Companion to tertiary-ppt-design (which stays the base house-style authority) — use THIS skill whenever the course is a soft-skills/knowledge course rather than a hands-on tool/technical course.
---

# Soft-Skills WSQ Course Deck — Design System & Activity Pattern

This skill extends **tertiary-ppt-design** (still the base authority for theme, fonts,
palette, cover/footer, and the overall deck structure) with two things a soft-skills
course needs that a tool/technical course (e.g. the n8n courses this pipeline was
originally built for) does not:

1. A **case-study / role-play activity pattern** instead of step-by-step instructions.
2. A richer **native-shape diagram library** so theory slides read like a designed
   report, not a bullet-point deck — validated against two real reference decks
   (see "What we learned from the reference decks" below).

Reach for this skill whenever the course being built is a knowledge/soft-skills WSQ
course: branding, communication, leadership, customer service, negotiation, etc. Keep
using plain step-by-step slides for hands-on tool courses (n8n, software, technical
labs) — a learner following along in a live tool genuinely needs "Step 1, Step 2, Step 3."
A learner discussing a stakeholder scenario does not.

## 1. Case study / role play — never step-by-step

A soft-skills activity is not a sequence of clicks. Model every in-class activity as
one of two types, chosen per activity by fit:

- **`case_study`** — the group analyses a scenario and produces an artifact (a matrix,
  plan, audit, dashboard). Use for audits, mapping, planning and budgeting activities.
- **`role_play`** — the group acts out a scenario with assigned personas, then debriefs.
  Use where a live conversation or negotiation is the actual skill being taught
  (active listening, stakeholder negotiation, crisis-response media handling, a sales
  or service conversation). Two or three role-plays across a whole course is usually
  enough — reserve it for activities where dialogue genuinely adds value over analysis.

### Data shape (per activity)

```python
dict(
    ...
    case_type="role_play",           # or "case_study"
    case_scenario=["Paragraph 1 — the situation.", "Paragraph 2 — the tension/stakes."],
    roles=[                          # role_play only; case_study uses roles=[]
        ("Role Name", "Their goal in one line", "Their brief / what they care about."),
        ...                          # 2-4 personas
    ],
    discussion_prompts=[             # 4-6 OPEN questions, never "do X then Y"
        "Which stakeholders matter most here, and why?",
        "Where does the group's initial assumption break down?",
        ...
    ],
    reflection_points=[              # 3-4 debrief reflection questions
        "What surprised you once you heard the other side's real concern?",
        ...
    ],
    debrief_check="What a complete, correct output looks like — describe it, "
                  "don't grade it pass/fail.",
)
```

### Slide sequence per activity

`scenario_slide` (the case narrative as a styled card, tagged CASE STUDY or ROLE
PLAY — never a bullet dump) → `role_cards_slide` (role-play only — one persona card
per role: name, goal, brief) → `discussion_slide` (numbered *question* cards, not
instruction cards) → `reflection_slide` (reflection questions + the facilitator's
debrief check, replacing any pass/fail "test" slide).

All four functions live in `build_slides.py` in a course that has adopted this
pattern (see the Customer-Centric Branding course for the reference implementation).
Port them into a new course's `build_slides.py` verbatim — they only depend on the
existing `rect/oval/txt/bullets/head/footer` primitives from tertiary-ppt-design.

## 2. Expanded diagram library

Beyond `tile_grid` / `process_v` / `two_col` / `table_slide` / `stats_bar` /
`big_statement` (tertiary-ppt-design's base set), add these for variety — native
python-pptx shapes/gradients/real charts only, no external images (nothing to
license, nothing that breaks when re-themed):

| Helper | Use it for | Data shape |
|---|---|---|
| `pyramid_steps` | An ascending N-level model (e.g. Keller's Brand Equity Pyramid) | `[(numeral, heading, caption), ...]` **index 0 = bottom/widest**, narrowing toward the top |
| `icon_cards_grad` | A 3-4 item component/pillar grid with real visual pop | `[(icon_kind, heading, body), ...]` |
| `pros_cons_arrows` | A named two-sided comparison (old vs new, reactive vs proactive) | two lists of `(icon_kind, heading, caption)` + two labels |
| `journey_loop` | A cyclical process (customer journey, advocacy loop, evaluation cycle) — NOT a one-way flow | `[(heading, caption), ...]`, 4-6 stages |
| `hex_model` | A named N-point framework (SMART, a 5-point model) | `[(numeral/letter, heading, caption), ...]` |
| `quadrant_2x2` | A 2-axis framework (power/interest, effort/impact) | 4 `(name, color_tag, [items])` tuples, order TL/TR/BL/BR |
| `road_process` | A 3-4 step production/build process, presented as a journey rather than a plain list | `[(icon_kind, heading, caption), ...]`, max 4 — nodes alternate in two narrow centre columns, joined by `MSO_CONNECTOR.ELBOW`; **do not** try to hand-draw the connecting path with `rect()` at a diagonal — the width/height math never lines up with off-axis nodes, use a real connector |
| `split_letter_cards` | A clean two-way category comparison with short labels (≤2 words each) | two `(letter_or_short_word, label, [items])` tuples |
| `donut_ring` | A **genuine share-of-a-whole** stat (platform mix, budget split) — a real native PowerPoint doughnut chart, not a hand-drawn approximation | `[(label, value), ...]` |
| `infographic_slide` | An AI-rendered infographic (65+ AntV templates — bar/column/line charts, hierarchy trees, relationship/network diagrams, richer cycle/pyramid renders) for when the native shape library above doesn't have a good fit, or you want a genuinely different visual texture on the page. **Not editable in PowerPoint afterward** (it embeds a rendered PNG) and needs a headless Chromium at build time (`courseware/build/infographic_render.py`, ported from `Reference/wsq-courseware-generator-claude-streamlit`'s deterministic AntV pipeline) — reach for the native helpers above first; use this when they genuinely can't express the diagram you need | same tuple shapes as the native helpers — `(kind, label)`, `(kind, heading, body)`, `(heading, caption)` or `(label, value)` — plus a `template` string from `infographic_render.TEMPLATE_MAP` |

`color_tag` for `quadrant_2x2` is a plain string (`"blue"/"teal"/"violet"/"grey"/"amber"`)
— map it to the real `RGBColor` constant in the build script's dispatcher, never inside
the data file. Keep data files free of pptx-internal objects.

**Only use `donut_ring` when the values are genuinely parts of one whole** (e.g.
platform share of total mentions). Don't reach for it just because a few
percentages happen to add up to 100 — two independent survey stats that
coincidentally sum to 100 are not a composition, and a pie/doughnut chart
visually claims they are. When in doubt, use `stats_bar` instead.

### Real vector icons, not generic glyphs

Use `icon_badge(shape, kind, cx, cy, diameter, badge_color)` everywhere a card
needs an icon — it draws a coloured circle with a small, *semantically
meaningful* icon built from real PowerPoint autoshapes (a magnifying glass for
"search", a 6-tooth gear for "process", a speech-bubble callout for "chat"...),
not a generic star/diamond/triangle. Recognised `kind` values: `chat`, `gear`,
`flag`, `search`, `chart`, `refresh`, `shield`, `people`, `clock`, `target`,
`star`, `lightning`, `check`, `idea`, `heart`. Any other string is rendered as
literal text inside the badge (safe fallback — a bare glyph like `"1"` or `"✓"`
still works). Match the icon to the concept it represents (Trust → `shield`,
Loyalty → `heart`, Awareness → `search`) — this is the single highest-leverage
change for making a deck look designed rather than templated.

A few autoshape presets need correction to read clearly at badge scale — don't
rediscover these the hard way: `GEAR_6` (not `GEAR_9` — the extra teeth
disappear at small size), `PENTAGON` rotated 90° for a shield/badge look (its
un-rotated point faces right, like home plate), `CIRCULAR_ARROW` needs a
generous bounding box (~2.7× the icon radius) or its arrowhead clips.

### Soft drop shadows

`add_shadow(shape)` applies a real OOXML outer shadow (there is no high-level
python-pptx API for this — it edits `<a:effectLst>` directly). `rect()`,
`oval()`, `ashape()` and `grad_rect()` all take a `shadow=True` kwarg that
calls it for you. Apply it to every card/badge/arrow background across the
whole deck (tile_grid, cards3, two_col, process_v, flow_h, and all of the
helpers above) — it's what actually reads as "depth" rather than flat shapes,
and it's the difference reviewers notice first. Never call `add_shadow` twice
on the same shape without removing the previous `<a:effectLst>` first (two
sibling `effectLst` elements is invalid OOXML and Office will repair-prompt on
open) — `add_shadow` already handles this, just don't bypass it with manual
XML.

**Wire them through a dispatcher, not a wall of if/else in the main loop.** Give each
activity three optional fields, `what_is_kind`, `compare_kind` and `visual_kind`
(default to the base `tile` / `two_col` / `tile`/`bar` if absent), and write one
`render_what_is(a, kicker)` / `render_compare(a, kicker)` / `render_visual(a, kicker)`
dispatcher function each that branches on the kind. This keeps the main topic/activity
loop short and lets each activity opt into a richer diagram just by setting a string.

**How much to upgrade, revised**: an earlier version of this rule said "upgrade a
subset, not every slide" — that undersold it and drew direct user pushback ("still
very wordy, no nice illustrations"). The corrected rule: **every activity's `what_is`
slide should use `icon_cards_grad`, not a plain `tile_grid`** — it's strictly better at
the same information density and costs nothing. For the `visual` (supporting-data) and
`compare` slots, aim for **every activity to carry one genuinely well-matched diagram**
from the library below rather than falling through to the generic `bar`/`tile`/`two_col`
default — the generic default is not free of visual interest, it's the visible seam
where "converted" stops and "not converted yet" begins. It is still true that not every
diagram type fits every activity — don't force a service blueprint onto content that
isn't about a multi-stage process just to tick a box; when nothing fits, `stats_bar` /
`tile_grid` / `two_col` are legitimate, deliberate choices, not a fallback you forgot to
replace.

### Round 2 additions — more diagram types, real-world case callouts

| Helper | Use it for | Data shape |
|---|---|---|
| `journey_map` | A customer's path across touchpoints, with an emotion/satisfaction curve underneath | `[(icon_kind, stage_name, touchpoint, emotion_1_to_5), ...]`, 4-5 stages — use the emotion score to **tell the actual story** (dip it at the pain point your scenario describes, don't just decorate) |
| `service_blueprint` | A multi-lane process (customer actions vs frontstage vs backstage vs support) across stages | `stage_labels` (4-5 column headers) + `lanes = [(lane_name, color, [cell_per_stage]), ...]`, exactly 4 lanes |
| `funnel_chart` | A narrowing progression (awareness→purchase, top-of-funnel→conversion) | `[(label, value_label, caption), ...]`, **index 0 = top/widest** |
| `empathy_map` | A single named persona's Says/Thinks/Does/Feels — pairs naturally with a role-play activity's own persona | four 2-item lists: `items_says, items_thinks, items_does, items_feels` — ground it in a persona already established in the course narrative, don't invent an unrelated one |
| `decision_tree` | A fork with 2-3 real consequence paths (crisis response, escalation choices) | `root` (one question string) + `branches = [(choice_label, outcome_heading, outcome_caption, color), ...]`, exactly 3. **The root box auto-sizes to the question length** — still keep it under ~100 characters, a very long root question degrades readability even once it technically fits |
| `kpi_dashboard` | 3-4 headline stats with a trend | `[(value, label, delta, trend), ...]`, `trend` ∈ `"up"/"down"/"flat"` |
| `persona_card` | 1-3 customer/stakeholder personas with goals vs frustrations | `[(name, role_tag, [goals], [frustrations]), ...]` |
| `ecosystem_map` | A hub-and-spoke stakeholder/brand network | `center_label` + `[(icon_kind, label), ...]`, 5-8 spokes |
| `case_study_callout` | A frequent, LIGHT-themed "REAL-WORLD EXAMPLE" card citing one named real company, directly under the theory it illustrates | `company, headline, insight` — this is NOT the rare dark `quote_callout`; use it on **every activity** where a real company genuinely illustrates the point (Apple/Starbucks/Zappos/Tesla/IKEA/Disney/Grab-style local relevance where useful). Only use real, verifiable, well-known facts — never invent a statistic or quote for the company. |

`ecosystem_map` is also valid as a **`what_is_kind`** option (not just `visual_kind`) —
it needs `what_is_center` (hub label) alongside the usual `what_is_items` reshaped to
`(icon_kind, label)` pairs. It's the natural choice for a "what is a stakeholder /
audience / ecosystem?" concept slide.

Two real layout bugs worth knowing about so you don't reintroduce them: (1) any text
box sized for a *short* label will silently collide with the box below it the first
time real content gives it a *long* label — size defensively (adaptive font size and/or
box height keyed off `len(text)`) rather than assuming your test string was
representative; (2) `decision_tree`'s root box originally had a fixed width/height that
overflowed on a realistic (~100-character) crisis-scenario question — it now computes
width/height/font from the question length. When adding a new text-bearing shape,
stress-test it with your *longest* plausible real string, not your shortest.

### Word-count discipline

"Wordy" is a specific, fixable complaint, not a vibe — hold every text field on a
diagram/card slide to a hard cap: item **bodies/captions under ~10 words**, headings
under ~5. If a sentence needs a comma to fit the idea, it's two ideas — split it or cut
the weaker one. This applies to `what_is_items`, `takeaways_items`, table cell text and
diagram captions; it does **not** apply to the case-study narrative prose
(`case_scenario`, `discussion_prompts`, `reflection_points`, `case_example_insight`) —
those are meant to read as real sentences and stay as long as the story needs.

### Dark "impact" accent slides — use sparingly

`quote_callout` (a full dark-navy slide for one big statement/quote) and
`playbook_numerals` (a dark-navy big-numeral executive-summary row) break the
otherwise strict all-white house rule. That's deliberate — a soft-skills deck
benefits from one dramatic beat per section, the way a keynote or an analyst report
does. The rule that keeps it from becoming a liability:

- **About once per Learning Unit** — one `quote_callout` as the LU's closing "why it
  matters" moment. Never more than that within a single LU.
- `playbook_numerals` is reserved for the **whole-course wrap-up**, once, near the end
  — one pillar per Learning Unit, not a per-activity thing.
- Never use a dark background for routine body content, theory slides, or activity
  slides. If in doubt, keep it white — the dark slide's power comes from its rarity.

## 3. Research-grounding rule

Before writing scenario content or citing a framework, do a short WebSearch pass
(3-6 queries is usually enough) and ground the deck in **real, named** frameworks,
models and — where useful — recent real-world examples, instead of vague placeholder
citations like "Source: Industry Report, 2024." Concretely:

- Cite the actual framework by name and originator where one exists (e.g. "Mendelow's
  Power-Interest Matrix, 1991", "Keller's Customer-Based Brand Equity Model", "the
  PESO Model, Gini Dietrich / Spin Sucks", "AMEC Integrated Evaluation Framework /
  Barcelona Principles 4.0").
- For illustrative numbers on a `stats_bar` chart (which is a presentational device,
  not a factual claim), label the source line "illustrative" rather than inventing a
  precise-sounding fake statistic with a fake citation.
- Real recent case examples (a crisis-response pattern, a benchmark range) are fair
  game for scenario colour and role-play grounding — cite them plainly ("Source: PR
  crisis-management case examples, 2024-2025") without over-claiming precision you
  don't have.
- Never fabricate a quote and attribute it to a real named person or company. Course
  quote-callout slides in this pipeline are written as anonymous "closing thought"
  lines, not attributed quotes — do the same unless you have a verified source.

## 4. One continuous scenario, tied to the assessment

If the course has a Case Study (CS) assessment that reuses one fictional company,
build every in-class activity's `case_scenario` on **that same company**, advancing
through its timeline activity by activity, so each Learning Unit's activities are
recognisably "the techniques practised in class" the assessment refers back to. Read
the CS assessment document first — don't invent a parallel scenario that never
connects to what's actually being assessed.

## What we learned from the reference decks

Two decks were used to calibrate this skill (see `Reference/TGS-2023035977-Agentic-AI-Automation-with-n8n/` in the Customer-Centric Branding repo where this was built):

- **`Architecting_Brand_Trust.pptx`** — a NotebookLM-generated soft-skills deck. Every
  slide is a single flattened full-bleed PNG (watercolour blobs, circuit-line accents,
  dark-navy quote/impact slides, an infinity journey-loop diagram, a hexagon model, a
  big-numeral "executive playbook" slide). **Not directly reusable**: no source, no
  WSQ cover/footer/branding, and several slides are pure dark backgrounds — but the
  *level of visual ambition* (one strong idea per slide, real diagrams instead of
  bullets, occasional dramatic dark beats) is exactly what this skill's diagram
  library and dark-accent rule reproduce natively and editably.
- **`Building AI Agents for Work Automation (SF).pptx`** (pages 13-15, 23-27, 35-39) —
  a WSQ house-style deck (white background, standard title textbox) with a single rich
  infographic image below the title: pros/cons cards with arrows, an ascending step
  pyramid linked to explanation cards, a 4-up gradient-header icon-card grid. This is
  the pattern `pyramid_steps`, `icon_cards_grad` and `pros_cons_arrows` were built to
  match — but as native shapes instead of a pasted image, so they stay editable and
  on-brand for every future course.

Don't re-derive this from scratch in a future session — extract this skill's helper
functions from an existing course's `build_slides.py` (Customer-Centric Branding and
Communication Tactics, TGS-2026061321, is the reference implementation) and adapt the
scenario/company to the new course.
