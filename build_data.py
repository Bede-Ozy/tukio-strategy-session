import json

# Master Slide Dataset for Tukio Konsults Ltd - 2026 Strategy Session
# Strictly aligned with the Official Lesson Note Plan & Strategy Agenda
# Directives:
# 1. Before each discussion, clear "Things to Learn" for each sub-topic.
# 2. Discussion-oriented: talking points, reflection cards, and prominent questions on slides.
# 3. Pointers only, punchy and clear.
# 4. Clean structure with takeaways at bottom of slide canvas.
# 5. Zero fabricated stories or assumed company histories.

slides = [
    {
        "id": 1,
        "session": "Welcome",
        "sessionNum": 1,
        "category": "TUKIO KONSULTS LTD • 2026 STRATEGY SESSION",
        "title": "2026 STRATEGY SESSION",
        "subtitle": "No. 8, Suites 9-12, Along 62 Road, 6th Avenue, Gwarinpa, Abuja",
        "layout": "title-cover",
        "date": "30th September 2026",
        "venue": "Gwarinpa, Abuja",
        "facilitator": "Shamzbridge Consult Ltd",
        "host": "Tukio Konsults Ltd",
        "notes": "Welcome the team and set the tone for an open, interactive strategy discussion."
    },
    {
        "id": 2,
        "session": "Agenda",
        "sessionNum": 1,
        "category": "STRATEGY SESSION AGENDA",
        "title": "Today's Agenda & Flow",
        "subtitle": "Overview of Sessions, Leads & Timelines",
        "layout": "agenda-table",
        "schedule": [
            {"time": "8:00 – 8:30 AM", "session": "Arrival and Welcome Address", "lead": "Facilitator / Mrs. Fisayo Olabisi"},
            {"time": "8:30 – 9:00 AM", "session": "Session 1: Opening, Expectations & Team Energizer", "lead": "Facilitator-Led"},
            {"time": "9:00 – 10:00 AM", "session": "Session 2: The Tukio Journey: Our Past, Present and Future", "lead": "Group Workshop"},
            {"time": "10:00 – 10:40 AM", "session": "Session 3: Mentorship Session with Mr. Bankole", "lead": "Mr. Bankole"},
            {"time": "10:40 – 11:15 AM", "session": "Tea & Refreshments Break", "lead": "All"},
            {"time": "11:15 AM – 12:00 PM", "session": "Session 4: The Tukio Konsult Business Check", "lead": "Group Workshop"},
            {"time": "12:00 – 12:40 PM", "session": "Session 5: Ownership in Chaos", "lead": "Mr. Folarin"},
            {"time": "12:40 – 1:30 PM", "session": "Session 6: Closing Leads & Revenue Generation", "lead": "Ms Jumoke"},
            {"time": "1:30 – 2:30 PM", "session": "Lunch & Team Bonding Challenge", "lead": "Group Activity"},
            {"time": "2:30 – 3:30 PM", "session": "Session 7: Customer Retention and Experience Strategy", "lead": "Mr. Shams / Facilitator"},
            {"time": "3:30 – 4:15 PM", "session": "Session 8: Branding, Marketing & Tukio Visibility", "lead": "Group Workshop"},
            {"time": "4:15 – 4:30 PM", "session": "Afternoon Refreshment Break", "lead": "All"},
            {"time": "4:30 – 5:15 PM", "session": "Session 9: Revenue Expansion Beyond Event Planning", "lead": "Group Workshop"},
            {"time": "5:15 – 5:45 PM", "session": "Tukio Strategy War Room: From Ideas to Priorities", "lead": "Group Strategy"},
            {"time": "5:45 – 6:00 PM", "session": "Commitments, Next Steps & Closing", "lead": "Facilitator / Management"}
        ],
        "notes": "Walk through the agenda flow and set expectations for timekeeping and participation."
    },
    {
        "id": 3,
        "session": "Agenda",
        "sessionNum": 1,
        "category": "8:00 – 8:30 AM • ARRIVAL & WELCOME",
        "title": "Arrival & Welcome Address",
        "subtitle": "Lead: Facilitator / Mrs. Fisayo Olabisi",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-user-voice-line",
                "title": "Welcome Address",
                "thingsToLearn": "Strategic alignment begins with psychological safety and an active commitment to speak openly across all levels.",
                "question": "What is our shared mindset as we convene today?",
                "points": [
                    "Opening remarks by Mrs. Fisayo Olabisi",
                    "Welcome to participants, leadership & facilitators",
                    "Setting an atmosphere of candid, constructive dialogue"
                ]
            },
            {
                "icon": "ri-focus-3-line",
                "title": "Purpose of the Workshop",
                "thingsToLearn": "Strategy sessions are not routine meetings; they exist to diagnose reality and redefine our 5-year commercial trajectory.",
                "question": "What core outcomes must we achieve by 6:00 PM?",
                "points": [
                    "State the purpose and objectives of today's session",
                    "Align on what we hope to accomplish together as Tukio",
                    "Shift from routine operations into strategic architecture"
                ]
            },
            {
                "icon": "ri-compass-3-line",
                "title": "Session Ground Rules",
                "thingsToLearn": "Constructive friction drives breakthrough decisions—critique processes and systems rigorously while respecting every team member.",
                "question": "How will we ensure candid, constructive debate?",
                "points": [
                    "Active participation & open, honest contributions",
                    "Focus on practical solutions and forward execution",
                    "Respect diverse perspectives and speak without hierarchy"
                ]
            }
        ],
        "notes": "State the purpose and objectives of the strategy session."
    },
    {
        "id": 4,
        "session": "Energiser",
        "sessionNum": 2,
        "category": "8:30 – 9:00 AM • SESSION 1: OPENING & ENERGIZER",
        "title": "The Tukio Connection",
        "subtitle": "Group Activity: Participants pair up for 5 minutes",
        "layout": "energiser-activity",
        "thingsToLearn": "A team cannot build the Tukio of our dreams without acknowledging what we already do exceptionally well and aligning on bold 12-month goals.",
        "timerSeconds": 300,
        "prompts": [
            {
                "tag": "Question 1",
                "q": "What is one thing you believe Tukio does exceptionally well?",
                "sub": "Pair up: Each person introduces their partner and shares their response"
            },
            {
                "tag": "Question 2",
                "q": "What is one thing you want Tukio to achieve in the next 12 months?",
                "sub": "All participant responses captured live on the flipchart"
            },
            {
                "tag": "Mindset",
                "q": "Bringing All The Energy Into The Tukio of Our Dreams",
                "sub": "Full team alignment on high expectations, ownership & ambition"
            }
        ],
        "takeaway": "You want Tukio of our dreams; we must bring in all the energy.",
        "notes": "Participants pair up for 5 minutes. Question 1: Introduce partner and share response. Question 2: Capture responses on flipchart."
    },
    {
        "id": 5,
        "session": "The Journey",
        "sessionNum": 3,
        "category": "9:00 – 10:00 AM • SESSION 2: THE TUKIO JOURNEY",
        "title": "The Tukio Journey: What Worked, Improved & To Stop",
        "subtitle": "Objective: Understand where Tukio has come from and extract lessons from the journey",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-checkbox-circle-line",
                "title": "What Worked",
                "thingsToLearn": "Sustainable growth comes from codifying and scaling the winning practices that consistently produce client delight and repeat business.",
                "question": "What standout wins, winning approaches & client successes worked exceptionally well?",
                "points": [
                    "Major milestone event deliveries and client-delighting moments",
                    "Winning operational practices and distinctive team strengths",
                    "Core services that built Tukio's trusted market reputation",
                    "Approaches that consistently won client confidence and referrals"
                ]
            },
            {
                "icon": "ri-arrow-up-circle-line",
                "title": "What Can Be Improved",
                "thingsToLearn": "Operational friction in handoffs and communication erodes profitability—streamlining workflows creates team speed and execution consistency.",
                "question": "Where did we experience friction, and what operational workflows must be improved?",
                "points": [
                    "Internal communication speed and inter-departmental handoffs",
                    "Project planning coordination, vendor reliability & consistency",
                    "Client onboarding, systematic feedback collection & follow-ups",
                    "Standardization of delivery checklists and quality controls"
                ]
            },
            {
                "icon": "ri-close-circle-line",
                "title": "What to Stop",
                "thingsToLearn": "Deciding what to STOP is just as critical as deciding what to START—tolerating bad habits drains energy from strategic priorities.",
                "question": "What bottlenecks, redundant habits & ineffective practices must we completely stop?",
                "points": [
                    "Preventable operational mistakes and last-minute scrambles",
                    "Uncontrolled scope creep and unbilled client additions",
                    "Inefficient manual routines and uncoordinated workflows",
                    "Allowing client relationships to end when the invoice is paid"
                ]
            }
        ],
        "takeaway": "At Tukio Konsult, we are moving forward with the best part of our past.",
        "notes": "Facilitator-led activity: What brought about Tukio Konsult? Group discussion examining What Worked, What Can Be Improved, and What to Stop."
    },
    {
        "id": 6,
        "session": "The Journey",
        "sessionNum": 3,
        "category": "9:00 – 10:00 AM • SESSION 2: THE TUKIO JOURNEY",
        "title": "Moments in the Journey of Tukio Konsult",
        "subtitle": "Group Conversations: Let's share some moments in the journey of Tukio Konsult",
        "layout": "journey-points-8",
        "thingsToLearn": "Moving forward with the best part of our past requires confronting difficult moments and mistakes with total honesty to extract lasting wisdom.",
        "dimensions": [
            {"letter": "a", "label": "Major Milestones"},
            {"letter": "b", "label": "Major Achievements"},
            {"letter": "c", "label": "Difficult Moments"},
            {"letter": "d", "label": "Major Clients / Projects"},
            {"letter": "e", "label": "Turning Points"},
            {"letter": "f", "label": "Mistakes"},
            {"letter": "g", "label": "Lessons"},
            {"letter": "h", "label": "Opportunities"}
        ],
        "debriefQuestions": [
            "What are we most proud of?",
            "What almost didn't work?",
            "What did we learn?",
            "What would we do differently if we could start again?"
        ],
        "notes": "Open the floor for group reflection across each dimension. Anchor the conversation using the 4 debriefing questions."
    },
    {
        "id": 7,
        "session": "The Journey",
        "sessionNum": 3,
        "category": "9:00 – 10:00 AM • SESSION 2: THE TUKIO JOURNEY",
        "title": "START | STOP | CONTINUE",
        "subtitle": "For us to achieve our overall objectives in 5 Years, here are things we MUST:",
        "layout": "start-stop-continue-interactive",
        "thingsToLearn": "Achieving our 5-year targets demands ruthless focus: start high-leverage standards, stop time-wasting routines, and double down on core strengths.",
        "columns": [
            {
                "id": "start",
                "type": "start",
                "title": "START",
                "phase": "Phase 1 of 3",
                "timeSeconds": 300,
                "prompt": "What new systems, initiatives, habits & standards must Tukio begin?",
                "nextLabel": "Next: STOP ➔"
            },
            {
                "id": "stop",
                "type": "stop",
                "title": "STOP",
                "phase": "Phase 2 of 3",
                "timeSeconds": 300,
                "prompt": "What bottlenecks, gaps, ineffective practices & habits must Tukio stop?",
                "nextLabel": "Next: CONTINUE ➔"
            },
            {
                "id": "continue",
                "type": "continue",
                "title": "CONTINUE",
                "phase": "Phase 3 of 3",
                "timeSeconds": 300,
                "prompt": "What winning approaches, core strengths & values must Tukio scale?",
                "nextLabel": "Complete Discussion (Review All) ✓"
            }
        ],
        "takeaway": "Clarity on what to stop is just as critical as deciding what to start.",
        "notes": "Interactive START | STOP | CONTINUE card session. Each card has a round timer with play button and +/-1 minute adjusters."
    },
    {
        "id": 8,
        "session": "The Journey",
        "sessionNum": 3,
        "category": "9:00 – 10:00 AM • SESSION 2: THE TUKIO JOURNEY",
        "title": "Building Our Objectives Board",
        "subtitle": "Group Activity: Let's build our operational and strategic objectives board",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-dashboard-line",
                "title": "Operational Objectives",
                "thingsToLearn": "Operational excellence relies on documented checklists and predictable delivery standards, not individual memory or heroics.",
                "question": "What immediate operational standards and delivery workflows must we set?",
                "points": [
                    "Immediate service delivery standards and execution checklists",
                    "Day-to-day coordination protocols across planning teams",
                    "Response time benchmarks and rigorous quality controls"
                ]
            },
            {
                "icon": "ri-line-chart-line",
                "title": "Strategic Objectives",
                "thingsToLearn": "Strategic targets bridge daily event coordination with multi-year institutional expansion and commercial resilience.",
                "question": "What 5-year organizational growth and market milestones must we achieve?",
                "points": [
                    "5-Year market positioning and regional expansion targets",
                    "Institutional capability, technology adoption & team scaling",
                    "Financial sustainability and high-margin revenue diversification"
                ]
            },
            {
                "icon": "ri-check-double-line",
                "title": "Ownership & Tracking",
                "thingsToLearn": "An objective without a single named owner and a strict review cadence will never be executed.",
                "question": "Who owns each objective, and how will review cadence be structured?",
                "points": [
                    "Assigned departmental and individual ownership for every objective",
                    "Clear KPIs, milestone metrics, and execution timelines",
                    "Monthly tracking check-ins and quarterly executive reviews"
                ]
            }
        ],
        "takeaway": "At Tukio Konsult, we are moving forward with the best part of our past.",
        "notes": "Group Activity: Build the operational and strategic objectives board on the workshop wall/flipchart."
    },
    {
        "id": 9,
        "session": "Mentorship",
        "sessionNum": 4,
        "category": "10:00 – 10:40 AM • SESSION 3: MENTORSHIP",
        "title": "Mentorship Session with Mr. Bankole",
        "subtitle": "Objective: To have an overview of the business environment • Lead: Mr. Bankole",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-global-line",
                "title": "Business Environment Overview",
                "thingsToLearn": "Macroeconomic shifts and corporate budget constraints require event firms to operate with lean overhead and high commercial agility.",
                "question": "What macro economic shifts and business dynamics impact Tukio today?",
                "points": [
                    "Current macroeconomic climate and market realities",
                    "Corporate budget dynamics and client decision-making trends",
                    "Navigating business volatility and rising event production costs"
                ]
            },
            {
                "icon": "ri-building-line",
                "title": "Institutional Systems & Scaling",
                "thingsToLearn": "To scale beyond the founder's personal capacity, Tukio must embed systems, governance, and delegated authority.",
                "question": "How do we transition from founder-dependent operations to sustainable systems?",
                "points": [
                    "Building resilient governance, operating structure & processes",
                    "Sustaining delivery quality across multiple concurrent client accounts",
                    "Fostering leadership discipline, team culture, and accountability"
                ]
            },
            {
                "icon": "ri-question-answer-line",
                "title": "Post-Mentorship Plenary",
                "thingsToLearn": "Mentorship produces real value only when insights are translated into concrete operational habits within our business.",
                "question": "What critical lessons are we implementing directly into Tukio Konsult?",
                "points": [
                    "a. What did we learn from Mr. Bankole's perspective?",
                    "b. What part of the discussion are we implementing in Tukio Konsult business?",
                    "Immediate strategic takeaways for executive leadership"
                ]
            }
        ],
        "takeaway": "Building institutional capacity is the only path to sustainable scaling.",
        "notes": "Hand over to Mr. Bankole for his mentorship session, followed by the plenary discussion."
    },
    {
        "id": 10,
        "session": "Break",
        "sessionNum": 5,
        "category": "10:40 – 11:15 AM • BREAK",
        "title": "Tea & Refreshments Break",
        "subtitle": "Time to recharge and engage in informal team conversations",
        "layout": "break-card",
        "duration": "10:40 – 11:15 AM (35 Minutes)",
        "nextSession": "Up Next: Session 4: The Tukio Konsult Business Check (11:15 AM)",
        "notes": "Ensure participants refresh and resume on time at 11:15 AM."
    },
    {
        "id": 11,
        "session": "Health Check",
        "sessionNum": 6,
        "category": "11:15 AM – 12:00 PM • SESSION 4: BUSINESS HEALTH CHECK",
        "title": "The Tukio Konsult Business Check",
        "subtitle": "Objective: Identify business principles, diagnose practice & open future opportunities",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-settings-4-line",
                "title": "Operations & Delivery",
                "thingsToLearn": "Operational health means zero surprises on event day—achieved through standardized vendor management and rigorous pre-event run-sheets.",
                "question": "What is healthy, what is unhealthy, and what is the underlying problem in Operations?",
                "points": [
                    "Event execution workflows and vendor coordination systems",
                    "On-ground delivery consistency and execution capacity",
                    "What must be done to make Operations work seamlessly?"
                ]
            },
            {
                "icon": "ri-customer-service-2-line",
                "title": "Sales, Marketing & CX",
                "thingsToLearn": "Sales and customer experience are intertwined: how we sell sets expectations, and how we deliver determines repeat revenue.",
                "question": "What is healthy, what is unhealthy, and what is the underlying problem in Sales & CX?",
                "points": [
                    "Client pipeline, conversion rates & lead management",
                    "Customer experience across the entire booking cycle",
                    "What must be done to make Sales & CX work seamlessly?"
                ]
            },
            {
                "icon": "ri-bank-card-line",
                "title": "Finance and Administration",
                "thingsToLearn": "Cash flow is the lifeblood of consulting: prompt milestone invoicing and cost discipline protect business sustainability.",
                "question": "What is healthy, what is unhealthy, and what is the underlying problem in Finance & Admin?",
                "points": [
                    "Invoicing promptness, cash flow discipline & cost control",
                    "Administrative support, team coordination & documentation",
                    "What must be done to make Finance & Admin work seamlessly?"
                ]
            }
        ],
        "takeaway": "An honest diagnosis of our departments is the first step toward organizational health.",
        "notes": "Introductory note: Tukio has existed for over a decade. Plenary discussion on the 4 core departments."
    },
    {
        "id": 12,
        "session": "Health Check",
        "sessionNum": 6,
        "category": "11:15 AM – 12:00 PM • SESSION 4: BUSINESS HEALTH CHECK",
        "title": "Tukio SWOT Analysis",
        "subtitle": "Group Activity: Let's Discuss TUKIO's SWOT (Turn SWOT into Decisions)",
        "layout": "swot-board-interactive",
        "thingsToLearn": "SWOT is not four boxes of sticky notes—it becomes valuable only when turned into decisions: leverage S, fix W, pursue O, and prepare for T.",
        "columns": [
            {
                "id": "strengths",
                "type": "strengths",
                "title": "STRENGTHS",
                "phase": "Phase 1 of 4",
                "timeSeconds": 300,
                "prompt": "Internal things Tukio does well • Decision: S ➔ What strengths can we leverage?",
                "nextLabel": "Next: WEAKNESSES ➔"
            },
            {
                "id": "weaknesses",
                "type": "weaknesses",
                "title": "WEAKNESSES",
                "phase": "Phase 2 of 4",
                "timeSeconds": 300,
                "prompt": "Internal limitations • Decision: W ➔ What weaknesses must we fix?",
                "nextLabel": "Next: OPPORTUNITIES ➔"
            },
            {
                "id": "opportunities",
                "type": "opportunities",
                "title": "OPPORTUNITIES",
                "phase": "Phase 3 of 4",
                "timeSeconds": 300,
                "prompt": "External conditions Tukio can take advantage of • Decision: O ➔ Which opportunities should we pursue?",
                "nextLabel": "Next: THREATS ➔"
            },
            {
                "id": "threats",
                "type": "threats",
                "title": "THREATS",
                "phase": "Phase 4 of 4",
                "timeSeconds": 300,
                "prompt": "External factors that could negatively affect the business • Decision: T ➔ Which threats must we prepare for?",
                "nextLabel": "Complete SWOT Discussion (Review All) ✓"
            }
        ],
        "takeaway": "SWOT becomes useful only when we turn it into decisions.",
        "notes": "Interactive SWOT Analysis. Each quadrant card has a round timer with play button and +/-1 minute adjusters."
    },
    {
        "id": 13,
        "session": "Health Check",
        "sessionNum": 6,
        "category": "11:15 AM – 12:00 PM • SESSION 4: BUSINESS HEALTH CHECK",
        "title": "Tukio 5 Strategy Issues Outlines",
        "subtitle": "Plenary Discussion: Prioritizing Critical Strategy Focus Areas & Referrals",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-user-shared-line",
                "title": "Corporate Client Referrals",
                "thingsToLearn": "The most cost-effective business development channel is warm referrals from existing corporate clients who trust our execution.",
                "question": "How do we use existing relationships to generate corporate client referrals?",
                "points": [
                    "Systematic post-event referral requests to corporate decision-makers",
                    "Incentivizing corporate client champions and partners",
                    "Leveraging board, leadership, and alumni networks for introductions"
                ]
            },
            {
                "icon": "ri-list-ordered",
                "title": "The Top 5 Strategic Issues",
                "thingsToLearn": "Focus requires sacrifice: identifying the five vital strategic issues forces the leadership team to prioritize what truly moves the needle.",
                "question": "\"If we can only address FIVE things from everything identified today, what should they be?\"",
                "points": [
                    "Synthesizing department health checks and SWOT decisions",
                    "Debating the 5 non-negotiable issues that govern our future",
                    "Aligning the full leadership team behind these core priorities"
                ]
            },
            {
                "icon": "ri-target-line",
                "title": "Strategic Focus & Alignment",
                "thingsToLearn": "Every strategic priority must directly improve customer delight, streamline operations, or accelerate commercial revenue.",
                "question": "What measurable impact will addressing these 5 issues unlock by 2027?",
                "points": [
                    "Immediate reduction of internal operational friction",
                    "Direct revenue acceleration and improved profitability",
                    "Strengthened client retention and corporate market share"
                ]
            }
        ],
        "takeaway": "If you have more than five priorities, you have no priorities.",
        "notes": "Plenary discussion focusing on corporate referrals and selecting the top 5 strategic issues."
    },
    {
        "id": 14,
        "session": "Ownership",
        "sessionNum": 7,
        "category": "12:00 – 12:40 PM • SESSION 5: OWNERSHIP IN CHAOS",
        "title": "Ownership in Chaos",
        "subtitle": "Facilitator: Mr Folarin • Willingness to take responsibility for outcomes in difficulty",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-alarm-warning-line",
                "title": "When Things Go Wrong",
                "thingsToLearn": "Under extreme event pressure, human instincts often default to panic or blame—recognizing this reaction is the first step to leadership control.",
                "question": "\"When things go wrong at Tukio, what usually happens?\"",
                "points": [
                    "Examining typical team reactions during high-pressure disruptions",
                    "Identifying tendencies toward panic, excuses, or shifting blame",
                    "Acknowledging how reaction patterns impact client confidence"
                ]
            },
            {
                "icon": "ri-shield-check-line",
                "title": "What Should Happen Instead",
                "thingsToLearn": "High-performing teams de-escalate crises through calm containment, rapid problem-solving, and clear client-facing reassurance.",
                "question": "\"What should happen instead when high-stress disruptions occur?\"",
                "points": [
                    "Immediate composure, containment, and clear team communication",
                    "Proactive ground ownership without waiting to be told what to do",
                    "Rapid collaborative problem-solving aimed at client delight"
                ]
            },
            {
                "icon": "ri-heart-pulse-line",
                "title": "The True Meaning of Ownership",
                "thingsToLearn": "Ownership is not taking blame for everything—it is taking 100% responsibility for everything within your circle of influence.",
                "question": "How do we cultivate extreme ownership across every Tukio project?",
                "points": [
                    "Ownership is not taking blame for everything",
                    "It is taking responsibility for what you can influence",
                    "Debriefing honestly after crises to build permanent safeguards"
                ]
            }
        ],
        "takeaway": "Ownership is not taking blame for everything. It is taking responsibility for what you can influence.",
        "notes": "Session led by Mr. Folarin. Post-session plenary discussion on ownership when things go wrong."
    },
    {
        "id": 15,
        "session": "Revenue",
        "sessionNum": 8,
        "category": "12:40 – 1:30 PM • SESSION 6: CLOSING LEADS & REVENUE",
        "title": "Closing Leads & Revenue Generation",
        "subtitle": "Facilitator: Ms Jumoke • Moving prospects from interest to commitment and payment",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-file-search-line",
                "title": "Reflections & Obstacles",
                "thingsToLearn": "Deals stall when clients sense uncertainty or perceive price without understanding the value and risk mitigation Tukio provides.",
                "question": "\"What stood out for you, and what challenges have you experienced before this session?\"",
                "points": [
                    "Where prospective client deals currently stall or drop off",
                    "Handling client price sensitivity and budget hesitation",
                    "Overcoming long corporate decision-making delays"
                ]
            },
            {
                "icon": "ri-funds-line",
                "title": "What Success Looks Like",
                "thingsToLearn": "Sales success is not merely getting inquiries—it is qualifying serious buyers, shortening the sales cycle, and securing prompt payment.",
                "question": "\"What does success look like, and what strategies recommend more revenue?\"",
                "points": [
                    "High conversion rate from initial inquiry to signed contract",
                    "Shorter sales cycles and prompt milestone payments",
                    "Converting one-off events into recurring retainer relationships"
                ]
            },
            {
                "icon": "ri-stethoscope-line",
                "title": "Diagnose Before You Prescribe",
                "thingsToLearn": "A good salesperson doesn't rush to present a solution; they diagnose before they prescribe to uncover the client's true priorities.",
                "question": "How do we deeply diagnose client pain points before presenting a solution?",
                "points": [
                    "A good salesperson doesn't rush to present a solution",
                    "Ask probing diagnostic questions to uncover true client priorities",
                    "Position Tukio's proposal as the exact cure, not a generic service"
                ]
            }
        ],
        "takeaway": "A good salesperson doesn't rush to present a solution. They diagnose before they prescribe.",
        "notes": "Session led by Ms Jumoke. Post-session plenary exploring challenges, success metrics, and consultative selling."
    },
    {
        "id": 16,
        "session": "Revenue",
        "sessionNum": 8,
        "category": "12:40 – 1:30 PM • SESSION 6: CLOSING LEADS & REVENUE",
        "title": "The Closing Room",
        "subtitle": "Group Activity: Divide into pairs • One person is Tukio, the other is Client • 5-Minute Challenge",
        "layout": "closing-room-activity",
        "thingsToLearn": "Objections are requests for clarity and value demonstration—never drop price without adjusting scope or terms.",
        "timerSeconds": 300,
        "clients": [
            {
                "id": "A",
                "name": "Client A",
                "objection": "Loves Tukio's proposal but says the price is too high."
            },
            {
                "id": "B",
                "name": "Client B",
                "objection": "Says, \"Let me discuss it with my team.\""
            },
            {
                "id": "C",
                "name": "Client C",
                "objection": "Received proposals from three event planners and is comparing prices."
            },
            {
                "id": "D",
                "name": "Client D",
                "objection": "Wants a discount before committing."
            }
        ],
        "challengeSteps": [
            "1. Understand the client's concern",
            "2. Demonstrate value",
            "3. Handle the objection",
            "4. Attempt to close the deal"
        ],
        "debrief": "What worked? What can be improved?",
        "takeaway": "A good salesperson doesn't rush to present a solution. They diagnose before they prescribe.",
        "notes": "Divide participants into pairs. Assign Client A, B, C, or D. 5 minutes to roleplay. Debrief on what worked."
    },
    {
        "id": 17,
        "session": "Lunch",
        "sessionNum": 9,
        "category": "1:30 – 2:30 PM • LUNCH & TEAM BONDING",
        "title": "Lunch & Team Bonding Challenge",
        "subtitle": "Group Activity: Refresh, connect, and bond as a team",
        "layout": "break-card",
        "duration": "1:30 – 2:30 PM (60 Minutes)",
        "nextSession": "Up Next: Session 7: Customer Retention and Experience Strategy (2:30 PM)",
        "notes": "Facilitate lunch and the team bonding challenge activity."
    },
    {
        "id": 18,
        "session": "Retention",
        "sessionNum": 10,
        "category": "2:30 – 3:30 PM • SESSION 7: CUSTOMER RETENTION & CX",
        "title": "Customer Experience is the Whole Journey",
        "subtitle": "Objective: Understand how organization behaviour, operations & activities affect customers",
        "layout": "customer-journey-walk",
        "thingsToLearn": "Customer experience spans all 7 touchpoints from discovery to post-event follow-up—every touchpoint speaks volumes about Tukio.",
        "introNote": "Getting a customer is one achievement; getting customers to: a. Return, b. Recommend Tukio, c. Trust Tukio for Bigger Jobs is another level of business success.",
        "stages": [
            {"num": 1, "name": "Discovery"},
            {"num": 2, "name": "Enquiry"},
            {"num": 3, "name": "Booking"},
            {"num": 4, "name": "Planning"},
            {"num": 5, "name": "Event"},
            {"num": 6, "name": "Post-Event"},
            {"num": 7, "name": "Follow-Up"}
        ],
        "walkQuestions": [
            {"tag": "Action", "q": "What is happening at this stage?"},
            {"tag": "Mindset", "q": "What am I thinking? (Thought)"},
            {"tag": "Emotion", "q": "What am I feeling?"},
            {"tag": "Needs", "q": "What do I need?"},
            {"tag": "Friction", "q": "What could frustrate me?"},
            {"tag": "Advocacy", "q": "What could make me recommend Tukio?"}
        ],
        "takeaway": "A customer doesn't experience only the event — every touchpoint communicates something about Tukio.",
        "notes": "Group Activity: 'The Walk In My Shoes' game. Map each stage of the customer journey."
    },
    {
        "id": 19,
        "session": "Retention",
        "sessionNum": 10,
        "category": "2:30 – 3:30 PM • SESSION 7: CUSTOMER RETENTION & CX",
        "title": "9 Customer Retention Strategies",
        "subtitle": "Turning Client Satisfaction into Repeat Business & Lifetime Advocacy",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-compass-discover-line",
                "title": "Experience Debrief",
                "thingsToLearn": "Customer churn occurs where friction goes unnoticed; retention happens when deliberate moments of delight exceed expectations.",
                "question": "\"Where are we currently creating friction, and where are we creating delight?\"",
                "points": [
                    "Identify touchpoints where clients experience anxiety or delays",
                    "Identify signature moments of unexpected client delight",
                    "What three things could make customers come back consistently?"
                ]
            },
            {
                "icon": "ri-user-heart-line",
                "title": "Retention Strategies (1 to 5)",
                "thingsToLearn": "The first 72 hours after an event determine whether a client becomes a repeat partner or forgets the relationship.",
                "question": "How do we maintain active relationships immediately after events?",
                "points": [
                    "1. Follow up immediately after events",
                    "2. Ask for structured, actionable feedback",
                    "3. Send personalized appreciation messages",
                    "4. Maintain an up-to-date customer database",
                    "5. Share relevant opportunities and industry insights"
                ]
            },
            {
                "icon": "ri-repeat-2-line",
                "title": "Retention Strategies (6 to 9)",
                "thingsToLearn": "Don't let the relationship end when the invoice is paid—formal referral mechanisms and ongoing corporate check-ins build recurring retainers.",
                "question": "How do we turn past clients into referring advocates and annual retainers?",
                "points": [
                    "6. Offer loyalty incentives where appropriate",
                    "7. Request testimonials and case study quotes",
                    "8. Create formal referral mechanisms & rewards",
                    "9. Maintain continuous corporate relationships"
                ]
            }
        ],
        "takeaway": "Don't let the relationship end when the invoice is paid.",
        "notes": "Facilitate debrief on friction vs delight, then walk through the 9 retention strategies."
    },
    {
        "id": 20,
        "session": "Branding",
        "sessionNum": 11,
        "category": "3:30 – 4:15 PM • SESSION 8: BRANDING & VISIBILITY",
        "title": "Branding, Marketing & Tukio Visibility",
        "subtitle": "Objective: Reshape the perception people have about Tukio Konsult's business",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-global-line",
                "title": "Brand Perception Plenary",
                "thingsToLearn": "Our brand is not our logo—it is the perception people have based on experiences. When brand promise matches delivery, authority scales.",
                "question": "\"What's your satisfaction rate with Tukio's Brand Identities (Website & Social Media)?\"",
                "points": [
                    "Our brand is not our logo — a logo is just an identity element",
                    "A brand is the perception people have based on experiences",
                    "When Tukio promises exceptional events, the reality must match",
                    "Examining what's working and what must change on digital channels"
                ]
            },
            {
                "icon": "ri-question-mark",
                "title": "\"Why Choose Tukio?\"",
                "thingsToLearn": "Corporate clients choose event partners who demonstrate proven competence, reduce risk, and understand their organizational objectives.",
                "question": "\"Imagine a client received proposals from 5 event companies. Why choose Tukio?\"",
                "points": [
                    "Who are we?",
                    "Who do we serve?",
                    "What makes us different from every other planner?",
                    "What do we promise?",
                    "Why should corporate clients trust us?"
                ]
            },
            {
                "icon": "ri-award-line",
                "title": "Crafting Our Value Proposition",
                "thingsToLearn": "A compelling value proposition answers who we serve, what unique outcome we guarantee, and why clients can trust us completely.",
                "question": "How do we craft a compelling Value Proposition to wrap our brand around?",
                "points": [
                    "Articulating our distinct value in 1-2 clear sentences",
                    "Eliminating the gap between brand promise and brand reality",
                    "Ensuring every team member embodies and delivers this promise"
                ]
            }
        ],
        "takeaway": "A brand is the perception people have about your business based on their experiences.",
        "notes": "Examine website and social media. Craft Tukio's Value Proposition through group activity."
    },
    {
        "id": 21,
        "session": "Branding",
        "sessionNum": 11,
        "category": "3:30 – 4:15 PM • SESSION 8: BRANDING & VISIBILITY",
        "title": "Marketing Channels & 90 Days to Visibility",
        "subtitle": "Getting the right message to the right people through the right channels at the right time",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-share-forward-line",
                "title": "Marketing Channels Review",
                "thingsToLearn": "Marketing is getting the right message to the right people through the right channels at the right time—focus on channels that generate revenue.",
                "question": "\"Which channels have generated the most revenue, and which do we strengthen, stop, or start?\"",
                "points": [
                    "Instagram, LinkedIn, WhatsApp & Targeted Email",
                    "Referrals, Strategic Partnerships & Executive Networking",
                    "Corporate relationships, Testimonials & Event content"
                ]
            },
            {
                "icon": "ri-calendar-event-line",
                "title": "\"90 Days to Visibility\"",
                "thingsToLearn": "Visibility compounds through structured consistency: combining authority content, targeted campaigns, and corporate partnerships.",
                "question": "Group Activity: \"You have 90 days to make Tukio significantly more visible.\"",
                "points": [
                    "Develop: 3 Content Ideas (demonstrating authority & mastery)",
                    "Develop: 2 Targeted Campaigns (lead acquisition)",
                    "Develop: 2 Strategic Corporate Partnerships",
                    "Develop: 1 Referral Generation System"
                ]
            },
            {
                "icon": "ri-video-line",
                "title": "Content That Converts",
                "thingsToLearn": "Content should demonstrate: What we know + What we've done + What customers say + What we can do.",
                "question": "How does our content prove our capability rather than just announce availability?",
                "points": [
                    "What we know (industry expertise & thought leadership)",
                    "What we've done (portfolio, behind-the-scenes & execution)",
                    "What customers say (testimonials & social proof)",
                    "What we can do (tailored capabilities for corporate clients)"
                ]
            }
        ],
        "takeaway": "Content should demonstrate: What we know + What we've done + What customers say + What we can do.",
        "notes": "Group Activity: 90 days to make Tukio visible. Formulate the 3 content ideas, 2 campaigns, 2 partnerships, 1 referral strategy."
    },
    {
        "id": 22,
        "session": "Break",
        "sessionNum": 12,
        "category": "4:15 – 4:30 PM • BREAK",
        "title": "Afternoon Refreshment Break",
        "subtitle": "Quick 15-minute recharge before final revenue expansion & war room",
        "layout": "break-card",
        "duration": "4:15 – 4:30 PM (15 Minutes)",
        "nextSession": "Up Next: Session 9: Revenue Expansion Beyond Event Planning (4:30 PM)",
        "notes": "Brief break to stretch and prepare for Revenue Expansion."
    },
    {
        "id": 23,
        "session": "Expansion",
        "sessionNum": 13,
        "category": "4:30 – 5:15 PM • SESSION 9: REVENUE EXPANSION",
        "title": "Revenue Expansion Beyond Event Planning",
        "subtitle": "Objective: Unpack various revenue streams of Tukio Konsult as a business",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-group-line",
                "title": "Our Customer Base",
                "thingsToLearn": "It costs 5x less to create more value for existing clients than to acquire new ones—mine existing relationships for untapped needs.",
                "question": "\"Who are our customers, and what are we currently doing to keep them?\"",
                "points": [
                    "Profiling existing corporate vs private event clients",
                    "Reviewing repeat purchase frequency and lifetime value",
                    "Identifying unserved needs within current client organizations"
                ]
            },
            {
                "icon": "ri-hand-coin-line",
                "title": "5 Ways to Generate Revenue",
                "thingsToLearn": "Revenue expands across 5 paths: more customers, more frequent purchases, higher value per transaction, new services, and new markets.",
                "question": "Which of the 5 growth paths are we looking to pursue to increase revenue, and how?",
                "points": [
                    "a. More Customers (Acquire new corporate & institutional clients)",
                    "b. More Frequent Purchases (Get clients to use Tukio across all events)",
                    "c. Higher Value per Customer (Add specialized consulting & production)",
                    "d. New Products/Services (Create additional recurring revenue streams)",
                    "e. New Markets (Serve new geographical or sector segments)"
                ]
            },
            {
                "icon": "ri-lightbulb-flash-line",
                "title": "Value Creation Mindset",
                "thingsToLearn": "Growth is our ability to create more value for the customers we already have by packaging advisory and retainer offerings.",
                "question": "How do we transition from transactional event gigs to ongoing value creation?",
                "points": [
                    "Growth isn't just our ability to get more customers",
                    "It is our ability to create more value for customers we already have",
                    "Packaging end-to-end event strategy, advisory & management retainers"
                ]
            }
        ],
        "takeaway": "Growth isn't our ability to get more customers; it's our ability to create more value for the customers we already have.",
        "notes": "Plenary discussion exploring the 5 ways to generate revenue at Tukio."
    },
    {
        "id": 24,
        "session": "Expansion",
        "sessionNum": 13,
        "category": "4:30 – 5:15 PM • SESSION 9: REVENUE EXPANSION",
        "title": "The TUKIO Money Tree",
        "subtitle": "Group Activity: \"What else can Tukio sell?\" (Branches = Other Values We Offer)",
        "layout": "money-tree-activity",
        "thingsToLearn": "Before launching any new revenue branch, validate it against the 4 litmus tests: active demand, operational competence, healthy profit margin, and low capital risk.",
        "coreQuestion": "What else can Tukio sell beyond event planning?",
        "branches": [
            {"icon": "ri-building-2-line", "title": "Corporate Event Strategy & Production", "desc": "End-to-end technical staging, AV, lighting & executive protocol"},
            {"icon": "ri-shield-star-line", "title": "Protocol & Concierge Advisory", "desc": "High-level VIP, diplomatic & executive protocol management"},
            {"icon": "ri-live-line", "title": "Event Tech & Hybrid Streaming", "desc": "Virtual broadcasting, hybrid attendee tech & digital registration"},
            {"icon": "ri-calendar-check-line", "title": "Annual Corporate Event Retainers", "desc": "Year-round event management retainers for corporate institutions"},
            {"icon": "ri-vip-crown-line", "title": "Proprietary Summits & Industry IP", "desc": "Owning annual conferences, ticketed masterclasses & industry summits"}
        ],
        "evaluationQuestions": [
            {"letter": "a", "q": "Is there demand? (Do clients actively want or need this?)"},
            {"letter": "b", "q": "Can we deliver it? (Do we have the operational competence?)"},
            {"letter": "c", "q": "Can we make money from it? (Is the profit margin healthy?)"},
            {"letter": "d", "q": "Can we start without a huge investment? (Low capital risk?)"}
        ],
        "debrief": "Solve more of the customer's problems, and money will come.",
        "takeaway": "Solve more of the customer's problems, and money will come.",
        "notes": "Group Activity: The TUKIO Money Tree. Debriefing: Solve more of the customer's problems, and money will come."
    },
    {
        "id": 25,
        "session": "War Room",
        "sessionNum": 14,
        "category": "5:15 – 5:45 PM • SESSION 9: STRATEGY WAR ROOM",
        "title": "Strategy War Room: Strategy is Where Ideas Become Choices",
        "subtitle": "Objective: Put all our deliberation together & subject every priority to the 5-point test",
        "layout": "priority-test-grid",
        "introNote": "By this stage, the team has discussed: Journey → SWOT → Ownership → Sales → Customer → Brand → Revenue. Now, \"What are the most important things we need to do next?\"",
        "thingsToLearn": "Strategy is where ideas become choices. For every strategy we will agree upon today, we must subject it to the 5-point Priority Test.",
        "tests": [
            {
                "name": "IMPACT",
                "question": "Will this significantly affect the business?",
                "desc": "Does it substantially increase revenue, elevate corporate market stature, or resolve a fundamental operational vulnerability?"
            },
            {
                "name": "URGENCY",
                "question": "Does it need attention now?",
                "desc": "Is this non-negotiable for immediate Q4 2026 / 2027 momentum, or is it a secondary initiative that can wait?"
            },
            {
                "name": "FEASIBILITY",
                "question": "Can we realistically execute it?",
                "desc": "Do we have the required manpower, technical capability, time bandwidth, and capital to deliver with excellence?"
            },
            {
                "name": "OWNERSHIP",
                "question": "Who will drive it?",
                "desc": "Is there a specific, accountable department champion who will take 100% personal responsibility for the outcome?"
            },
            {
                "name": "MEASUREMENT",
                "question": "How will we know it worked?",
                "desc": "What concrete metric, revenue number, or quantifiable KPI will prove whether the initiative succeeded?"
            }
        ],
        "takeaway": "Strategy is where ideas become choices.",
        "notes": "Introductory note & the 5 Priority Tests (Impact, Urgency, Feasibility, Ownership, Measurement)."
    },
    {
        "id": 26,
        "session": "War Room",
        "sessionNum": 14,
        "category": "5:15 – 5:45 PM • SESSION 9: STRATEGY WAR ROOM",
        "title": "Compiling Our Work: 5 Strategic Focus Areas",
        "subtitle": "Group Activity: Aligning our work across 5 Pillars & answering the 4 Core Strategic Questions",
        "layout": "compiling-strategy-grid",
        "thingsToLearn": "A complete corporate strategy unifies all 5 pillars. For each pillar, the leadership team must answer the 4 foundational questions.",
        "pillars": [
            {"letter": "a", "title": "Sales & Business Development", "desc": "Closing high-value corporate deals, pipeline management, consultative pitching"},
            {"letter": "b", "title": "Customer Experience & Retention", "desc": "7-touchpoint customer journey, post-event delight, lifetime referrals"},
            {"letter": "c", "title": "Brand & Marketing", "desc": "Distinct value proposition, 90-day visibility, authority content creation"},
            {"letter": "d", "title": "Revenue Expansion", "desc": "Money tree service branches, corporate retainers, advisory packages"},
            {"letter": "e", "title": "Team & Operations", "desc": "Ownership in chaos, standardized delivery checklists, vendor reliability"}
        ],
        "coreQuestions": [
            {"label": "Current State", "question": "Where are we?", "desc": "Honest diagnosis of our current operational standing & baseline."},
            {"label": "Target Vision", "question": "Where do we want to go?", "desc": "Specific milestones and commercial ambitions for 2026-2027."},
            {"label": "Action Plan", "question": "What must we do?", "desc": "Concrete tactical steps, required systems & process changes."},
            {"label": "Success Metrics", "question": "How will we measure success?", "desc": "Measurable KPIs, revenue benchmarks & client satisfaction scores."}
        ],
        "takeaway": "Where are we? Where do we want to go? What must we do? How will we measure success?",
        "notes": "Group Activity: Compile all deliberations across the 5 pillars and debate the 4 strategic questions."
    },
    {
        "id": 27,
        "session": "War Room",
        "sessionNum": 14,
        "category": "5:15 – 5:45 PM • SESSION 9: STRATEGY WAR ROOM",
        "title": "Tukio Strategic Planning Matrix",
        "subtitle": "From Ideas to Priorities: Populating the 10 Sections of the Master Execution Matrix",
        "layout": "matrix-framework",
        "thingsToLearn": "Priorities without assigned ownership, required resources, and measurable KPIs remain merely wishes.",
        "matrixHeaders": [
            {"title": "Vision Area", "desc": "Key organizational priority"},
            {"title": "Desired Outcome", "desc": "Specific result to achieve"},
            {"title": "Existing Efforts", "desc": "What has been done previously"},
            {"title": "Gaps to Eliminate", "desc": "Ineffective practices to discontinue"},
            {"title": "Areas to Improve", "desc": "Operations needing strengthening"},
            {"title": "Strategic Initiatives", "desc": "Practical strategies to execute"},
            {"title": "Required Resources", "desc": "Financial, human, and tech needs"},
            {"title": "Responsible Teams", "desc": "Assigned ownership and accountability"},
            {"title": "KPIs", "desc": "Measurable indicators of success"},
            {"title": "Key Action Steps", "desc": "Immediate follow-up activities"}
        ],
        "takeaway": "Priorities without ownership and resources are merely wishes.",
        "notes": "Group Strategy War Room: Convert today's deliberations into the 10 sections of the Strategic Planning Matrix."
    },
    {
        "id": 28,
        "session": "Closing",
        "sessionNum": 15,
        "category": "5:45 – 6:00 PM • COMMITMENTS & CLOSING",
        "title": "Commitments, Next Steps & Closing",
        "subtitle": "Lead: Facilitator-Led / Management",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-check-line",
                "title": "Team Commitments",
                "thingsToLearn": "Execution begins tomorrow morning: individual commitment to immediate priorities transforms strategic intent into operational reality.",
                "question": "\"What are our immediate agreed personal and departmental action commitments?\"",
                "points": [
                    "Personal and departmental action commitments for Q4 2026",
                    "Agreed immediate priorities starting first thing tomorrow morning",
                    "Clear leadership ownership for every strategic workstream"
                ]
            },
            {
                "icon": "ri-file-list-3-line",
                "title": "Documentation & Communique",
                "thingsToLearn": "Clear documentation within 48 hours locks in consensus and prevents strategic drift.",
                "question": "How will the session communique and implementation matrix be circulated?",
                "points": [
                    "Circulation of strategy session summary report within 48 hours",
                    "Master implementation timeline & responsibility matrix",
                    "Live action tracker shared across the management team"
                ]
            },
            {
                "icon": "ri-calendar-check-line",
                "title": "Follow-Up Cadence",
                "thingsToLearn": "Strategy is kept alive only through disciplined monthly milestones and quarterly leadership reviews.",
                "question": "What monthly and quarterly review cadence will keep this strategy alive?",
                "points": [
                    "Monthly review meetings to assess milestone execution",
                    "Quarterly and annual strategy evaluation sessions",
                    "Holding every team member accountable to committed outcomes"
                ]
            }
        ],
        "takeaway": "Strategy becomes reality only through disciplined execution and accountability.",
        "notes": "Final wrap-up, management closing remarks, and group photograph."
    }
]

code = '// Master Slide Dataset for Tukio Konsults Ltd - 2026 Strategy Session\n'
code += '// Strictly aligned with the Official Lesson Note Plan & Strategy Agenda\n'
code += '// Strict User Directives: Before each discussion, add things to learn about each sub-topic.\n'
code += '// Pure talking points, topics, cards, and prominent questions. Zero assumed narratives.\n\n'
code += 'const tukioStrategyData = ' + json.dumps(slides, indent=2) + ';\n\n'
code += 'if (typeof module !== "undefined") { module.exports = tukioStrategyData; }\n'

with open('js/slidesData.js', 'w', encoding='utf-8') as f:
    f.write(code)

print('js/slidesData.js successfully generated with', len(slides), 'slides.')
