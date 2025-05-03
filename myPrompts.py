
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
    "quick_summary": "Very long information description that summarizes all of these cards or sub modules",
    "sub_modules": [
        {
        "title": "Core Business & Strategy",
"completed":false,
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
"completed":false,
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
"completed":false,
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
"completed":false,
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
"completed":false,
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
"completed":false,
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
   *Primary Goal:* Generate a deep analysis of the product ecosystem most relevant to the this role described, tailored for a PM interview perspective, consolidated into 6 insightful cards. The key is to intelligently determine the most likely product focus.

    *Step 1: Identify Mentioned Products:*
    - Carefully read the *Job Description* (and Resume) to identify *ALL* specific products, product lines, platforms, or teams mentioned (e.g., "Search", "Maps", "Assistant", "Cloud Platform"). List them internally.

    *Step 2: Determine Primary Focus Product & Contextual Products (PM Role Context):*
    - *Analyze the JD for PM Responsibility Signals:* Look specifically within the "Responsibilities", "What You'll Do", or similar sections for keywords indicating direct ownership or primary focus for the PM role. Prioritize products associated with phrases like:
        - "own the roadmap for [Product X]"
        - "define the strategy for [Product X]"
        - "responsible for the success of [Product X]"
        - "drive the development of [Product X]"
        - "manage the lifecycle of [Product X]"
        - "gather requirements for [Product X]"
    - *Identify Primary Focus based on Signals:*
        - *If* one product is clearly associated with these PM responsibility keywords/phrases, designate it as the *Primary Focus Product. List any other mentioned products as **Contextual Products*.
    - *If No Clear Ownership Signal, Analyze JD Emphasis & Resume Alignment:*
        - *If* multiple products are mentioned without clear ownership keywords:
            - Assess which product receives the most emphasis or detailed description within the core responsibilities section of the JD.
            - *If* a resume is provided, assess if the candidate's experience (e.g., industry, technology, past product types) aligns more strongly with one mentioned product over the others.
            - *Prioritize based on this hierarchy:* (1st) Strong emphasis in JD Responsibilities, (2nd) Clear alignment with Resume Experience. Designate the product identified via this analysis as the *Primary Focus Product. List others as **Contextual Products*.
    - *Handle Single Mention:*
        - *If* only one product is mentioned throughout the JD, it is the *Primary Focus Product*.
    - *Fallback Logic (If No Specific Product Identified Above):*
        - *If* no specific product is mentioned OR the JD remains vague despite the analysis above:
            - Attempt to identify the company's single *main/flagship/core product* from General Company Info. Designate it as the *Primary Focus Product (Fallback)*.
            - If no single flagship is clear, identify the relevant *product category/business line* (e.g., "Cloud Data Services"). Designate this category as the *Primary Focus (Category Fallback)*.

    *Step 3: Generate Analysis (Primary Focus + Comparative Mentions):*
    - Populate the requested 6-card JSON structure below.
    - The deep analysis in each card should center on the *Primary Focus Product/Category* determined in Step 2.
    - *Crucially:* Where relevant within the subPoints for the Primary Focus Product, *briefly mention the Contextual Products* (identified in Step 2) to provide comparison or show interplay (e.g., "integrates with [Contextual Product]", "unlike [Contextual Product] which focuses on X"). Do not dedicate separate points just for contextual products.

    # Module 2 - Know the Product (Analyze the Key Offering & Ecosystem)

    1. Quick Summary (Executive Overview & Context):

    - Purpose: Provide a concise summary of the analysis below, explicitly stating the context and the reasoning for the product identification strategy used.
    - Content (Populate the 'quick_summary' field in the JSON):
        - *Start with the identification statement:* Clearly state the *Primary Focus Product/Category* and specifically explain the reasoning based on Step 2 (e.g., "The JD emphasizes PM ownership ('owning the roadmap') for *Search, designating it as the primary focus...", "Multiple products (Search, Maps) were mentioned; **Search* is selected as the primary focus due to greater emphasis in the role's responsibilities...", "Based on the candidate's AI background in the resume aligning with mentions of AI features, *Search AI initiatives* are inferred as the primary focus...", "As no specific product was clearly defined for PM ownership, this analysis focuses on the flagship *[Fallback Product Name]...", "JD vague, focusing analysis on the *[Category Fallback]** category...").
        - *If Contextual Products exist, list them:* (e.g., "...while acknowledging the role interacts with *Maps* and *Assistant*.").
        - *Summarize Key Findings:* Briefly cover the Primary Focus Product's core function & problem solved, target user, key differentiator/USP, market position, latest news/release, and monetization, synthesizing info from the 6 cards.

    6-Card Structure Guidance (Primary Focus + Comparative Mentions):

    # (Cards 1 through 6 remain exactly the same as the previous version,
    # including titles "Product Identity & Value" and "Strategy, News & Outlook",
    # and instructions to focus on [Primary Focus Product] while mentioning
    # [Contextual Products] where relevant in subPoints.
    # No changes needed to the card definitions themselves here.)

    - Card 1: Product Identity & Value
        - title: "Product Identity & Value"
        - summary: "Understand the core purpose, problems solved, and unique value of the primary product focus."
        - details (Map to 'points' array using 'main'/'subPoints'):
             # (Instructions as before: Core Function, Problems Solved, UVP, Differentiators - focused on Primary, mention Contextual)
            - main: "Primary Focus: Core Function", subPoints: ["Describe precisely what the [Primary Focus Product] does.", "What capability does it primarily enable?"]
            - main: "Primary Focus: Problems Solved", subPoints: ["List the top 2-3 specific pain points the [Primary Focus Product] addresses."]
            - main: "Primary Focus: Unique Value Proposition (UVP)", subPoints: ["What is the main reason customers choose the [Primary Focus Product]?", "Quantify value if possible."]
            - main: "Primary Focus: Key Differentiators", subPoints: ["List 2-3 specific aspects differentiating the [Primary Focus Product].", "(Mention relevant comparisons to *Contextual Products* here if applicable, e.g., '...differentiates from *[Contextual Product]* by focusing on X')."]

    - Card 2: Target Audience & Key Use Cases
         # (Instructions as before)
        - title: "Target Audience & Key Use Cases"
        - summary: "Define the ideal users for the primary product focus and how they interact with it and potentially related products."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Primary Focus: Target User Personas", subPoints: ["Describe the main user segment(s) for the [Primary Focus Product]."]
            - main: "Primary Focus: Key Use Cases / Workflows", subPoints: ["Describe the top 2-3 common tasks/workflows using the [Primary Focus Product].", "(Note if these workflows often involve *Contextual Products, e.g., '...often followed by using *[Contextual Product]** for Y')."]
            - main: "Primary Focus: Jobs-To-Be-Done (JTBD)", subPoints: ["What 'job' are users hiring the [Primary Focus Product] to do?"]


    - Card 3: Market Landscape & Positioning
         # (Instructions as before)
        - title: "Market Landscape & Positioning"
        - summary: "Analyze the competitive environment for the primary product focus and its place within the market."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Primary Focus: Direct Competitors", subPoints: ["[Competitor 1 Name]: Key strength/focus, How [Primary Focus Product] differentiates.", "[Competitor 2 Name]: ..."]
            - main: "Primary Focus: Indirect Competitors / Alternatives", subPoints: ["What other solutions might users employ instead?", "(Mention if *Contextual Products* sometimes serve as alternatives for specific tasks)."]
            - main: "Primary Focus: Market Segment & Position", subPoints: ["Describe the specific market segment targeted by the [Primary Focus Product].", "Its perceived position (Leader, Challenger, etc.)."]
            - main: "Market Trends Impacting Ecosystem", subPoints: ["List 1-2 key industry trends affecting the [Primary Focus Product] and potentially the *Contextual Products*."]


    - Card 4: Strategy, News & Outlook
         # (Instructions as before)
        - title: "Strategy, News & Outlook"
        - summary: "Understand the strategic direction, recent developments, and future outlook for the primary product focus."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Latest News (Primary Focus or Relevant)", subPoints: ["Identify the most recent relevant public announcement about the [Primary Focus Product] OR highly relevant company news impacting it.", "Summarize its key message.", "*If none found, state explicitly:* 'No specific recent public announcements found directly relating to [Primary Focus Product].'"]
            - main: "Inferred Vision/Goal (Primary Focus)", subPoints: ["Based on available info, what seems to be the long-term aspiration for the [Primary Focus Product]?"]
            - main: "Recent Strategic Shifts (Primary Focus)", subPoints: ["Have there been noticeable changes in focus for the [Primary Focus Product] in the last 6-12 months?"]
            - main: "Potential Future Directions (Ecosystem)", subPoints: ["Based on trends, what are plausible next steps for the [Primary Focus Product]?", "(Mention potential interplay or impact on *Contextual Products* if relevant)."]


    - Card 5: Key Features, Technology & Monetization
         # (Instructions as before)
        - title: "Key Features, Technology & Monetization"
        - summary: "Highlight defining features, relevant tech, integrations, and the business model for the primary product focus."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Primary Focus: Defining Features & Value", subPoints: ["[Feature 1 Name]: Describe & explain its contribution to UVP.", "[Feature 2 Name]: ..."]
            - main: "Primary Focus: Relevant Technology", subPoints: ["Mention tech only if strategically important (scalability, differentiation e.g., 'Proprietary AI')."]
            - main: "Integration Ecosystem", subPoints: ["Note key integrations, especially mentioning *Contextual Products* if they integrate tightly (e.g., 'Integrates natively with *[Contextual Product]* for Z')."]
            - main: "Primary Focus: Monetization Strategy", subPoints: ["How is value captured for the [Primary Focus Product]?"]
            - main: "Primary Focus: Pricing Structure (if known)", subPoints: ["Describe key tiers/structure for the [Primary Focus Product]."]


    - Card 6: SWOT Analysis (Primary Focus)
         # (Instructions as before)
        - title: "SWOT Analysis (Primary Focus)"
        - summary: "A strategic summary of the primary product's internal strengths/weaknesses and external opportunities/threats."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Strengths (Primary Focus)", subPoints: ["List 2-3 internal advantages of the [Primary Focus Product]."]
            - main: "Weaknesses (Primary Focus)", subPoints: ["List 2-3 internal disadvantages of the [Primary Focus Product]."]
            - main: "Opportunities (Ecosystem Context)", subPoints: ["List 1-2 external opportunities for the [Primary Focus Product], (consider synergies with *Contextual Products*)."]
            - main: "Threats (Ecosystem Context)", subPoints: ["List 1-2 key external threats to the [Primary Focus Product], (consider competitive moves involving *Contextual Products*)."]
    ----
    Give me response in this JSON format only:
    {
    "quick_summary": "Very long information description that summarizes all of these cards or sub modules",
    "sub_modules": [
        {
        "title": "Product Identity & Value",
"completed":false,
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
        "title": "Target Audience & Key Use Cases",
"completed":false,
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
        "title": "Market Landscape & Positioning",
"completed":false,
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
        "title": "Strategy, News & Outlook",
"completed":false,
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
        "title": "Key Features, Technology & Monetization",
"completed":false,
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
        "title": "SWOT Analysis (Primary Focus)",
"completed":false,
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
            }
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
    "quick_summary": "Very long information description that summarizes all of these cards or sub modules",
    "sub_modules": [
        {
        "title": "Core Responsibility",
"completed":false,
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
"completed":false,
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
"completed":false,
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
"completed":false,
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
    "quick_summary": "Very long information description that summarizes all of these cards or sub modules",
    "sub_modules": [
        {
        "title": "Key Strengths & Alignment",
"completed":false,
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
"completed":false,
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
"completed":false,
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
