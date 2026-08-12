"""Detailed step-by-step facilitation guides for the 17 in-class activities.

WHY THIS MODULE EXISTS
----------------------
House rule for this course: the SLIDE DECK never shows step-by-step
instructions — slides carry the scenario, the roles, the discussion prompts
and the debrief only. The *detailed* steps live in the Learner Guide (and the
per-activity artefact folders), so the trainer facilitates from the deck while
learners work from the guide.

Everything here is keyed by activity number (1..17) and merged into the
activity dicts by data_domainN loading order, so build_learner_guide.py and
build_activities.py can render it without either knowing about the others.

Each entry provides:
  steps      -- ordered (heading, instruction) pairs; the actual "do this next"
  timing     -- (minutes, phase) pairs that sum to the activity duration
  artefact   -- what the group physically produces
  checklist  -- self-check items learners tick before the debrief
  tips       -- facilitator notes: what to watch for, common wrong turns
"""

STEPS = {

# ================================================================= LU1
1: dict(
    timing=[(3, "Brief the scenario and assign the three roles"),
            (7, "Individually list stakeholders, then pool them at the table"),
            (8, "Plot each stakeholder on the Power-Interest Grid"),
            (5, "Agree an engagement approach per quadrant"),
            (2, "Prepare your one-sentence rationale for the debrief")],
    artefact="A Power-Interest map with 12 stakeholders placed and an engagement "
             "approach written against each quadrant.",
    steps=[
        ("Set up the grid",
         "Draw a 2×2 grid on your worksheet or flipchart. Label the horizontal axis "
         "Interest (low → high) and the vertical axis Power (low → high). Name the four "
         "quadrants: Monitor (low/low), Keep Informed (low power/high interest), "
         "Keep Satisfied (high power/low interest), Manage Closely (high/high)."),
        ("Assign the three roles",
         "One person takes the Founder, one the Retail Operations Lead, one the Retail "
         "Partner Buyer. Everyone else at the table acts as the brand team facilitating. "
         "Role-holders answer in character for the rest of the activity."),
        ("List stakeholders individually first",
         "Working alone for three minutes, write down every stakeholder group touched by "
         "the sustainable-packaging relaunch decision. Aim for at least eight. Working "
         "alone first prevents the loudest voice at the table from anchoring the list."),
        ("Pool and split internal from external",
         "Combine the individual lists on one sheet. Draw a line down the middle: internal "
         "(management, employees, operations) on the left; external (customers, retail "
         "partners, investors, media, regulators) on the right. Trim or merge duplicates "
         "until you have 6 internal and 6 external — 12 in total."),
        ("Interview the three roles for their real concern",
         "Ask each role-holder in turn: “What is your actual worry here?” Write the stated "
         "position and, underneath it, the underlying concern. The gap between the two is "
         "the point of this step — the Retail Partner Buyer's stated position is about "
         "shelf space, but the real concern is supply reliability."),
        ("Plot all 12 on the grid",
         "Place each stakeholder in a quadrant based on power (can they stop or change this "
         "decision?) and interest (how much do they care about the outcome?). Where the "
         "table disagrees, argue it out — the disagreement is where the learning is."),
        ("Match an engagement approach to each quadrant",
         "Assign one approach per quadrant: Manage Closely → co-design; Keep Satisfied → "
         "consult; Keep Informed → brief regularly; Monitor → light-touch watch. Then "
         "sanity-check each stakeholder: does that approach actually address the underlying "
         "concern you recorded earlier?"),
        ("Prepare the debrief line",
         "Agree one sentence: “The stakeholder we would most easily have under-managed is "
         "____, because ____.” Nominate a spokesperson."),
    ],
    checklist=[
        "The grid has both axes labelled and all four quadrants named.",
        "Exactly 12 stakeholders are placed — 6 internal, 6 external.",
        "Each stakeholder has a stated position AND an underlying concern recorded.",
        "Every quadrant has an engagement approach written against it.",
        "The table can name one stakeholder they would have under-managed, and why.",
    ],
    tips=[
        "Watch for tables that place every stakeholder in Manage Closely — push them: if "
        "everything is a priority, nothing is.",
        "The vocal customer community is the instructive case: high interest, low formal "
        "power, but capable of becoming high power overnight through social media.",
        "If a table finishes early, ask them what changes if the retail partner voices "
        "hesitation publicly tomorrow.",
    ]),

2: dict(
    timing=[(3, "Read the scenario and set up the matrix"),
            (8, "Define what each of the four audiences needs to hear"),
            (7, "Assign a tailored key message per segment"),
            (5, "Choose and justify a primary channel per segment"),
            (2, "Pick your one 'fully tailor this first' segment")],
    artefact="A four-row audience matrix: segment | what they need to hear | tailored key "
             "message | primary channel | why this channel.",
    steps=[
        ("Draw the matrix",
         "Five columns: Segment, What they need to hear, Tailored key message, Primary "
         "channel, Why this channel. Four rows — loyal customers, new/comparison shoppers, "
         "the wellness retail chain, the lifestyle press."),
        ("Separate the need from the pitch",
         "For each segment write what the AUDIENCE needs in order to act — not what Nimbus "
         "wants to say. Loyal customers need reassurance the brand hasn't left them behind; "
         "the retail chain needs supply and sell-through evidence. Keep these two things in "
         "different columns and the message writes itself."),
        ("Mark emotional vs logical drivers",
         "Tag each segment B2C-emotional or B2B-logical. Loyal and new customers are largely "
         "emotional (identity, belonging, trust); the retail chain and press are largely "
         "logical (numbers, proof, newsworthiness). Note where those pull in opposite "
         "directions — that tension is exactly why one deck cannot serve all four."),
        ("Write one tailored key message per segment",
         "One sentence each, in the audience's own vocabulary, stating the benefit to THEM. "
         "Test each against the 5 C's — Clear, Concise, Concrete, Correct, Courteous. If a "
         "message would work unchanged for a different segment, it is not yet tailored."),
        ("Choose a primary channel and justify it",
         "Name one primary channel per segment and write why in the final column. The test "
         "is where the audience actually spends attention — not what is easiest for Nimbus "
         "to produce. A press release is easy; it does not reach a loyal customer."),
        ("Build the evidence for the Marketing Lead",
         "Prepare the argument you would make to her: point to two rows in your matrix whose "
         "messages contradict each other, and show what the shared deck would have to omit "
         "to serve both."),
        ("Choose your priority segment",
         "If you could fully tailor only one segment's message this month, which and why? "
         "Base it on which segment most affects the relaunch outcome."),
    ],
    checklist=[
        "All four segments have a distinct key message — no two are interchangeable.",
        "Each segment has a named primary channel with a written justification.",
        "Emotional vs logical drivers are marked for each segment.",
        "The table can point to two segments whose messages genuinely conflict.",
        "A priority segment is chosen with a reason tied to relaunch impact.",
    ],
    tips=[
        "The classic error is four messages that are the same sentence with the nouns "
        "swapped. Challenge any table whose messages pass the swap test.",
        "Press is not a customer segment — it is an amplifier. Tables that treat the press "
        "like a buyer usually write the weakest message of the four.",
    ]),

3: dict(
    timing=[(4, "Read the scenario; capture the three conflicting descriptions"),
            (8, "List candidate hard attributes and verify each is a fact"),
            (8, "Derive the soft attribute each hard attribute creates"),
            (6, "Locate Nimbus on the CBBE pyramid"),
            (4, "Draft and stress-test one brand concept line")],
    artefact="A two-column attribute map (3 hard → 3 soft) with one approved brand "
             "concept line and the CBBE level it strengthens.",
    steps=[
        ("Write up the three current descriptions",
         "Put Retail's “affordable self-care”, Marketing's “clean beauty for real skin” and "
         "Customer Service's “the brand that actually replies” at the top of your sheet. "
         "These are your evidence that the brand is currently undefined."),
        ("List candidate hard attributes",
         "Brainstorm the measurable, provable facts about the Nimbus range — ingredient "
         "standards, price point, response times, packaging, formulation claims. Apply one "
         "test to each: could you put a number or a verifiable statement against it? If not, "
         "it is a soft attribute pretending to be a hard one."),
        ("Select your three hard attributes",
         "Choose the three that Nimbus can genuinely claim AND that a customer would care "
         "about. Something true but irrelevant does not earn a place on the map."),
        ("Derive the soft attribute from each hard one",
         "For each hard attribute ask “so what does that make the customer FEEL?” Draw an "
         "arrow to the soft attribute. Fast replies → feeling heard. Clean formulation → "
         "feeling safe. Accessible price → feeling the brand is for people like me."),
        ("Test the soft attributes against the three teams",
         "Compare your soft attributes with what Retail, Marketing and Customer Service each "
         "say. Where a team's description has no matching soft attribute on your map, decide: "
         "is the team wrong, or is your map incomplete?"),
        ("Place Nimbus on the CBBE pyramid",
         "Work up Keller's levels — Salience (are we noticed?), Performance and Imagery (are "
         "we understood?), Judgments and Feelings (are we felt?), Resonance (are we "
         "recommended?). Mark the level where Nimbus is weakest today and note the evidence."),
        ("Draft the brand concept line",
         "Write one line the founder could approve. It must connect at least one hard "
         "attribute to its soft attribute. Then stress-test it: could Retail, Marketing AND "
         "Customer Service each restate it in their own words without contradicting each "
         "other? If not, redraft."),
    ],
    checklist=[
        "Three hard attributes, each verifiable with a number or provable statement.",
        "Three soft attributes, each linked by an arrow to the hard attribute causing it.",
        "The weakest CBBE level is named with evidence.",
        "One brand concept line is written and connects a hard attribute to a soft one.",
        "All three teams could restate the line consistently.",
    ],
    tips=[
        "Tables routinely list “trusted” or “premium” as hard attributes. Send them back: "
        "those are feelings, and feelings belong in the soft column.",
        "The strongest concept lines usually come from Customer Service's description, "
        "because it is the one grounded in an actual repeated customer experience.",
    ]),

4: dict(
    timing=[(5, "Scope the audit: choose and justify three platforms"),
            (12, "Sample and code recent mentions by sentiment"),
            (12, "Cluster the coded mentions into recurring themes"),
            (10, "Write one response action per theme"),
            (6, "Assemble the leadership-ready summary")],
    artefact="A reputation report: three platforms, a sentiment breakdown per platform, "
             "three named recurring themes, and one response action per theme.",
    steps=[
        ("Choose three platforms and justify each",
         "Pick the three platforms most likely to reveal genuine customer feeling about "
         "Nimbus — typically one review platform, one social platform, and one marketplace "
         "or retailer listing. Write one line per platform on why it earns a place. Choosing "
         "where your brand is most flattered is the wrong instinct."),
        ("Define your sentiment coding rules before you read",
         "Agree what counts as positive, neutral and negative BEFORE sampling — otherwise "
         "the coding drifts. A useful rule: negative = would discourage a prospective buyer; "
         "neutral = factual with no recommendation either way; positive = would encourage."),
        ("Sample recent mentions",
         "Take the most recent 10–15 mentions or reviews per platform from the supplied pack. "
         "Recency matters more than volume: you are auditing where reputation stands today, "
         "not its all-time average."),
        ("Code each mention",
         "Tag every sampled mention positive, neutral or negative, and note the phrase that "
         "decided it. Those phrases are your raw material for the next step."),
        ("Tally the sentiment split per platform",
         "Produce a simple percentage breakdown per platform. Then compare it against what "
         "the founder currently believes. Name the gap explicitly — that gap is the finding "
         "leadership most needs."),
        ("Cluster into recurring themes",
         "Group the phrases you recorded into themes. Push past the surface complaint to the "
         "cause: “doesn't feel personal anymore” usually decomposes into slower replies, "
         "templated responses, or a loss of founder voice. Name exactly three themes."),
        ("Write one response action per theme",
         "Each action must be specific, owned and doable — name what happens, who does it, "
         "and by when. “Improve communication” is not an action; “reply to all reviews within "
         "48 hours, owned by Customer Service, from Monday” is."),
        ("Assemble the leadership summary",
         "One page: the three platforms with sentiment splits, the three themes, the three "
         "actions, and one sentence on the single highest-priority action before the relaunch "
         "brief is finalised."),
    ],
    checklist=[
        "Three platforms named, each with a written justification.",
        "Sentiment coding rules were agreed before reading any mentions.",
        "A percentage sentiment breakdown exists for each platform.",
        "The gap between actual sentiment and the founder's belief is stated explicitly.",
        "Exactly three themes, each with a specific, owned, time-bound action.",
    ],
    tips=[
        "This is the longest activity (45 min) — hold tables to the clock at the coding "
        "stage, which is where groups over-run.",
        "If a table reports overwhelmingly positive sentiment, check their sample: they have "
        "usually sampled the brand's own channels, where critics are least present.",
        "The best leadership summaries lead with the gap, not the data.",
    ]),

# ================================================================= LU2
5: dict(
    timing=[(3, "Recap the Activity 4 findings and Marketing's official position"),
            (7, "Build the two-column belief-vs-evidence table"),
            (6, "Classify each gap as Technical or Value Quality"),
            (6, "Rank the top 3 gaps and assign an owner"),
            (3, "Define what 'closed' looks like for the most urgent gap")],
    artefact="A perception-gap table: Marketing's internal belief vs actual customer "
             "feedback, with the top 3 gaps ranked, classified and owned.",
    steps=[
        ("Set up the comparison",
         "Three columns: What Marketing believes | What customers actually say | The gap. "
         "Carry your Activity 4 themes straight into the middle column — this activity "
         "builds directly on that evidence rather than starting fresh."),
        ("State Marketing's position precisely",
         "Write Marketing's claim as they would defend it: formulas, ingredients and "
         "packaging are unchanged from a year ago. Note that this is a claim about the "
         "PRODUCT, and hold on to that — it is the crux of the whole activity."),
        ("Separate technical quality from value quality",
         "Define the two before you classify anything. Technical Quality = what the product "
         "does, objectively measurable. Value Quality = how it feels to deal with the brand. "
         "Marketing's evidence covers only the first."),
        ("Classify each gap",
         "Take each gap in your table and tag it Technical or Value. Expect most to land in "
         "Value Quality — that is the finding. Where a gap looks technical, ask whether the "
         "customer is really describing the product or the experience of buying it."),
        ("Interrogate the improving metrics",
         "Customer Service's reply times have IMPROVED, yet perception has worsened. Discuss "
         "at your table how that is possible. The answer — faster macros made replies "
         "quicker but less personal — is the single most important insight of this activity: "
         "a metric can improve while the experience it was meant to measure degrades."),
        ("Rank the top three gaps",
         "Order by urgency before the relaunch brief is locked. Rank on impact to the "
         "relaunch, not on how easy the gap is to fix."),
        ("Define 'closed' and assign an owner",
         "For each of the three, write what closed actually looks like in observable terms, "
         "and name the team that owns it. If you cannot describe how you would recognise "
         "'closed', the gap is stated too vaguely — rewrite it."),
    ],
    checklist=[
        "The table compares Marketing's stated belief against real customer feedback.",
        "Every gap is tagged Technical Quality or Value Quality.",
        "The table can explain how reply times improved while perception worsened.",
        "Three gaps are ranked by urgency, with a reason for the ordering.",
        "Each gap has an observable definition of 'closed' and a named owning team.",
    ],
    tips=[
        "The self-checkout kiosks and chat macros are the planted clue — if no table spots "
        "that efficiency gains caused the personalisation loss, surface it in the debrief.",
        "Push back on 'improve communication' as an action; require something observable.",
    ]),

6: dict(
    timing=[(3, "Recap the Value Quality finding from Activity 5"),
            (7, "Sort the mixed feedback to identify genuine advocates"),
            (6, "Map Nimbus onto the Advocacy Loop and find the break point"),
            (6, "Design the ask and the reciprocal offer"),
            (3, "Name target metrics and how each is tracked")],
    artefact="An advocacy strategy mapped to the Advocacy Loop, naming target advocates, "
             "the loop stage it strengthens, the ask, and tracked metrics.",
    steps=[
        ("Draw the Advocacy Loop",
         "Sketch the loop: Satisfied → Loyal → Advocate → Influences a new customer → back "
         "into Awareness. You are looking for where Nimbus's loop breaks before it reaches "
         "a new customer."),
        ("Define what separates an advocate from a satisfied customer",
         "Agree the evidence test at your table BEFORE sorting anyone. Satisfied customers "
         "are happy; advocates take unprompted public action on the brand's behalf — they "
         "post, review, recommend, defend. Repeat purchase alone is loyalty, not advocacy."),
        ("Sort the mixed feedback into three groups",
         "Read the supplied feedback and sort into: genuine advocates, on-the-fence, and "
         "the critics driving the 'doesn't feel personal' narrative. Record the specific "
         "evidence that put each customer in their group."),
        ("Find the break point in the loop",
         "Mark where Nimbus is strongest and where the loop breaks. The green-packaging "
         "community is a strong signal — they are advocating and asking for more, which "
         "means the break is usually not at Satisfied or Loyal but at the point where "
         "advocacy is never invited or amplified."),
        ("Design the ask",
         "Decide what you would genuinely ask advocates to do for the relaunch — and be "
         "specific. 'Share our post' is weak; 'tell us what nearly made you leave, on the "
         "record' is a real ask that also produces insight."),
        ("Design the reciprocal offer",
         "Write what Nimbus gives in return so the exchange feels genuine, not "
         "transactional. Early access, a voice in the packaging decision and public "
         "credit outperform discount codes, which convert advocates into bargain hunters."),
        ("Build the risk guard",
         "A competitor's viral moment caused the original damage. Write one safeguard for "
         "what happens if an advocate has a bad experience during the campaign — who "
         "responds, how fast, and through which channel."),
        ("Name the metrics",
         "At least two target metrics with how each will be tracked and by whom. Advocacy "
         "metrics should measure action taken, not sentiment felt."),
    ],
    checklist=[
        "An evidence-based test distinguishes advocates from merely satisfied customers.",
        "Feedback is sorted into advocates / on-the-fence / critics with evidence recorded.",
        "The break point in the Advocacy Loop is named.",
        "There is a specific ask AND a reciprocal offer that is not a discount.",
        "A safeguard exists for an advocate having a bad experience mid-campaign.",
        "At least two metrics, each with a tracking method and an owner.",
    ],
    tips=[
        "Tables often default to a discount code as the reciprocal offer — challenge it: "
        "discounts attract deal-seekers, not advocates.",
        "The customers complaining loudest are frequently the most convertible advocates, "
        "because they still care enough to complain. Raise this if no table notices.",
    ]),

7: dict(
    timing=[(3, "Reconstruct what the pilot campaign actually consisted of"),
            (7, "Sort every element into Paid, Earned, Shared, Owned"),
            (6, "Attach at least one metric per media type"),
            (5, "Mark the data gaps honestly"),
            (4, "Draft the reusable documentation framework")],
    artefact="A PESO-sorted reception report for the pilot, with a metric per media type, "
             "gaps flagged, and a reusable documentation template.",
    steps=[
        ("List every element of the pilot",
         "Reconstruct 'Behind the Jar' from the scenario: the Instagram Stories series, the "
         "boosted post, the unpaid lifestyle-blog write-up, and the Nimbus website post. "
         "Add anything else the scenario implies."),
        ("Define the four PESO categories",
         "Paid = you bought the placement. Earned = someone else chose to cover you. "
         "Shared = social and community activity. Owned = channels you control. Agree these "
         "definitions before sorting, because the boosted post is the one people argue over."),
        ("Sort each element into a category",
         "Place all four elements. The boosted post is Paid even though it lives on a Shared "
         "channel — the money decides the category. The blog write-up is Earned precisely "
         "because it was unpaid."),
        ("Attach at least one metric per category",
         "For each PESO category name the metric that would actually show customer "
         "reception, not just volume. Reach shows how many were exposed; saves, replies and "
         "sentiment show whether anyone cared."),
        ("Mark the gaps honestly",
         "Flag every category where the data does not exist or lives in someone's "
         "spreadsheet or memory. Being honest about gaps is the point of the audit — a "
         "report that hides its gaps cannot be trusted by the Board."),
        ("Compare effort against reception",
         "Note where the team spent the most effort versus where the strongest reception "
         "actually happened. A mismatch here is the most useful finding for the full "
         "relaunch budget."),
        ("Draft the reusable framework",
         "Design the template the team will fill in DURING the real relaunch: which fields, "
         "captured by whom, at what cadence, stored where. It must be simple enough that it "
         "actually gets filled in — that is the real design constraint."),
        ("Choose the Board evidence",
         "Select the single strongest piece of pilot evidence you would put in front of the "
         "Board to justify the relaunch PR budget, and say why it is the most persuasive."),
    ],
    checklist=[
        "All four pilot elements are sorted into PESO with the boosted post correctly Paid.",
        "Each PESO category has at least one reception metric, not just a volume metric.",
        "Missing data is explicitly flagged rather than glossed over.",
        "The effort-vs-reception mismatch is identified.",
        "The framework names fields, an owner, a cadence and a storage location.",
    ],
    tips=[
        "If a table puts the boosted post under Shared, use it to teach the Paid/Shared "
        "boundary — it is the most common PESO error in practice.",
        "Frameworks that require more than about five fields per campaign never get filled "
        "in. Push tables toward something realistically small.",
    ]),

8: dict(
    timing=[(4, "Assign roles and brief the Observer on the 3 P's"),
            (8, "Run the call as a live role play"),
            (5, "Observer coaches against Presence, Patience, Paraphrasing"),
            (5, "Name the emotion behind the words"),
            (3, "Write the actionable insight for the relaunch team")],
    artefact="A customer-perspective analysis: the emotion behind Priya's words, a coaching "
             "note against the 3 P's, and one actionable insight for the relaunch team.",
    steps=[
        ("Assign the three roles",
         "Customer (Priya), Nimbus Service Rep, Observer/Coach. Groups of three exactly. If "
         "your table has more, run two parallel trios rather than adding spectators."),
        ("Brief the Observer before the call starts",
         "The Observer prepares a three-column note — Presence, Patience, Paraphrasing — and "
         "says NOTHING during the role play. Their only job is to record the moment and the "
         "exact words where each P appeared or was missed."),
        ("Brief Priya privately",
         "Priya is not asking for a refund. She wants to know whether anyone at Nimbus still "
         "cares. She should not state this directly — she should express it as frustration "
         "about small things, the way real customers do. That gap is what the Rep must hear."),
        ("Brief the Rep on the real tension",
         "The Rep has an average-handle-time target and macros that would close this in under "
         "two minutes. They must feel that pressure genuinely — the learning comes from "
         "choosing listening over speed while the pressure is real."),
        ("Run the call",
         "Play it live for the full time. Do not stop to correct — the Observer's notes "
         "depend on the call running uninterrupted, including its mistakes."),
        ("Coach against the three P's",
         "The Observer walks through their notes: Presence (was the Rep fully attending or "
         "queuing a macro?), Patience (did they let silences sit, or fill them?), "
         "Paraphrasing (did they reflect Priya's meaning back without judgement?). Cite "
         "specific moments and words, never general impressions."),
        ("Name the emotion behind the words",
         "Separate the literal complaint from the emotion driving it. The words are about "
         "service speed and templates; the emotion is usually feeling forgotten by a brand "
         "she helped build. Write the emotion in one honest sentence."),
        ("Paraphrase Priya's perspective in one sentence",
         "Draft the single sentence the Rep could have said that would have made Priya feel "
         "heard — without judgement and without minimising. Test it on the person who played "
         "Priya: would it have landed?"),
        ("Write the actionable insight",
         "Convert the call into one insight the relaunch team can act on. 'The customer was "
         "upset' is an observation, not an insight. 'Long-tenure customers read macro "
         "replies as evidence the brand has outgrown them' is actionable."),
    ],
    checklist=[
        "Three roles were assigned and the Observer stayed silent during the call.",
        "The Observer can cite specific moments for each of the three P's.",
        "The emotion behind Priya's words is named separately from her literal complaint.",
        "A one-sentence non-judgemental paraphrase is written and tested on 'Priya'.",
        "The insight is actionable by the relaunch team, not a restatement of the complaint.",
    ],
    tips=[
        "Reps almost always start solving before Priya finishes. Let it happen — it is the "
        "most teachable moment the Observer will capture.",
        "If Priya states 'I want to know if anyone cares' outright, the exercise loses its "
        "point. Re-brief and restart if needed.",
        "Rotate roles if time allows; playing Priya changes how people take calls afterwards.",
    ]),

# ================================================================= LU3
9: dict(
    timing=[(4, "Recap the approved brand concept line from Activity 3"),
            (8, "Draft the visual-identity specifications"),
            (7, "Write the brand values and mission statement"),
            (7, "Define the voice, and where tone flexes vs stays fixed"),
            (4, "Write one do/don't usage pair and the rollout roadmap")],
    artefact="A one-page brand-guidelines draft: visual identity, values, voice with an "
             "example, one do/don't pair, and an implementation roadmap.",
    steps=[
        ("Start from the approved concept line",
         "Write the brand concept line from Activity 3 at the top of the page. Every "
         "specification that follows must protect that line — if a rule does not, it does "
         "not belong in the guidelines."),
        ("Specify the visual identity",
         "Cover logo usage (minimum size, clear space, what is forbidden), colour palette "
         "(primary and secondary, with where each is used), and typography (heading and body "
         "faces, and the hierarchy). Write specifications a designer could follow without "
         "asking a follow-up question."),
        ("Write the brand values",
         "Three to five values, each with one line on what it means in practice. A value "
         "that could belong to any skincare brand is not a value — it is a platitude. Test "
         "each by asking whether a competitor could claim the opposite and still be credible."),
        ("Write the mission statement",
         "One sentence, in plain language, that Retail, Marketing and Customer Service could "
         "each restate in their own words without contradicting one another."),
        ("Define the voice",
         "Describe how Nimbus sounds using three or four adjectives, each paired with its "
         "opposite for clarity ('warm, not chummy'; 'direct, not blunt'). Opposites do more "
         "work than adjectives alone."),
        ("Show where tone flexes and where it stays fixed",
         "Write the same message twice — once as a customer service email, once as an "
         "Instagram caption. Mark what changed (register, length, emoji) and what must never "
         "change (the values, the honesty, the willingness to say what went wrong)."),
        ("Write one do/don't pair",
         "Take the actual inconsistency the founder noticed and write the correct version "
         "beside the wrong one. A concrete pair stops more drift than a page of principles."),
        ("Draft the implementation roadmap",
         "List what gets updated, in what order, by whom, before the relaunch: website, "
         "in-store signage, Instagram bio, staff scripts. Sequence by customer visibility."),
    ],
    checklist=[
        "The approved brand concept line is on the page and every rule traces back to it.",
        "Visual identity covers logo, colour and typography at specification level.",
        "Values are specific enough that a competitor could not claim the opposite.",
        "The voice is described with adjective/opposite pairs.",
        "One concrete do/don't pair addresses the founder's observed inconsistency.",
        "The roadmap names what, who and in what order.",
    ],
    tips=[
        "Tables tend to over-invest in colour palettes and under-invest in voice — voice is "
        "what Customer Service actually needs to do their job.",
        "Ask: could a new hire write an on-brand caption from this page alone? That is the "
        "only test of a guidelines document that matters.",
    ]),

10: dict(
    timing=[(3, "Review the discount campaign against the brand concept"),
            (6, "List the identity elements that should have appeared"),
            (5, "Score the campaign for consistency with evidence"),
            (4, "Locate and size the gap"),
            (2, "Write two or three concrete recommendations")],
    artefact="A brand-audit report: consistency score, the missing identity elements, and "
             "two to three recommendations for brand-marketing integration.",
    steps=[
        ("Restate the brand identity",
         "List the identity elements Nimbus has already approved — the concept line, the "
         "values, the hard and soft attributes from Activity 3. This is your audit standard; "
         "without it written down, the audit becomes opinion."),
        ("Inventory what the campaign actually said",
         "Write down what the two-week discount push communicated: the serum, the price cut, "
         "the urgency. Be strict — record only what was actually said, not what the team "
         "intended to imply."),
        ("Compare element by element",
         "Tick each identity element that appeared in the campaign and cross those that did "
         "not. The crosses are your finding, and there will be many."),
        ("Score consistency with evidence",
         "Give a consistency score out of 10 and justify it in one sentence citing your "
         "ticks and crosses. A score without evidence is just a feeling."),
        ("Weigh the loyal-customer comment",
         "Customers said it 'felt like any other skincare sale.' Discuss what that reveals: "
         "the campaign succeeded commercially while borrowing equity from the brand rather "
         "than building it. Both things are true at once, and the Board needs to hear both."),
        ("Size the gap",
         "State how wide the gap is between what the campaign said and what the brand stands "
         "for — and whether one more campaign like it would materially damage the brand or "
         "merely fail to help it."),
        ("Write the recommendations",
         "Two or three concrete changes that would make the next campaign build equity while "
         "still moving stock. Do not recommend abandoning promotions — recommend how a "
         "promotion can carry the brand's values while still being a promotion."),
    ],
    checklist=[
        "The brand identity standard is written down before the audit begins.",
        "Each identity element is ticked or crossed against the actual campaign.",
        "The consistency score cites specific evidence.",
        "The report acknowledges the campaign succeeded on sales AND failed on brand.",
        "Recommendations keep promotion viable rather than banning discounts.",
    ],
    tips=[
        "The trap is treating 'it sold well' and 'it hurt the brand' as contradictory. The "
        "strongest audits hold both.",
        "This is the shortest LU3 activity (20 min) — keep the inventory step brisk.",
    ]),

11: dict(
    timing=[(4, "Define the core message answering the perception gap"),
            (8, "Choose 3-4 channels and their distinct jobs"),
            (10, "Design the experiential element"),
            (5, "Set the brand-recall metric"),
            (3, "Build the timeline and budget split")],
    artefact="A campaign-strategy document: core message, 3-4 channels with distinct roles, "
             "one experiential element, timeline, budget split and a brand-recall metric.",
    steps=[
        ("Write the core message",
         "One message the whole relaunch carries. It must answer 'doesn't feel personal "
         "anymore' directly — not by asserting that Nimbus is personal, but by demonstrating "
         "it. Trace the message back to the approved brand concept line."),
        ("Choose three or four channels",
         "Select across owned, earned and paid. For each, write the specific job it does that "
         "the others cannot. If two channels have the same job, cut one and reallocate."),
        ("Adapt the message per channel without breaking voice",
         "Write how the core message appears on each channel. The register flexes; the "
         "message does not change. Check each against the voice guidelines from Activity 9."),
        ("Design the experiential element",
         "The founder's non-negotiable: something people can walk into, touch or take part "
         "in. Design it against three tests — relevant (connects to the brand concept, not "
         "just eye-catching), emotionally engaging (creates a feeling that matches your soft "
         "attributes), and genuinely shareable (people want to post it unprompted, without "
         "being asked)."),
        ("Stress-test the experience",
         "Ask the hardest question: would someone post this if there were no hashtag "
         "competition or prize attached? If the honest answer is no, it is a photo backdrop, "
         "not an experience. Redesign it."),
        ("Connect the experience to the perception gap",
         "Show explicitly how the experiential element makes the brand feel personal again. "
         "If it cannot be traced to that gap, it is a good idea for a different campaign."),
        ("Set the brand-recall metric",
         "Define how you will know the activation built recall, not just footfall. Recall "
         "requires asking people afterwards what they remember and attribute to Nimbus — "
         "attendance numbers cannot answer that."),
        ("Build the timeline and budget split",
         "Lay out the phases across the run-up to the anniversary and allocate budget "
         "proportionally across your channels plus the experience."),
    ],
    checklist=[
        "The core message answers the personalisation gap by demonstration, not assertion.",
        "Each of the 3-4 channels has a distinct, non-overlapping job.",
        "The experiential element passes relevant / emotional / shareable.",
        "It survives the 'would they post it without a prize?' test.",
        "A brand-recall metric is defined that is not attendance or impressions.",
        "A timeline and budget split exist.",
    ],
    tips=[
        "Nearly every table's first experiential idea is a photo wall. Push once and the "
        "second idea is usually far better.",
        "The strongest designs invite customers into the packaging decision itself — turning "
        "the original complaint into participation.",
    ]),

12: dict(
    timing=[(4, "Review positioning and the perception gap the budget must close"),
            (8, "Allocate percentages across the PESO channels"),
            (5, "Decide what to deliberately underfund and why"),
            (4, "Set the reserve fund and its trigger"),
            (4, "Define reputation KPIs the Board can hold the team to")],
    artefact="A PR budget proposal: a percentage split across Paid/Earned/Shared/Owned, a "
             "reserve fund with a defined trigger, and Board-grade reputation KPIs.",
    steps=[
        ("Anchor to positioning, not convenience",
         "Write Nimbus's brand positioning and the perception gap at the top. Every "
         "allocation must be defensible against these, not against which channel is easiest "
         "for Marketing to book."),
        ("Allocate across the four PESO channels",
         "Assign a percentage to Paid, Earned, Shared and Owned. They must total 100% "
         "including your reserve. Write a one-line rationale beside each figure."),
        ("Justify the largest share",
         "Name the channel taking the biggest share and argue why it is right for THIS "
         "relaunch. Given a credibility problem, Earned and Shared usually deserve more than "
         "Paid — paid reach does not repair trust, and a brand shouting louder about being "
         "personal tends to prove the opposite."),
        ("Decide what to underfund deliberately",
         "Name the channel you are consciously underfunding and why. Deliberate underfunding "
         "is a strategic decision; leaving something out silently is an oversight. The CEO "
         "will ask about this."),
        ("Set the reserve and its trigger",
         "Hold back a percentage and — critically — write what specific event would release "
         "it. A reserve without a trigger becomes either unspent or spent on impulse. The "
         "packaging-defect scenario in Activity 15 is exactly the kind of trigger to plan for."),
        ("Define reputation KPIs, not reach KPIs",
         "The Board wants proof of reputation improvement. Impressions and reach measure "
         "exposure. Sentiment shift, share of positive voice, review-score movement and "
         "earned-mention quality measure reputation. Choose the latter."),
        ("Pressure-test the proposal",
         "Have one person at the table play the CEO and challenge each allocation. Revise "
         "anything that cannot be defended in one sentence."),
    ],
    checklist=[
        "Percentages across Paid/Earned/Shared/Owned plus reserve total 100%.",
        "Each allocation has a one-line rationale tied to positioning.",
        "One channel is explicitly and deliberately underfunded, with a reason.",
        "The reserve has a written trigger condition.",
        "KPIs measure reputation, not reach.",
        "Every allocation survived a CEO-style challenge.",
    ],
    tips=[
        "Tables default to a paid-heavy split out of habit — ask whether buying reach can "
        "fix a trust problem.",
        "A reserve of roughly 10-15% with a named trigger is a realistic professional norm.",
    ]),

# ================================================================= LU4
13: dict(
    timing=[(3, "Set the pre-relaunch baseline question"),
            (5, "Choose three platforms that reveal reputation, not volume"),
            (6, "Assign leading and lagging indicators per platform"),
            (4, "Separate genuine shift from relaunch-week noise"),
            (2, "Write the one-sentence verdict for the Board")],
    artefact="A platform-by-platform audit with at least one leading and one lagging "
             "indicator each, and a one-sentence verdict on real movement vs noise.",
    steps=[
        ("Establish the baseline problem",
         "Note the central difficulty first: Marketing has post-relaunch screenshots but no "
         "pre-relaunch baseline. Without a before, no after can prove movement. State this "
         "explicitly — it is the finding the Board most needs to hear."),
        ("Choose three platforms for signal, not volume",
         "Pick the platforms where customers actually complain — Google reviews and the "
         "retail chain's app — over the platforms with the biggest impression counts. "
         "Auditing where you look best is not an audit."),
        ("Define leading vs lagging indicators",
         "Leading indicators warn early (sentiment trend in new reviews, question volume, "
         "share of negative mentions this week). Lagging indicators confirm after the fact "
         "(average review score, repeat-purchase rate, NPS). You need both: leading to steer, "
         "lagging to prove."),
        ("Assign indicators per platform",
         "At least one leading and one lagging indicator for each of the three platforms, "
         "with the data source for each."),
        ("Separate signal from relaunch-week noise",
         "Design the test that distinguishes a real sentiment shift from hype. The strongest "
         "approach is to track whether the specific 'feels personal' language recurs in "
         "unprompted comments several weeks after the spike, when campaign attention has "
         "faded."),
        ("Handle the mixed-evidence case",
         "Decide in advance what you would tell the Board if quantitative numbers look "
         "strong but no qualitative comment mentions feeling more personal. This is the most "
         "likely real outcome, and the honest answer is that the campaign moved attention "
         "but not perception."),
        ("Write the verdict",
         "One sentence for the Board: genuine reputation shift, or relaunch-week spike — "
         "with the evidence that decides it."),
    ],
    checklist=[
        "The missing pre-relaunch baseline is called out explicitly.",
        "Three platforms chosen for signal, including where customers complain.",
        "Each platform has at least one leading and one lagging indicator with a source.",
        "A test exists to separate genuine shift from campaign-week hype.",
        "A one-sentence Board verdict is written, backed by evidence.",
    ],
    tips=[
        "The baseline gap is the intended discovery. If no table raises it, ask what they "
        "are comparing their numbers against.",
        "Twenty minutes is tight — keep platform selection to five minutes.",
    ]),

14: dict(
    timing=[(3, "Set up the four-pillar scorecard"),
            (8, "Rate each pillar with named evidence"),
            (6, "Diagnose the reviews-up / repeat-purchase-flat gap"),
            (5, "Choose where one more month of measurement goes"),
            (3, "Write the improvement action for the weakest pillar")],
    artefact="A one-page brand-health scorecard across Awareness, Loyalty, Financial Impact "
             "and Trust, with evidence per rating and one improvement action.",
    steps=[
        ("Build the scorecard",
         "Four rows — Awareness, Loyalty, Financial Impact, Trust. Columns: rating, evidence, "
         "confidence in that evidence. The founder must defend this line by line, so anything "
         "without evidence cannot carry a rating."),
        ("Define each pillar before rating",
         "Awareness = do people know us. Loyalty = do they come back. Financial Impact = does "
         "the brand command price and volume. Trust = do they believe us when we speak. "
         "Agreeing definitions prevents the ratings from becoming vibes."),
        ("Rate each pillar with evidence",
         "Assign a rating and cite the specific evidence. Where evidence is thin — likely for "
         "Trust — say so in the confidence column rather than inventing a number. A scorecard "
         "that admits low confidence is more defensible than one that does not."),
        ("Diagnose the central puzzle",
         "Reviews have improved but repeat-purchase has not moved. Work out which pillar that "
         "sits in: Trust is recovering (people say better things) while Loyalty has not yet "
         "followed (they have not bought again). Sentiment recovers before behaviour does."),
        ("Draw the lesson about recovery time",
         "State what that gap tells the founder: reputation repair shows up in words first "
         "and in money later. A Board expecting both simultaneously will judge the relaunch a "
         "failure too early. This is the sentence worth putting in the Board pack."),
        ("Choose where to spend one more month of measurement",
         "Pick the single pillar where more measurement would most move Board confidence, and "
         "justify it. Usually Loyalty — because it is the pillar where the evidence is "
         "genuinely incomplete rather than merely weak."),
        ("Separate act-now from watch indicators",
         "Write the rule your table would use: an indicator demands action when it is "
         "leading, sustained across periods, and tied to revenue or trust; it is worth "
         "watching when it is lagging, volatile, or a single data point."),
        ("Write the improvement action",
         "One concrete action for the weakest pillar, with an owner and a review date."),
    ],
    checklist=[
        "All four pillars are rated with named evidence and a confidence level.",
        "The reviews-up / purchases-flat gap is correctly diagnosed across Trust and Loyalty.",
        "The scorecard states that sentiment recovers before behaviour.",
        "One pillar is chosen for further measurement with a justification.",
        "A rule distinguishes act-now indicators from watch-only ones.",
        "The weakest pillar has one action with an owner and review date.",
    ],
    tips=[
        "The five-star-reviews / flat-repeat-purchase detail is the whole lesson. If a table "
        "reads it as contradictory data, guide them to the time-lag explanation.",
        "Guard against tables rating all four pillars 'medium' to avoid committing.",
    ]),

15: dict(
    timing=[(4, "Assign roles and establish what is actually known at 9pm"),
            (7, "Decide tonight's holding response"),
            (7, "Run the next-morning interview as a live role play"),
            (4, "Benchmark against a real 2024-25 crisis"),
            (3, "Write the 24-hour follow-up commitment")],
    artefact="A same-night crisis-response script — public holding statement plus next-day "
             "interview line — rehearsed and benchmarked against a real crisis example.",
    steps=[
        ("Assign the three roles",
         "Spokesperson, Journalist, Crisis-Response Lead. The Journalist must genuinely "
         "press — a soft interview teaches nothing."),
        ("Separate what is known from what is assumed",
         "Three columns: confirmed, suspected, unknown. Confirmed — jars are cracking and a "
         "thread is growing. Suspected — a single bad batch. Unknown — how many units, and "
         "whether it is supplier fault or Nimbus QC. You may only speak publicly to column "
         "one."),
        ("Resolve the silence question",
         "Debate whether saying nothing until Operations confirms everything is safer. It is "
         "not: a vacuum gets filled by the thread, and by morning the story is written "
         "without Nimbus in it. Acknowledging without concluding is the professional move."),
        ("Draft tonight's holding statement",
         "Write what Nimbus posts within hours. It must acknowledge, show the issue is being "
         "taken seriously, state what is being done now, and say when the next update comes — "
         "without admitting a cause nobody has confirmed. Say what is true, say what you are "
         "doing, say when you will say more."),
        ("Prepare the Spokesperson's honest commitments",
         "List what can be committed to before root cause is known: investigating, replacing "
         "affected units, updating by a stated time. These are process commitments, which are "
         "always available; cause commitments are not."),
        ("Run the interview",
         "The Journalist asks directly whether Nimbus knew about a defect before launch. The "
         "Spokesperson must answer honestly without speculating. Watch for the two failure "
         "modes: over-promising a cause not yet confirmed, and stonewalling into a "
         "'no comment' that reads as guilt."),
        ("Keep internal and external in sync",
         "Define how the Crisis-Response Lead and Spokesperson stay aligned — one shared "
         "fact-sheet, updated at a fixed cadence, from which all public statements are drawn. "
         "Crises are usually made worse by two people saying different true things."),
        ("Benchmark against a real example",
         "Compare your plan against a real 2024-25 brand crisis. Decide whether yours "
         "resembles the fast-and-transparent response or the delayed-and-silent one, and name "
         "which specific choice in your plan puts it in that category."),
        ("Write the 24-hour commitment",
         "State the follow-up Nimbus commits to publicly within 24 hours, and who owns it."),
    ],
    checklist=[
        "Confirmed / suspected / unknown are separated before anything is drafted.",
        "A holding statement exists that acknowledges without admitting an unconfirmed cause.",
        "It names what is being done now and when the next update comes.",
        "The interview was run live with the Journalist pressing hard.",
        "A single shared fact-sheet keeps internal and external messaging in sync.",
        "The plan is benchmarked against a real crisis with the deciding choice named.",
        "A 24-hour follow-up commitment has an owner.",
    ],
    tips=[
        "The instinct to wait for full facts is near-universal and is the core error — draw "
        "it out rather than correcting it early.",
        "Watch for a Spokesperson blaming the supplier. Customers bought from Nimbus; "
        "deflection reads as evasion even when factually accurate.",
    ]),

16: dict(
    timing=[(3, "Audit what each department currently tracks"),
            (6, "Select 3 internal and 3 external KPIs"),
            (6, "Run one KPI through the full SMART test"),
            (3, "Assign owner, target, source and review date"),
            (2, "Define the missed-target escalation")],
    artefact="A SMART KPI framework — 3 internal + 3 external KPIs, each with an owner, "
             "target, data source, review deadline and a missed-target trigger.",
    steps=[
        ("Audit the current state",
         "List what each department tracks today: Marketing on followers, Retail on footfall, "
         "Customer Service on response times. Mark that none has a target or a deadline — "
         "that is precisely why 'engagement is up' was meaningless."),
        ("Distinguish internal from external KPIs",
         "Internal KPIs measure what Nimbus does (response time, publishing cadence, staff "
         "training completion). External KPIs measure how the market responds (sentiment, "
         "repeat purchase, share of voice). A framework of only internal KPIs measures "
         "activity, not results."),
        ("Select three of each",
         "Choose for decision value, not for ease of extraction. The test: if this number "
         "moved, would the Board actually do something differently? If not, cut it."),
        ("Run one KPI through the full SMART test",
         "Take your weakest KPI and test it: Specific (exactly what is counted?), Measurable "
         "(from which system?), Achievable (given the team and budget?), Relevant (to the "
         "relaunch objective?), Time-bound (by when?). Note where it first breaks — usually "
         "Specific or Time-bound — and fix it."),
        ("Repair the rest",
         "Apply the same test quickly to the remaining five and tighten each."),
        ("Assign the four fields",
         "Every KPI needs a named owner (a person, not a department), a numeric target, a "
         "data source, and a review deadline. A KPI without an owner is nobody's job."),
        ("Define the escalation",
         "Write what happens if a KPI misses target two months running — who is told, what "
         "gets reviewed, what decision is triggered. Without this the dashboard is reporting, "
         "not governance."),
        ("Design the five-minute view",
         "The founder is not a numbers person. Choose the smallest set of numbers that still "
         "tells the whole story on one slide, and lay it out. Usually one headline number per "
         "pillar with a trend arrow."),
    ],
    checklist=[
        "Three internal and three external KPIs are named and distinguished.",
        "Every KPI would change a Board decision if it moved.",
        "At least one KPI is walked through all five SMART letters with its break point named.",
        "Each KPI has a person as owner, a target, a source and a review date.",
        "A two-month-miss escalation is written.",
        "A five-minute, one-slide view exists for the founder.",
    ],
    tips=[
        "Follower count is the classic KPI that fails Relevant — use it to teach the "
        "decision-value test.",
        "Departments as owners ('Marketing') let accountability evaporate; insist on a person.",
    ]),

17: dict(
    timing=[(4, "Map the relaunch onto the four AMEC stages"),
            (7, "Find the stage where evidence gets weakest"),
            (6, "Diagnose the impressions-up / sentiment-flat pattern"),
            (5, "Write three stage-specific recommendations"),
            (3, "Turn the audit into a repeatable habit")],
    artefact="An AMEC audit across Inputs, Outputs, Outcomes and Impact, with the weakest "
             "stage evidenced and three recommendations each fixing a different stage.",
    steps=[
        ("Define the four AMEC stages",
         "Inputs = what you invested (budget, time, people). Outputs = what you produced and "
         "distributed (posts, coverage, events). Outcomes = what changed in the audience "
         "(awareness, sentiment, intent). Impact = what changed for the organisation "
         "(revenue, reputation, shelf space). Write these down before mapping anything."),
        ("Map the relaunch to each stage",
         "Place the actual evidence from the whole Nimbus arc into the four stages — the "
         "budget from Activity 12, the channels and experience from Activity 11, the platform "
         "audit from Activity 13, the health scorecard from Activity 14."),
        ("Find where the evidence thins",
         "Move up the chain and mark where evidence gets weakest. It is almost always "
         "Outcomes and Impact: Inputs and Outputs are easy to count, while changes in belief "
         "and business results are harder and are usually not instrumented in advance."),
        ("Diagnose the central pattern",
         "Impressions up, sentiment only partly recovered. Classify it precisely: an Outputs "
         "success and an Outcomes shortfall. Nimbus successfully produced and distributed "
         "the campaign; it did not fully change what people believe."),
        ("Read the retail-partner signal",
         "One retail partner is still hesitant on shelf space. Place that at Impact — it is "
         "the clearest evidence that business results have not yet followed the activity, and "
         "it connects straight back to the Activity 1 stakeholder who wanted proof."),
        ("Name the measurement gap",
         "State the single biggest gap between what Nimbus measured and what the Board needed "
         "to know. Usually: Nimbus measured what it did, while the Board wanted to know what "
         "changed."),
        ("Write three stage-specific recommendations",
         "One recommendation each for three different AMEC stages. Three variations of "
         "'measure more' is a failed audit — each must fix a structurally different problem, "
         "such as baselining before launch (Outcomes), instrumenting shelf-space and "
         "repeat-purchase (Impact), and reallocating spend (Inputs)."),
        ("Make it repeatable",
         "Specify when this audit runs after every future campaign, who owns it, and which "
         "template it uses — closing the loop with the documentation framework from "
         "Activity 7."),
    ],
    checklist=[
        "All four AMEC stages are defined and populated with real evidence from the arc.",
        "The weakest stage is named with evidence for why.",
        "The impressions/sentiment pattern is classified as Outputs success, Outcomes gap.",
        "The hesitant retail partner is placed at Impact.",
        "Three recommendations each fix a DIFFERENT stage.",
        "A repeatable cadence, owner and template are named.",
    ],
    tips=[
        "This is the capstone — encourage tables to pull evidence from earlier activities "
        "rather than treating it as standalone.",
        "Reject three recommendations that all amount to 'measure more'; that is the single "
        "most common failure here.",
    ]),
}
