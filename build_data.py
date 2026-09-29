import json

# Master Slide Dataset for Tukio Konsults Ltd - 2026 Strategy Session
# Strictly aligned with "Tukio Konsult Strategy Session Agenda.pdf"
# Directives:
# 1. Pure talking points and discussion questions for the presenter to lead debate.
# 2. Zero assumed narratives or fabricated company stories.
# 3. Present talking points as topics, cards, or table headers.
# 4. Only takeaways appear as extra footer content at the bottom of the slide canvas.

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
            {"time": "8:30 – 9:00 AM", "session": "Opening, Expectations & Team Energiser", "lead": "Facilitator"},
            {"time": "9:00 – 10:00 AM", "session": "The Tukio Journey: Where We Are Coming From & Where We Are Going", "lead": "Group Workshop"},
            {"time": "10:00 – 10:40 AM", "session": "Mentorship Session with Mr. Bankole", "lead": "Mr. Bankole"},
            {"time": "10:40 – 11:15 AM", "session": "Break", "lead": "All"},
            {"time": "11:15 AM – 12:00 PM", "session": "Business Health Check: Where Are We Now?", "lead": "Group Workshop"},
            {"time": "12:00 – 12:40 PM", "session": "Ownership in Chaos", "lead": "Mr. Folarin"},
            {"time": "12:40 – 1:30 PM", "session": "Closing Leaders and Revenue Generation", "lead": "Ms Jumoke"},
            {"time": "1:30 – 2:30 PM", "session": "Lunch & Team Bonding Challenge", "lead": "Group Activity"},
            {"time": "2:30 – 3:30 PM", "session": "Customer Retention & Customer Experience", "lead": "Facilitator-Led / Group Workshop"},
            {"time": "3:30 – 4:15 PM", "session": "Branding, Marketing & Visibility", "lead": "Facilitator-Led / Group Workshop"},
            {"time": "4:15 – 4:30 PM", "session": "Break", "lead": "All"},
            {"time": "4:30 – 5:15 PM", "session": "Revenue Expansion: Beyond Event Planning", "lead": "Facilitator-Led / Group Workshop"},
            {"time": "5:15 – 5:45 PM", "session": "Tukio Strategy War Room: From Ideas to Priorities", "lead": "Group Strategy"},
            {"time": "5:45 – 6:00 PM", "session": "Commitments, Next Steps & Closing", "lead": "Facilitator-Led / Management"}
        ],
        "notes": "Walk through the agenda flow and set expectations for timekeeping."
    },
    {
        "id": 3,
        "session": "Arrival",
        "sessionNum": 1,
        "category": "8:00 – 8:30 AM • ARRIVAL & WELCOME",
        "title": "Arrival & Welcome Address",
        "subtitle": "Lead: Facilitator / Mrs. Fisayo Olabisi",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-user-voice-line",
                "title": "Welcome Address",
                "question": "What is our shared mindset as we convene today?",
                "points": [
                    "Opening remarks by Mrs. Fisayo Olabisi",
                    "Welcome to participants and leadership team"
                ]
            },
            {
                "icon": "ri-focus-3-line",
                "title": "Purpose of the Workshop",
                "question": "What core outcomes must we achieve by 6:00 PM?",
                "points": [
                    "State the purpose and objectives of today's session",
                    "What we hope to accomplish together as an organization"
                ]
            },
            {
                "icon": "ri-compass-3-line",
                "title": "Session Ground Rules",
                "question": "How will we ensure candid, constructive debate?",
                "points": [
                    "Active participation & open dialogue",
                    "Focus on practical solutions and forward planning"
                ]
            }
        ],
        "notes": "State the purpose and objectives of the strategy session."
    },
    {
        "id": 4,
        "session": "Energiser",
        "sessionNum": 2,
        "category": "8:30 – 9:00 AM • OPENING, EXPECTATIONS & ENERGISER",
        "title": "The Tukio Connection",
        "subtitle": "Group Activity: Participants pair up for 5 minutes",
        "layout": "energiser-activity",
        "timerSeconds": 300,
        "prompts": [
            {
                "tag": "Question 1",
                "q": "What is one thing you believe Tukio does exceptionally well?",
                "sub": "Introduce your partner and share their response"
            },
            {
                "tag": "Question 2",
                "q": "What is one thing you want Tukio to achieve in the next 12 months?",
                "sub": "Responses to be captured on the flipchart"
            },
            {
                "tag": "Icebreaker",
                "q": "If you were an animal in business, what would you be and why?",
                "sub": "Brief introduction and reflection"
            }
        ],
        "takeaway": "You want Tukio of our dreams; we must bring in all the energy.",
        "notes": "Pair up participants for 5 minutes. Capture responses on the flipchart."
    },
    {
        "id": 5,
        "session": "The Journey",
        "sessionNum": 3,
        "category": "9:00 – 10:00 AM • THE TUKIO JOURNEY",
        "title": "The Tukio Journey: Where We Are Coming From & Where We Are Going",
        "subtitle": "Group Workshop • Lead: Facilitator / All",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-history-line",
                "title": "Where We Are Coming From",
                "question": "What brought about Tukio Konsult, and what was the original vision?",
                "points": [
                    "Original vision and founding motivation",
                    "Early milestones and foundational experiences",
                    "Evolution of the business over time"
                ]
            },
            {
                "icon": "ri-radar-line",
                "title": "Where We Are Today",
                "question": "What has worked well so far, and what could be improved across operations?",
                "points": [
                    "Current operational standing & reality",
                    "What has worked exceptionally well",
                    "Areas where execution could be sharpened"
                ]
            },
            {
                "icon": "ri-flight-takeoff-line",
                "title": "Where We Are Going",
                "question": "What is our 5-year outlook, and what high-level milestones must we achieve?",
                "points": [
                    "5-Year growth outlook & future vision",
                    "Strategic ambitions and key milestones",
                    "Setting the direction for long-term impact"
                ]
            }
        ],
        "takeaway": "Understanding our journey is the foundation for defining our future.",
        "notes": "Facilitator-led workshop exploring the journey so far, current reality, and long-term vision."
    },
    {
        "id": 6,
        "session": "The Journey",
        "sessionNum": 3,
        "category": "9:00 – 10:00 AM • THE TUKIO JOURNEY",
        "title": "Moments in the Journey of Tukio Konsult",
        "subtitle": "Group Conversations: Reflections across 8 key dimensions",
        "layout": "journey-points-8",
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
        "notes": "Open the floor for group reflection across each of the 8 moments from the journey."
    },
    {
        "id": 7,
        "session": "The Journey",
        "sessionNum": 3,
        "category": "9:00 – 10:00 AM • THE TUKIO JOURNEY",
        "title": "START | STOP | CONTINUE",
        "subtitle": "For us to achieve our overall objectives in 5 Years time, here are things we MUST:",
        "layout": "start-stop-continue-interactive",
        "columns": [
            {
                "id": "start",
                "type": "start",
                "title": "START",
                "phase": "Phase 1 of 3",
                "timeSeconds": 300,
                "prompt": "What new processes, service standards, or initiatives must Tukio start?",
                "nextLabel": "Next: STOP ➔"
            },
            {
                "id": "stop",
                "type": "stop",
                "title": "STOP",
                "phase": "Phase 2 of 3",
                "timeSeconds": 300,
                "prompt": "What bottlenecks, redundant habits, or ineffective practices must Tukio stop?",
                "nextLabel": "Next: CONTINUE ➔"
            },
            {
                "id": "continue",
                "type": "continue",
                "title": "CONTINUE",
                "phase": "Phase 3 of 3",
                "timeSeconds": 300,
                "prompt": "What winning approaches, customer strengths, and values must Tukio scale?",
                "nextLabel": "Complete Discussion (Review All) ✓"
            }
        ],
        "takeaway": "Clarity on what to stop is just as critical as deciding what to start.",
        "notes": "Interactive START | STOP | CONTINUE card session. Each card has a round timer with play button and +/-1 minute adjusters. Presenter clicks 'Next Plan' to advance the discussion."
    },
    {
        "id": 8,
        "session": "The Journey",
        "sessionNum": 3,
        "category": "9:00 – 10:00 AM • THE TUKIO JOURNEY",
        "title": "Building Our Objectives Board",
        "subtitle": "Group Activity: Let's build our operational and strategic objectives board",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-dashboard-line",
                "title": "Operational Objectives Board",
                "question": "What immediate workflow improvements and delivery standards must we set?",
                "points": [
                    "Immediate workflow improvements",
                    "Service delivery and execution standards",
                    "Day-to-day team responsibilities & coordination"
                ]
            },
            {
                "icon": "ri-line-chart-line",
                "title": "Strategic Objectives Board",
                "question": "What are our 5-year organizational growth and market expansion targets?",
                "points": [
                    "5-Year growth and organizational targets",
                    "Milestones for business expansion & sustainability",
                    "Long-term value creation"
                ]
            },
            {
                "icon": "ri-check-double-line",
                "title": "Accountability & Alignment",
                "question": "Who owns each objective, and how will tracking and review be structured?",
                "points": [
                    "Assigned ownership for every objective",
                    "Tracking mechanisms, KPIs, and review cadence",
                    "Clear execution timelines"
                ]
            }
        ],
        "notes": "Group Activity: Facilitate the construction of the operational and strategic objectives board."
    },
    {
        "id": 9,
        "session": "Mentorship",
        "sessionNum": 4,
        "category": "10:00 – 10:40 AM • MENTORSHIP SESSION",
        "title": "Mentorship Session with Mr. Bankole",
        "subtitle": "Lead: Mr. Bankole",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-shield-user-line",
                "title": "Strategic Leadership & Governance",
                "question": "What leadership systems and institutional structures must we build now?",
                "points": [
                    "Building institutional capacity & structure",
                    "Leadership discipline and team accountability",
                    "Fostering organizational culture and excellence"
                ]
            },
            {
                "icon": "ri-lightbulb-line",
                "title": "Navigating Growth & Market Scaling",
                "question": "How do we manage operational complexity and sustain quality as we scale?",
                "points": [
                    "Managing complexity as the company expands",
                    "Strategic lessons from seasoned experience",
                    "Sustaining quality across multiple client accounts"
                ]
            },
            {
                "icon": "ri-question-answer-line",
                "title": "Interactive Discussion & Q&A",
                "question": "What critical questions do we need guidance on from seasoned experience?",
                "points": [
                    "Open floor questions with Mr. Bankole",
                    "Key takeaways and reflections for Tukio leadership"
                ]
            }
        ],
        "notes": "Hand over to Mr. Bankole for his mentorship session, followed by reflections."
    },
    {
        "id": 10,
        "session": "Break",
        "sessionNum": 5,
        "category": "10:40 – 11:15 AM • BREAK",
        "title": "Tea & Refreshments Break",
        "subtitle": "Time to recharge and engage in informal discussions",
        "layout": "break-card",
        "duration": "10:40 – 11:15 AM (35 Minutes)",
        "nextSession": "Up Next: Business Health Check: Where Are We Now?",
        "notes": "Ensure participants refresh and resume on time at 11:15 AM."
    },
    {
        "id": 11,
        "session": "Health Check",
        "sessionNum": 6,
        "category": "11:15 AM – 12:00 PM • BUSINESS HEALTH CHECK",
        "title": "Business Health Check: Where Are We Now?",
        "subtitle": "Group Workshop: Evaluating the company's current operational standing",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-pulse-line",
                "title": "Operational Health",
                "question": "How efficient and reliable are our current project delivery workflows?",
                "points": [
                    "Execution workflows and delivery capacity",
                    "Internal team coordination and efficiency",
                    "Standards, processes, and service consistency"
                ]
            },
            {
                "icon": "ri-bank-card-line",
                "title": "Financial Health",
                "question": "How resilient, diversified, and stable are our revenue streams and cash flow?",
                "points": [
                    "Revenue streams and cash flow stability",
                    "Cost management and profitability margins",
                    "Financial resilience and commercial sustainability"
                ]
            },
            {
                "icon": "ri-global-line",
                "title": "Brand & Digital Assets",
                "question": "What is the true outlook of our website, digital channels, and market reputation?",
                "points": [
                    "Outlook of the company website and digital portfolio",
                    "Public perception, reputation & marketing collateral",
                    "Market presence and client reach"
                ]
            }
        ],
        "takeaway": "An honest diagnosis is the first step toward organizational health.",
        "notes": "Group Workshop: Review current operational performance, resources, and company assets."
    },
    {
        "id": 12,
        "session": "Health Check",
        "sessionNum": 6,
        "category": "11:15 AM – 12:00 PM • BUSINESS HEALTH CHECK",
        "title": "Tukio SWOT Analysis",
        "subtitle": "Group Workshop: Identifying internal capabilities and external market dynamics",
        "layout": "swot-board-interactive",
        "columns": [
            {
                "id": "strengths",
                "type": "strengths",
                "title": "STRENGTHS",
                "phase": "Phase 1 of 4",
                "timeSeconds": 300,
                "prompt": "What are Tukio's core competitive strengths, unique delivery capabilities, and standout value drivers?",
                "nextLabel": "Next: WEAKNESSES ➔"
            },
            {
                "id": "weaknesses",
                "type": "weaknesses",
                "title": "WEAKNESSES",
                "phase": "Phase 2 of 4",
                "timeSeconds": 300,
                "prompt": "What internal operational bottlenecks, resource constraints, or process gaps hold us back?",
                "nextLabel": "Next: OPPORTUNITIES ➔"
            },
            {
                "id": "opportunities",
                "type": "opportunities",
                "title": "OPPORTUNITIES",
                "phase": "Phase 3 of 4",
                "timeSeconds": 300,
                "prompt": "What emerging market trends, high-margin event segments, and partnership opportunities should we capture?",
                "nextLabel": "Next: THREATS ➔"
            },
            {
                "id": "threats",
                "type": "threats",
                "title": "THREATS",
                "phase": "Phase 4 of 4",
                "timeSeconds": 300,
                "prompt": "What market risks, competitive pressures, vendor dependencies, and economic shifts must we mitigate?",
                "nextLabel": "Complete SWOT Discussion (Review All) ✓"
            }
        ],
        "takeaway": "Leverage our strengths, eliminate weaknesses, capture opportunities, mitigate threats.",
        "notes": "Interactive SWOT Analysis card session. Each quadrant card has a round discussion timer with play button and +/-1 minute adjusters. Facilitator advances through Strengths, Weaknesses, Opportunities, and Threats before reviewing all."
    },
    {
        "id": 13,
        "session": "Ownership",
        "sessionNum": 7,
        "category": "12:00 – 12:40 PM • OWNERSHIP IN CHAOS",
        "title": "Ownership in Chaos",
        "subtitle": "Lead: Mr. Folarin",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-fire-line",
                "title": "Leading Through Uncertainty",
                "question": "How do we maintain composure and decisive leadership during chaotic moments?",
                "points": [
                    "Navigating unexpected project and event challenges",
                    "Maintaining composure and clear direction under pressure",
                    "Decisive leadership during critical project moments"
                ]
            },
            {
                "icon": "ri-shield-check-line",
                "title": "Personal & Team Accountability",
                "question": "How do we cultivate individual and collective ownership without excuses or blame shifting?",
                "points": [
                    "Taking responsibility for outcomes without shifting blame",
                    "Proactive problem solving and ownership on the ground",
                    "Fostering trust and reliability within the team"
                ]
            },
            {
                "icon": "ri-tools-line",
                "title": "Creating Order From Chaos",
                "question": "What standard protocols and communication channels protect execution under pressure?",
                "points": [
                    "Standard operating protocols during high-stress situations",
                    "Building resilient communication and escalation channels",
                    "Debriefing and learning from operational disruptions"
                ]
            }
        ],
        "notes": "Session led by Mr. Folarin on ownership, leadership, and execution during chaotic situations."
    },
    {
        "id": 14,
        "session": "Revenue",
        "sessionNum": 8,
        "category": "12:40 – 1:30 PM • REVENUE GENERATION",
        "title": "Closing Leaders and Revenue Generation",
        "subtitle": "Lead: Ms Jumoke",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-funds-line",
                "title": "Revenue Generation Strategy",
                "question": "What high-value commercial revenue streams should Tukio actively pursue?",
                "points": [
                    "Identifying and qualifying high-value revenue streams",
                    "Building a proactive, structured commercial pipeline",
                    "Diversifying client acquisition channels"
                ]
            },
            {
                "icon": "ri-shake-hands-line",
                "title": "Closing Deals & Pitching",
                "question": "How do we refine our client pitch, negotiate value, and close high-stake deals?",
                "points": [
                    "Client proposal presentation and value articulation",
                    "Negotiation techniques and closing high-stake accounts",
                    "Overcoming objections and securing client commitment"
                ]
            },
            {
                "icon": "ri-team-line",
                "title": "Commercial Mindset in Leadership",
                "question": "How do we empower leaders across the team to drive business growth?",
                "points": [
                    "Empowering leaders across the team to drive commercial growth",
                    "Setting measurable revenue targets and accountability",
                    "Aligning delivery excellence with business growth"
                ]
            }
        ],
        "notes": "Session led by Ms Jumoke focusing on closing deals, commercial strategy, and revenue generation."
    },
    {
        "id": 15,
        "session": "Lunch",
        "sessionNum": 9,
        "category": "1:30 – 2:30 PM • LUNCH & TEAM BONDING",
        "title": "Lunch & Team Bonding Challenge",
        "subtitle": "Group Activity: Refresh, connect, and bond as a team",
        "layout": "break-card",
        "duration": "1:30 – 2:30 PM (60 Minutes)",
        "nextSession": "Up Next: Customer Retention & Customer Experience (2:30 PM)",
        "notes": "Facilitate lunch and the team bonding challenge activity."
    },
    {
        "id": 16,
        "session": "Retention",
        "sessionNum": 10,
        "category": "2:30 – 3:30 PM • CUSTOMER RETENTION & EXPERIENCE",
        "title": "Customer Retention & Customer Experience",
        "subtitle": "Facilitator-Led / Group Workshop (Facilitated by Mr Shams)",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-user-heart-line",
                "title": "The Customer Experience Journey",
                "question": "What are our critical client touchpoints before, during, and after engagements?",
                "points": [
                    "Key client touchpoints before, during, and after engagements",
                    "Setting and delivering exceptional service standards",
                    "Mapping client perceptions and satisfaction"
                ]
            },
            {
                "icon": "ri-repeat-line",
                "title": "Retention & Repeat Business",
                "question": "How do we systematically convert one-time event clients into recurring annual retainers?",
                "points": [
                    "Transforming one-off projects into long-term retainers",
                    "Client relationship stewardship and ongoing engagement",
                    "Creating structured post-project follow-up processes"
                ]
            },
            {
                "icon": "ri-service-line",
                "title": "Handling Difficult Scenarios",
                "question": "How do we manage difficult client expectations and crisis moments while preserving trust?",
                "points": [
                    "Crisis de-escalation and managing client expectations",
                    "Sustaining client trust through high delivery standards",
                    "Protecting brand reputation through rapid resolution"
                ]
            }
        ],
        "takeaway": "Client retention is the cornerstone of sustainable consulting growth.",
        "notes": "Session facilitated by Mr Shams on customer retention, relationship management, and service excellence."
    },
    {
        "id": 17,
        "session": "Branding",
        "sessionNum": 11,
        "category": "3:30 – 4:15 PM • BRANDING, MARKETING & VISIBILITY",
        "title": "Branding, Marketing & Visibility",
        "subtitle": "Facilitator-Led / Group Workshop: Positioning Tukio Konsult for Growth",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-megaphone-line",
                "title": "Event Marketing Strategy",
                "question": "What specific multi-channel promotional strategies will effectively market and sell out events?",
                "points": [
                    "How to market and sell out events effectively",
                    "Multi-channel promotional campaigns and sponsor outreach",
                    "Audience segmentation and ticket monetization strategies"
                ]
            },
            {
                "icon": "ri-layout-top-line",
                "title": "Digital Assets & Website",
                "question": "How should our website and digital portfolio be positioned for inbound lead generation?",
                "points": [
                    "Outlook of the company website and digital portfolio",
                    "Leveraging online channels for authority and inbound leads",
                    "Showcasing credibility, case studies, and brand narrative"
                ]
            },
            {
                "icon": "ri-broadcast-line",
                "title": "Public Relations & Brand Stature",
                "question": "What strategic PR and thought leadership moves will build our corporate stature?",
                "points": [
                    "Brand positioning across corporate and public sectors",
                    "Media visibility, thought leadership, and PR presence",
                    "Establishing Tukio as a premier industry reference"
                ]
            }
        ],
        "notes": "Group discussion on marketing events, brand positioning, website assets, and visibility strategy."
    },
    {
        "id": 18,
        "session": "Break",
        "sessionNum": 12,
        "category": "4:15 – 4:30 PM • BREAK",
        "title": "Afternoon Refreshment Break",
        "subtitle": "Quick 15-minute recharge before final strategy sessions",
        "layout": "break-card",
        "duration": "4:15 – 4:30 PM (15 Minutes)",
        "nextSession": "Up Next: Revenue Expansion: Beyond Event Planning (4:30 PM)",
        "notes": "Brief break to stretch and prepare for Revenue Expansion."
    },
    {
        "id": 19,
        "session": "Expansion",
        "sessionNum": 13,
        "category": "4:30 – 5:15 PM • REVENUE EXPANSION",
        "title": "Revenue Expansion: Beyond Event Planning",
        "subtitle": "Facilitator-Led / Group Workshop: Exploring Diversified Growth Horizons",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-node-tree",
                "title": "Adjacent Service Offerings",
                "question": "What complementary service lines can Tukio develop beyond event coordination?",
                "points": [
                    "What complementary service lines can Tukio introduce?",
                    "Expanding advisory, project management, and specialized consulting",
                    "Creating packaged offerings for corporate and public clients"
                ]
            },
            {
                "icon": "ri-vip-crown-line",
                "title": "Proprietary Events & IP",
                "question": "What flagship events, platforms, or industry IP can Tukio create and monetize?",
                "points": [
                    "Developing and owning Tukio-branded flagship events",
                    "Creating annual summits, industry conferences, and platforms",
                    "Monetizing sponsorships, partnerships, and event intellectual property"
                ]
            },
            {
                "icon": "ri-briefcase-line",
                "title": "Strategic Retainers & Partnerships",
                "question": "How can we structure annual retainer agreements with corporate and institutional clients?",
                "points": [
                    "Structuring annual retainer agreements with corporate clients",
                    "Exploring institutional advisory partnerships",
                    "Transitioning from transactional gigs to recurring revenue"
                ]
            }
        ],
        "takeaway": "Expansion requires leveraging our core strengths into higher-value service offerings.",
        "notes": "Explore revenue expansion paths beyond traditional event coordination."
    },
    {
        "id": 20,
        "session": "War Room",
        "sessionNum": 14,
        "category": "5:15 – 5:45 PM • STRATEGY WAR ROOM",
        "title": "Tukio Strategy War Room: From Ideas to Priorities",
        "subtitle": "Group Strategy: Populating the Strategic Planning Matrix",
        "layout": "matrix-framework",
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
        "notes": "Group Strategy War Room: Convert today's discussions into the 10 sections of the Strategic Planning Matrix."
    },
    {
        "id": 21,
        "session": "Closing",
        "sessionNum": 15,
        "category": "5:45 – 6:00 PM • COMMITMENTS & CLOSING",
        "title": "Commitments, Next Steps & Closing",
        "subtitle": "Lead: Facilitator-Led / Management",
        "layout": "talking-points-grid",
        "cards": [
            {
                "icon": "ri-check-line",
                "title": "Team & Individual Commitments",
                "question": "What are our immediate agreed personal and departmental action commitments?",
                "points": [
                    "Personal and departmental action commitments",
                    "Agreed immediate priorities starting tomorrow",
                    "Leadership ownership for critical workstreams"
                ]
            },
            {
                "icon": "ri-file-list-3-line",
                "title": "Documentation & Communique",
                "question": "How will the session communique and implementation matrix be circulated?",
                "points": [
                    "Circulation of strategy session summary report",
                    "Master implementation timeline & responsibility matrix",
                    "Action tracker shared across the management team"
                ]
            },
            {
                "icon": "ri-calendar-check-line",
                "title": "Follow-Up Cadence",
                "question": "What monthly and quarterly review cadence will keep this strategy alive?",
                "points": [
                    "Monthly review meetings to assess progress",
                    "Quarterly and annual strategy evaluation sessions",
                    "Maintaining team alignment and accountability"
                ]
            }
        ],
        "takeaway": "Strategy becomes reality only through disciplined execution and accountability.",
        "notes": "Final wrap-up, management closing remarks, and group photograph."
    }
]

code = '// Master Slide Dataset for Tukio Konsults Ltd - 2026 Strategy Session\n'
code += '// Strictly aligned with "Tukio Konsult Strategy Session Agenda.pdf"\n'
code += '// Strict User Directives: Pure talking points, topics, cards, and table headers.\n'
code += '// Zero assumed narratives or fabricated stories.\n\n'
code += 'const tukioStrategyData = ' + json.dumps(slides, indent=2) + ';\n\n'
code += 'if (typeof module !== "undefined") { module.exports = tukioStrategyData; }\n'

with open('js/slidesData.js', 'w', encoding='utf-8') as f:
    f.write(code)

print('js/slidesData.js successfully generated with', len(slides), 'slides.')
