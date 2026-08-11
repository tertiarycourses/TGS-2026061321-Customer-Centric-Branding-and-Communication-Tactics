"""LU1 — Stakeholders and Organisation: in-class activities 1-4.

Each activity carries the underlying Knowledge/Ability (K/A) topic's theory
content — a "what is X?" concept slide, a process/model slide, a compare
slide, a supporting data visual, and (where set) a real-world "case_example_*"
callout — so the deck teaches the concept before the hands-on activity.
`what_is_kind` / `compare_kind` / `process_kind` / `visual_kind` select which
renderer build_slides.py uses for those slots (see the dispatch tables
render_what_is/render_compare/render_process/render_visual there); omit any
key to fall back to the plain tile-grid / two-column / vertical-list default.
Each kind expects a specific data shape — see the matching helper's docstring
in build_slides.py (e.g. visual_kind="journey" needs visual_items shaped for
journey_map(); visual_kind="empathy" needs visual_says/thinks/does/feels).

All four activities run on one continuous scenario — Nimbus Wellness Pte
Ltd, a Singapore boutique skincare & wellness brand three months from its
5th-anniversary relaunch — so the in-class work builds directly toward the
Day 2 Case Study assessment, which reuses this exact company.

Every activity is a case study or role play (never a numbered step list):
`case_scenario` is the narrative, `roles` (role-play only) are the personas
to assign, `discussion_prompts` are open questions the group works through,
and `reflection_points` + `debrief_check` close the activity out."""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Stakeholder Influence Mapping",
        objective="Identify internal and external stakeholders influencing the brand",
        t_statement="Internal and external stakeholders influencing the brand",
        what_is_kind="ecosystem",
        what_is_center="NIMBUS",
        what_is_items=[
            ("people", "Employees"),
            ("star", "Retail Partners"),
            ("chat", "Media & Press"),
            ("shield", "Regulators"),
            ("heart", "Loyal Customers"),
            ("flag", "Investors"),
        ],
        what_is_source="Source: Mendelow, A. (1991), Stakeholder Mapping",
        process_kind="infographic",
        process_template="sequence-roadmap-vertical-simple",
        process_title="Stakeholder Management Process",
        process_items=[
            ("Identify", "Map every stakeholder group touched by the decision."),
            ("Map Power & Interest", "Plot each group's influence and how much they care."),
            ("Match the Approach", "Engage, consult, inform or monitor — matched to the quadrant."),
        ],
        process_source="Source: Mendelow's Power-Interest Matrix, adapted",
        compare_kind="infographic",
        compare_template="quadrant-quarter-simple-card",
        compare_title="Stakeholder Power-Interest Grid",
        compare_xaxis="Interest (low → high)",
        compare_yaxis="Power (low → high)",
        compare_items=[
            ("Keep Informed", "Retail floor staff, Loyal-customer community"),
            ("Manage Closely", "Founder / CEO, Key retail partner buyer"),
            ("Monitor", "Peripheral suppliers, Distant regulators"),
            ("Keep Satisfied", "Board / investors, Wholesale distributors"),
        ],
        compare_quadrants=[
            ("Keep Informed", "teal", ["Retail floor staff", "Loyal-customer community"]),
            ("Manage Closely", "blue", ["Founder / CEO", "Key retail partner buyer"]),
            ("Monitor", "grey", ["Peripheral suppliers", "Distant regulators"]),
            ("Keep Satisfied", "violet", ["Board / investors", "Wholesale distributors"]),
        ],
        compare_source="Source: Mendelow's Power-Interest Matrix, 1991 (adapted)",
        table_title="Stakeholder Analysis at a Glance",
        table_rows=[
            ("Power/Interest Grid", "Plot stakeholders by influence and interest level", "A CEO = high power, high interest; a junior clerk = low power, low interest"),
            ("Primary Stakeholders", "Directly affected by, or involved in, brand decisions", "Employees, customers, direct suppliers"),
            ("Secondary Stakeholders", "Indirectly affected, but can still shape opinion", "Media, regulators, industry analysts"),
            ("Engagement Cadence", "How often each group needs updates", "Weekly for employees, quarterly for investors"),
        ],
        table_source="Source: Stakeholder analysis frameworks, industry synthesis",
        big_line1="Ignore a stakeholder, and they will define your brand for you.",
        big_line2="The groups you don't actively manage still form opinions — just without your input.",
        visual_kind="infographic",
        visual_template="chart-pie-donut-plain-text",
        visual_title="Stakeholder Distribution Analysis",
        visual_items=[("Internal", 45), ("External", 35), ("Hybrid", 20)],
        visual_source="Source: illustrative distribution, stakeholder-mapping workshops",
        takeaways_title="Brand Stakeholder Success Factors",
        takeaways_items=[
            ("Early Involvement", "Increase ownership and commitment levels"),
            ("Message Consistency", "Align internal and external communications"),
            ("Feedback Loops", "Two-way communication and advisory systems"),
            ("Reputation Gap", "Prevent internal-external perception misalignment"),
        ],
        takeaways_source="Source: internal/external communication best practice",
        case_example_company="Singapore Airlines",
        case_example_headline="Internal Culture Is the First Stakeholder You Manage",
        case_example_insight="SIA's famed inflight service isn't a customer-facing script — it's "
             "the product of decades of internal training investment. Staff who feel genuinely valued "
             "as stakeholders are the ones who convincingly make customers feel valued too.",
        case_type="role_play",
        case_scenario=[
            "Nimbus Wellness Pte Ltd, a 25-person Singapore boutique skincare and wellness brand, is three "
            "months from its 5th-anniversary relaunch. The founder has committed to a new sustainable-"
            "packaging line as the centrepiece of the relaunch story.",
            "Not everyone is convinced. Retail operations worries the new packaging will raise unit cost and "
            "slow reorders. A wellness retail chain that carries Nimbus in 40 outlets wants proof the change "
            "won't disrupt supply before it commits fresh shelf space. Meanwhile a vocal community of "
            "long-time customers on social media is already asking why Nimbus hasn't \"gone green\" sooner.",
            "Before the founder locks the relaunch brief, your table must map who genuinely has power and "
            "interest in this decision — and design how to bring each group along, not just announce it to them.",
        ],
        roles=[
            ("The Founder", "Protect the relaunch vision",
             "Wants sustainability to be the headline story of the anniversary campaign and is impatient "
             "with anything that looks like delay."),
            ("Retail Operations Lead", "Protect margin and delivery reliability",
             "Worried the new packaging supplier will slow reorders right before the relaunch peak season."),
            ("Retail Partner Buyer", "Protect their own shelf-space risk",
             "Will only commit expanded shelf space once supply reliability through the transition is proven."),
        ],
        discussion_prompts=[
            "Which 6 internal and 6 external stakeholders matter most to this relaunch decision, and why?",
            "Using the Power-Interest Grid, where does each stakeholder sit — and which quadrant deserves "
            "your table's limited attention this month?",
            "What is each stakeholder's real underlying concern, not just their stated position?",
            "What engagement approach — brief, consult or co-design — fits each stakeholder's concern and "
            "influence level?",
        ],
        reflection_points=[
            "Which stakeholder's position surprised you once you heard their actual concern instead of "
            "assuming it?",
            "Did power and interest always move together on your map, or did a low-power/high-interest voice "
            "turn out to be worth listening to anyway?",
            "If the retail partner buyer voiced hesitation publicly tomorrow, how would that change your grid?",
        ],
        debrief_check="Every group can show a completed Power-Interest map with both internal and external "
             "stakeholders placed, and an engagement approach per quadrant that matches the stakeholder's "
             "real concern — not just their job title.",
        build="A stakeholder Power-Interest map (12 stakeholders) with a matched engagement approach for each quadrant",
        duration="25 minutes",
    ),
    dict(
        num=2,
        topic=1,
        title="Audience Mapping Workshop",
        objective="Recognise the types of external audience and their needs",
        t_statement="Types of external audience",
        what_is_kind="infographic",
        what_is_template="list-zigzag-down-simple",
        what_is_items=[
            ("Customers", "Prospects and loyal brand advocates"),
            ("Partners", "Business collaborators and suppliers"),
            ("Investors", "Financial stakeholders and shareholders"),
            ("Media", "Press and communication channels"),
        ],
        what_is_source="Source: external-audience segmentation frameworks",
        process_kind="infographic",
        process_template="sequence-roadmap-vertical-simple",
        process_title="Audience Analysis Framework",
        process_items=[
            ("Identify Segments", "Map the primary audience groups."),
            ("Analyse Demographics", "Age, gender, education and other hard factors."),
            ("Study Psychographics", "Values, attitudes and beliefs that drive behaviour."),
            ("Map Preferences", "The communication channels each segment actually uses."),
        ],
        process_source="Source: audience research synthesis",
        compare_kind="infographic",
        compare_template="compare-binary-horizontal-simple-fold",
        compare_title="B2C vs B2B Audience Approaches",
        compare_lhead="B2C — Consumers",
        compare_rhead="B2B — Organisations",
        compare_items=[
            ("Emotion Driven", "Feeling-based purchase decisions"),
            ("Broad Reach", "Mass-market targeting"),
            ("Logic Driven", "Data-based purchase decisions"),
            ("Targeted", "Niche market focus"),
        ],
        compare_left=[
            "Emotion Driven — feeling-based purchase decisions",
            "Broad Reach — mass-market targeting",
            "Quick Decisions — impulse purchase patterns",
        ],
        compare_right=[
            "Logic Driven — data-based purchase decisions",
            "Targeted Approach — niche market focus",
            "Long Process — extended, multi-stakeholder buying cycles",
        ],
        compare_source="Source: B2C/B2B marketing research synthesis",
        table_title="External Audience Segments at a Glance",
        table_rows=[
            ("Customers", "People who buy or could buy the product", "A first-time app downloader"),
            ("Partners", "Organisations that distribute or co-market the brand", "A retail chain stocking the product"),
            ("Investors", "Parties with a financial interest in performance", "A shareholder reading the quarterly report"),
            ("Media", "Channels that shape the public narrative", "A lifestyle journalist covering the relaunch"),
        ],
        table_source="Source: external-audience segmentation frameworks",
        big_line1="One message rarely fits every audience.",
        big_line2="Segment first — then tailor the message, not the truth.",
        visual_kind="persona",
        visual_title="Two Nimbus Audience Personas",
        visual_items=[
            ("Amara Lim", "Existing Loyal Customer",
             ["Feel like Nimbus still “gets” her", "Be recognised for years of support"],
             ["New marketing feels generic", "Unsure what's actually changed"]),
            ("Wei Jie Tan", "Retail Chain Buyer",
             ["Confirm the relaunch won't disrupt supply", "See proof of consistent demand"],
             ["Cautious about more shelf space", "Wants data, not just brand promises"]),
        ],
        visual_source="Source: audience-mapping workshop synthesis",
        takeaways_title="Key Implementation Takeaways",
        takeaways_items=[
            ("Segment First", "Split the audience before writing a single message."),
            ("Research Deep", "Go beyond demographics into values and motivations."),
            ("Message Match", "Tailor the benefit emphasised to each segment."),
            ("Monitor Always", "Audience needs shift — revisit the segmentation regularly."),
        ],
        takeaways_source="Source: audience-segmentation best practice",
        case_example_company="Nike",
        case_example_headline="One Brand, Radically Different Messages Per Segment",
        case_example_insight="Nike speaks to elite athletes through performance data and to "
             "everyday joggers through identity and self-belief — same brand, same logo, "
             "deliberately different message for each audience it serves.",
        case_type="case_study",
        case_scenario=[
            "Nimbus Wellness's 5th-anniversary relaunch has to speak to four very different audiences at "
            "once: existing loyal customers who feel the brand has drifted from them, new customers "
            "discovering Nimbus while comparing it to a competitor, the wellness retail chain deciding "
            "whether to expand shelf space, and the lifestyle press deciding whether the relaunch is even "
            "a story worth covering.",
            "The Marketing Lead has one shared relaunch deck for all four groups. Your table's job is to show "
            "her, with evidence, why it cannot say the same thing to all four the same way — and what should "
            "change for each.",
        ],
        roles=[],
        discussion_prompts=[
            "What does each of the four audience segments actually need to hear to act — not just what "
            "Nimbus wants to say?",
            "Where do B2C emotional drivers and B2B/partner logic-driven drivers pull the message in "
            "different directions?",
            "Which channel does each segment genuinely pay attention to, and does the current \"one deck\" "
            "plan reach it?",
            "If you only had budget to fully tailor one segment's message this month, which would you choose "
            "— and why?",
        ],
        reflection_points=[
            "Which audience did your table initially lump together with another — and what made you split "
            "them apart?",
            "Was a channel choice driven by what's easy for Nimbus to produce, or by where the audience "
            "actually spends attention?",
            "How would your messaging change if the lifestyle press turned out to be sceptical rather than "
            "curious about the relaunch?",
        ],
        debrief_check="Every group can show a matrix with a tailored key message and a named primary channel "
             "for all four segments, and can explain in one sentence why each message differs from the others.",
        build="An audience mapping matrix (4 segments) with a tailored key message and primary channel for each",
        duration="25 minutes",
    ),
    dict(
        num=3,
        topic=1,
        title="Brand Attribute Mapping",
        objective="Draft branding designs and ideas highlighting the product or service's attributes and benefits",
        t_statement="Draft branding designs and ideas highlighting the product or service's attributes and benefits",
        what_is_kind="infographic",
        what_is_template="list-grid-candy-card-lite",
        what_is_items=[
            ("target", "Brand Strategy", "Defines the unique selling proposition"),
            ("star", "Visual Identity", "Builds a recognisable design system"),
            ("chat", "Value Communication", "Translates features into benefits"),
            ("shield", "Consistency", "One brand experience, every touchpoint"),
        ],
        what_is_source="Source: brand strategy & identity practice",
        process_kind="infographic",
        process_template="sequence-snake-steps-simple",
        process_title="Systematic Brand Development Process",
        process_items=[
            ("Define Strategy", "Establish the brand positioning framework."),
            ("Research Industry", "Analyse competitors and the target audience."),
            ("Identify Attributes", "Define the hard and soft characteristics to lead with."),
        ],
        process_source="Source: brand development practice",
        compare_kind="infographic",
        compare_template="compare-binary-horizontal-badge-card-arrow",
        compare_title="Hard vs Soft Brand Attributes",
        compare_lhead="Hard Attributes — Features",
        compare_rhead="Soft Attributes — Feelings",
        compare_items=[
            ("Performance", "Quantifiable product capabilities"),
            ("Features", "Specific functional elements"),
            ("Prestige", "Perceived status and craft"),
            ("Trust", "Reliability and confidence"),
        ],
        compare_left=[
            "Performance — quantifiable product capabilities",
            "Features — specific functional elements",
            "Quality — measurable build/ingredient standards",
        ],
        compare_right=[
            "Prestige — perceived status and craft",
            "Trust — reliability and confidence",
            "Belonging — the feeling of being genuinely known",
        ],
        compare_source="Source: hard/soft brand-attribute framework",
        table_title="Hard vs Soft Attributes — Feature to Benefit",
        table_rows=[
            ("Hard Attribute", "A measurable product fact", "Formulated with 3 clinically-tested actives"),
            ("Soft Attribute", "The feeling that fact creates", "Confidence your skin is genuinely cared for"),
            ("Feature", "What the product does", "Fragrance-free, dermatologist-reviewed formula"),
            ("Benefit", "Why the customer actually cares", "Peace of mind for sensitive, reactive skin"),
        ],
        table_source="Source: feature-to-benefit mapping practice",
        big_line1="Customers don't buy features — they buy what the feature lets them feel.",
        big_line2="Always translate the spec sheet into a benefit before it reaches the customer.",
        visual_kind="infographic",
        visual_template="sequence-pyramid-simple",
        visual_title="Keller's Customer-Based Brand Equity Pyramid",
        visual_items=[
            ("01", "Salience — Identity", "Is the brand noticed, and easily recalled, at all?"),
            ("02", "Performance & Imagery — Meaning", "What the product does, and the lifestyle it signals."),
            ("03", "Judgments & Feelings — Response", "The customer's rational verdict and emotional reaction."),
            ("04", "Resonance — Relationships", "Deep loyalty — the customer becomes an active advocate."),
        ],
        visual_source="Source: Keller, K.L. — Customer-Based Brand Equity (CBBE) Model, Strategic Brand Management",
        takeaways_title="Visual Identity System Components",
        takeaways_items=[
            ("Primary Elements", "The foundation visual components of the identity"),
            ("Logo", "The primary brand mark"),
            ("Colour Palette", "The brand's colour system"),
            ("Typography", "The font family selection"),
        ],
        takeaways_source="Source: visual identity system practice",
        case_example_company="Apple",
        case_example_headline="Hard Specs Sold as a Soft Feeling",
        case_example_insight="\"Designed by Apple in California\" turns a hard attribute (where "
             "it's engineered) into a soft one (craft, care, exclusivity) — the same discipline "
             "Nimbus needs to turn \"3 clinically-tested actives\" into \"your skin, genuinely cared for.\"",
        case_type="case_study",
        case_scenario=[
            "For the relaunch, the founder wants one page that finally settles what Nimbus stands for — "
            "because right now the brand isn't described the same way twice. Retail calls it \"affordable "
            "self-care.\" Marketing calls it \"clean beauty for real skin.\" Customer Service calls it \"the "
            "brand that actually replies.\"",
            "Your table must map Nimbus's hard attributes (the real product facts) and soft attributes (the "
            "feelings those facts create) into one brand concept the founder can approve — and that all "
            "three teams could say in their own words.",
        ],
        roles=[],
        discussion_prompts=[
            "What are three hard attributes (measurable facts) Nimbus can genuinely claim about its skincare "
            "range?",
            "What soft attribute — the feeling — does each hard attribute actually create, and is it the same "
            "feeling Retail, Marketing and Customer Service currently describe?",
            "Using Keller's Brand Equity Pyramid, which level is Nimbus weakest at right now: being noticed "
            "(Salience), understood (Performance/Imagery), felt (Judgments/Feelings), or trusted enough to be "
            "recommended (Resonance)?",
            "What single brand concept line could the founder approve that all three teams could restate "
            "consistently?",
        ],
        reflection_points=[
            "Was it harder for your table to agree on the hard attributes or the soft attributes — and why?",
            "Which pyramid level did your table disagree about the most?",
            "If a customer only ever experienced Nimbus through a five-minute Customer Service chat, which "
            "attribute would that conversation need to prove true?",
        ],
        debrief_check="Every group can show 3 hard + 3 soft attributes connected to one brand concept line, "
             "and can name the CBBE pyramid level the concept is designed to strengthen.",
        build="A brand attribute map (3 hard + 3 soft attributes) linked to one approved brand concept line",
        duration="30 minutes",
    ),
    dict(
        num=4,
        topic=1,
        title="Digital Reputation Audit Exercise",
        objective="Assess the organisation's reputation on social media and other platforms",
        t_statement="Assess organisation's reputation on social media and other platforms",
        what_is_kind="infographic",
        what_is_template="list-zigzag-up-simple",
        what_is_items=[
            ("search", "Brand Monitoring", "Tracks mentions across digital platforms"),
            ("heart", "Sentiment Analysis", "Reads the tone behind customer feedback"),
            ("people", "Multi-Platform", "Covers every social and review site"),
            ("chart", "Strategic Response", "Turns findings into an action plan"),
        ],
        what_is_source="Source: digital reputation monitoring practice",
        process_kind="infographic",
        process_template="sequence-roadmap-vertical-plain-text",
        process_title="Reputation Assessment Process Steps",
        process_items=[
            ("Conduct Audit", "Review the organisation's current digital presence."),
            ("Set Monitoring", "Implement tracking systems across the chosen platforms."),
            ("Analyse Sentiment", "Evaluate the tone of customer feedback."),
        ],
        process_source="Source: reputation-assessment frameworks",
        compare_kind="infographic",
        compare_template="compare-binary-horizontal-underline-text-vs",
        compare_title="Reactive vs Proactive Reputation Monitoring",
        compare_lhead="Reactive",
        compare_rhead="Proactive",
        compare_items=[
            ("clock", "Damage Control", "Crisis-response focus, after the fact"),
            ("flag", "Post-Issue", "Action only once problems occur"),
            ("search", "Prevention Focus", "Early issue identification"),
            ("refresh", "Continuous Tracking", "Ongoing brand monitoring"),
        ],
        compare_left=[
            ("clock", "Damage Control", "Crisis-response focus, after the fact"),
            ("flag", "Post-Issue", "Action only once problems occur"),
            ("shield", "High Risk", "Damage is already visible"),
        ],
        compare_right=[
            ("search", "Prevention Focus", "Early issue identification"),
            ("refresh", "Continuous Tracking", "Ongoing brand monitoring"),
            ("check", "Risk Mitigation", "Caught before it spreads"),
        ],
        compare_source="Source: reputation-monitoring best practice",
        table_title="Reputation Audit at a Glance",
        table_rows=[
            ("Mention", "Any online reference to the brand", "A customer tagging the brand in a story"),
            ("Sentiment", "The emotional tone of a mention", "Positive, neutral or negative"),
            ("Share of Voice", "The brand's mentions vs competitors' combined", "20% of category conversation"),
            ("Response Time", "How fast the brand replies to feedback", "Under 4 hours for negative reviews"),
        ],
        table_source="Source: social listening & reputation-audit practice",
        big_line1="Reputation is measured in real time, whether you're watching or not.",
        big_line2="A monitoring gap is a blind spot competitors can exploit first.",
        visual_kind="donut",
        visual_title="Platform Distribution Statistics",
        visual_items=[("Google", 38), ("Instagram", 38), ("Other Platforms", 24)],
        visual_source="Source: illustrative distribution, digital reputation audits",
        takeaways_title="Key Assessment Takeaways",
        takeaways_items=[
            ("Platform Focus", "Prioritise the platforms customers actually use first"),
            ("Quarterly Reviews", "Run regular strategy-assessment cycles"),
            ("Three Perspectives", "Weigh employee, customer and leadership viewpoints"),
            ("Response Protocol", "Follow a strategic engagement framework"),
        ],
        takeaways_source="Source: reputation-assessment best practice",
        case_example_company="Airbnb",
        case_example_headline="Reviews Are the Reputation, Not Just a Reflection of It",
        case_example_insight="Airbnb's entire trust model runs on visible, unfiltered reviews — "
             "hosts who monitor and respond fast build measurably higher booking rates than hosts "
             "who only check in when something goes wrong.",
        case_type="case_study",
        case_scenario=[
            "Six months ago a competitor's viral campaign pulled attention away from Nimbus Wellness. Since "
            "then, engagement has fallen and reviews increasingly say the brand \"doesn't feel personal "
            "anymore.\"",
            "Before the founder finalises the relaunch brief, leadership wants a clear-eyed audit of where "
            "Nimbus's reputation actually stands today — not where the founder assumes it stands.",
        ],
        roles=[],
        discussion_prompts=[
            "Which three platforms will actually reveal how customers feel about Nimbus right now — and why "
            "those three?",
            "Looking at a sample of recent mentions and reviews, what recurring themes sit behind \"doesn't "
            "feel personal anymore\"?",
            "How would you categorise the balance of positive, neutral and negative sentiment — and does it "
            "match what the founder currently believes?",
            "What is the single highest-priority response action leadership should take before the relaunch "
            "brief is finalised?",
        ],
        reflection_points=[
            "Did the sentiment split match what you expected before you actually read the reviews?",
            "Which recurring theme was hardest to reduce to one line for a leadership summary?",
            "If \"doesn't feel personal anymore\" kept appearing after the relaunch too, what would that tell "
            "you about the relaunch plan itself?",
        ],
        debrief_check="Every group can show a platform-by-platform sentiment breakdown, three named "
             "recurring themes, and one response action per theme leadership could act on this week.",
        build="A reputation-assessment report (3 platforms) with sentiment breakdown and a response action per theme",
        duration="45 minutes",
    ),
]
