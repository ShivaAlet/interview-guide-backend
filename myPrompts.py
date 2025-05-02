
def company_research_fun(data):
    # Consider adding role description here if available:
    # role_context = "The target role is a Product Manager focused on ML platforms."
    # Add role_context to the initial instruction if used.

    company_research = '''
    Analyze the provided company data:
    '''+data+'''
    ----
    *Goal:* Generate concise yet insightful information specifically relevant for someone preparing for an interview at this company. Focus on strategy, market position, challenges, recent developments, and potential talking points. Populate the requested JSON structure below accurately and thoughtfully. Ensure the subPoints provide specific details and insights where possible, not just vague statements.

    # Module 1 - Know the Company

    1. Quick Summary (Interview Angle):

    - Purpose: A ~2-minute, high-impact overview hitting key interview talking points.
    - Content (Populate the 'quick_summary' field in the JSON):
        - Company's core mission/vision (in impactful terms).
        - Primary product/service and its main differentiator or value proposition.
        - Key target customer segment and the main problem solved for them.
        - Top 1-2 strategic competitors and the company's primary competitive advantage against them.
        - One significant recent development (funding, launch, acquisition) and its implication (e.g., signals growth, shift in strategy).

    Revised Card Structure Guidance (for populating 'sub_modules' in JSON):

    - Card 1: Core Business & Strategy
        - title: "Core Business & Strategy"
        - summary: "Understand the company's strategic direction, core offerings, business model, and market positioning."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Company Mission & Vision Analysis", subPoints: ["Explain the stated mission/vision", "Identify 1-2 potential implications for company culture or strategy based on it."]
            - main: "Main Products/Services & Value", subPoints: ["[List key offering 1 and its core value/problem solved]", "[List key offering 2 and its core value/problem solved]", "..."]
            - main: "Core Business Model", subPoints: ["Primary revenue stream(s) (e.g., SaaS subscription, transaction fees)", "Note any recent shifts or diversification if apparent."]
            - main: "Strategic Priorities (if evident)", subPoints: ["Identify 1-2 key strategic goals apparent from the data (e.g., 'Expand into enterprise market')", "'Increase focus on AI integration'"]
            - main: "Current Market Position & Trajectory", subPoints: ["Describe position (e.g., 'Leader in X', 'Challenger in Y')", "Note indicators of growth or market share trend (e.g., 'Rapidly growing user base', 'Facing increased competition')."]

    - Card 2: Target Market & Customers
        - title: "Target Market & Customers"
        - summary: "Identify who the company serves, the key problems solved, and how they reach their customers."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Primary Customer Segments", subPoints: ["Describe key B2B/B2C segments", "Note defining characteristics or needs."]
            - main: "Key Customer Pain Points Addressed", subPoints: ["List the specific problems the company solves for its target customers."]
            - main: "Industries Focused On", subPoints: ["List key verticals/industries served."]
            - main: "Notable Clients/Partnerships (Significance)", subPoints: ["[List Example Client/Partner 1]", "Briefly note its significance (e.g., 'Validates enterprise readiness')", "[List Example Client/Partner 2]", "Briefly note its significance (e.g., 'Key distribution channel')"]

    - Card 3: Competitive Landscape
        - title: "Competitive Landscape"
        - summary: "Analyze key competitors, the company's unique positioning, and its core advantages/disadvantages."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Main Competitors", subPoints: ["[List top 3-5 rivals]", "Note their primary focus area if different."]
            - main: "Key Differentiators (USPs)", subPoints: ["What makes the company stand out from competitors in the eyes of customers? (List 1-3 points)"]
            - main: "Competitive Strengths", subPoints: ["Identify 1-3 core advantages (e.g., 'Proprietary technology in X', 'Strong network effects', 'Established brand trust')."]
            - main: "Potential Weaknesses/Challenges", subPoints: ["Identify 1-3 potential vulnerabilities relative to competitors (e.g., 'Smaller R&D budget', 'Dependency on single product line', 'Navigating regulatory hurdles')."]

    - Card 4: Company Vitals & Culture Indicators
        - title: "Company Vitals & Culture Indicators"
        - summary: "Key operational facts, leadership insights, and indicators of company culture."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Size, Status & Location", subPoints: ["Approx Employee Count", "Public/Private Status", "HQ Location", "Other Key Office Locations (if relevant)."]
            - main: "Organizational Structure Notes", subPoints: ["Parent Company (if any)", "Key Subsidiaries/Divisions (if any)", "Note recent restructuring if known."]
            - main: "Key Leadership (Interview Relevant)", subPoints: ["CEO: [Name]", "CPO/Head of Product: [Name]", "CTO/Head of Engineering: [Name]", "Other VPs/Heads relevant to data/role."]
            - main: "Financial Health & Funding", subPoints: ["Recent Funding: [Round/Amount/Date/Key Investors]", "Mention Profitability/Revenue trends if stated", "Note other growth signals."]
            - main: "Culture Clues (from data)", subPoints: ["Infer potential cultural aspects from mission, values, quotes, news", "Example: 'Emphasis on innovation suggested by recent product launches'", "Example: 'Data points to a collaborative environment'", "State if information is scarce."] # NEW

    - Card 5: Recent News & Developments (Impact Focus)
        - title: "Recent News & Developments (Impact Focus)"
        - summary: "Highlight major recent events (last 6-12 months) and analyze their potential impact."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Key Recent Events & Significance", subPoints: ["[Event 1: e.g., 'Launched Product X']", "Significance: [e.g., 'Opens up new market segment']", "[Event 2: e.g., 'Acquired Company Y']", "Significance: [e.g., 'Adds crucial AI talent/technology']", "[Event 3: e.g., 'Secured Series C Funding']", "Significance: [e.g., 'Provides capital for international expansion']", "..."] # Enhanced Structure

    - Card 6: Industry Context & Company Fit
        - title: "Industry Context & Company Fit"
        - summary: "Understand key industry trends and how the company is positioned within the broader market."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Key Industry Trends Impacting the Company", subPoints: ["[Trend 1]", "How it specifically affects this company", "[Trend 2]", "How it specifically affects this company"] # Enhanced
            - main: "Strategic Opportunities", subPoints: ["Based on trends and company strengths, identify 1-2 key growth opportunities."] # Refined
            - main: "Potential Headwinds/Risks", subPoints: ["Based on trends and company weaknesses/market dynamics, identify 1-2 key risks or challenges."] # Refined
    ----
    Give me response in this JSON format only. Adhere strictly to the structure provided:
    {
    "quick_summary": "",
    "sub_modules": [
        {
        "title": "Core Business & Strategy",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Target Market & Customers",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Competitive Landscape",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Company Vitals",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Recent News & Developments",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Industry Context",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        }
    ]
    }

    '''
    return company_research

def product_research_fun(data):
    product_research = '''
    Analyse this entire
    '''+data+'''
    ----
   # Product Research —> Know The Product

**Updated Plain Text Breakdown of Sections and Content:**

**Module Title:** Analyze the Key Offering

**Top-Level Identifiers:** (Remain the same)

- Researched Product: [Name of prioritized product/service OR Fallback description]
- Other Relevant Products: [List of other mentioned products OR empty list]

**Quick Summary:** (Remains the same - focused on the researched product/fallback)

---

**Card 1: Core Offering**

- **Title:** Core Offering
- **Summary Preview:** Understand the offering's primary function, pain points solved, and value proposition.
- **Expanded Details:** (Content points as before)
- **Sources:** [List of URLs/references.]

---

**Card 2: Market** Position

- **Title:** Market Position
- **Summary Preview:** Explore the offering's target users, competitors, and unique differentiators.
- **Expanded Details:** (Content points as before)
- **Sources:** [List of URLs/references.]

---

**Card 3: Product Strategy & Tech**

- **Title:** Product Strategy & Tech
- **Summary Preview:** Review the offering's monetization, tech basis, recent updates, and future direction.
- **Expanded Details:** (Content points as before)
- **Sources:** [List of URLs/references.]

---

**Card 4: Key Trends**

- **Title:** Key Trends
- **Summary Preview:** Analyze key market, tech, and environmental trends impacting the offering.
- **Expanded Details:**
    - Market Trends: [Key trends in the offering's specific market.]
    - Technology Trends: [Relevant tech advancements impacting the space.]
    - Regulatory Environment: [Key regulations or compliance factors OR "No major specific factors noted".]
    - Cultural/Societal Shifts: [Relevant changes in user behavior or societal expectations OR "No major specific factors noted".]
    - Economic Environment: [Relevant macroeconomic factors OR "No major specific factors noted".]
- **Sources:** [List of URLs/references - likely broader sources
    ----
    Give me response in this JSON format only:
    {
    "quick_summary": "",
    "sub_modules": [
        {
        "title": "Core Offering",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Market Position",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Product Strategy & Tech",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Key Trends",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        }
    ]
    }

    '''
    return product_research

def job_description_analysis_fun(data):
    job_description_analysis = '''
    Analyse this entire
    '''+data+'''
    ----
   # Job Description Analysis —> Decode The Role (JD Analysis)

**Updated Plain Text Breakdown (Module 3: Decode the Role - 4 Cards):**

**Module Title:** Decode the Role

**Key Interview Prep Snapshot (Quick Summary)**

- **Core Responsibility:** [Synthesized main focus/task from JD]
- **Critical Skill:** [Most emphasized required skill/experience]
- **Success Proof:** [Likely measurement area OR "Success factors unclear"]
- **Key Collaborator/Theme:** [Prominent collaborator OR Key interview theme derived from JD]

---

**Card 1: Core Responsibility**

- **Title:** Core Responsibility
- **Summary Preview:** What the core job is and its difficulties.
- **Expanded Details:**
    - Primary Mission/Problem: [What the role is hired to solve.]
    - Key Objectives/Tasks: [Action-oriented summary of responsibilities.]
    - Potential Challenges Implied: [Inferred difficulties OR "Specific challenges not clearly implied in JD".]

---

**Card 2: Skills & Experience Needed**

- **Title:** Skills & Experience Needed
- **Summary Preview:** What qualifications and attributes are needed.
- **Expanded Details:**
    - Essential Technical Skills/Tools: [Must-have tech OR "Specific required tech not listed"].
    - Critical Methodologies/Processes: [Essential ways of working OR "Specific methodologies not listed"].
    - Required Experience Level/Domain: [Baseline experience required].
    - Implied Seniority & Autonomy: [Inferred level/autonomy OR "Seniority/Autonomy level unclear from JD"].
    - Crucial Soft Skills: [Top behaviors needed].
    - Preferred/Standout Qualifications: [What preferred qualifications suggest makes an ideal
    candidate OR "Specific standout profile not detailed"].

---

**Card 3: How Your Impact Will Be Measured**

- **Title:** How Your Impact Will Be Measured
- **Summary Preview:** How performance is measured for this role.
- **Expanded Details:**
    - Likely Success Metrics/KPIs: [Inferred metrics/goals OR "Measurement criteria not specified in JD"].
    - Expected Business/Product Impact: [The specific positive changes expected].
    - Inferred Definition of 'High Performance': [What likely constitutes exceeding
    expectations OR "High performance definition unclear from JD"].

---

**Card 4: Team Structure**

- **Title:** Team Structure
- **Summary Preview:** Understand key stakeholders and collaborators.
- **Expanded Details:**
    - Key Collaborators & Stakeholders: [Specific teams (Eng, Design, Sales)
    or roles mentioned as partners OR "Key collaborators not specified"].
    - Reporting Structure: [Who the role reports to, if mentioned OR "Reporting structure not specified"].
    - Implied Collaboration Style: [Inference about cross-functional interaction style OR "Collaboration style not detailed"].
    ----
    Give me response in this JSON format only:
    {
    "quick_summary": "",
    "sub_modules": [
        {
        "title": "Core Responsibility",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Skills & Experience Needed",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "How Your Impact Will Be Measured",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Team Structure",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        }
    ]
    }

    '''
    return job_description_analysis


def resume_experience_to_highlight_to_stand_out_fun(data):
    resume_experience_to_highlight_to_stand_out = '''
    Analyse this entire
    '''+data+'''
    ----
   # **Resume Experience you can highlight to stand out - Module 4**

This is current module 7 but in the new system it will be module 4

**Module Explanation (What's in it for the user):**

This module helps you strategically prepare for your interviews by directly comparing this resume against the specific {Job Description}
 you're targeting. It analyzes both documents to give you actionable 
insights, ensuring you can confidently showcase your most relevant 
qualifications and proactively address any potential concerns.

Here's what you'll get:

1. **Key Strengths & Alignment:** Pinpoints the areas where your resume clearly demonstrates the skills
and experiences the job description is asking for. This helps you
identify your strongest talking points.
2. **Potential Gaps & How to Address:** Constructively highlights significant requirements from the job
description that might not be immediately obvious from your resume.
Importantly, it provides suggestions on how to frame your existing
experience, discuss transferable skills, or prepare specific answers to
bridge these perceived gaps during the interview.
3. **Standout Experiences to Highlight:** Goes beyond simple keyword matching to identify 2-4 specific accomplishments or experiences from *your* resume that are particularly compelling for *this* role. For each standout point, it explains *why* it's relevant to the JD and *why* emphasizing it will help you differentiate yourself from other candidates.

Essentially,
 this module transforms your resume and the JD into a personalized 
interview prep guide, focusing your efforts on what matters most to 
stand out as a strong fit.
    ----
    Give me response in this JSON format only:
    {
    "quick_summary": "",
    "sub_modules": [
        {
        "title": "Key Strengths & Alignment",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Potential Gaps & How to Address",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Standout Experiences to Highlight",
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        }
        ]
        }
    ]
    }

    '''
    return resume_experience_to_highlight_to_stand_out
