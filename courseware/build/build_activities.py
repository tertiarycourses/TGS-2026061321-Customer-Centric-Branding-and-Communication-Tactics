#!/usr/bin/env python3
"""Generate the activities/ folder — one Markdown activity sheet per in-class
activity (17 total), plus activities/README.md and activities/tools.md — in the
same style as the Tertiary Infotech reference activity folders (e.g. the CLSSBB
course). Content is driven by course_data.py + data_domain1..4.py so the
activity sheets stay aligned with the slide deck, Lesson Plan and Learner Guide.
"""
import os, re, sys

HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import course_data as C
from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3; from data_domain4 import DOMAIN4
ACT=DOMAIN1+DOMAIN2+DOMAIN3+DOMAIN4
REPO=os.path.dirname(os.path.dirname(HERE))
ACTIVITIES=os.path.join(REPO,"activities")

FOOTER=f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 Tertiary Infotech Academy Pte Ltd*"

def slug(text):
    s=re.sub(r"[^a-z0-9]+","-",text.lower()).strip("-")
    return s

TOPIC_BY_NUM={t["num"]:t for t in C.TOPICS}

ACTIVITY_TYPE_LABEL={"role_play":"In-class role play","case_study":"In-class case study"}

def activity_md(a):
    t=TOPIC_BY_NUM[a["topic"]]
    act_type=ACTIVITY_TYPE_LABEL.get(a.get("case_type"),"In-class workshop")
    lines=[]
    lines.append(f"# Activity {a['num']} — {a['title']}")
    lines.append("")
    lines.append(f"**Learning Unit:** {t['code']} — {t['title']}  |  **Activity type:** {act_type}  |  "
                 f"**Course:** {C.TITLE} ({C.COURSE_CODE})")
    lines.append("")
    lines.append("## Objective")
    lines.append("")
    lines.append(f"{a['objective']}.")
    lines.append("")
    lines.append("## Scenario")
    lines.append("")
    for para in a["case_scenario"]:
        lines.append(para)
        lines.append("")
    lines.append("## What you will produce")
    lines.append("")
    lines.append(a["build"] + ".")
    lines.append("")
    lines.append(f"**Duration:** {a['duration']}")
    lines.append("")
    if a.get("roles"):
        lines.append("## Roles")
        lines.append("")
        lines.append("Assign one role per participant (or per small group):")
        lines.append("")
        for name,goal,brief in a["roles"]:
            lines.append(f"- **{name}** — *Goal: {goal}.* {brief}")
        lines.append("")
    lines.append("## Discussion & Decision Prompts")
    lines.append("")
    lines.append("Work through these together — there is no single correct order, and no click-by-click "
                 "script to follow:")
    lines.append("")
    for i,p in enumerate(a["discussion_prompts"],1):
        lines.append(f"{i}. {p}")
    lines.append("")
    lines.append("## Reflect & Discuss")
    lines.append("")
    for p in a["reflection_points"]:
        lines.append(f"- {p}")
    lines.append("")
    lines.append("## Debrief it")
    lines.append("")
    lines.append(a["debrief_check"])
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
    lines=[f"# {C.TITLE} Activities",""]
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
        "Every activity is a case study or role play — never a numbered instruction list — built on one "
        "continuous scenario (Nimbus Wellness Pte Ltd) and produces a concrete artifact (a matrix, plan, "
        "audit report or dashboard) that the learner keeps. Each closes with open discussion prompts and "
        "reflection points instead of a pass/fail check. All 17 activities are in-class activities assessed "
        "indirectly through the Case Study (CS) component of the formal WSQ assessment, which reuses the "
        "same techniques on the same continuous scenario.")
    lines.append("")
    lines.append("## Activities")
    lines.append("")
    lines.append("| # | Learning Unit | Activity | Type | Duration |")
    lines.append("|---|---|---|---|---|")
    for a in ACT:
        t=TOPIC_BY_NUM[a["topic"]]
        fname=f"activity-{a['num']:02d}-{slug(a['title'])}.md"
        atype="Role Play" if a.get("case_type")=="role_play" else "Case Study"
        lines.append(f"| {a['num']} | {t['code']} | [{a['title']}]({fname}) | {atype} | {a['duration']} |")
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
    os.makedirs(ACTIVITIES,exist_ok=True)
    with open(os.path.join(ACTIVITIES,"README.md"),"w",encoding="utf-8") as f: f.write(readme_md())
    print("Wrote",os.path.join(ACTIVITIES,"README.md"))
    with open(os.path.join(ACTIVITIES,"tools.md"),"w",encoding="utf-8") as f: f.write(tools_md())
    print("Wrote",os.path.join(ACTIVITIES,"tools.md"))
    for a in ACT:
        fname=f"activity-{a['num']:02d}-{slug(a['title'])}.md"
        path=os.path.join(ACTIVITIES,fname)
        with open(path,"w",encoding="utf-8") as f: f.write(activity_md(a))
        print("Wrote",path)
