#!/usr/bin/env python3
"""Generate the labs/ folder — one Markdown activity sheet per in-class
activity (17 total), plus labs/README.md and labs/tools.md — in the same
style as the Tertiary Infotech reference labs folders (e.g. the CLSSBB
course). Content is driven by course_data.py + data_domain1..4.py so the
lab sheets stay aligned with the slide deck, Lesson Plan and Learner Guide.
"""
import os, re, sys

HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import course_data as C
from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3; from data_domain4 import DOMAIN4
ACT=DOMAIN1+DOMAIN2+DOMAIN3+DOMAIN4
REPO=os.path.dirname(os.path.dirname(HERE))
LABS=os.path.join(REPO,"labs")

FOOTER=f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 Tertiary Infotech Academy Pte Ltd*"

def slug(text):
    s=re.sub(r"[^a-z0-9]+","-",text.lower()).strip("-")
    return s

TOPIC_BY_NUM={t["num"]:t for t in C.TOPICS}

def lab_md(a):
    t=TOPIC_BY_NUM[a["topic"]]
    lines=[]
    lines.append(f"# Activity {a['num']} — {a['title']}")
    lines.append("")
    lines.append(f"**Learning Unit:** {t['code']} — {t['title']}  |  **Activity type:** In-class workshop  |  "
                 f"**Course:** {C.TITLE} ({C.COURSE_CODE})")
    lines.append("")
    lines.append("## Objective")
    lines.append("")
    lines.append(f"{a['objective']}.")
    lines.append("")
    lines.append("## Scenario")
    lines.append("")
    lines.append(a["desc"])
    lines.append("")
    lines.append("## What you will produce")
    lines.append("")
    lines.append(a["build"] + ".")
    lines.append("")
    lines.append(f"**Duration:** {a['duration']}")
    lines.append("")
    lines.append("## Steps")
    lines.append("")
    for i,(instr,_cmd) in enumerate(a["steps"],1):
        lines.append(f"### Step {i}")
        lines.append("")
        lines.append(instr)
        lines.append("")
    lines.append("## Check your work (Debrief it)")
    lines.append("")
    lines.append(a["test"])
    lines.append("")
    lines.append("## Deliverable")
    lines.append("")
    lines.append(f"Save your output — it forms part of your {t['code']} workbook, which you may draw on "
                 f"for the open-book Case Study assessment on Day 2.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(FOOTER)
    lines.append("")
    return "\n".join(lines)

def readme_md():
    by_lu={}
    for a in ACT: by_lu.setdefault(a["topic"],[]).append(a)
    lines=[f"# {C.TITLE} Labs",""]
    lines.append(
        "This course structure organises 17 progressive in-class activities across 4 Learning Units, "
        "where participants apply each Learning Unit's concepts to a running set of branding and "
        "communication exercises that build into an open-book Case Study assessment on Day 2.")
    lines.append("")
    lines.append("## Course Structure")
    lines.append("")
    lines.append("The activities span four Learning Units:")
    lines.append("")
    for t in C.TOPICS:
        acts=by_lu[t["num"]]
        rng=f"Activities {acts[0]['num']}-{acts[-1]['num']}"
        lines.append(f"- **{t['code']} — {t['title']} ({rng}):** {t['subtitle']}")
    lines.append("")
    lines.append("## Key Features")
    lines.append("")
    lines.append(
        "Every activity is scenario-based and produces a concrete artifact (a matrix, plan, audit report "
        "or dashboard) that the learner keeps. All 17 activities are in-class workshop activities assessed "
        "indirectly through the Case Study (CS) component of the formal WSQ assessment, which reuses the "
        "same techniques on a single continuous scenario.")
    lines.append("")
    lines.append("## Activities")
    lines.append("")
    lines.append("| # | Learning Unit | Activity | Duration |")
    lines.append("|---|---|---|---|")
    for a in ACT:
        t=TOPIC_BY_NUM[a["topic"]]
        fname=f"lab-{a['num']:02d}-{slug(a['title'])}.md"
        lines.append(f"| {a['num']} | {t['code']} | [{a['title']}]({fname}) | {a['duration']} |")
    lines.append("")
    return "\n".join(lines)

def tools_md():
    lines=["# Customer-Centric Branding Toolkit","",f"*{C.TITLE} · {C.COURSE_CODE}*",""]
    lines.append("## Frameworks used in the activities")
    lines.append("")
    lines.append("| Framework | What it does | Used in |")
    lines.append("|---|---|---|")
    rows=[
        ("Stakeholder Influence Matrix","Scores each stakeholder's influence (1-5) and defines an engagement approach per group.","Activity 1"),
        ("Audience segmentation & messaging map","Profiles external audience segments and tailors message + channel per segment.","Activity 2"),
        ("Hard/soft brand attribute mapping","Separates product features (hard) from lifestyle benefits (soft) to build a brand concept.","Activity 3"),
        ("Digital reputation audit","Samples mentions/reviews across platforms and categorises sentiment into recurring themes.","Activities 4, 13"),
        ("Perception-gap analysis","Compares internal quality metrics against customer feedback to find where perception diverges from reality.","Activity 5"),
        ("3 P's active listening (Presence, Patience, Paraphrasing)","A structured technique for hearing the emotion behind a customer's words, not just the words.","Activity 8"),
        ("Brand guidelines framework","Defines core values, visual identity and voice guidelines from an audit of existing touchpoints.","Activity 9"),
        ("Brand activation planning canvas","Plans a multi-channel campaign — audience, message, channels, experiential element, recall metric.","Activity 11"),
        ("PR budget allocation (earned / owned / paid)","Splits a PR budget across earned, owned and paid channels against defined KPIs.","Activity 12"),
        ("Brand health scorecard","Tracks awareness, loyalty and performance metrics against benchmarks on a recurring cadence.","Activity 14"),
        ("KPI framework (internal / external)","Defines measure, target, data source and frequency for a balanced set of brand KPIs.","Activity 16"),
        ("AMEC measurement framework","An industry framework for evaluating PR/communication campaign effectiveness and surfacing gaps.","Activity 17"),
    ]
    for r in rows: lines.append(f"| {r[0]} | {r[1]} | {r[2]} |")
    lines.append("")
    lines.append("## SMART KPI quick reference")
    lines.append("")
    lines.append("| Letter | Meaning |")
    lines.append("|---|---|")
    for l,m in [("S","Specific — states exactly what is being measured"),
                ("M","Measurable — has a number or verifiable state"),
                ("A","Attainable — realistic given resources and timeframe"),
                ("R","Realistic — relevant to the brand's actual goals"),
                ("T","Time-bound — has a deadline or review cadence")]:
        lines.append(f"| **{l}** | {m} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*© 2026 Tertiary Infotech Academy Pte Ltd*")
    lines.append("")
    return "\n".join(lines)

if __name__=="__main__":
    os.makedirs(LABS,exist_ok=True)
    with open(os.path.join(LABS,"README.md"),"w",encoding="utf-8") as f: f.write(readme_md())
    print("Wrote",os.path.join(LABS,"README.md"))
    with open(os.path.join(LABS,"tools.md"),"w",encoding="utf-8") as f: f.write(tools_md())
    print("Wrote",os.path.join(LABS,"tools.md"))
    for a in ACT:
        fname=f"lab-{a['num']:02d}-{slug(a['title'])}.md"
        path=os.path.join(LABS,fname)
        with open(path,"w",encoding="utf-8") as f: f.write(lab_md(a))
        print("Wrote",path)
