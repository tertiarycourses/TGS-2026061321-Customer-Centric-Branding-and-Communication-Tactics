"""LU3 — Branding in Marketing: in-class activities 9-12.

Each activity carries the underlying Knowledge/Ability (K/A) topic's theory
content — a "what is X?" concept slide, a process/model slide, a compare
slide and a supporting data visual — so the deck teaches the concept before
the hands-on activity. `compare_kind` / `visual_kind` select which renderer
build_slides.py uses for those two slots (see the dispatch tables there);
omit either key to fall back to the plain two-column / tile-grid default.

All four activities run on one continuous scenario — Nimbus Wellness Pte
Ltd, a Singapore boutique skincare & wellness brand three months from its
5th-anniversary relaunch — so the in-class work builds directly toward the
Day 2 Case Study assessment, which reuses this exact company. LU3 picks up
right after LU1's approved brand concept and reputation audit: the team now
has to lock brand guidelines, audit brand-vs-marketing consistency, plan the
relaunch activation, and allocate the PR budget — exactly what Case Study
Question 3 asks candidates to reproduce.

Every activity is a case study (never a numbered step list): `case_scenario`
is the narrative, `roles` (role-play only — empty here, LU3 is planning
work, not a live conversation) are the personas to assign, `discussion_
prompts` are open questions the group works through, and `reflection_
points` + `debrief_check` close the activity out."""

DOMAIN3 = [
    dict(
        num=9,
        topic=3,
        title="Brand Audit Workshop",
        objective="Explain the basics of branding",
        t_statement="Basics in branding",
        what_is_kind="infographic",
        what_is_template="list-sector-plain-text",
        what_is_items=[
            ("star", "Visual Identity", "Logo, colours and typography, defined once"),
            ("heart", "Brand Values", "The mission every decision should reflect"),
            ("chat", "Brand Voice", "One tone, consistently written"),
            ("shield", "Brand Guidelines", "The standard every team applies"),
        ],
        what_is_source="Source: brand guidelines / brand identity system practice",
        process_kind="infographic",
        process_template="sequence-snake-steps-underline-text",
        process_title="Brand Development Process",
        process_items=[
            ("Define Mission", "Establish the brand's purpose and core values."),
            ("Create Visual ID", "Design the logo and colour palette."),
            ("Develop Guidelines", "Document the standards and specifications."),
        ],
        process_source="Source: brand guidelines / brand identity system practice",
        compare_kind="infographic",
        compare_template="compare-binary-horizontal-badge-card-arrow",
        compare_title="Consistent vs Inconsistent Branding",
        compare_lhead="Consistent Brand",
        compare_rhead="Inconsistent Brand",
        compare_items=[
            ("Revenue Boost", "Measurably higher financial performance"),
            ("Recognition", "A single colour/voice system customers recall"),
            ("Lower Trust", "Reduced consumer confidence"),
            ("Weak Recognition", "Confused brand identity across teams"),
        ],
        compare_left=["Revenue Boost — measurably higher financial performance",
                       "Recognition — a single colour/voice system customers recall",
                       "Trust Building — stronger consumer confidence"],
        compare_right=["Lower Trust — reduced consumer confidence",
                        "Weak Recognition — confused brand identity across teams",
                        "Market Confusion — unclear value proposition"],
        compare_source="Source: brand guidelines / brand identity system practice",
        table_title="Brand Identity Building Blocks",
        table_rows=[
            ("Logo", "The visual mark", "A wordmark or symbol"),
            ("Colour Palette", "The consistent colour system", "A primary + 2 accent colours"),
            ("Typography", "The font system", "One display + one body font"),
            ("Brand Voice", "How the brand \"talks\"", "Friendly, expert, playful, etc."),
        ],
        table_source="Source: brand guidelines / brand identity system practice",
        big_line1="A brand isn't a logo — a logo is just the doorway.",
        big_line2="Everything behind that doorway has to feel consistent, or the logo is lying.",
        visual_kind="infographic",
        visual_template="list-grid-badge-card",
        visual_title="Brand Guidelines System",
        visual_items=[
            ("star", "Visual Identity", "The logo, colour palette and typography every touchpoint must use."),
            ("heart", "Brand Values", "The mission and principles the brand concept line is built on."),
            ("chat", "Brand Voice", "The tone — friendly, expert, warm — every team writes in."),
            ("shield", "Usage Guidelines", "Concrete do's and don'ts so the standard survives contact with real work."),
        ],
        visual_source="Source: brand guidelines / brand identity system practice",
        takeaways_title="Key Branding Takeaways",
        takeaways_items=[
            ("Consistency", "The same brand, at every touchpoint"),
            ("Authenticity", "Values the brand genuinely lives"),
            ("Recognition", "A memorable visual and verbal identity"),
            ("Trust Building", "A brand experience customers can rely on"),
        ],
        takeaways_source="Source: brand guidelines / brand identity system practice",
        case_example_company="IKEA",
        case_example_headline="One Guidelines System, 60+ Markets, Zero Guesswork",
        case_example_insight="IKEA's showroom logic, product naming and flat-pack "
             "identity read as unmistakably IKEA whether you're in Singapore or "
             "Stockholm — proof a written standard, not local instinct, is what keeps "
             "a brand recognisable at scale. It's exactly the gap Nimbus's differing "
             "Retail, Marketing and Customer Service descriptions expose today.",
        case_type="case_study",
        case_scenario=[
            "Nimbus Wellness now has an approved brand concept line from the LU1 attribute-mapping work — but "
            "the founder has noticed that the website, the in-store signage and the Instagram bio still each "
            "describe the brand slightly differently. Nothing has actually been written down as a standard.",
            "With the 5th-anniversary relaunch three months away, the founder wants one brand-guidelines "
            "document that Retail, Marketing and Customer Service can all point to — before a single relaunch "
            "asset (banner, caption, staff script) gets produced.",
            "Your table has been asked to draft that guidelines document from the brand concept line Nimbus "
            "already approved.",
        ],
        roles=[],
        discussion_prompts=[
            "Starting from Nimbus's approved brand concept line, what visual-identity specifications (logo "
            "usage, colour palette, typography) actually protect that concept?",
            "What brand values and mission statement belong in the guidelines so all three teams can restate "
            "them the same way?",
            "What does \"Nimbus's voice\" sound like in a customer email versus an Instagram caption — where "
            "should the tone flex, and where must it stay fixed?",
            "What is one concrete usage example (a do/don't pair) that would stop the inconsistency the "
            "founder has already noticed?",
        ],
        reflection_points=[
            "Which building block — visual identity, values, voice or usage rules — was hardest for your "
            "table to pin down in concrete terms?",
            "Did your voice guideline actually sound different from a generic \"friendly and professional\" "
            "brand, or could it apply to any wellness company?",
            "If a new hire in Customer Service only ever read your guidelines document, would they write in "
            "Nimbus's voice by the end of week one?",
        ],
        debrief_check="Every group can show a one-page brand-guidelines draft — visual identity spec, brand "
             "values, a voice description with an example, and at least one concrete usage do/don't — that "
             "Retail, Marketing and Customer Service could each apply without further clarification.",
        build="A brand-guidelines document — visual standards, voice guidelines and an implementation roadmap",
        duration="30 minutes",
    ),
    dict(
        num=10,
        topic=3,
        title="Brand-Marketing Audit Exercise",
        objective="Explain the role of branding in marketing",
        t_statement="Role of branding in marketing",
        what_is_kind="infographic",
        what_is_template="list-column-done-list",
        what_is_items=[
            ("star", "Brand Identity", "A unique, recognisable set of values"),
            ("shield", "Trust Building", "Confidence that compounds over time"),
            ("target", "Differentiation", "A clear stand-out from competitors"),
            ("heart", "Emotional Connection", "A relationship, not just a purchase"),
        ],
        what_is_source="Source: brand marketing practice synthesis",
        process_kind="infographic",
        process_template="sequence-roadmap-vertical-plain-text",
        process_title="Brand-Marketing Integration Process",
        process_items=[
            ("Define Identity", "Establish the brand's purpose and values."),
            ("Align Objectives", "Match brand goals with marketing objectives."),
            ("Create Messaging", "Develop a consistent brand voice."),
            ("Go Multi-Channel", "Implement that voice across every touchpoint."),
        ],
        process_source="Source: brand marketing practice synthesis",
        compare_kind="infographic",
        compare_template="compare-binary-horizontal-simple-fold",
        compare_items=[
            ("Product Focus", "Sells features"),
            ("Short-term", "Campaign by campaign"),
            ("Identity Focus", "Sells what the brand stands for"),
            ("Long-term", "Builds equity over years"),
        ],
        compare_title="Traditional Marketing vs Brand Marketing",
        compare_lhead="Traditional Marketing",
        compare_rhead="Brand Marketing",
        compare_left=("T", "Traditional Marketing",
                       ["Product Focus — sells features",
                        "Short-term — campaign by campaign",
                        "Transactional — one purchase at a time"]),
        compare_right=("B", "Brand Marketing",
                        ["Identity Focus — sells what the brand stands for",
                         "Long-term — builds equity over years",
                         "Emotional — builds a relationship with the customer"]),
        compare_source="Source: brand marketing practice synthesis",
        table_title="Branding vs a Single Campaign",
        table_rows=[
            ("Campaign", "A time-boxed push with a specific goal", "A 4-week relaunch teaser push"),
            ("Brand", "The lasting identity behind every campaign", "What Nimbus stands for, always"),
            ("Short-term Win", "An immediate engagement lift", "A spike in likes during launch week"),
            ("Long-term Asset", "Equity that compounds over years", "Customers who choose Nimbus without comparing"),
        ],
        table_source="Source: brand marketing practice synthesis",
        big_line1="Campaigns get attention. Brands get loyalty.",
        big_line2="Every campaign should build the brand, not just borrow from it.",
        visual_kind="funnel",
        visual_title="From Transactional Funnel to Brand Loyalty",
        visual_items=[
            ("Awareness", "100%", "Notices the brand exists — a traditional-marketing win"),
            ("Consideration", "55%", "Weighs Nimbus against alternatives"),
            ("Preference", "28%", "Chooses Nimbus specifically, not just an option"),
            ("Loyalty", "12%", "Returns and advocates without comparing again"),
        ],
        visual_source="Source: illustrative narrowing, brand-marketing funnel synthesis",
        takeaways_title="Brand Equity Takeaways",
        takeaways_items=[
            ("Brand Equity", "The value a brand adds beyond the product"),
            ("Brand Awareness", "How well the brand is recognised and recalled"),
            ("Brand Loyalty", "Retention and advocacy, not one sale"),
            ("Measurable Impact", "Equity shows up in revenue and trust"),
        ],
        takeaways_source="Source: brand marketing practice synthesis",
        case_example_company="Disney",
        case_example_headline="One Theme-Park Trip, a Lifetime of Loyalty",
        case_example_insight="Disney never markets a single visit — every touchpoint "
             "is built to turn one trip into decades of return visits, merchandise "
             "and generational loyalty. It's the Brand Marketing column in action: "
             "identity and emotion compounding, not a transaction closed and forgotten.",
        case_type="case_study",
        case_scenario=[
            "The Marketing Lead has just shown your table Nimbus's most recent campaign: a two-week "
            "discount push on the best-selling serum, promoted purely on price. It performed well on sales, "
            "but the founder is uneasy — it never once mentioned the brand values from the LU1 attribute map, "
            "and a few loyal customers commented that it \"felt like any other skincare sale.\"",
            "Before the relaunch campaign is greenlit, leadership wants proof that Nimbus's marketing "
            "activity is actually building the brand, not just borrowing short-term attention from it. Your "
            "table has been asked to audit the discount campaign against Nimbus's approved brand identity.",
        ],
        roles=[],
        discussion_prompts=[
            "Which core identity elements from Nimbus's approved brand concept should this campaign have "
            "reflected — and which of them actually appeared in the discount push?",
            "Was the discount campaign's messaging aligned with the brand's identity, or did it lean on "
            "price alone the way a generic competitor would?",
            "Where exactly is the gap between what the campaign said and what the brand stands for — and how "
            "wide is it?",
            "What two or three concrete changes would make the next relaunch-adjacent campaign build brand "
            "equity instead of just moving stock?",
        ],
        reflection_points=[
            "Did your table's consistency score match what the loyal-customer comments already hinted at?",
            "Was the gap you found about the message itself, or about which channel carried it?",
            "If every future Nimbus campaign scored this low on brand alignment, what would that do to the "
            "5th-anniversary relaunch's credibility?",
        ],
        debrief_check="Every group can show a brand-audit report with a consistency assessment score for the "
             "discount campaign, the specific identity elements that were missing, and two or three concrete "
             "recommendations for better brand-marketing integration.",
        build="A brand-audit report with a consistency assessment and recommendations",
        duration="20 minutes",
    ),
    dict(
        num=11,
        topic=3,
        title="Brand Activation Planning Workshop",
        objective="Execute branding campaigns, events and activities to increase brand awareness",
        t_statement="Execute branding campaigns, events and activities to increase brand awareness",
        what_is_kind="infographic",
        what_is_template="list-zigzag-down-simple",
        what_is_items=[
            ("Campaign Planning", "A multi-channel strategy, built before launch"),
            ("Event Activation", "An experiential, interactive brand moment"),
            ("Channel Coordination", "One consistent message across platforms"),
            ("Performance Measurement", "Brand recall and recognition tracked"),
        ],
        what_is_source="Source: experiential-marketing / brand-activation practice, Singapore 2025",
        process_kind="infographic",
        process_template="sequence-roadmap-vertical-simple",
        process_title="Campaign Execution Process",
        process_items=[
            ("Define Audience", "Identify the target demographics precisely."),
            ("Core Message", "Develop the unique selling proposition."),
            ("Channel Selection", "Choose the optimal marketing platforms."),
            ("Visual Consistency", "Create unified brand assets across channels."),
        ],
        process_road_items=[
            ("search", "Define Audience", "Identify the target demographics precisely."),
            ("chat", "Core Message", "Develop the unique selling proposition."),
            ("target", "Channel Selection", "Choose the optimal marketing platforms."),
            ("star", "Visual Consistency", "Create unified brand assets across channels."),
        ],
        process_source="Source: experiential-marketing / brand-activation practice, Singapore 2025",
        compare_kind="infographic",
        compare_template="compare-binary-horizontal-simple-fold",
        compare_items=[
            ("flag", "Print & Press Ads", "One-way placements in newspapers and lifestyle magazines"),
            ("chat", "Radio Spots", "Audio commercial broadcasts with no direct interaction"),
            ("star", "Interactive Pop-Up", "A gamified, multi-sensory space customers step into and explore"),
            ("people", "Live Brand Event", "A hands-on activation built around the anniversary story"),
        ],
        compare_title="Traditional Campaign vs Experiential Activation",
        compare_lhead="Traditional",
        compare_rhead="Experiential",
        compare_left=[
            ("flag", "Print & Press Ads", "One-way placements in newspapers and lifestyle magazines"),
            ("chat", "Radio Spots", "Audio commercial broadcasts with no direct interaction"),
            ("chart", "Digital Banner Ads", "Passive display advertising customers scroll past"),
        ],
        compare_right=[
            ("star", "Interactive Pop-Up", "A gamified, multi-sensory space customers step into and explore"),
            ("people", "Live Brand Event", "A hands-on activation built around the anniversary story"),
            ("refresh", "UGC-Ready Moments", "Social-share-ready touchpoints designed for guests to post themselves"),
        ],
        compare_source="Source: experiential-marketing / brand-activation practice, Singapore 2025",
        table_title="Campaign Channel Toolkit",
        table_rows=[
            ("Owned Channel", "Platforms the brand controls", "Website, email list, app"),
            ("Earned Channel", "Coverage the brand doesn't pay for", "Press mentions, organic reviews"),
            ("Paid Channel", "Placements the brand pays for", "Social ads, sponsorships"),
            ("Experiential", "In-person or interactive activation", "A pop-up store, a live event"),
        ],
        table_source="Source: experiential-marketing / brand-activation practice, Singapore 2025",
        big_line1="Awareness built on one channel alone is awareness at risk.",
        big_line2="A campaign that only lives in one place dies the moment that channel changes.",
        visual_kind="kpi",
        visual_title="Relaunch Pop-Up — Illustrative Activation KPIs",
        visual_items=[
            ("+42%", "Pop-Up Foot Traffic", "vs an average retail week", "up"),
            ("1,850", "Social Mentions", "UGC-tagged posts, launch week", "up"),
            ("18%", "Sample-to-Purchase", "Conversion rate at the pop-up", "up"),
            ("31%", "Follow-Up Email Opens", "vs a 22% baseline average", "up"),
        ],
        visual_source="Source: illustrative values, brand-activation KPI benchmarks",
        takeaways_title="Key Campaign Success Factors",
        takeaways_items=[
            ("Message Alignment", "Speaks to values, not just demographics"),
            ("Visual Consistency", "One identity across every channel"),
            ("Interactive Experiences", "Something memorable the audience does"),
            ("Measurement Framework", "Track recall and recognition, not just reach"),
        ],
        takeaways_source="Source: experiential-marketing / brand-activation practice, Singapore 2025",
        case_example_company="Starbucks",
        case_example_headline="A Seasonal Cup Turns One Visit Into a Shareable Moment",
        case_example_insight="Starbucks's seasonal pop-up drinks and store experiences "
             "aren't really about the product — they're multi-sensory moments customers "
             "queue for, photograph and post themselves. It's the same experiential "
             "principle behind Nimbus's relaunch pop-up: give people something to walk "
             "into, not just an ad to scroll past.",
        case_type="case_study",
        case_scenario=[
            "The brand guidelines are drafted and the consistency gaps are named. Now the founder needs an "
            "actual activation plan for the 5th-anniversary relaunch — the campaign that has to win back "
            "the customers who say Nimbus \"doesn't feel personal anymore\" while reaching new customers who "
            "are comparing Nimbus to the competitor whose viral campaign started this six months ago.",
            "The founder has one non-negotiable: the relaunch needs at least one experiential element, not "
            "just another round of social ads — something people can walk into, touch or take part in, and "
            "want to share themselves.",
            "Your table's job is to design the channel mix, the core message and that one experiential "
            "element, all traceable back to the brand concept and voice Nimbus has already approved.",
        ],
        roles=[],
        discussion_prompts=[
            "What is the one core message the relaunch campaign should carry everywhere — and how does it "
            "answer the \"doesn't feel personal anymore\" perception gap directly?",
            "Which 3-4 channels (owned, earned, paid) should carry that message, and what does each channel "
            "need to do differently to stay true to Nimbus's brand voice?",
            "What is your one experiential element, and what makes it relevant, emotionally engaging and "
            "genuinely shareable rather than just an expensive photo backdrop?",
            "How will you know the activation actually built brand recall, not just short-term foot traffic "
            "or impressions?",
        ],
        reflection_points=[
            "Did your experiential idea start from the brand story, or did the brand story get bolted on "
            "afterward to justify an idea your table already liked?",
            "Which channel in your mix was hardest to keep consistent with Nimbus's brand voice, and why?",
            "If the experiential element only reached 200 people in person, what would have to be true about "
            "the rest of your channel mix for the relaunch to still feel successful?",
        ],
        debrief_check="Every group can show a campaign plan naming 3-4 channels, one core message traceable "
             "to the brand concept, one experiential element with a clear rationale, and a brand-recall "
             "metric for measuring success — not just a reach or attendance number.",
        build="A campaign-strategy document with timeline, budget allocation and success metrics",
        duration="30 minutes",
    ),
    dict(
        num=12,
        topic=3,
        title="PR Campaign Budget Planning",
        objective="Execute public-relations campaigns in alignment to brand positioning strategies, "
                   "operational plans and budget",
        t_statement="Execute public relations campaigns in alignment to brand positioning strategies, "
                    "operational plans and budget",
        what_is_kind="infographic",
        what_is_template="list-grid-candy-card-lite",
        what_is_items=[
            ("target", "Brand Positioning", "The foundation every PR message builds on"),
            ("gear", "Operational Plans", "A structured plan for campaign delivery"),
            ("chart", "Budget Management", "Resource allocation and cost control"),
            ("check", "Strategic Alignment", "Everything traces back to one strategy"),
        ],
        what_is_source="Source: PESO Model (Paid, Earned, Shared, Owned), Gini Dietrich / Spin Sucks",
        process_kind="infographic",
        process_template="sequence-roadmap-vertical-plain-text",
        process_title="PR Campaign Planning Process",
        process_items=[
            ("Define Positioning", "Establish the unique brand identity behind the campaign."),
            ("Set Objectives", "Write clear, measurable campaign goals."),
            ("Identify Audiences", "Define each target group precisely."),
            ("Craft Messages", "Tailor the content to each audience."),
        ],
        process_source="Source: PESO Model (Paid, Earned, Shared, Owned), Gini Dietrich / Spin Sucks",
        compare_kind="infographic",
        compare_template="compare-binary-horizontal-underline-text-vs",
        compare_items=[
            ("Brand Fit First", "Every dollar traces back to the approved brand concept"),
            ("Owned as Base", "The channels Nimbus controls carry the core story at near-zero cost"),
            ("Paid to Fill Gaps", "Boosted reach only where owned and earned fall short"),
            ("Reserve for Response", "Budget held back for the CS perception gap resurfacing"),
        ],
        compare_title="Budget Allocation Logic — Anchor vs Adjust",
        compare_lhead="Anchor on Positioning",
        compare_rhead="Adjust for the Moment",
        compare_left=["Brand Fit First — every dollar traces back to the approved brand concept",
                       "Owned as Base — the channels Nimbus controls carry the core story at near-zero cost",
                       "Earned as Credibility — press and reviews lend outside validation paid media can't buy"],
        compare_right=["Paid to Fill Gaps — boosted reach only where owned and earned fall short",
                        "Reserve for Response — budget held back for the CS perception gap resurfacing",
                        "Review Mid-Campaign — reallocate if one channel is clearly outperforming the rest"],
        compare_source="Source: PESO Model (Paid, Earned, Shared, Owned), Gini Dietrich / Spin Sucks",
        table_title="PR Budget Allocation Model",
        table_rows=[
            ("Earned Media", "Coverage secured through relationships, unpaid", "A feature article from a pitched story"),
            ("Owned Media", "Content published on brand-controlled channels", "A company blog post"),
            ("Paid Media", "Sponsored placements and promotion", "A boosted social post"),
            ("Reserve Fund", "Budget held back for crisis response", "5-10% held for unplanned needs"),
        ],
        table_source="Source: PESO Model (Paid, Earned, Shared, Owned), Gini Dietrich / Spin Sucks",
        big_line1="A PR budget with no reserve is a plan with no plan B.",
        big_line2="Hold something back — the crisis you don't budget for is the one that costs the most.",
        visual_kind="hex",
        visual_title="The PESO Budget Model",
        visual_items=[
            ("1", "Paid", "Sponsored placements and promotion — reach money can buy directly."),
            ("2", "Earned", "Press coverage and reviews secured through relationships, unpaid."),
            ("3", "Shared", "Social conversation and community amplification around the brand."),
            ("4", "Owned", "Content on channels the brand fully controls — website, email, app."),
        ],
        visual_source="Source: PESO Model (Paid, Earned, Shared, Owned), Gini Dietrich / Spin Sucks",
        takeaways_title="Core Content Framework",
        takeaways_items=[
            ("Brand Foundation", "The positioning everything else builds on"),
            ("Content Pillars", "Three to five themes PR content returns to"),
            ("Key Messages", "Audience-specific versions of one message"),
            ("Brand Voice", "One consistent tone, every release"),
        ],
        takeaways_source="Source: PESO Model (Paid, Earned, Shared, Owned), Gini Dietrich / Spin Sucks",
        case_example_company="Coca-Cola",
        case_example_headline="Decades of Brand Investment, Not a Single Big Campaign",
        case_example_insight="Coca-Cola's dominance isn't one PR win — it's disciplined "
             "investment across earned press, owned channels and paid placement, sustained "
             "for decades rather than spent in a single burst. The same discipline should "
             "shape Nimbus's PESO split: a durable allocation, not a one-off relaunch spend.",
        case_type="case_study",
        case_scenario=[
            "The CEO has approved a bounded PR budget for the 5th-anniversary relaunch — but not a blank "
            "cheque. Before a single dollar is spent, the CEO wants to see it allocated across earned, owned "
            "and paid channels in a way that visibly matches Nimbus's brand positioning, not just whichever "
            "channel the Marketing team finds easiest to book.",
            "The Board has already flagged a second concern for after the relaunch: they want ongoing proof "
            "the campaign improved Nimbus's reputation, not just its impression count — so today's budget "
            "plan needs KPIs the Board can actually hold the team to.",
            "Your table has been asked to build the PR budget proposal the CEO will sign off on.",
        ],
        roles=[],
        discussion_prompts=[
            "Using the PESO model, how should the budget split across paid, earned, shared and owned "
            "channels given Nimbus's brand positioning and the perception gap it's trying to close?",
            "Which channel deserves the largest share of spend for this specific relaunch — and which would "
            "you deliberately underfund, and why?",
            "What percentage, if any, should be held back as a reserve fund, and what would trigger Nimbus "
            "to actually spend it?",
            "What KPIs would let the Board judge reputation improvement, not just reach or impressions?",
        ],
        reflection_points=[
            "Did your allocation favour the channel that's easiest to execute, or the one the brand "
            "positioning actually calls for?",
            "How did you decide the size of the reserve fund — was it a rule of thumb or tied to a specific "
            "risk Nimbus is facing?",
            "If the Board rejected your KPI list as \"just vanity metrics,\" what would you replace them "
            "with?",
        ],
        debrief_check="Every group can show a PR budget proposal with a percentage split across paid, "
             "earned, shared and owned channels, a stated reserve fund, and a KPI list the Board could use "
             "to judge reputation impact rather than reach alone.",
        build="A PR budget proposal with channel allocation and success metrics",
        duration="25 minutes",
    ),
]
