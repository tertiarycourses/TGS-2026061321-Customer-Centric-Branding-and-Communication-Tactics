"""LU2 — Customer Influence: in-class activities 5-8.

Each activity also carries the underlying Knowledge/Ability (K/A) topic's
theory content — a "what is X?" concept slide plus one supporting data
visual — so the deck teaches the concept before the hands-on activity."""

DOMAIN2 = [
    dict(
        num=5,
        topic=2,
        title="Brand Perception Audit",
        objective="Assess customer perceptions of the brand, products and services",
        t_statement="Perceptions of customers of the brand, products and services",
        what_is_kind="tile",
        what_is_items=[
            ("Product View", "Customer attitudes toward offerings"),
            ("Brand Identity", "Customer understanding of brand values"),
            ("Service Quality", "Perceived value of interactions"),
            ("Perception Gap", "Difference between reality and belief"),
        ],
        what_is_source="Source: Qualtrics, 2024",
        visual_kind="bar",
        visual_title="The Perception Gap Reality",
        visual_items=[("Companies Believe", 54.1), ("Service Purchase", 40.5), ("Customers Agree", 5.4)],
        visual_source="Source: Qualtrics & Zendesk, 2024",
        desc="Your company recently received mixed customer reviews. Management believes service quality is "
             "excellent, but customer-satisfaction scores are declining. Conduct a perception audit to "
             "identify the gaps.",
        build="A perception-gap analysis report comparing internal quality metrics with customer feedback",
        duration="25 minutes",
        steps=[
            ("Survey 20 recent customers about their service experience.", ""),
            ("Compare internal quality metrics with the customer feedback.", ""),
            ("Identify the top 3 perception gaps.", ""),
            ("Develop an action plan to address the gaps.", ""),
        ],
        test="Present the perception-gap analysis report with improvement recommendations for each of the "
             "top 3 gaps.",
    ),
    dict(
        num=6,
        topic=2,
        title="Brand Advocacy Assessment",
        objective="Recognise the importance of the customer in influencing brand reputation",
        t_statement="Importance of the customer in influencing the brand reputation",
        what_is_kind="tile",
        what_is_items=[
            ("Trust Factor", "Personal recommendations drive purchase decisions"),
            ("Viral Spread", "Positive experiences multiply through networks"),
            ("Digital Voice", "Online reviews equal family recommendations"),
            ("Reputation Control", "Customers actively shape the brand image"),
        ],
        what_is_source="Source: WebFX, Digital Silk 2024",
        visual_kind="bar",
        visual_title="Word-of-Mouth Impact Statistics",
        visual_items=[("Trust WOM", 88), ("Share Good", 72), ("Purchase Factor", 74), ("Review Trust", 82)],
        visual_source="Source: Buyapowa, WebFX 2024",
        desc="Your company recently received mixed reviews online. As brand manager, analyse customer "
             "feedback and develop an advocacy strategy to improve brand reputation through existing "
             "satisfied customers.",
        build="A customer-advocacy strategy document with target impact metrics",
        duration="25 minutes",
        steps=[
            ("Review the provided customer feedback data.", ""),
            ("Identify satisfied customers for the advocacy programme.", ""),
            ("Design an advocacy campaign that leverages their positive experiences.", ""),
            ("Present the strategy together with its expected impact metrics.", ""),
        ],
        test="Present a comprehensive advocacy strategy document with named target metrics and how they will "
             "be tracked.",
    ),
    dict(
        num=7,
        topic=2,
        title="Campaign Documentation Audit",
        objective="Document customer reception to the brand and the outcome of branding campaigns",
        t_statement="Document customer reception to brand and outcome of branding campaigns",
        what_is_kind="flow",
        what_is_items=[
            "Feedback Collection — systematic recording of customer responses",
            "Campaign Metrics — measuring effectiveness through customer data",
            "Analysis Systems — documentation frameworks for brand reception",
            "Outcome Tracking — recording measurable campaign results",
        ],
        what_is_source="Source: Multiple branding studies, 2024-2026",
        visual_kind="tile",
        visual_title="Key Performance Statistics",
        visual_items=[
            ("Trust Impact", "Builds confidence in the brand's promises"),
            ("Loyalty Rate", "Drives repeat engagement with the brand"),
            ("Repeat Spending", "Increases customer lifetime value"),
            ("Revenue Growth", "Converts documented reception into business results"),
        ],
        visual_source="Source: Fit Small Business 2024, Wiser Review 2026",
        desc="Your company launched a new product branding campaign three months ago. Management needs a "
             "documentation report on customer reception and campaign outcomes to inform future marketing "
             "investment.",
        build="A structured campaign-reception report with metrics, analysis and optimisation recommendations",
        duration="25 minutes",
        steps=[
            ("Identify three key metrics from the campaign data.", ""),
            ("Analyse customer feedback patterns and sentiment trends.", ""),
            ("Create a documentation framework for ongoing measurement.", ""),
            ("Present the findings with actionable recommendations.", ""),
        ],
        test="Present the structured campaign-reception report, including the documentation framework that "
             "will be reused for the next campaign.",
    ),
    dict(
        num=8,
        topic=2,
        title="Customer Perspective Analysis",
        objective="Perform active listening from the customer to understand the customer's perspective of the organisation",
        t_statement="Perform active listening from customer to understand customer's perspective of the organisation",
        what_is_kind="tile",
        what_is_items=[
            ("Full Attention", "Eliminate distractions during customer interactions"),
            ("3 P's Framework", "Presence, Patience, and Paraphrasing approach"),
            ("Emotion Focus", "Understanding the feelings behind customer words"),
            ("Strategic Insight", "Gather valuable customer perception data"),
        ],
        what_is_source="Source: Active Listening in Customer Service, 2024",
        visual_kind="bar",
        visual_title="Key Statistics on Customer Satisfaction and Active Listening",
        visual_items=[("Feel Understood", 56), ("Want Skills", 57), ("Loyalty Boost", 1.5), ("Churn Reduction", 15)],
        visual_source="Source: CPD Online, Industry Research, 2024",
        desc="You receive a complaint from a long-term customer expressing frustration about recent service "
             "changes. They say they feel 'unheard' and 'unimportant' to your organisation.",
        build="A completed customer-perspective analysis report with actionable insights",
        duration="25 minutes",
        steps=[
            ("Apply the 3 P's framework — Presence, Patience, Paraphrasing — during the conversation.", ""),
            ("Identify the emotions behind the customer's specific words.", ""),
            ("Paraphrase the customer's perspective back to them without judgement.", ""),
            ("Document the insights for strategic decision-making.", ""),
        ],
        test="Present the completed customer-perspective analysis report — the trainer checks that the "
             "emotion behind the words (not just the words) is captured, and that the insight is actionable.",
    ),
]
