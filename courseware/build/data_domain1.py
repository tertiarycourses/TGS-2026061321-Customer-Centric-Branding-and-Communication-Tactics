"""LU1 — Stakeholders and Organisation: in-class activities 1-4.

Each activity also carries the underlying Knowledge/Ability (K/A) topic's
theory content — a "what is X?" concept slide plus one supporting data
visual — so the deck teaches the concept before the hands-on activity."""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Stakeholder Influence Mapping",
        objective="Identify internal and external stakeholders influencing the brand",
        t_statement="Internal and external stakeholders influencing the brand",
        what_is_kind="tile",
        what_is_items=[
            ("Internal Power", "Direct brand influence through operations"),
            ("External Impact", "Market-driven perception and revenue influence"),
            ("Stakeholder Mapping", "Strategic categorisation by interest and influence"),
            ("Message Alignment", "Consistent communication across all groups"),
        ],
        what_is_source="Source: Brand Stakeholders Guide, 2024",
        visual_kind="bar",
        visual_title="Stakeholder Distribution Analysis",
        visual_items=[("Internal", 45), ("External", 35), ("Hybrid", 20)],
        visual_source="Source: Stakeholder Analysis, Miro 2024",
        desc="Your company is launching a new sustainability initiative. Map internal and external "
             "stakeholders, assess their influence levels, and design engagement strategies for each group.",
        build="A stakeholder influence matrix (12 stakeholders) with an engagement strategy for each group",
        duration="25 minutes",
        steps=[
            ("List 6 internal and 6 external stakeholders for the sustainability initiative.", ""),
            ("Rate each stakeholder's influence on a 1–5 scale.", ""),
            ("Identify each stakeholder's primary brand concern.", ""),
            ("Design a specific communication approach for each group.", ""),
        ],
        test="Present a completed stakeholder influence matrix with an engagement strategy for every "
             "stakeholder — the trainer checks that internal and external groups are both represented and "
             "that each strategy matches the stakeholder's stated concern.",
    ),
    dict(
        num=2,
        topic=1,
        title="Audience Mapping Workshop",
        objective="Recognise the types of external audience and their needs",
        t_statement="Types of external audience",
        what_is_kind="flow",
        what_is_items=[
            "Customers — prospects and loyal brand advocates",
            "Partners — business collaborators and suppliers",
            "Investors — financial stakeholders and shareholders",
            "Media — press and communication channels",
        ],
        what_is_source="Source: Trust Insights, 2024",
        visual_kind="bar",
        visual_title="Audience Distribution Analysis",
        visual_items=[("Customers", 40), ("Partners", 25), ("Investors", 20), ("Media", 15)],
        visual_source="Source: Trust Insights, 2024",
        desc="Your company is launching a new sustainability product line. Map external audiences and "
             "develop targeted messaging strategies for each segment.",
        build="An audience mapping matrix covering 4 external segments with tailored messaging and channels",
        duration="25 minutes",
        steps=[
            ("Identify four primary external audience segments for the product.", ""),
            ("Research the demographic and psychographic profile of each segment.", ""),
            ("Create a tailored key message for each segment, emphasising the relevant benefit.", ""),
            ("Select the appropriate communication channel(s) for each audience.", ""),
            ("Present the audience mapping matrix with its messaging strategy.", ""),
        ],
        test="Present a comprehensive audience-analysis matrix with segment profiles and a customised "
             "communication plan per segment.",
    ),
    dict(
        num=3,
        topic=1,
        title="Brand Attribute Mapping",
        objective="Draft branding designs and ideas highlighting the product or service's attributes and benefits",
        t_statement="Draft branding designs and ideas highlighting the product or service's attributes and benefits",
        what_is_kind="tile",
        what_is_items=[
            ("Brand Strategy", "Define unique selling proposition"),
            ("Visual Identity", "Create a recognisable design system"),
            ("Value Communication", "Translate features into benefits"),
            ("Consistency", "Maintain a unified brand experience"),
        ],
        what_is_source="Source: Duck Design, SmashBrand 2024",
        visual_kind="bar",
        visual_title="Visual Brand Impact Statistics",
        visual_items=[("Visual Impact", 85), ("Soft Attributes", 60), ("Hard Attributes", 40)],
        visual_source="Source: Duck Design, Clay Global 2024",
        desc="Design a brand identity for a new fitness app targeting busy professionals, mapping both hard "
             "attributes (features) and soft attributes (lifestyle benefits) into a compelling visual concept.",
        build="A brand attribute map (3 hard + 3 soft attributes), a mood board and a logo concept",
        duration="30 minutes",
        steps=[
            ("List 3 hard attributes and 3 soft attributes for the fitness app.", ""),
            ("Create a visual mood board that represents the brand personality.", ""),
            ("Design a logo concept that incorporates the key attributes.", ""),
            ("Present a brand narrative that connects the features to the benefits.", ""),
        ],
        test="Present the complete brand attribute map alongside the visual concept, showing a clear line "
             "from each hard attribute to the soft benefit it supports.",
    ),
    dict(
        num=4,
        topic=1,
        title="Digital Reputation Audit Exercise",
        objective="Assess the organisation's reputation on social media and other platforms",
        t_statement="Assess organisation's reputation on social media and other platforms",
        what_is_kind="tile",
        what_is_items=[
            ("Brand Monitoring", "Track mentions across digital platforms"),
            ("Sentiment Analysis", "Analyse customer feedback patterns"),
            ("Multi-Platform", "Coverage of social and review sites"),
            ("Strategic Response", "Data-driven brand improvement actions"),
        ],
        what_is_source="Source: Sprout Social, 2024",
        visual_kind="bar",
        visual_title="Platform Distribution Statistics",
        visual_items=[("Google", 38), ("Facebook", 38), ("Other Platforms", 24)],
        visual_source="Source: Sprout Social, 2024",
        desc="Your organisation has received mixed customer feedback across social platforms. Conduct a "
             "reputation assessment to identify improvement opportunities and develop an action plan.",
        build="A reputation-assessment report covering 3 platforms with sentiment breakdown and an action plan",
        duration="45 minutes",
        steps=[
            ("Select three platforms (e.g. Google, Facebook, one competitor platform).", ""),
            ("Document 10 recent mentions/reviews per platform.", ""),
            ("Categorise each piece of feedback as positive, neutral or negative.", ""),
            ("Identify three recurring themes or issues across the feedback.", ""),
            ("Develop a targeted response strategy for each theme.", ""),
        ],
        test="Present the reputation-assessment report — platform-by-platform analysis, an overall sentiment "
             "breakdown, the three key themes, and a strategic recommendation for each.",
    ),
]
