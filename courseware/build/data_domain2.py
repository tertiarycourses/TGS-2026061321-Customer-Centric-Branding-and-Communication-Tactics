"""LU2 — Customer Influence: in-class activities 5-8.

Each activity carries the underlying Knowledge/Ability (K/A) topic's theory
content — a "what is X?" concept slide, a process/model slide, a compare
slide and a supporting data visual — so the deck teaches the concept before
the hands-on activity. `compare_kind` / `visual_kind` select which renderer
build_slides.py uses for those two slots (see the dispatch tables there);
omit either key to fall back to the plain two-column / tile-grid default.

All four activities continue the one running scenario from LU1 — Nimbus
Wellness Pte Ltd, a Singapore boutique skincare & wellness brand three
months from its 5th-anniversary relaunch. LU1 ended with a digital
reputation audit that surfaced one recurring theme: customers say the
brand "doesn't feel personal anymore," while Marketing believes product
quality is unchanged — a possible perception gap. Activities 5-8 pick up
directly from that finding to investigate the gap, assess advocacy,
document campaign reception, and practise active listening on it — the
exact techniques Case Study Question 2 asks candidates to apply.

Every activity is a case study or role play (never a numbered step list):
`case_scenario` is the narrative, `roles` (role-play only) are the personas
to assign, `discussion_prompts` are open questions the group works through,
and `reflection_points` + `debrief_check` close the activity out."""

DOMAIN2 = [
    dict(
        num=5,
        topic=2,
        title="Brand Perception Audit",
        objective="Assess customer perceptions of the brand, products and services",
        t_statement="Perceptions of customers of the brand, products and services",
        what_is_kind="infographic",
        what_is_template="list-column-vertical-icon-arrow",
        what_is_items=[
            ("star", "Product View", "Customer verdict on product quality"),
            ("flag", "Brand Identity", "Customer grasp of core brand values"),
            ("chat", "Service Quality", "Perceived value of every interaction"),
            ("idea", "Perception Gap", "Gap between belief and reality"),
        ],
        what_is_source="Source: Qualtrics, 2024",
        process_kind="infographic",
        process_template="sequence-roadmap-vertical-plain-text",
        process_title="Perception Management Process",
        process_items=[
            ("Gather Feedback", "Collect systematic customer input, not just anecdotes."),
            ("Analyse Gaps", "Identify where perception differs from reality."),
            ("Align Values", "Match delivery to customer expectations."),
            ("Deliver Quality", "Make the brand experience consistent, every time."),
        ],
        process_source="Source: Brand enhancement strategies, 2024",
        compare_kind="infographic",
        compare_template="compare-binary-horizontal-badge-card-arrow",
        compare_title="Technical Quality vs Value Quality",
        compare_lhead="Technical Quality",
        compare_rhead="Value Quality",
        compare_items=[
            ("Specifications", "What the product objectively does"),
            ("Performance", "How reliably it does it"),
            ("Brand Image", "How the brand is perceived"),
            ("Perception", "The customer's subjective read"),
        ],
        compare_left=["Specifications — what the product objectively does",
                       "Performance — how reliably it does it",
                       "Reliability — consistency over time"],
        compare_right=["Brand Image — how the brand is perceived",
                        "Perception — the customer's subjective read",
                        "Experience — how it feels to interact with the brand"],
        compare_source="Source: brand perception-gap research, CX practice",
        table_title="Customer Perception Building Blocks",
        table_rows=[
            ("Expectation", "What the customer believes they'll get", "A brand that still feels personal, as it always has"),
            ("Experience", "What actually happens", "A faster but more generic-sounding reply from Customer Service"),
            ("Gap", "The distance between the two", "The service is correct, but the warmth is gone"),
            ("Perception", "The lasting belief that gap creates", "\"Nimbus doesn't feel personal anymore\""),
        ],
        table_source="Source: brand perception-gap research, CX practice",
        big_line1="A single broken promise can outweigh ten kept ones.",
        big_line2="Perception is built on the gap between expectation and experience — close it deliberately.",
        visual_kind="journey",
        visual_title="The Nimbus Perception Gap Journey",
        visual_items=[
            ("search", "Discovers Nimbus", "Sees the anniversary relaunch teaser", 4),
            ("chat", "Reads Reviews", "Spots \"doesn't feel personal\" comments", 3),
            ("clock", "Contacts Support", "Fast reply, but feels scripted", 2),
            ("star", "Makes a Purchase", "Product quality still meets expectations", 3),
            ("heart", "Post-Purchase Follow-Up", "A genuine, personal thank-you note", 4),
        ],
        visual_source="Source: illustrative distribution, Qualtrics & Zendesk 2024",
        takeaways_title="Key Perception Takeaways",
        takeaways_items=[
            ("Close the Gap", "Close the gap between belief and reality"),
            ("Measure Quality", "Track both technical and value quality"),
            ("Monitor Feedback", "Make feedback collection continuous, not one-off"),
            ("Build Loyalty", "Closing the gap earns long-term loyalty"),
        ],
        takeaways_source="Source: Customer perception best practices, 2024",
        case_example_company="Zappos",
        case_example_headline="Radical Customer Focus Closes the Perception Gap",
        case_example_insight="Zappos reps have no call-time targets and no scripts — one legendary "
             "call ran past ten hours because the goal was connection, not resolution. That is the "
             "instinct Nimbus's faster-but-generic chat macros are quietly losing: speed without "
             "warmth is still a gap.",
        case_type="case_study",
        case_scenario=[
            "The Activity 4 reputation audit surfaced one theme again and again: customers say Nimbus "
            "Wellness \"doesn't feel personal anymore.\" Marketing's official position is that nothing has "
            "changed — the formulas, ingredients and packaging are exactly what they were a year ago. If the "
            "product itself hasn't moved, something else has.",
            "A closer look at Customer Service's own numbers hints at where: average reply time has improved "
            "since two outlets added self-checkout kiosks and the contact-centre adopted faster chat macros. "
            "The technical quality — what the product does — looks unchanged on paper. But the value quality "
            "— how it feels to deal with Nimbus — may have quietly slipped underneath the metrics leadership "
            "actually tracks.",
            "Before the founder locks the relaunch brief, your table must compare what Marketing believes "
            "against what a sample of real customer feedback actually says, and turn the difference into a "
            "short, prioritised gap list leadership can act on this week.",
        ],
        roles=[],
        discussion_prompts=[
            "Looking at the Activity 4 findings alongside what Marketing believes internally, where exactly "
            "does customer perception diverge from the company's own view of itself?",
            "Is the drift really in Technical Quality (the product itself) or in Value Quality (the "
            "experience around it) — and what evidence from the audit supports that?",
            "What are the top 3 perception gaps your table would put in front of the founder, and which one "
            "is most urgent to close before the relaunch brief is finalised?",
            "For each gap, what would \"closed\" actually look like, and which team would need to own fixing "
            "it?",
        ],
        reflection_points=[
            "Did your table's top gap turn out to be about the product itself, or about how people are "
            "treated when they interact with the brand?",
            "Was there a gap the data supported that still felt uncomfortable to put in front of the "
            "founder — and why?",
            "If Marketing pushed back and insisted the product is the whole story, what evidence would you "
            "point to first?",
        ],
        debrief_check="Every group can show a gap-analysis table comparing Marketing's internal belief "
             "against real customer feedback, with the top 3 perception gaps ranked and one concrete action "
             "proposed for each.",
        build="A Nimbus perception-gap analysis comparing internal quality metrics with customer feedback, "
              "ranking the top 3 gaps with an action for each",
        duration="25 minutes",
    ),
    dict(
        num=6,
        topic=2,
        title="Brand Advocacy Assessment",
        objective="Recognise the importance of the customer in influencing brand reputation",
        t_statement="Importance of the customer in influencing the brand reputation",
        what_is_kind="infographic",
        what_is_template="list-grid-ribbon-card",
        what_is_items=[
            ("shield", "Trust Factor", "Personal recommendations drive purchase decisions"),
            ("lightning", "Viral Spread", "Positive experiences multiply through networks"),
            ("chat", "Digital Voice", "Online reviews equal family recommendations"),
            ("people", "Reputation Control", "Customers actively shape the brand image"),
        ],
        what_is_source="Source: WebFX, Digital Silk 2024",
        process_kind="infographic",
        process_template="sequence-snake-steps-compact-card",
        process_title="Customer Advocacy Process",
        process_items=[
            ("Experience", "The customer interacts with the brand."),
            ("Evaluate", "The customer forms an emotional connection — or doesn't."),
            ("Share", "The customer tells others about the experience."),
        ],
        process_source="Source: Nestify Marketing Insights, 2024",
        compare_kind="infographic",
        compare_template="compare-binary-horizontal-simple-fold",
        compare_title="Positive vs Negative Word-of-Mouth Impact",
        compare_lhead="Positive Experience",
        compare_rhead="Negative Experience",
        compare_items=[
            ("Recommendation", "36% recommend within two weeks"),
            ("Emotional Bond", "3x more word-of-mouth generated"),
            ("Share Bad", "45% share negative experiences"),
            ("Brand Avoidance", "26% completely avoid the brand"),
        ],
        compare_left=["Recommendation — 36% recommend within two weeks",
                       "Emotional Bond — 3x more word-of-mouth generated",
                       "Trust Building — builds lasting brand loyalty"],
        compare_right=["Share Bad — 45% share negative experiences",
                        "Brand Avoidance — 26% completely avoid the brand",
                        "Reputation Damage — long-term perception harm"],
        compare_source="Source: Trustmary, WiserReview 2024",
        table_title="Word-of-Mouth Mechanics",
        table_rows=[
            ("Trigger", "The moment a customer decides to talk", "A Customer Service rep who genuinely remembered their order"),
            ("Channel", "Where they share it", "The loyal-customer community Facebook group"),
            ("Amplification", "How far it travels from there", "A friend's friend sees the post and asks where to buy"),
            ("Outcome", "The net effect on the brand", "New leads for the relaunch, or a louder version of \"not personal anymore\""),
        ],
        table_source="Source: WebFX, Digital Silk 2024",
        big_line1="Every customer is a broadcaster now.",
        big_line2="Design experiences worth repeating, because they will be repeated.",
        visual_kind="infographic",
        visual_template="sequence-circular-simple",
        visual_title="The Advocacy Loop",
        visual_items=[
            ("Experience", "A genuine, well-handled touchpoint with Nimbus — in store, online or on a call."),
            ("Satisfaction", "The customer's private verdict on that touchpoint, good or bad."),
            ("Word-of-Mouth", "A satisfied customer voluntarily tells others — a post, a tag, a conversation."),
            ("New-Customer Discovery", "A prospect meets Nimbus through that story, restarting the loop."),
        ],
        visual_source="Source: customer advocacy loop, adapted from WebFX / Digital Silk 2024",
        takeaways_title="Key Advocacy Takeaways",
        takeaways_items=[
            ("Trust Priority", "Personal recommendation beats any paid ad"),
            ("Amplification", "Happy customers multiply reach for free"),
            ("Digital Equality", "Online reviews now carry word-of-mouth weight"),
            ("Strategic Asset", "Advocacy is a channel to invest in"),
        ],
        takeaways_source="Source: Compiled Research, 2024",
        case_example_company="Tesla",
        case_example_headline="Owners, Not Ads, Built the Tesla Brand",
        case_example_insight="Tesla spends close to nothing on traditional advertising — owners "
             "self-organise meetups, share referral codes and post their own reviews instead. "
             "Nimbus's loyal Facebook community is the same asset already in hand, waiting to be "
             "invested in rather than replaced by paid media.",
        case_type="case_study",
        case_scenario=[
            "Activity 5 traced the perception gap mostly to Value Quality — the feeling of being known — "
            "rather than to the product itself. That is, in one sense, good news: it means Nimbus already has "
            "the raw material to fix it. The same loyal-customer Facebook community that has been asking "
            "\"why hasn't Nimbus gone green sooner?\" is still active, still buying, and still willing to "
            "talk about the brand.",
            "The founder now wants the relaunch to lean on these genuine advocates rather than paid media "
            "alone. But the online review picture is mixed — some customers are clearly still delighted, "
            "others are the ones driving the \"doesn't feel personal anymore\" narrative, and a few are firmly "
            "on the fence.",
            "Your table's job is to read the available feedback, identify who the real advocates are, and "
            "design an advocacy assessment and strategy that strengthens the loop before the anniversary "
            "campaign goes live — without ignoring the risk that a negative experience could restart the "
            "narrative that hurt Nimbus six months ago.",
        ],
        roles=[],
        discussion_prompts=[
            "Reading the mixed feedback, which customers are the strongest genuine candidates for an "
            "advocacy programme, and what evidence marks them out from a merely satisfied customer?",
            "Using the Advocacy Loop, at which stage is Nimbus currently strongest, and at which stage does "
            "the loop most often break down before it reaches a new customer?",
            "Given that a competitor's viral moment is what hurt Nimbus six months ago, how real is the risk "
            "that one bad experience among these advocates could restart the same narrative — and how would "
            "you guard against it?",
            "What would you actually ask advocates to do for the relaunch, and what would Nimbus need to give "
            "them in return for it to feel genuine rather than transactional?",
        ],
        reflection_points=[
            "Did your table pick advocates based on how loudly they post, or on how consistently satisfied "
            "they actually are?",
            "Which stage of the Advocacy Loop did your table find hardest to strengthen with the resources "
            "Nimbus realistically has?",
            "If one of your chosen advocates had a bad experience next week, would your strategy survive it?",
        ],
        debrief_check="Every group can show an advocacy strategy mapped onto the Advocacy Loop, naming which "
             "customers to engage, what stage of the loop it strengthens, and at least one target metric with "
             "how it will be tracked.",
        build="A customer-advocacy strategy mapped to the Advocacy Loop, with named target metrics and how "
              "each will be tracked",
        duration="25 minutes",
    ),
    dict(
        num=7,
        topic=2,
        title="Campaign Documentation Audit",
        objective="Document customer reception to the brand and the outcome of branding campaigns",
        t_statement="Document customer reception to brand and outcome of branding campaigns",
        what_is_kind="infographic",
        what_is_template="list-row-horizontal-icon-arrow",
        what_is_items=[
            ("Feedback Collection", "Systematic recording of customer responses"),
            ("Campaign Metrics", "Measuring effectiveness through customer data"),
            ("Analysis Systems", "Documentation frameworks for brand reception"),
            ("Outcome Tracking", "Recording measurable campaign results"),
        ],
        what_is_source="Source: Multiple branding studies, 2024-2026",
        process_kind="infographic",
        process_template="sequence-ascending-steps",
        process_title="Documentation Process Steps",
        process_items=[
            ("Define Metrics", "Establish the measurement criteria up front."),
            ("Collect Feedback", "Gather the customer-response data systematically."),
            ("Analyse Data", "Process the collected information into findings."),
        ],
        process_source="Source: Marketing campaign best practices, 2024",
        compare_kind="infographic",
        compare_template="compare-binary-horizontal-underline-text-vs",
        compare_title="Traditional vs Modern Documentation Approaches",
        compare_lhead="Traditional",
        compare_rhead="Modern",
        compare_items=[
            ("Manual Surveys", "Paper-based feedback collection"),
            ("Basic Analytics", "Simple metrics and reporting"),
            ("Real-Time Monitoring", "Instant sentiment tracking"),
            ("AI Insights", "Automated pattern recognition"),
        ],
        compare_left=["Manual Surveys — paper-based feedback collection",
                       "Basic Analytics — simple metrics and reporting",
                       "Delayed Insights — weekly or monthly reporting cycles"],
        compare_right=["Real-Time Monitoring — instant sentiment tracking",
                        "AI Insights — automated pattern recognition",
                        "Predictive Analytics — trend forecasting capability"],
        compare_source="Source: Marketing technology evolution studies, 2024",
        table_title="Campaign Documentation Fields",
        table_rows=[
            ("Metric", "What is being tracked", "Engagement rate on the pilot posts"),
            ("Source", "Where the data comes from", "Social platform analytics, press clippings, blog traffic"),
            ("Baseline", "The value before the campaign", "2.1% engagement"),
            ("Result", "The value after the campaign", "4.8% engagement"),
        ],
        table_source="Source: Marketing campaign best practices, 2024",
        big_line1="What isn't documented gets re-argued next quarter.",
        big_line2="A simple, consistent record beats a brilliant memory every time.",
        visual_kind="infographic",
        visual_template="list-grid-badge-card",
        visual_title="The PESO Model",
        visual_items=[
            ("flag", "Paid Media", "Boosted posts and sponsored placements Nimbus paid to run."),
            ("star", "Earned Media", "Unprompted press coverage and mentions Nimbus didn't pay for."),
            ("people", "Shared Media", "Reposts, tags and comments the community generated on its own."),
            ("shield", "Owned Media", "The blog post, email newsletter and product page Nimbus fully controls."),
        ],
        visual_source="Source: PESO Model (Paid, Earned, Shared, Owned), Gini Dietrich / Spin Sucks",
        takeaways_title="Key Documentation Takeaways",
        takeaways_items=[
            ("Systematic Collection", "Use a structured feedback-gathering process"),
            ("Real-Time Analytics", "Monitor responses as they happen"),
            ("Comprehensive Metrics", "Track more than one measurement dimension"),
            ("Continuous Optimisation", "Feed findings into the next campaign"),
        ],
        takeaways_source="Source: Comprehensive branding research, 2024-2026",
        case_example_company="Netflix",
        case_example_headline="Every Test Gets Measured, Every Time",
        case_example_insight="Netflix documents disciplined A/B tests down to thumbnail images and "
             "runs every creative change against hard viewership data — nothing ships on a hunch. "
             "That documentation discipline is exactly what Nimbus's pilot campaign lacked: a record "
             "consistent enough to trust before scaling it up.",
        case_type="case_study",
        case_scenario=[
            "Three months ago, before committing the full relaunch budget, the Marketing Lead quietly piloted "
            "a small \"Behind the Jar\" campaign — a short Instagram Stories series introducing the new "
            "sustainable-packaging story to a slice of the loyal-customer community, alongside one boosted "
            "post, a short unpaid write-up from a local lifestyle blog, and a supporting post on the Nimbus "
            "website.",
            "Nobody kept a single, consistent record of how it performed. Some numbers live in a Marketing "
            "team member's spreadsheet, some in a Notion page nobody else can find, and the rest is only in "
            "people's memory of \"it went pretty well.\" With the Board wanting proof that the full relaunch "
            "campaign works — not just louder impressions — that will not be good enough this time.",
            "Your table's job is to reconstruct what actually happened to the pilot campaign across paid, "
            "earned, shared and owned media, and turn it into a documentation framework the team can reuse "
            "for the real relaunch three months from now.",
        ],
        roles=[],
        discussion_prompts=[
            "Sorting the pilot's activity into Paid, Earned, Shared and Owned media, where did the strongest "
            "customer reception actually happen — and does that match where the team spent the most effort?",
            "Which pieces of the pilot's story are you missing data for entirely, and how would you close "
            "that gap before the full relaunch campaign launches?",
            "What documentation framework would you standardise now, so results don't have to be "
            "reconstructed from memory again after the real relaunch?",
            "Based on the pilot's results, what is the strongest evidence you would put in front of the Board "
            "to justify the relaunch's PR budget?",
        ],
        reflection_points=[
            "Which of the four PESO categories was hardest to find any real data for — and what does that "
            "tell you about Nimbus's current documentation habits?",
            "Did the channel that felt most successful in the room match the channel the numbers actually "
            "supported?",
            "If the Board asked \"how do we know this worked?\" right now, could your documentation answer "
            "them convincingly?",
        ],
        debrief_check="Every group can show a PESO-sorted reception report for the pilot campaign with at "
             "least one metric per media type, the gaps in current data called out honestly, and a reusable "
             "documentation framework for the full relaunch.",
        build="A structured PESO-based campaign-reception report for the pilot, with metrics, gaps and a "
              "documentation framework the team can reuse for the full relaunch",
        duration="25 minutes",
    ),
    dict(
        num=8,
        topic=2,
        title="Customer Perspective Analysis",
        objective="Perform active listening from the customer to understand the customer's perspective of the organisation",
        t_statement="Perform active listening from customer to understand customer's perspective of the organisation",
        what_is_kind="infographic",
        what_is_template="list-grid-candy-card-lite",
        what_is_items=[
            ("target", "Full Attention", "Eliminate distractions during customer interactions"),
            ("gear", "3 P's Framework", "Presence, Patience, and Paraphrasing approach"),
            ("heart", "Emotion Focus", "Understanding the feelings behind customer words"),
            ("idea", "Strategic Insight", "Gather valuable customer perception data"),
        ],
        what_is_source="Source: the 3 P's active-listening framework (Presence, Patience, Paraphrasing), "
                        "customer-service training practice",
        process_kind="infographic",
        process_template="sequence-roadmap-vertical-simple",
        process_title="Active Listening Implementation Steps",
        process_items=[
            ("Eliminate", "Remove all distractions completely before you start."),
            ("Focus", "Give the customer your full attention."),
            ("Receive", "Gather all the information actively — don't half-listen."),
            ("Interpret", "Understand the customer's perspective deeply, not just their words."),
        ],
        process_source="Source: the 3 P's active-listening framework, customer-service training practice",
        compare_kind="infographic",
        compare_template="compare-binary-horizontal-badge-card-arrow",
        compare_title="Passive Hearing vs Active Listening",
        compare_lhead="Passive Hearing",
        compare_rhead="The 3 P's — Active Listening",
        compare_items=[
            ("chat", "Word Focus", "Hearing only the literal words, missing the tone underneath them."),
            ("clock", "Response Ready", "Mentally drafting the scripted reply while the customer is still talking."),
            ("star", "Presence", "Full attention, phone and scripts aside — genuinely there for the call."),
            ("heart", "Patience", "Letting the customer finish completely before responding, without rushing."),
        ],
        compare_left=[
            ("chat", "Word Focus", "Hearing only the literal words, missing the tone underneath them."),
            ("clock", "Response Ready", "Mentally drafting the scripted reply while the customer is still talking."),
            ("flag", "Surface Level", "Closing the call once the words stop, without checking the feeling behind them."),
        ],
        compare_right=[
            ("star", "Presence", "Full attention, phone and scripts aside — genuinely there for the call."),
            ("heart", "Patience", "Letting the customer finish completely before responding, without rushing."),
            ("check", "Paraphrasing", "Reflecting the concern back in your own words to confirm you understood it."),
        ],
        compare_source="Source: the 3 P's active-listening framework (Presence, Patience, Paraphrasing), "
                        "customer-service training practice.",
        table_title="The 3 P's Framework",
        table_rows=[
            ("Presence", "Being fully, mentally there", "Put the phone away, make eye contact"),
            ("Patience", "Letting the customer finish, unrushed", "Wait a beat before replying"),
            ("Paraphrasing", "Reflecting back what you heard", "\"So what I'm hearing is...\""),
            ("Follow-through", "Acting on what was actually said", "Closing the loop with a concrete fix"),
        ],
        table_source="Source: the 3 P's active-listening framework, customer-service training practice",
        big_line1="Listening isn't waiting for your turn to talk.",
        big_line2="The customer's next word usually tells you more than your prepared response would.",
        visual_kind="empathy",
        visual_title="Customer Empathy Map — Priya",
        visual_says=[
            "\"Why doesn't Nimbus feel personal anymore?\"",
            "\"I've bought from you since year one.\"",
        ],
        visual_thinks=[
            "Does anyone here still actually care?",
            "Maybe I'm just an order number now.",
        ],
        visual_does=[
            "Calls Customer Service instead of emailing.",
            "Reads the community Facebook thread nightly.",
        ],
        visual_feels=[
            "Frustrated and quietly disappointed.",
            "Still hopeful Nimbus can win her back.",
        ],
        visual_source="Source: empathy-mapping practice, adapted from the Activity 8 role-play",
        takeaways_title="Key Takeaways for Active Customer Listening",
        takeaways_items=[
            ("Framework Use", "Apply the 3 P's consistently, always"),
            ("Emotion Focus", "Prioritise feelings over the literal words used"),
            ("No Prejudgment", "Understand the customer without assuming the answer"),
            ("Strategic Value", "Turn each insight into a concrete action"),
        ],
        takeaways_source="Source: Multiple Research Sources, 2024",
        case_example_company="Amazon",
        case_example_headline="The Empty Chair That Represents the Customer",
        case_example_insight="Amazon famously keeps an empty chair in meetings to represent the "
             "customer whose voice isn't otherwise in the room — a physical reminder to listen "
             "before deciding. The 3 P's do the same work on a live call: they force Presence, "
             "Patience and Paraphrasing instead of assumption.",
        case_type="role_play",
        case_scenario=[
            "Priya has bought from Nimbus Wellness since its first year. Last night she read the same "
            "community Facebook thread the Activity 4 audit flagged — customers saying Nimbus \"doesn't feel "
            "personal anymore\" — and she agrees. This morning she calls Customer Service, frustrated, "
            "wanting to know why the brand she used to feel loyal to now treats her like any other order "
            "number.",
            "The rep taking the call has a real average-handle-time target and a bank of quick-reply macros "
            "that would close this call in under two minutes. But leadership has asked every Customer Service "
            "call this week to be an active-listening opportunity, not just a resolution — because this exact "
            "situation is what the relaunch's active-listening approach will need to prove it can handle.",
            "Your group of three will run this call as a role play, coached in real time against the 3 P's, "
            "then turn what was actually said — not just what was resolved — into a documented "
            "customer-perspective insight for the relaunch team.",
        ],
        roles=[
            ("The Customer (Priya)", "Be heard and taken seriously, not just processed",
             "A five-year loyal customer who feels increasingly like a transaction. She isn't asking for a "
             "refund — she wants to know if anyone at Nimbus still cares."),
            ("Nimbus Service Rep", "Resolve the call by genuinely listening, not by closing it fast",
             "Under real pressure to keep the call short, but has been told this week that how the call feels "
             "matters as much as how quickly it ends."),
            ("Observer / Coach", "Apply the 3 P's framework as a coaching lens on the call",
             "Says nothing during the role play itself, but tracks exactly where Presence, Patience and "
             "Paraphrasing show up — or don't — to coach the Rep afterwards."),
        ],
        discussion_prompts=[
            "As the call plays out, where does the Rep genuinely apply Presence, Patience and Paraphrasing "
            "— and where do they slip back into passive hearing?",
            "What emotion is actually behind Priya's words, as distinct from the literal complaint she's "
            "making?",
            "How would the Observer paraphrase Priya's perspective back in one honest sentence, without "
            "judgement and without minimising it?",
            "Beyond \"the customer was upset,\" what concrete, actionable insight should this call generate "
            "for the relaunch team?",
        ],
        reflection_points=[
            "As the Customer, at what point in the call did you feel genuinely heard — or feel yourself give "
            "up on being heard?",
            "As the Rep, was it harder to stay patient, or harder to paraphrase without sounding scripted?",
            "As the Observer, which of the 3 P's was missing most often, and what would you coach first?",
        ],
        debrief_check="Every group can show a completed customer-perspective analysis that names the emotion "
             "behind Priya's words (not just the words themselves), cites a specific moment where a P was "
             "applied or missed, and closes with one actionable insight for the relaunch team.",
        build="A completed customer-perspective analysis report — the emotion behind the words, a coaching "
              "note against the 3 P's, and one actionable insight for the relaunch team",
        duration="25 minutes",
    ),
]
