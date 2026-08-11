"""LU4 — Branding Effectiveness: in-class activities 13-17.

Each activity carries the underlying Knowledge/Ability (K/A) topic's theory
content — a "what is X?" concept slide, a process/model slide, a compare
slide, a supporting data visual, and (where set) a real-world "case_example_*"
callout — so the deck teaches the concept before the hands-on activity.
`what_is_kind` / `compare_kind` / `visual_kind` select which renderer
build_slides.py uses for those slots (see the dispatch tables
render_what_is/render_compare/render_visual there); omit any key to fall
back to the plain tile-grid / two-column / vertical-list default. Each kind
expects a specific data shape — see the matching helper's docstring in
build_slides.py (e.g. visual_kind="blueprint" needs visual_stage_labels +
visual_items shaped for service_blueprint(); visual_kind="tree" needs
visual_root + visual_items shaped for decision_tree()).

`service_blueprint`'s lane colour and `decision_tree`'s branch colour are
both passed straight through to python-pptx shape/line APIs by
render_visual() in build_slides.py — unlike compare_quadrants, there is no
COLOR_TAGS string-tag lookup for these two visual kinds. They need real
RGBColor objects, so this module defines its own colour constants below,
matching build_slides.py's PALETTE hex values exactly, and uses those
objects directly inside visual_items/visual_root tuples.

This is the final Learning Unit, and all five activities close out the same
continuous scenario used across the whole course — Nimbus Wellness Pte Ltd,
a Singapore boutique skincare & wellness brand now mid-way through its
5th-anniversary relaunch. LU1 mapped its stakeholders and brand concept, LU2
investigated its "doesn't feel personal anymore" perception gap, and LU3
planned the relaunch activation and PR budget. LU4 moves from measuring
where Nimbus's reputation stands post-relaunch, through what to do if the
campaign attracts negative coverage, to how the brand keeps improving after
— rehearsing exactly the ground the Day 2 Case Study Question 4 covers.

Every activity is a case study or role play (never a numbered step list):
`case_scenario` is the narrative, `roles` (role-play only) are the personas
to assign, `discussion_prompts` are open questions the group works through,
and `reflection_points` + `debrief_check` close the activity out."""

from pptx.dml.color import RGBColor

# Match build_slides.py's PALETTE hex values exactly — needed because
# service_blueprint()/decision_tree() take real RGBColor objects for lane/
# branch colour, with no string-tag lookup in render_visual()'s dispatch.
BLUE = RGBColor(0x1F, 0x6F, 0xEB)
TEAL = RGBColor(0x10, 0xB9, 0x81)
VIOLET = RGBColor(0x7C, 0x3A, 0xED)
AMBER = RGBColor(0xF5, 0x9E, 0x0B)

DOMAIN4 = [
    dict(
        num=13,
        topic=4,
        title="Platform Reputation Audit",
        objective="Identify measures or indicators of the organisation's reputation on different platforms",
        t_statement="Measures or indicators of organisation's reputation on different platforms",
        what_is_kind="infographic",
        what_is_template="list-grid-ribbon-card",
        what_is_items=[
            ("chat", "Social Media", "Followers, engagement and sentiment tracked live"),
            ("search", "Digital Metrics", "Website traffic, search rankings, brand mentions"),
            ("chart", "Business KPIs", "NPS, satisfaction and financial impact"),
            ("people", "Stakeholder Data", "Customer, employee and investor perceptions"),
        ],
        what_is_source="Source: Meltwater, 2024",
        process_kind="infographic",
        process_template="sequence-roadmap-vertical-simple",
        process_title="Reputation Monitoring Process",
        process_items=[
            ("Set Objectives", "Define clear measurement goals up front."),
            ("Monitor Sources", "Track multiple data channels, not just one."),
            ("Analyse Sentiment", "Measure the positive/negative tone of the feedback."),
            ("Track Engagement", "Monitor how the audience actually interacts."),
        ],
        process_source="Source: Digimind, 2024",
        compare_kind="infographic",
        compare_template="compare-binary-horizontal-underline-text-vs",
        compare_items=[
            ("Single Channel", "Limited platform coverage"),
            ("Reactive", "Response only after issues occur"),
            ("Multi-Platform", "Comprehensive cross-channel tracking"),
            ("Predictive", "Forecasts stakeholder behaviour patterns"),
        ],
        compare_title="Traditional vs Modern Reputation Monitoring",
        compare_lhead="Traditional",
        compare_rhead="Modern",
        compare_left=["Single Channel — limited platform coverage",
                       "Reactive — response only after issues occur",
                       "Basic Metrics — simple measurement tools"],
        compare_right=["Multi-Platform — comprehensive cross-channel tracking",
                        "Predictive — forecasts stakeholder behaviour patterns",
                        "AI Analytics — real-time sentiment analysis"],
        compare_source="Source: Caliber, 2026",
        table_title="Reputation Indicator Types",
        table_rows=[
            ("Leading Indicator", "Predicts a future reputation change", "Rising negative sentiment this week"),
            ("Lagging Indicator", "Confirms a change that already happened", "Last quarter's NPS score"),
            ("Qualitative Signal", "Descriptive, not numeric", "Comments describing \"poor service\""),
            ("Quantitative Signal", "Numeric and trackable", "A 12% drop in 5-star reviews"),
        ],
        table_source="Source: Meltwater, 2024",
        big_line1="If you only track lagging indicators, you'll always be reacting late.",
        big_line2="Leading indicators are what let a brand get ahead of a problem.",
        visual_kind="blueprint",
        visual_title="Where Nimbus's Reputation Is Actually Built",
        visual_stage_labels=["Discover", "Browse", "Purchase", "Post-Purchase"],
        visual_items=[
            ("Customer Actions", BLUE,
             ["Sees an ad or search result", "Reads reviews, compares options",
              "Buys online or in-store", "Posts a review or complaint"]),
            ("Frontstage", TEAL,
             ["Social post, search ranking", "Product page, shelf display",
              "Checkout, staff interaction", "Review reply, service chat"]),
            ("Backstage", VIOLET,
             ["Content team tracks mentions", "Merchandising tracks page analytics",
              "Fulfilment team processes order", "Support team logs sentiment"]),
            ("Support", AMBER,
             ["Monitoring tool flags mentions", "Analytics dashboard tracks traffic",
              "CRM records purchase history", "Alert tool flags negative posts"]),
        ],
        visual_source="Source: service-blueprint methodology (Shostack, 1984, adapted); Meltwater, 2024",
        takeaways_title="Key Reputation Success Factors",
        takeaways_items=[
            ("Trust Scores", "One number tracks sentiment over time"),
            ("Share of Voice", "How much of the conversation you own"),
            ("NPS Tracking", "Loyalty measured straight from customers"),
            ("Forecast & Review", "Use data to anticipate reputation risk"),
        ],
        takeaways_source="Source: NPS industry benchmarks, 2025 (illustrative); Reputation Forecast, 2024",
        case_example_company="Grab",
        case_example_headline="One Reputation, Measured Across a Dozen Touchpoints at Once",
        case_example_insight="Grab's reputation lives in app ratings, driver reviews, social media and news "
             "coverage simultaneously — a single bad headline can move all four at once, which is why a "
             "platform audit can't treat any one channel in isolation.",
        case_type="case_study",
        case_scenario=[
            "Three weeks after Nimbus Wellness's 5th-anniversary relaunch went live, the founder is "
            "celebrating a spike in impressions and website traffic. The Board isn't satisfied with raw "
            "numbers, though — it wants to know whether the relaunch actually repaired the \"doesn't feel "
            "personal anymore\" perception gap uncovered before the campaign, or just produced a short-term "
            "spike in attention.",
            "Marketing has a folder of screenshots — likes, shares, a handful of glowing reviews — but no "
            "one has compared this to what reputation looked like before the relaunch, or checked the "
            "platforms customers actually complain on, like Google reviews and the wellness retail chain's "
            "own app.",
            "Before Marketing reports back to the Board next week, your table must build the audit that "
            "separates real reputation movement from relaunch-week noise.",
        ],
        roles=[],
        discussion_prompts=[
            "Which 3 platforms will actually tell you whether Nimbus's reputation has shifted since the "
            "relaunch — not just which platforms have the most impressions?",
            "Which of your chosen metrics are leading indicators that warn of a problem early, and which are "
            "lagging indicators that only confirm what already happened?",
            "How would you separate a genuine sentiment shift on \"feels personal again\" from a short-term "
            "spike caused by relaunch hype alone?",
            "What would you tell the Board next week if the quantitative numbers looked good but the "
            "qualitative comments never mentioned feeling more \"personal\" at all?",
        ],
        reflection_points=[
            "Did your table lean too heavily on quantitative metrics before someone asked what the "
            "qualitative comments actually said?",
            "Which platform did you almost leave out of the audit — and why did it turn out to matter?",
            "If the relaunch metrics stay strong for one more month and then fade, what would that suggest "
            "about whether the reputation gap was really closed?",
        ],
        debrief_check="Every group can show a platform-by-platform audit naming at least one leading and one "
             "lagging indicator per platform, and can state in one sentence whether the evidence shows a "
             "genuine reputation shift or just a relaunch-week spike.",
        build="A platform-by-platform reputation audit (3+ platforms) with leading and lagging indicators "
              "tracked, and a leadership-ready read on whether the relaunch actually shifted reputation",
        duration="20 minutes",
    ),
    dict(
        num=14,
        topic=4,
        title="Brand Health Assessment",
        objective="Recognise the indicators of successful branding",
        t_statement="Indicators of successful branding",
        what_is_kind="infographic",
        what_is_template="list-column-vertical-icon-arrow",
        what_is_items=[
            ("search", "Brand Awareness", "Recognition and recall measured directly"),
            ("heart", "Customer Loyalty", "Retention and repeat-purchase rates tracked"),
            ("chart", "Financial Impact", "Revenue growth and market share"),
            ("shield", "Trust Metrics", "Consumer confidence and perception measured"),
        ],
        what_is_source="Source: Brand Health Tracking Best Practices, 2024",
        process_kind="infographic",
        process_template="sequence-roadmap-vertical-plain-text",
        process_title="Brand Measurement Framework",
        process_items=[
            ("Define Metrics", "Decide what you're going to track, and why."),
            ("Track Awareness", "Measure recognition and recall over time."),
            ("Measure Loyalty", "Track retention and repeat-purchase rates."),
            ("Assess Perception", "Check whether the brand is seen the way it intends."),
        ],
        process_source="Source: Brand Metrics Evaluation Strategy, 2024",
        compare_kind="infographic",
        compare_template="compare-binary-horizontal-badge-card-arrow",
        compare_items=[
            ("Surveys", "Customer feedback collection"),
            ("Focus Groups", "Qualitative brand perception"),
            ("Analytics", "Real-time performance tracking"),
            ("Social Media", "Engagement and sentiment monitoring"),
        ],
        compare_title="Traditional vs Digital Brand Measurement",
        compare_lhead="Traditional",
        compare_rhead="Digital",
        compare_left=["Surveys — customer feedback collection",
                       "Focus Groups — qualitative brand perception",
                       "Quarterly — periodic assessment cycles"],
        compare_right=["Analytics — real-time performance tracking",
                        "Social Media — engagement and sentiment monitoring",
                        "Continuous — always-on measurement"],
        compare_source="Source: How to Measure Branding Success, 2024",
        table_title="Brand Success Indicator Set",
        table_rows=[
            ("Awareness", "Do people recognise the brand", "Unprompted recall in a survey"),
            ("Consideration", "Would they consider buying it", "Appears on a shortlist of 3"),
            ("Preference", "Would they choose it over rivals", "Picked in a head-to-head test"),
            ("Advocacy", "Would they recommend it", "Refers a friend unprompted"),
        ],
        table_source="Source: Brand Health Tracking Best Practices, 2024",
        big_line1="Awareness gets you noticed. Advocacy gets you customers for free.",
        big_line2="Track the whole funnel, not just the top of it.",
        visual_kind="infographic",
        visual_template="list-grid-badge-card",
        visual_title="The Four Brand Health Pillars",
        visual_items=[
            ("search", "Awareness", "Do people recognise Nimbus unprompted, and recall it against name-brand "
                                "competitors?"),
            ("heart", "Loyalty", "Do existing customers keep coming back, and how many repeat-purchase within a "
                              "season?"),
            ("chart", "Financial Impact", "Is brand strength actually translating into revenue growth and share "
                                       "of category spend?"),
            ("shield", "Trust", "Do customers believe Nimbus's claims and feel confident recommending it to a "
                            "friend?"),
        ],
        visual_source="Source: Brand Health Tracking Best Practices, 2024; NPS industry benchmarks, 2025 "
                       "(illustrative)",
        takeaways_title="Brand Health Dimensions",
        takeaways_items=[
            ("Awareness", "Website traffic and social reach"),
            ("Loyalty", "NPS score and retention"),
            ("Performance", "Revenue growth and market share"),
            ("Continuous Monitoring", "Track all four pillars every month"),
        ],
        takeaways_source="Source: Brand Health Tracking, 2024",
        case_example_company="DBS Bank",
        case_example_headline="Brand Health Is a Tracked Metric, Not a One-Off Survey",
        case_example_insight="DBS's widely-reported \"World's Best Bank\" recognition wasn't a lucky survey "
             "result — it was built on years of measurable digital and customer-experience metrics tracked "
             "continuously, the same discipline Nimbus needs to prove ongoing brand health to its Board.",
        case_type="case_study",
        case_scenario=[
            "The Board's real question isn't \"did the relaunch get noticed\" — it's whether Nimbus's brand "
            "is genuinely healthier than it was six months ago. Marketing has awareness numbers on hand, but "
            "no one has looked at loyalty, financial impact or trust together.",
            "The founder is due to present a \"State of the Brand\" update to the Board in two weeks, right "
            "after the relaunch's first full sales cycle closes. She has asked your table for a one-page "
            "brand-health scorecard she can defend line by line.",
            "Customer Service has also noticed something odd: several long-time customers who complained the "
            "brand \"feels distant\" are now leaving five-star reviews again — but repeat-purchase data "
            "hasn't moved yet.",
        ],
        roles=[],
        discussion_prompts=[
            "Across Awareness, Loyalty, Financial Impact and Trust, which pillar is Nimbus strongest on right "
            "now, and which is weakest — and what evidence would prove it either way?",
            "The reviews have improved but repeat-purchase data hasn't moved — which pillar does that gap sit "
            "in, and what does it tell the founder about how long a real recovery actually takes?",
            "If you could only fund one more month of measurement in a single pillar, which would move the "
            "Board's confidence most, and why?",
            "What separates a brand-health indicator the Board should act on immediately from one that's "
            "just worth watching?",
        ],
        reflection_points=[
            "Which pillar did your table find hardest to find real evidence for — awareness, loyalty, "
            "financial impact or trust?",
            "Did the group's instinct about Nimbus's strongest pillar match what the evidence actually "
            "showed?",
            "If financial impact keeps lagging the other three pillars for another quarter, is that a "
            "marketing problem or an operations problem?",
        ],
        debrief_check="Every group can show a one-page scorecard rating Nimbus on all four pillars with "
             "named evidence for each rating, plus one improvement action for the weakest pillar.",
        build="A brand-health scorecard across all four pillars (Awareness, Loyalty, Financial Impact, "
              "Trust) with evidence and one improvement action for the weakest pillar",
        duration="25 minutes",
    ),
    dict(
        num=15,
        topic=4,
        title="PR Crisis Response Plan",
        objective="Apply public-relations tactics",
        t_statement="Public relations tactics",
        what_is_kind="infographic",
        what_is_template="list-zigzag-up-simple",
        what_is_items=[
            ("chat", "Media Relations", "Build journalist partnerships for visibility"),
            ("people", "Community Outreach", "Engage local audiences and stakeholders"),
            ("shield", "Crisis Management", "Protect reputation during a challenge"),
            ("refresh", "Digital Engagement", "Social media and online interactions"),
        ],
        what_is_source="Source: PR Strategy Essentials, 2024",
        process_kind="infographic",
        process_template="sequence-roadmap-vertical-simple",
        process_title="PR Implementation Process",
        process_items=[
            ("Target Audience", "Identify the stakeholder groups affected."),
            ("Core Messaging", "Develop one consistent line of communication."),
            ("Media Relationships", "Build the journalist connections you'll need."),
            ("Campaign Execution", "Deploy the tactical activities on schedule."),
        ],
        process_source="Source: PR Strategy Guide, 2024",
        compare_kind="arrows",
        compare_title="Reactive vs Proactive Crisis Response",
        compare_lhead="Reactive — Defensive & Silent",
        compare_rhead="Proactive — Fast & Transparent",
        compare_left=[
            ("clock", "Wait for Full Certainty", "Cracker Barrel's 2025 rebrand backlash festered for a week "
                                              "before the company reversed course — and revenue still fell "
                                              "roughly 6% that quarter, even after the reversal."),
            ("shield", "Deny or Minimise", "Downplaying a complaint thread as \"a few unhappy customers\" reads as "
                                      "dismissive once hundreds of people are sharing their own photos."),
            ("flag", "Let Silence Fill the Vacuum", "An information vacuum left by delay gets filled by critics, "
                                                  "not facts — the story gets written without you in it."),
        ],
        compare_right=[
            ("chat", "Confirm and Communicate Fast", "McDonald's 2024 E. coli response traced the supply-chain "
                                                    "source quickly and shared an improvement plan across "
                                                    "multiple platforms before the story could spiral."),
            ("refresh", "Give Frequent, Plain-Language Updates", "Slack's 2025 outage updates used a public status "
                                                            "page with timestamped, plain-language updates — "
                                                            "transparency about the technical problem built "
                                                            "trust instead of breaking it."),
            ("check", "Publish the Full Explanation After", "Slack followed each outage with a full post-incident "
                                                          "explanation — closing the loop shows the company "
                                                          "learned, not just reacted."),
        ],
        compare_source="Source: PR crisis-management case examples, 2024-2025 (McDonald's, Slack, Cracker "
                        "Barrel)",
        table_title="PR Tactic Toolkit",
        table_rows=[
            ("Press Release", "A formal written announcement", "Product-launch announcement"),
            ("Media Pitch", "A tailored story angle sent to one journalist", "An exclusive interview offer"),
            ("Media Event", "An in-person or virtual press gathering", "A product-launch press conference"),
            ("Community Programme", "Ongoing local or niche engagement", "Sponsoring a local event series"),
        ],
        table_source="Source: PR Strategy Essentials, 2024",
        big_line1="If you don't fill the vacuum with facts, someone else will.",
        big_line2="Speed and transparency are what separate a story that fades from one that snowballs.",
        visual_kind="tree",
        visual_title="The Nimbus Crisis Response Fork",
        visual_root="A defective-product video is going viral the night before Nimbus's biggest interview — "
                     "what happens tonight?",
        visual_items=[
            ("Stay Silent", "Silence Fills the Vacuum",
             "Critics and the journalist write the story for Nimbus — \"knew and hid it\" becomes the "
             "headline.", AMBER),
            ("Respond Fast", "Trust Preserved",
             "Confirm what's known, commit to a fix, and give an honest on-record line before tomorrow's "
             "interview.", TEAL),
            ("Escalate Fully", "Crisis Protocol Activated",
             "For a widespread defect: recall affected units, activate the crisis team, notify every "
             "platform at once.", VIOLET),
        ],
        visual_source="Source: crisis-communication decision frameworks; PR Strategy Essentials, 2024",
        takeaways_title="The Seven PR Categories (Key Four)",
        takeaways_items=[
            ("External Relations", "All public-facing communications overall"),
            ("Media Relations", "Journalist partnerships and pitching"),
            ("Community Relations", "Local stakeholder engagement"),
            ("Customer Relations", "Direct client and customer communication"),
        ],
        takeaways_source="Source: PR Strategy Essentials, 2024",
        case_example_company="Johnson & Johnson",
        case_example_headline="The Textbook Case: Fast, Transparent, Costly — and Trust-Preserving",
        case_example_insight="When cyanide-laced Tylenol capsules killed seven people in 1982, Johnson & "
             "Johnson pulled every bottle from shelves nationwide within days and introduced the tamper-proof "
             "packaging the whole industry later adopted — still taught today as the standard for fast, "
             "transparent crisis response.",
        case_type="role_play",
        case_scenario=[
            "It's 9pm, the night before the founder's biggest relaunch media interview yet. A customer posts "
            "a video of her new Nimbus jar — from the new sustainable packaging line launched with the "
            "anniversary campaign — cracked and leaking product, captioned \"the 'eco-friendly' packaging "
            "Nimbus is so proud of.\" Within two hours it has hundreds of shares and a wave of other "
            "customers replying with their own photos.",
            "Operations thinks it may be a single bad batch from the new packaging supplier, but can't "
            "confirm numbers until morning. The journalist doing tomorrow's interview has already seen the "
            "thread and has emailed asking whether Nimbus knew about a defect before launch.",
            "The founder wants to say nothing until Operations has the full facts — but the thread is "
            "growing every hour, and tomorrow's interview is unavoidable. Your group must decide what Nimbus "
            "does tonight, and what the spokesperson says tomorrow morning.",
        ],
        roles=[
            ("Spokesperson", "Represent Nimbus publicly without over-promising",
             "Must decide what Nimbus can credibly say before every fact is confirmed, and how much to "
             "reveal in tomorrow's interview."),
            ("Journalist", "Get a real, on-record answer for tomorrow's story",
             "Already has screenshots of the complaint thread and will ask directly whether Nimbus knew "
             "about the packaging issue before the relaunch."),
            ("Crisis-Response Lead", "Coordinate the facts and the fix before Nimbus says anything publicly",
             "Is still confirming with Operations exactly how many units are affected, and whether it's a "
             "supplier fault or a Nimbus quality-control miss."),
        ],
        discussion_prompts=[
            "Is staying silent until Operations confirms every fact actually the safer choice tonight, or "
            "does it leave a vacuum the thread will fill for Nimbus?",
            "What can the Spokesperson honestly commit to in tomorrow's interview before the root cause is "
            "even confirmed?",
            "How should the Crisis-Response Lead's internal fact-finding and the Spokesperson's public "
            "statement stay in sync without one getting ahead of the other?",
            "What would Nimbus need to say and do in the first 24 hours to be judged as fast and transparent "
            "rather than defensive?",
        ],
        reflection_points=[
            "Did your Spokesperson end up promising more, or less, than Nimbus could actually deliver by "
            "morning?",
            "Where did the Journalist's questions expose a gap between what the Crisis-Response Lead knew "
            "and what the Spokesperson said?",
            "Looking at the Cracker Barrel and McDonald's examples, which pattern did your group's response "
            "end up closer to — and was that a deliberate choice?",
        ],
        debrief_check="Every group can perform or narrate a same-night response that names what Nimbus "
             "confirms publicly within hours, what it says in tomorrow's interview, and a follow-up "
             "commitment — and can point to which real-world example (fast/transparent vs delayed/silent) "
             "their plan resembles.",
        build="A same-night crisis-response script (public statement + next-day interview line) rehearsed "
              "through the three roles, benchmarked against a real 2024-2025 crisis example",
        duration="25 minutes",
    ),
    dict(
        num=16,
        topic=4,
        title="KPI Dashboard Design",
        objective="Monitor the success of the brand against Key Performance Indicators (KPI)",
        t_statement="Monitor the success of the brand against Key Performance Indicators (KPI)",
        what_is_kind="infographic",
        what_is_template="list-zigzag-up-simple",
        what_is_items=[
            ("target", "SMART KPIs", "Specific, measurable, attainable, realistic, time-bound"),
            ("search", "Data Collection", "Analytics tools and brand guidelines"),
            ("chart", "Performance Analysis", "Interpret trends and what's changing"),
            ("refresh", "Strategic Optimisation", "Insights drive real brand improvements"),
        ],
        what_is_source="Source: Frontify, 2024",
        process_kind="infographic",
        process_template="sequence-roadmap-vertical-plain-text",
        process_title="KPI Monitoring Process",
        process_items=[
            ("Collect Data", "Gather the analytics and brand guidelines."),
            ("Interpret", "Analyse the trends and what's changing."),
            ("Optimise", "Apply the insights to real improvements."),
            ("Repeat Monthly", "Keep the cycle continuous, not a one-off review."),
        ],
        process_source="Source: Frontify, 2024",
        compare_kind="infographic",
        compare_template="compare-binary-horizontal-simple-fold",
        compare_items=[
            ("Team Adoption", "Brand-guideline compliance"),
            ("Consistency", "Cross-channel brand alignment"),
            ("Market Perception", "Customer brand sentiment"),
            ("Competitive Position", "Market-share comparison"),
        ],
        compare_title="Brand KPI Categories — Internal vs External Focus",
        compare_lhead="Internal Focus",
        compare_rhead="External Focus",
        compare_left=["Team Adoption — brand-guideline compliance",
                       "Consistency — cross-channel brand alignment",
                       "Engagement — internal brand activation"],
        compare_right=["Market Perception — customer brand sentiment",
                        "Competitive Position — market-share comparison",
                        "Awareness — brand recognition metrics"],
        compare_source="Source: Frontify, 2024",
        table_title="SMART KPI Worksheet",
        table_rows=[
            ("Specific", "Exactly what is being measured", "Instagram engagement rate among the 25-34 core "
                                                             "segment"),
            ("Measurable", "How it's quantified", "% of followers who engage per post, from platform "
                                                   "analytics"),
            ("Attainable", "A realistic target given current resources", "+2% over the current baseline, "
                                                                          "not a 10x jump"),
            ("Realistic", "Tied to something the brand can actually influence", "Engagement rate, not a "
                                                                                 "competitor's market share"),
            ("Time-bound", "The review deadline", "Reviewed monthly at the Board update"),
        ],
        table_source="Source: Frontify, 2024",
        big_line1="A KPI without a deadline is just an opinion with a number attached.",
        big_line2="SMART turns a vague goal into something the team can actually be held to.",
        visual_kind="hex",
        visual_title="The SMART KPI Model",
        visual_items=[
            ("S", "Specific", "Name exactly what's being measured — not \"brand awareness\" in general, but "
                               "unprompted recall among Nimbus's core segment."),
            ("M", "Measurable", "State how it's quantified — percentage, score or count — and where the "
                                 "number comes from."),
            ("A", "Attainable", "Set a target Nimbus can realistically move given its size and budget, not "
                                 "an aspirational guess."),
            ("R", "Realistic", "Tie the KPI to something the brand can actually influence, not a market "
                                "force outside its control."),
            ("T", "Time-bound", "Give the KPI a review deadline — monthly, quarterly — so it forces a real "
                                 "decision, not a standing report."),
        ],
        visual_source="Source: SMART goal-setting framework (Doran, 1981, adapted); Frontify, 2024",
        takeaways_title="KPI Monitoring Key Takeaways",
        takeaways_items=[
            ("Balanced Mix", "Track internal and external metrics together"),
            ("Monthly Tracking", "Review monthly, not whenever convenient"),
            ("Strategic Alignment", "Every KPI should tie to a real objective"),
            ("Continuous Cycle", "Collect, interpret, optimise, repeat"),
        ],
        takeaways_source="Source: Multiple sources, 2024-2026",
        case_example_company="Google",
        case_example_headline="A Culture Built Around Measurable Goals",
        case_example_insight="Google's well-known OKR (Objectives and Key Results) practice ties every "
             "team's work to a small set of measurable, time-bound goals reviewed on a regular cycle — the "
             "same discipline behind a SMART KPI framework.",
        case_type="case_study",
        case_scenario=[
            "The Board's ask is specific: it wants a KPI framework it can check every month after the "
            "relaunch, not a one-off report from Marketing whenever someone remembers to send it. The "
            "founder, who is not a numbers person, has asked for something she can read in five minutes and "
            "still trust.",
            "Right now every department tracks something different — Marketing watches follower counts, "
            "Retail watches footfall, Customer Service watches response times — and none of it is compared "
            "against a target or a deadline. Last month someone reported \"engagement is up\" without saying "
            "up from what, or by when it should keep rising.",
            "Your table's job is to turn this scattered activity into a small set of SMART KPIs the Board "
            "can actually govern the relaunch by.",
        ],
        roles=[],
        discussion_prompts=[
            "Which 3 internal and 3 external KPIs would actually tell the Board whether the relaunch is "
            "working — not just which numbers are easiest for each department to pull?",
            "Take one of your KPIs through the full SMART test — where does it break down first, and how do "
            "you fix that?",
            "Who owns each KPI, and what happens if the number misses target two months in a row?",
            "If the Board can only look at one dashboard slide, what's the smallest set of numbers that "
            "still tells the whole story?",
        ],
        reflection_points=[
            "Which of your KPIs was hardest to make genuinely Measurable rather than just a description of "
            "activity?",
            "Did your table set a target that was Attainable, or did ambition win out over realism?",
            "If one KPI is red for two straight months, does your framework actually say what happens next "
            "— or does it stop at reporting the number?",
        ],
        debrief_check="Every group can show 3 internal + 3 external KPIs, each SMART-tested with a named "
             "owner, target, data source and review deadline, and can explain what action a missed target "
             "would trigger.",
        build="A SMART KPI framework (3 internal + 3 external KPIs) with an owner, target, data source and "
              "review deadline for each",
        duration="20 minutes",
    ),
    dict(
        num=17,
        topic=4,
        title="PR Campaign Audit Exercise",
        objective="Provide suggestions to improve public-relations campaign effectiveness",
        t_statement="Provide suggestions to improve public relations campaign effectiveness",
        what_is_kind="infographic",
        what_is_template="list-sector-plain-text",
        what_is_items=[
            ("search", "Performance Gaps", "Find weaknesses through data analysis"),
            ("target", "Strategic Planning", "Set measurable objectives and tactics"),
            ("chat", "Media Relations", "Build strong journalist partnerships"),
            ("star", "Content Quality", "Create compelling, research-backed stories"),
        ],
        what_is_source="Source: AMEC Integrated Evaluation Framework; Barcelona Principles 4.0 (2025)",
        process_kind="infographic",
        process_template="sequence-snake-steps-compact-card",
        process_title="Campaign Optimisation Process",
        process_items=[
            ("Set Goals", "Define clear, measurable objectives."),
            ("Define Audience", "Target specific stakeholder segments."),
            ("Create Content", "Develop compelling, research-backed stories."),
        ],
        process_source="Source: PR Strategy Essentials, 2024",
        compare_kind="infographic",
        compare_template="compare-binary-horizontal-underline-text-vs",
        compare_items=[
            ("Reach", "Total audience exposure"),
            ("Impressions", "Content visibility metrics"),
            ("Business Impact", "Revenue and growth correlation"),
            ("Behaviour Change", "Audience action and engagement"),
        ],
        compare_title="Output Metrics vs Outcome Metrics",
        compare_lhead="Output Metrics",
        compare_rhead="Outcome Metrics",
        compare_left=["Reach — total audience exposure",
                       "Impressions — content visibility metrics",
                       "Volume — quantity of coverage"],
        compare_right=["Business Impact — revenue and growth correlation",
                        "Behaviour Change — audience action and engagement",
                        "Quality Metrics — message penetration and sentiment"],
        compare_source="Source: AMEC Integrated Evaluation Framework; Barcelona Principles 4.0 (2025)",
        table_title="AMEC Framework at a Glance",
        table_rows=[
            ("Inputs", "What went into the campaign", "Budget, planning, content produced"),
            ("Outputs", "What was distributed", "Number of press releases sent"),
            ("Outtakes", "What the audience took away", "Message recall, sentiment shift"),
            ("Outcomes", "The business impact", "Sales lift, share-price movement"),
        ],
        table_source="Source: AMEC Integrated Evaluation Framework; Barcelona Principles 4.0 (2025)",
        big_line1="Impressions are not impact.",
        big_line2="The AMEC framework forces the question every campaign should answer: so what?",
        visual_kind="loop",
        visual_title="The AMEC Evaluation Loop",
        visual_items=[
            ("Objectives", "Set what the campaign is meant to change, not just what it will publish."),
            ("Inputs", "Budget, planning and content committed before anything goes live."),
            ("Outputs", "What was actually distributed — releases, posts, pitches sent."),
            ("Outcomes", "What the audience did as a result — recall, sentiment shift, enquiries."),
            ("Impact", "The business result — sales lift, reputation recovery — that feeds the next round "
                        "of objectives."),
        ],
        visual_source="Source: AMEC Integrated Evaluation Framework; Barcelona Principles 4.0 (2025)",
        takeaways_title="Implementation Takeaways",
        takeaways_items=[
            ("Data Analytics", "Use metrics to guide the next decision"),
            ("AMEC Framework", "Apply an industry-standard measurement approach"),
            ("Media Quality", "Prioritise tier-one relationships over raw volume"),
            ("Regression Analysis", "Find the activity-outcome correlations that matter"),
        ],
        takeaways_source="Source: AMEC Integrated Evaluation Framework; Barcelona Principles 4.0 (2025)",
        case_example_company="Dove",
        case_example_headline="Two Decades of Tracked Impact, Not Just One Campaign",
        case_example_insight="Unilever's Dove \"Real Beauty\" campaign is one of the most measured PR "
             "campaigns in marketing history — tracked for over 20 years against brand-trust and sales "
             "metrics, the same Outcomes-to-Impact discipline an AMEC-style audit asks Nimbus to apply.",
        case_type="case_study",
        case_scenario=[
            "It's now two months after the 5th-anniversary relaunch. The Board has seen the KPI dashboard "
            "designed in the last activity, and the numbers are mixed: impressions are up sharply, but the "
            "\"doesn't feel personal anymore\" sentiment has only partly recovered, and one retail partner "
            "is still hesitant to expand shelf space.",
            "The founder wants one final audit before she reports to the Board — not a scorecard of what "
            "Nimbus did, but a verdict on whether the relaunch campaign actually worked, and three concrete "
            "recommendations for what happens next.",
            "This is the same audit the Board will expect Nimbus to repeat after every future campaign — so "
            "your table isn't just closing out the relaunch, it's building the habit the brand will run on "
            "going forward.",
        ],
        roles=[],
        discussion_prompts=[
            "Run the relaunch campaign through AMEC's Inputs → Outputs → Outcomes → Impact chain — at which "
            "stage does the evidence get weakest?",
            "Impressions are up but the \"feels personal\" sentiment has only partly recovered — is that an "
            "Outputs success but an Outcomes failure, or something else?",
            "What would you tell the founder is the single biggest gap between what Nimbus measured and "
            "what the Board actually needed to know?",
            "What three recommendations would you make for the next campaign, and which AMEC stage does "
            "each one fix?",
        ],
        reflection_points=[
            "Looking back across all five LU4 activities, which measurement habit would have caught today's "
            "gap earliest — the reputation audit, the brand-health scorecard, or the KPI dashboard?",
            "Did your table's recommendations fix the root cause, or just add another metric to track?",
            "If Nimbus only adopts one habit from this whole course to run every future campaign by, what "
            "should it be?",
        ],
        debrief_check="Every group can map the relaunch campaign to all four AMEC stages (Inputs, Outputs, "
             "Outcomes, Impact), name the weakest stage with evidence, and give three recommendations that "
             "each fix a different stage — not three versions of the same idea.",
        build="An AMEC-based campaign audit (Inputs/Outputs/Outcomes/Impact) with three stage-specific "
              "recommendations for the next campaign",
        duration="25 minutes",
    ),
]
