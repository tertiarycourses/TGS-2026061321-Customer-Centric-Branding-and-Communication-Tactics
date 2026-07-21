"""LU4 — Branding Effectiveness: in-class activities 13-17.

Each activity also carries the underlying Knowledge/Ability (K/A) topic's
theory content — a "what is X?" concept slide plus one supporting data
visual — so the deck teaches the concept before the hands-on activity."""

DOMAIN4 = [
    dict(
        num=13,
        topic=4,
        title="Platform Reputation Audit",
        objective="Identify measures or indicators of the organisation's reputation on different platforms",
        t_statement="Measures or indicators of organisation's reputation on different platforms",
        what_is_kind="flow",
        what_is_items=[
            "Social Media — followers, engagement, sentiment tracking",
            "Digital Metrics — website traffic, search rankings, mentions",
            "Business KPIs — NPS scores, satisfaction, financial impact",
            "Stakeholder Data — customer, employee, investor perceptions",
        ],
        what_is_source="Source: Meltwater, 2024",
        visual_kind="bar",
        visual_title="Core Indicator Categories",
        visual_items=[("Social Media", 33), ("Digital", 33), ("Business", 34)],
        visual_source="Source: Meltwater, 2024",
        desc="Your organisation needs to establish reputation monitoring for a new product launch across "
             "social media, review sites, and business platforms.",
        build="A reputation-monitoring framework with defined metrics and tracking systems",
        duration="20 minutes",
        steps=[
            ("Map the stakeholder groups and select 3 key platforms per group.", ""),
            ("Define specific KPIs for the social, digital and business indicators.", ""),
            ("Set up monitoring tools and establish baseline measurements.", ""),
            ("Create a weekly reporting dashboard showing sentiment trends.", ""),
        ],
        test="Present the comprehensive reputation-monitoring framework with its metrics and tracking system.",
    ),
    dict(
        num=14,
        topic=4,
        title="Brand Health Assessment",
        objective="Recognise the indicators of successful branding",
        t_statement="Indicators of successful branding",
        what_is_kind="tile",
        what_is_items=[
            ("Brand Awareness", "Recognition and recall measurement"),
            ("Customer Loyalty", "Retention and repeat purchase rates"),
            ("Financial Impact", "Revenue growth and market share"),
            ("Trust Metrics", "Consumer confidence and perception"),
        ],
        what_is_source="Source: Brand Health Tracking Best Practices, 2024",
        visual_kind="bar",
        visual_title="Key Brand Performance Statistics",
        visual_items=[("Trust Required", 83), ("Pay Premium", 90), ("Try New", 86), ("Revenue Boost", 33)],
        visual_source="Source: Zippia 2023, G2 2025",
        desc="You are a marketing manager evaluating your company's brand performance using both traditional "
             "and digital metrics.",
        build="A brand-health scorecard with metric definitions, current performance and an improvement plan",
        duration="25 minutes",
        steps=[
            ("Select 3 key metrics from the awareness, loyalty and performance categories.", ""),
            ("Design a measurement approach that combines survey and digital analytics.", ""),
            ("Create a monthly tracking dashboard with benchmarks.", ""),
            ("Present the findings with actionable recommendations.", ""),
        ],
        test="Present the brand-health scorecard — metric definitions, current performance and the "
             "improvement plan.",
    ),
    dict(
        num=15,
        topic=4,
        title="PR Crisis Response Plan",
        objective="Apply public-relations tactics",
        t_statement="Public relations tactics",
        what_is_kind="tile",
        what_is_items=[
            ("Media Relations", "Build journalist partnerships for visibility"),
            ("Community Outreach", "Engage local audiences and stakeholders"),
            ("Crisis Management", "Protect reputation during challenges"),
            ("Digital Engagement", "Social media and online interactions"),
        ],
        what_is_source="Source: PR Strategy Essentials, 2024",
        visual_kind="bar",
        visual_title="Journalist Preferences Data",
        visual_items=[("Press Releases", 46.3), ("Research Reports", 38.1), ("High Pitch Volume", 15.6)],
        visual_source="Source: Meltwater Research, 2024",
        desc="Your company faces negative social-media coverage about product-quality issues. Design a "
             "comprehensive PR response strategy using the tactics learned.",
        build="A crisis-communication plan with timelines and responsible parties",
        duration="25 minutes",
        steps=[
            ("Identify the affected stakeholder groups and media outlets.", ""),
            ("Develop core messaging that addresses the concerns transparently.", ""),
            ("Create a media-outreach plan with personalised pitches.", ""),
            ("Design the social-media response and community-engagement plan.", ""),
            ("Establish measurement metrics for reputation recovery.", ""),
        ],
        test="Present the complete crisis-communication plan with a timeline and the party responsible for "
             "each action.",
    ),
    dict(
        num=16,
        topic=4,
        title="KPI Dashboard Design",
        objective="Monitor the success of the brand against Key Performance Indicators (KPI)",
        t_statement="Monitor the success of the brand against Key Performance Indicators (KPI)",
        what_is_kind="tile",
        what_is_items=[
            ("SMART KPIs", "Specific, measurable, attainable, realistic, time-bound"),
            ("Data Collection", "Analytics tools and brand guidelines"),
            ("Performance Analysis", "Interpret trends and changes"),
            ("Strategic Optimisation", "Insights drive brand improvements"),
        ],
        what_is_source="Source: Frontify, 2024",
        visual_kind="bar",
        visual_title="KPI Distribution",
        visual_items=[("Internal KPIs", 50), ("External KPIs", 50), ("Leading Indicators", 40), ("Lagging Indicators", 60)],
        visual_source="Source: Frontify & Improvado, 2024-2026",
        desc="Create a brand KPI monitoring framework for a retail company launching new product lines.",
        build="A complete KPI framework with a tracking schedule",
        duration="20 minutes",
        steps=[
            ("Select 3 internal and 3 external KPIs.", ""),
            ("Define the measure, target, data source and frequency for each KPI.", ""),
            ("Design a monthly tracking dashboard.", ""),
        ],
        test="Present the complete KPI framework with its tracking schedule — 3 internal + 3 external KPIs, "
             "each with a measure, target, source and frequency.",
    ),
    dict(
        num=17,
        topic=4,
        title="PR Campaign Audit Exercise",
        objective="Provide suggestions to improve public-relations campaign effectiveness",
        t_statement="Provide suggestions to improve public relations campaign effectiveness",
        what_is_kind="tile",
        what_is_items=[
            ("Performance Gaps", "Identify weaknesses through data analysis"),
            ("Strategic Planning", "Develop measurable objectives and tactics"),
            ("Media Relations", "Build strong journalist partnerships"),
            ("Content Quality", "Create compelling research-backed stories"),
        ],
        what_is_source="Source: AMEC Framework, 2024",
        visual_kind="bar",
        visual_title="Key Performance Indicators",
        visual_items=[("Message Success", 70), ("Sentiment Improvement", 60), ("Tier 1 Coverage", 30)],
        visual_source="Source: Agility PR & Determ, 2024",
        desc="Your organisation's recent product-launch campaign achieved 500K impressions but only 15% "
             "top-tier coverage and 45% message penetration. Stakeholders are questioning the campaign's "
             "business impact.",
        build="An improvement proposal with metrics, built using the AMEC measurement framework",
        duration="25 minutes",
        steps=[
            ("Apply the AMEC framework to identify the performance gaps.", ""),
            ("Develop three strategic recommendations using best practice.", ""),
            ("Create a measurement plan with specific KPIs.", ""),
        ],
        test="Present the comprehensive improvement proposal — the three recommendations must each map to a "
             "specific gap surfaced by the AMEC analysis.",
    ),
]
