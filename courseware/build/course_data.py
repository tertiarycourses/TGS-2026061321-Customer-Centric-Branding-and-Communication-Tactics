"""
SINGLE SOURCE OF TRUTH for the Customer-Centric Branding and Communication
Tactics courseware.

Every artifact — the slide deck (PPT), Lesson Plan (LP) and Learner Guide (LG)
— is generated from the data in this module (+ data_domain1..4.py), so
titles, topic numbering, activities, learning outcomes and the schedule can
never drift apart.

Content source: Skills Framework TSC "Brand Management" (TSC Code
ICT-SNM-3002-1.1, Proficiency Level 3), 4 Learning Units (LU1-LU4), 17
Knowledge/Ability-based topics and 17 in-class activities, supplied by the
course owner.

Edit here, then re-run build_slides.py / build_lesson_plan.py /
build_learner_guide.py (or ./build_courseware.sh).
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Customer-Centric Branding and Communication Tactics"
SHORT_TITLE  = "Customer-Centric Branding and Communication Tactics"
COURSE_CODE  = "TGS-2026061321"
VERSION      = "v1"          # slide-deck version (part of the .pptx filename)
DOC_VERSION  = "1.0"         # Lesson Plan / Learner Guide DOCX version (N.N)
VERSION_DATE = "20 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "[Trainer Name]"          # placeholder — to be filled in by the assigned trainer
DAYS         = 2

TSC_TITLE   = "Brand Management"
TSC_CODE    = "ICT-SNM-3002-1.1"
TSC_LEVEL   = "Level 3"

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Identify the internal and external stakeholders and audiences who influence the brand, "
    "and create branding designs and reputation assessments that reflect the organisation's product "
    "or service attributes and benefits.",
    "LO2: Capture and analyse customer insights through strategic active-listening approaches — "
    "understanding customer perceptions of the brand and documenting the reception and outcomes of "
    "branding campaigns.",
    "LO3: Apply branding fundamentals within the marketing mix — executing branding campaigns, "
    "events and public-relations activities that increase brand awareness in alignment with brand "
    "positioning strategy, operational plans and budget.",
    "LO4: Evaluate brand and public-relations effectiveness using reputation indicators and KPIs "
    "across platforms, and recommend improvements to strengthen public-relations campaign "
    "performance.",
]

# ------------------------------------------------------------------ topics (= Learning Units)
# num, code, title, subtitle, concept bullets for the section (one per Knowledge/Ability statement)
TOPICS = [
    dict(num=1, code="LU1",
         title="Stakeholders and Organisation",
         subtitle="Internal & External Stakeholders · Audience Types · Brand Design · Reputation Assessment",
         concepts=[
            "Internal stakeholders (management, employees) and external stakeholders (customers, partners, "
            "investors, media) each hold a different level of influence over — and interest in — the brand.",
            "External audiences segment into customers, partners, investors and media; each needs its own "
            "communication approach and message.",
            "Branding designs and ideas should foreground the product or service's attributes and the "
            "concrete benefits they deliver to the audience.",
            "Assessing an organisation's reputation on social media and other platforms — reviews, mentions, "
            "sentiment — is the starting point for every branding decision.",
         ]),
    dict(num=2, code="LU2",
         title="Customer Influence",
         subtitle="Customer Perceptions · Brand Reputation · Campaign Reception · Active Listening",
         concepts=[
            "Customers form perceptions of a brand, its products and its services from quality, experience "
            "and communication — a gap often exists between what a company believes and what customers "
            "actually feel.",
            "Customers actively shape brand reputation through word-of-mouth, reviews and advocacy — their "
            "voice can amplify or damage a brand faster than any paid campaign.",
            "Documenting customer reception and the outcome of branding campaigns turns anecdotal feedback "
            "into evidence for future campaign decisions.",
            "Active listening — full attention, a structured framework, and paraphrasing without judgement — "
            "reveals the customer's true perspective of the organisation.",
         ]),
    dict(num=3, code="LU3",
         title="Branding in Marketing",
         subtitle="Branding Basics · Role in Marketing · Awareness Campaigns · PR Execution",
         concepts=[
            "Branding basics — visual identity, brand values, brand voice and brand guidelines — give a "
            "business a consistent, recognisable presence.",
            "Branding plays a central role in marketing: it builds trust, differentiates from competitors "
            "and creates the emotional connection that drives loyalty.",
            "Executing branding campaigns, events and activities — from social pushes to experiential "
            "pop-ups — raises brand awareness across the target audience.",
            "Public-relations campaigns must align to the brand positioning strategy, the operational plan "
            "and the marketing budget to stay credible and sustainable.",
         ]),
    dict(num=4, code="LU4",
         title="Branding Effectiveness",
         subtitle="Reputation Metrics · Success Indicators · PR Tactics · KPI Monitoring · Continuous Improvement",
         concepts=[
            "Reputation is measured through social metrics, digital metrics (traffic, mentions) and business "
            "KPIs (NPS, satisfaction) across every platform the organisation touches.",
            "Successful branding shows up in awareness, customer loyalty, financial impact and trust metrics "
            "— tracked consistently over time, not measured once.",
            "Public-relations tactics — media relations, community outreach, crisis management and digital "
            "engagement — extend the brand's message beyond paid channels.",
            "Monitoring the brand against SMART KPIs and acting on the gaps turns brand management into a "
            "continuous-improvement cycle rather than a one-off campaign.",
         ]),
]

# ------------------------------------------------------------------ 2-day schedule (WSQ house format)
# Day 1: full teaching day, 9:30am-6:30pm, 1-hour lunch, no assessment.
# Day 2: teaching until 4:00pm, then the 2-hour Assessment block (WA 1h + Case Study 1h), ending 6:00pm.
DAY_THEMES = {
    1: "Stakeholders, Customer Influence & Branding in Marketing (starts)",
    2: "Branding in Marketing (cont'd), Branding Effectiveness & Assessment",
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book.",
    practical="Case Study (CS) — one continuous branding scenario with open-ended tasks, 1 hour, open book.",
    note="A minimum of 75% attendance (per SSG Digital Attendance record) is required to be eligible for "
         "assessment and funding. Learners must be assessed as Competent and complete the TRAQOM survey.",
)
