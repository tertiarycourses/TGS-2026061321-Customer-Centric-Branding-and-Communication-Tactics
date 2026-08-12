"""Concept-enrichment slides imported from the reference deck
"Architecting Brand Trust — Aligning Strategy, Emotion, and Agentic AI"
(courseware/PPT References/Architecting_Brand_Trust (2).pptx).

Each Learning Unit gets a set of insight slides rendered AFTER its
Key Concepts slide. Content was transcribed from the reference deck and
redrawn in the Tertiary house white theme; three diagram-heavy visuals
are imported directly (assets/brandtrust/*.png, watermark removed).

Slide spec kinds understood by build_slides.py:
  pillars   -> tile_grid of (title, desc) tuples
  table     -> two-column comparison table with coloured headers
  stats     -> big-number stat tiles + optional callout band
  image     -> full-width imported visual with house header
  quote     -> big statement slide
  flow      -> horizontal chevron flow (optional note band)
  playbook  -> numbered 01..04 columns + tagline band
  twocol    -> two-column comparison panels
"""

BRAND_TRUST = {

# ---------------------------------------------------------------- LU1
1: [
    ("pillars", dict(
        title="The Modern Brand Ecosystem",
        kicker="LU1 · THE BIG PICTURE",
        intro="Four forces now shape how customers trust and choose brands.",
        items=[
            ("The Shift — Philosophy",
             "Moving from product-centric innovation to a customer-back business "
             "model (CBM) to drive sustainable growth."),
            ("The Mechanics — System",
             "Abandoning the linear funnel for a non-linear, infinitely looping "
             "customer journey."),
            ("The Core — Emotion",
             "Engineering authenticity and shared values as the primary engines "
             "of brand loyalty and trust."),
            ("The Scale — AI",
             "Governing the new frontier where agentic AI acts autonomously on "
             "behalf of the brand."),
        ])),
    ("table", dict(
        title="The Strategic Paradigm Shift",
        kicker="LU1 · PRODUCT vs CUSTOMER",
        intro="Customer-centric organisations think, innovate and measure differently.",
        colheads=("Product-Centric", "Customer-Centric"),
        rows=[
            ("Core philosophy", "“If we build it, they will come”",
             "“Obsession with customer pain points and delight”"),
            ("Innovation style", "High-risk, creates new markets, heavy R&D",
             "Incremental, read-and-react, user research-driven"),
            ("Risk profile", "High tolerance for failure and pivots",
             "Lower risk, focused on continuous feedback loops"),
            ("Success metric", "One-time, big-ticket sales",
             "Lifetime value, reduced churn, Net Promoter Scores"),
        ])),
    ("stats", dict(
        title="The Economics of Customer Obsession",
        kicker="LU1 · WHY IT PAYS",
        intro="Firms implementing a customer-experience (CX) approach routinely "
              "outperform product-led peers.",
        stats=[("+49%", "Faster profit growth"),
               ("+41%", "Higher revenue expansion"),
               ("+51%", "Stronger customer retention")],
        note="73% of customers now expect companies to treat them as individuals, "
             "not numbers — up from just 39% in 2023.")),
],

# ---------------------------------------------------------------- LU2
2: [
    ("funnel_journey", dict(
        title="The Marketing Funnel vs the Customer Journey",
        kicker="LU2 · TWO MENTAL MODELS",
        intro="The funnel explains where customers drop off; the journey explains why.",
        note="The funnel ends at the sale. The journey treats the sale as the "
             "halfway point.")),
    ("journey_loop", dict(
        title="Mapping the 5-Stage Journey Loop",
        kicker="LU2 · THE JOURNEY LOOP",
        intro="Awareness → Consideration → Decision → Retention → Advocacy — and "
              "advocacy feeds awareness again.",
        note="Every stage is a listening post: what you hear there tells you what "
             "to fix at the stage before it.")),
    ("stats", dict(
        title="The Engine of Loyalty: Emotional Branding",
        kicker="LU2 · EMOTION DRIVES PERCEPTION",
        intro="Affect-driven purchasing decisions outpace purely rational choices.",
        stats=[("45.2%", "say an emotional connection with a brand is very important"),
               ("42%", "associate their favourite brands with trust & reliability"),
               ("88.1%", "actively choose branded products over non-branded alternatives")],
        note="55% of loyalty is driven by quality — but 32% is driven entirely by "
             "customer service and emotional support.")),
],

# ---------------------------------------------------------------- LU3
3: [
    ("pillars", dict(
        title="The Anatomy of Brand Authenticity",
        kicker="LU3 · AUTHENTICITY",
        intro="Authenticity is engineered through four repeatable practices.",
        items=[
            ("Radical Transparency",
             "Open communication about business practices and product origins — "
             "e.g. Patagonia's Footprint Chronicles detailing supply-chain realities."),
            ("Value Alignment",
             "Emotional connection forged through shared beliefs and societal "
             "commitment — e.g. Ben & Jerry's integration of social justice into "
             "core operations."),
            ("Authentic Storytelling",
             "Humanising the brand through relatable, non-fabricated narratives — "
             "e.g. Nike highlighting genuine struggles and triumphs of real athletes."),
            ("Quality Assurance",
             "Trust earned through unwavering consistency and reliability — "
             "e.g. Toyota's rigorous quality control building global dependability."),
        ])),
    ("twocol", dict(
        title="The Trust Fracture: the Say-Do Gap",
        kicker="LU3 · WHAT BREAKS TRUST",
        lhead="How trust fractures",
        rhead="Case: the Volkswagen emissions scandal",
        left=[
            "Brand authenticity is destroyed by inauthentic practices — when a "
            "company's actions contradict its stated promises.",
            "Discrepancies between marketing claims and operational reality create "
            "a trust fracture that severs the customer journey loop permanently.",
            "PR campaigns can only amplify what operations can prove.",
        ],
        right=[
            "Software was installed to cheat emissions tests.",
            "The deception directly contradicted public claims of environmental "
            "responsibility.",
            "Result: immediate, catastrophic loss of consumer trust — a say-do "
            "gap no campaign could repair.",
        ])),
],

# ---------------------------------------------------------------- LU4
4: [
    ("quote", dict(
        line1="“The agent is becoming the brand.”",
        line2="Nine in ten US marketing agencies now use generative AI, and half use "
              "agentic AI for execution. AI is no longer just generating content — it "
              "is deciding, spending, personalising and interacting directly with "
              "customers.",
        kicker="LU4 · THE NEXT FRONTIER: AGENTIC AI")),
    ("flow", dict(
        title="The Risk Vector: Authority Concentration",
        kicker="LU4 · AI BRAND RISK",
        color="VIOLET",
        steps=[
            "Content agent — permission to draft copy + access the CMS",
            "Media agent — permission to optimise spend + finance workflows",
            "Personalisation engine — tailors experiences + sensitive data",
            "Concentration node — combined permissions create high risk",
        ],
        note="In an agentic enterprise, risk moves through authority pathways, not "
             "people. Human approvals cannot scale at machine speed to monitor "
             "these intersections.")),
    ("flow", dict(
        title="The Brand Authority Model",
        kicker="LU4 · GOVERNANCE",
        color="BLUE",
        steps=[
            "Identity — which human and non-human identities can act on behalf of the brand?",
            "Access — what systems, data and workflows are they permitted to touch?",
            "Inheritance — what authority do they hold after delegation and integrations?",
            "Concentration — where does authority unintentionally combine into high risk?",
            "Revocation — how quickly can authority be severed if boundaries are breached?",
        ],
        note="Enterprise Authority Assurance replaces the editorial calendar.")),
    ("architecture", dict(
        title="The Architecture of Modern Brand Trust",
        kicker="LU4 · PUTTING IT TOGETHER",
        intro="The customer at the centre — anchored by emotion, navigated through "
              "journey mapping, scaled safely within strict AI authority boundaries.")),
    ("playbook", dict(
        title="The Executive Playbook",
        kicker="LU4 · FROM INSIGHT TO ACTION",
        items=[
            ("Shift the Metric",
             "Move away from pure acquisition costs. Restructure KPIs around "
             "lifetime value, Net Promoter Scores and journey retention."),
            ("Map the Reality, Not the Theory",
             "Audit the 5-stage customer journey loop using actual behavioural "
             "data, not internal corporate assumptions. Find the friction."),
            ("Close the Say-Do Gap",
             "Audit your brand's authenticity. Ensure marketing claims — "
             "environmental, social, quality — are rigidly matched by operational "
             "reality."),
            ("Build the Authority Model",
             "Stop relying on human bottlenecks for AI approval. Map identity, "
             "access and authority concentration for every agentic system touching "
             "your brand."),
        ],
        tagline="Trust cannot be retrofitted. It must be engineered.")),
],
}

# ---------------------------------------------------------------------------
# COMMUNICATION TACTICS enrichment
#
# The course title promises "Communication Tactics" as much as branding, so
# these slides give the communication half the same evidence base as the brand
# half. Sourced and synthesised from the industry references supplied by the
# course owner: Atlassian/Loom, Zendesk, HelpDesk, Freshworks, Bitrix24, Slack,
# Pedowitz Group, ChiefCXOfficer and LinkedIn's customer-experience series.
#
# Rendered by build_slides.py through the same render_insight() dispatcher, so
# these use the native chart / scorecard / process_map components — no imported
# raster art.
# ---------------------------------------------------------------------------

COMMS = {

# ---------------------------------------------------------------- LU1
1: [
    ("chart", dict(
        title="What Customers Now Expect From Communication",
        kicker="LU1 · THE EXPECTATION GAP",
        chart="bar",
        intro="Communication is no longer the wrapper around the product — for most "
              "customers it IS the product experience.",
        categories=["Say how a company communicates matters\nas much as what it sells",
                    "Expect immediate response\nwhen they make contact",
                    "Would switch after multiple\npoor experiences",
                    "Expect to be treated as an individual,\nnot a number"],
        series=[("% of consumers",[88,77,73,73])],
        legend=False,
        number_format='0"%"',
        note="If 88% judge you on how you communicate, communication quality is a "
             "brand attribute — not an admin overhead.",
        source="Source: HelpDesk, Slack and Zendesk customer-communication research, 2024–25")),
],

# ---------------------------------------------------------------- LU2
2: [
    ("pillars", dict(
        title="The 5 C's of Customer Communication",
        kicker="LU2 · A MESSAGE QUALITY TEST",
        intro="Run any customer message through these five tests before it is sent.",
        items=[
            ("Clear","Could the reader act on it without asking a follow-up question? "
                     "Plain language beats precise jargon every time."),
            ("Concise","Is every word doing work? Length is not thoroughness — it is "
                       "usually an unedited first draft."),
            ("Concrete","Are there specifics — a date, a number, a name — rather than "
                        "generalities the reader has to interpret?"),
            ("Correct","Is it accurate, current and error-free? One wrong detail "
                       "undermines the credibility of everything around it."),
        ])),
    ("process_map", dict(
        title="Active Listening — The 3 P's in a Live Conversation",
        kicker="LU2 · WHAT GOOD LISTENING LOOKS LIKE",
        intro="Active listening is a sequence you can observe and coach, not a personality trait.",
        lanes=[
            ("Presence",["Remove distractions","Let the customer finish","Note the emotion, not just the facts",""]),
            ("Patience",["Allow silence to sit","Resist solving too early","Ask one clarifying question",""]),
            ("Paraphrasing",["Reflect the meaning back","Check: 'have I got that right?'","Confirm before resolving","Close the loop"]),
        ],
        note="Courteous is the fifth C — and the one most often lost when a team is under "
             "time pressure.",
        source="Source: Zendesk, Freshworks and Bitrix24 active-listening guidance")),
    ("table", dict(
        title="Language That Builds Trust vs Language That Breaks It",
        kicker="LU2 · SAY THIS, NOT THAT",
        intro="The same fact, framed two ways, produces two different customer relationships.",
        colheads=("Avoid — closes the conversation","Use — keeps it open"),
        rows=[
            ("Deflecting","“That's not something I deal with.”",
             "“Let me find that out for you and come back by 3pm.”"),
            ("Leading with the limit","“The dress isn't in stock for two weeks.”",
             "“You can have the dress in two weeks — I can order it now.”"),
            ("Dismissing the feeling","“There's nothing wrong with the product.”",
             "“I can see why that was frustrating — let me look into it.”"),
            ("Vague commitment","“We'll look into it and revert.”",
             "“I'll update you by Thursday, even if it isn't resolved yet.”"),
        ])),
],

# ---------------------------------------------------------------- LU3
3: [
    ("chart", dict(
        title="Why Channel Choice Is a Brand Decision",
        kicker="LU3 · OMNICHANNEL PAYS",
        chart="column",
        intro="Meeting customers on the channels they already use measurably outperforms "
              "broadcasting on the channel that is easiest to produce.",
        categories=["Higher order rate using\n3+ channels vs one",
                    "Spend more when issues resolve\non their preferred channel",
                    "Buy more with seamless\nconversational experiences",
                    "Favour brands that respond\non social media"],
        series=[("% uplift / share of consumers",[494,64,70,54])],
        legend=False,
        note="A 3+ channel mix produced a 494% higher order rate than single-channel "
             "campaigns — the single largest effect in the research set.",
        source="Source: Zendesk and Freshworks omnichannel research, 2024–25")),
    ("process_map", dict(
        title="The Customer Communication Management Workflow",
        kicker="LU3 · FROM MESSAGE TO IMPROVEMENT",
        intro="A repeatable five-stage cycle — the operational backbone behind a consistent brand voice.",
        lanes=[
            ("Brand team",["Create\nbranded templates","Personalise\nwith customer data","","",""]),
            ("Service team",["","","Deliver on the\npreferred channel","Track in one\ncentral record",""]),
            ("Insight team",["","","","","Optimise from\nperformance data"]),
        ],
        note="The loop only closes if tracking is centralised — scattered records are why "
             "most teams cannot say whether their communication improved.",
        source="Source: HelpDesk customer-communication management framework")),
],

# ---------------------------------------------------------------- LU4
4: [
    ("scorecard", dict(
        title="The Communication Metrics That Matter",
        kicker="LU4 · WHAT TO PUT ON THE DASHBOARD",
        intro="Four service-communication measures the Board can actually govern by.",
        cards=[
            dict(value="FRT", label="First Response Time — how long before a customer hears "
                                    "anything at all", target="< 4 hours", trend="leading",
                 direction="up"),
            dict(value="ART", label="Average Resolution Time — how long to actually close "
                                    "the issue", target="< 48 hours", trend="lagging",
                 direction="flat"),
            dict(value="CSAT", label="Customer Satisfaction — how the interaction felt to "
                                     "the customer", target="≥ 85%", trend="lagging",
                 direction="up"),
            dict(value="FCR", label="First Contact Resolution — solved without the customer "
                                    "chasing again", target="≥ 75%", trend="leading",
                 direction="up"),
        ],
        note="FRT and FCR are leading indicators — they warn you early. CSAT and ART confirm "
             "afterwards. A dashboard of only lagging metrics cannot be steered by.",
        source="Source: Zendesk, Bitrix24 and Freshworks service-metric guidance")),
    ("flow", dict(
        title="Structuring a Message So It Lands",
        kicker="LU4 · THE SCR STRUCTURE",
        intro="Lead with the conclusion, not the build-up — the discipline behind every "
              "clear executive update.",
        color="VIOLET",
        steps=[
            ("Situation","State the shared context both sides already agree on. Keep it to "
                         "one or two sentences."),
            ("Complication","Name what changed or what is at risk. This is the reason the "
                            "message exists at all."),
            ("Resolution","State the recommendation or decision needed — and exactly what "
                          "you want the reader to do next."),
        ],
        note="Minto's principle: give the answer first, then the supporting detail. Readers "
             "who need convincing read on; readers who trust you can stop after line one.")),
],
}
