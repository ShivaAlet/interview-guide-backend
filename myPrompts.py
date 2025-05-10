
def company_research_fun(data):
    # Consider adding role description here if available:
    # role_context = "The target role is a Product Manager focused on ML platforms."
    # Add role_context to the initial instruction if used.

    company_research = '''
     You will be provided with a Job Description (JD) below. Your primary task is to help a user prepare for an interview for the role detailed in this JD.

    1.  Identify Company: First, accurately identify the name of the company from the Job Description.
    2.  Research Company: Using the identified company name, leverage your knowledge base and search capabilities (if available) to gather comprehensive information about this company.
    3.  Generate Interview Prep Content: Populate the JSON structure below with information specifically tailored to help the user prepare for their interview. Focus on strategy, market position, challenges, recent developments, and potential talking points relevant to both the company and the specific role mentioned in the JD.

    '''+data+'''
    ----
   Revised Goal: For the company identified from the JD, generate concise yet insightful information specifically relevant for someone preparing for an interview for the role described in the JD. Focus on its strategy, market position, challenges, recent developments, and potential talking points. Populate the requested JSON structure accurately and thoughtfully. Ensure the subPoints provide specific details and insights where possible, not just vague statements. If, after your research, information for a specific point cannot be found, explicitly state 'Information not found' or 'Publicly available information is scarce for this point.'

    # Module 1 - Know the Company

    1. Quick Summary (Interview Angle):

    - Purpose: A ~2-minute, high-impact overview hitting key interview talking points.
    - Content (Populate the 'quick_summary' field in the JSON based on your research of the identified company):
        - Company's core mission/vision (in impactful terms).
        - Primary product/service and its main differentiator or value proposition.
        - Key target customer segment and the main problem solved for them.
        - Top 1-2 strategic competitors and the company's primary competitive advantage against them.
        - One significant recent development (funding, launch, acquisition) and its implication (e.g., signals growth, shift in strategy) – for this point only, analyze implication.

    Revised Card Structure Guidance (for populating 'sub_modules' in JSON):

    - Card 1: Company Overview
        - title: "Company Overview"
        - summary: "[Generate a 2-3 sentence summary of this card's key findings regarding the Company Overview, based on the 'points' and 'subPoints' populated below.]" # MODIFIED
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Company Snapshot", subPoints: ["Based on your research, provide a concise description of the identified company."]
            - main: "Origins & Founders", subPoints: ["Based on your research, detail when and where the company was founded.", "List the key founder(s).", "Explain the inspiration or vision behind its creation."]
            - main: "Product & Services Portfolio", subPoints: ["Based on your research, breakdown the company’s full range of products.", "List its services and solutions.", "Highlight key offerings.", "Mention significant innovation areas."]
            - main: "Revenue Model", subPoints: ["Based on your research, explain how the company generates revenue.", "Describe its pricing structure if known.", "Outline its core monetization strategy.", "Identify primary income streams."]

    - Card 2: Target Market & Customers
        - title: "Target Market & Customers"
        - summary: "[Generate a 2-3 sentence summary of this card's key findings regarding the Target Market & Customers, based on the 'points' and 'subPoints' populated below.]" # MODIFIED
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Primary Customer Segments", subPoints: ["Describe the primary B2B and/or B2C customer segments of the identified company.", "Highlight defining characteristics, demographics, or firmographics of these segments (e.g., size of business, user persona)."]
            - main: "Key Customer Challenges Solved", subPoints: ["List the specific problems, unmet needs, or challenges the identified company's products/services directly solve for its target customers.", "Focus on the core value proposition from the customer's perspective."]
            - main: "Key Reasons Customers Choose the Company", subPoints: ["Identify the top 2-3 compelling reasons, differentiators, or unique selling propositions (USPs) that make customers select the identified company over competitors.", "Examples: superior technology, better user experience, cost-effectiveness, specific features, strong customer support, brand reputation."]
            - main: "Key Industries Served", subPoints: ["List the primary industries or verticals that the identified company's products/services cater to.", "Note if any industry represents a particular strategic focus or significant market share."]
            - main: "Notable Clients", subPoints: ["From your research of publicly available information about the identified company, list 5-7 significant or well-known clients.", "Briefly state the potential interview-relevant significance of these clients (e.g., 'Validates enterprise readiness', 'Represents major market penetration in X industry').", "If fewer than 5-7 are prominent from your research, list those found."]

    - Card 3: Competitive Landscape
        - title: "Competitive Landscape"
        - summary: "[Generate a 2-3 sentence summary of this card's key findings regarding the Competitive Landscape, based on the 'points' and 'subPoints' populated below.]" # MODIFIED
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Main Competitors", subPoints: ["List 5-7 significant or well-known competitors of the identified company, or as many as publicly available from your research if not that many.", "Note their primary focus area if different."]
            - main: "Key Differentiators (USPs)", subPoints: ["What makes the identified company stand out from competitors in the eyes of customers? (List 1-3 points based on your research)"]
            - main: "Competitive Strengths", subPoints: ["Based on your research, identify 1-3 core advantages of the identified company (e.g., 'Proprietary technology in X', 'Strong network effects', 'Established brand trust')."]
            - main: "Potential Weaknesses/Challenges", subPoints: ["Based on your research, identify 1-3 potential vulnerabilities of the identified company relative to competitors (e.g., 'Smaller R&D budget', 'Dependency on single product line', 'Navigating regulatory hurdles')."]

    - Card 4: Org Structure, Leadership & Culture
        - title: "Org Structure, Leadership & Culture"
        - summary: "[Generate a 2-3 sentence summary of this card's key findings regarding Org Structure, Leadership & Culture, based on the 'points' and 'subPoints' populated below.]" # MODIFIED
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Size, Status & Location", subPoints: ["Approx Employee Count", "Public/Private Status", "HQ Location", "Other Key Office Locations (if relevant)."]
            - main: "Organizational Structure", subPoints: ["Parent Company (if any)", "Key Subsidiaries/Divisions (if any)", "Note recent restructuring if known."]
            - main: "Key Leadership", subPoints: ["CEO: [Name]", "CPO/Head of Product: [Name]", "CTO/Head of Engineering: [Name]", "Other VPs/Heads relevant to the role in the JD or company data functions."]
            - main: "Financial Health & Funding", subPoints: ["Recent Funding: [Round/Amount/Date/Key Investors]", "Mention Profitability/Revenue trends if stated", "Note other growth signals."]
            - main: "Company Culture", subPoints: ["Based on your research (e.g., the identified company's stated mission/values, reputable employee review aggregators, news reports), infer 2-3 potential cultural aspects.", "Example: 'Emphasis on innovation suggested by recent product launches.'", "Example: 'Data points to a collaborative environment.'", "If information is scarce or highly speculative, state so."]

    - Card 5: Recent News & Key Developments
        - title: "Recent News & Key Developments"
        - summary: "[Generate a 1-2 sentence summary highlighting the most significant recent news or developments from the 'points' populated below. Focus on the nature of the events without analyzing impact.]" # MODIFIED
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Key Recent Events", # Previously MODIFIED: Changed "Key Recent Events & Factual Details" to "Key Recent Events"
              subPoints: [ # Previously MODIFIED: Instructions for one-line summaries
                  "For Event 1, provide a concise one-line summary incorporating key factual details. Example: 'Raised over $500 million from strategic investors like Sequoia, Google Ventures, Kleiner Perkins, and OpenAI.'",
                  "For Event 2, provide a concise one-line summary incorporating key factual details. Example: 'Launched Product X, an AI-powered analytics tool, on YYYY-MM-DD.'",
                  "For Event 3, provide a concise one-line summary incorporating key factual details. Example: 'Acquired Company Y, specializing in Z technology, for an undisclosed amount.'",
                  "List up to 3-5 key recent events from the last 2 years. Each event should be a single, concise line summarizing the event and its most important factual details (like funding amounts, key partners, product names, dates if significant). Focus on factual reporting without impact analysis."
              ]

    - Card 6: Industry Context & Company Fit
        - title: "Industry Context & Company Fit"
        - summary: "[Generate a 2-3 sentence summary of this card's key findings regarding Industry Context & Company Fit, based on the 'points' and 'subPoints' populated below.]" # MODIFIED
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Key Industry Trends Impacting the Company", subPoints: ["[Trend 1 affecting the industry/company]", "How it specifically affects the identified company", "[Trend 2 affecting the industry/company]", "How it specifically affects the identified company"]
            - main: "Strategic Opportunities", subPoints: ["Based on industry trends and the identified company's strengths, identify 1-2 key growth opportunities."]
            - main: "Potential Headwinds/Risks", subPoints: ["Based on industry trends and the identified company's weaknesses/market dynamics, identify 1-2 key risks or challenges."]
    ----
    Give me response in this JSON format only. Adhere strictly to the structure provided:
    {
    "quick_summary": "A 2-minute, high-impact overview of the identified company, hitting key interview talking points such as its mission, primary product/value, target customers, main competitors, and a significant recent development with its implication.",
    "sub_modules": [
        {
        "title": "Company Overview",
"completed":false,
        "summary": "[A generated 2-3 sentence summary of the Company Overview based on its populated points will appear here.]", # MODIFIED
        "content": "Detailed textual information synthesized from the points below, forming a coherent narrative about the company's overview.",
        "points": [
            {
            "main": "Company Snapshot",
            "subPoints": ["Concise description of the identified company."]
            },
            {
            "main": "Origins & Founders",
            "subPoints": ["Details about when, where, and by whom the company was founded, vision behind creation."]
            },
            {
            "main": "Product & Services Portfolio",
            "subPoints": ["Breakdown of the company’s full range of products, services, solutions, key offerings, innovation areas."]
            },
            {
            "main": "Revenue Model",
            "subPoints": ["Explanation of how the company generates revenue, pricing structure, monetization strategy, income streams."]
            }
        ]
        },
        {
        "title": "Target Market & Customers",
"completed":false,
        "summary": "[A generated 2-3 sentence summary of the Target Market & Customers based on its populated points will appear here.]", # MODIFIED
        "content": "Detailed textual information synthesized from the points below, forming a coherent narrative about the company's target market and customers.",
        "points": [
            {
            "main": "Primary Customer Segments",
            "subPoints": ["Description of primary B2B/B2C segments and their characteristics."]
            },
            {
            "main": "Key Customer Challenges Solved",
            "subPoints": ["List of specific problems/needs the company solves for its customers."]
            },
            {
            "main": "Key Reasons Customers Choose the Company",
            "subPoints": ["Top 2-3 reasons/USPs why customers select this company."]
            },
            {
            "main": "Key Industries Served",
            "subPoints": ["Primary industries/verticals the company's products/services cater to."]
            },
            {
            "main": "Notable Clients",
            "subPoints": ["List of 5-7 significant clients (publicly mentioned or on company website) and their importance."]
            }
        ]
        },
        {
        "title": "Competitive Landscape",
"completed":false,
        "summary": "[A generated 2-3 sentence summary of the Competitive Landscape based on its populated points will appear here.]", # MODIFIED
        "content": "Detailed textual information synthesized from the points below, forming a coherent narrative about the company's competitive landscape.",
        "points": [
            {
            "main": "Main Competitors",
            "subPoints": ["List of 5-7 significant competitors (or as many as publicly available) and their primary focus areas."]
            },
            {
            "main": "Key Differentiators (USPs)",
            "subPoints": ["What makes the company stand out (1-3 points)."]
            },
            {
            "main": "Competitive Strengths",
            "subPoints": ["1-3 core advantages of the company."]
            },
            {
            "main": "Potential Weaknesses/Challenges",
            "subPoints": ["1-3 potential vulnerabilities relative to competitors."]
            }
        ]
        },
        {
        "title": "Org Structure, Leadership & Culture",
"completed":false,
        "summary": "[A generated 2-3 sentence summary of the Org Structure, Leadership & Culture based on its populated points will appear here.]", # MODIFIED
        "content": "Detailed textual information synthesized from the points below, forming a coherent narrative about the company's org structure, leadership, and culture.",
        "points": [
            {
            "main": "Size, Status & Location",
            "subPoints": ["Approx Employee Count, Public/Private, HQ, Key Offices."]
            },
            {
            "main": "Organizational Structure",
            "subPoints": ["Parent Company, Key Subsidiaries/Divisions, recent restructuring."]
            },
            {
            "main": "Key Leadership",
            "subPoints": ["CEO, CPO/Product Head, CTO/Engineering Head, other relevant VPs/Heads."]
            },
            {
            "main": "Financial Health & Funding",
            "subPoints": ["Recent Funding, Profitability/Revenue trends, growth signals."]
            },
            {
            "main": "Company Culture",
            "subPoints": ["Inferred cultural aspects from mission, values, news; examples."]
            }
        ]
        },
        {
        "title": "Recent News & Key Developments",
"completed":false,
        "summary": "[A generated 1-2 sentence summary of the key recent events (e.g., funding, launches) based on its populated points will appear here.]", # MODIFIED
        "content": "Detailed textual information synthesized from the points below, forming a coherent narrative about recent news and developments.",
        "points": [
            {
            "main": "Key Recent Events", # Previously MODIFIED
            "subPoints": [ # Previously MODIFIED
                "Raised over $500 million from strategic investors like Sequoia, Google Ventures, Kleiner Perkins, and OpenAI.",
                "Launched Product X, an AI-powered analytics tool, on YYYY-MM-DD.",
                "Acquired Company Y, specializing in Z technology, for an undisclosed amount.",
                "Up to 3-5 key recent events, each summarized in a single line with key factual details."
                ]
            }
        ]
        },
        {
        "title": "Industry Context & Company Fit",
"completed":false,
        "summary": "[A generated 2-3 sentence summary of the Industry Context & Company Fit based on its populated points will appear here.]", # MODIFIED
        "content": "Detailed textual information synthesized from the points below, forming a coherent narrative about the industry context and company fit.",
        "points": [
            {
            "main": "Key Industry Trends Impacting the Company",
            "subPoints": ["Trend 1 and its specific effect on the company", "Trend 2 and its specific effect on the company"]
            },
            {
            "main": "Strategic Opportunities",
            "subPoints": ["1-2 key growth opportunities based on trends and strengths."]
            },
            {
            "main": "Potential Headwinds/Risks",
            "subPoints": ["1-2 key risks/challenges based on trends and weaknesses/market dynamics."]
            }
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
        - summary: "Understand the core purpose, problems solved, and unique value of the primary product."
        - details (Map to 'points' array using 'main'/'subPoints'):
             # (Instructions as before: Core Function, Problems Solved, UVP, Differentiators - focused on Primary, mention Contextual)
            - main: "Core Function", subPoints: ["Describe precisely what the [Primary Focus Product] does.", "What capability does it primarily enable?"]
            - main: "Problems Solved", subPoints: ["List the top 2-3 specific pain points the [Primary Focus Product] addresses."]
            - main: "Unique Value Proposition (UVP)", subPoints: ["What is the main reason customers choose the [Primary Focus Product]?", "Quantify value if possible."]
            - main: "Key Differentiators", subPoints: ["List 2-3 specific aspects differentiating the [Primary Focus Product].", "(Mention relevant comparisons to *Contextual Products* here if applicable, e.g., '...differentiates from *[Contextual Product]* by focusing on X')."]

    - Card 2: Target Audience & Key Use Cases
         # (Instructions as before)
        - title: "Target Audience & Key Use Cases"
        - summary: "Define the ideal users for the primary product and how they interact with it and potentially related products."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Target User Personas", subPoints: ["Describe the main user segment(s) for the [Primary Focus Product]."]
            - main: "Key Use Cases / Workflows", subPoints: ["Describe the top 2-3 common tasks/workflows using the [Primary Focus Product].", "(Note if these workflows often involve *Contextual Products, e.g., '...often followed by using *[Contextual Product]** for Y')."]
            - main: "Jobs-To-Be-Done (JTBD)", subPoints: ["What 'job' are users hiring the [Primary Focus Product] to do?"]


    - Card 3: Market Landscape & Positioning
         # (Instructions as before)
        - title: "Market Landscape & Positioning"
        - summary: "Analyze the competitive environment for the primary product and its place within the market."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Direct Competitors", subPoints: ["[Competitor 1 Name]: Key strength/focus, How [Primary Focus Product] differentiates.", "[Competitor 2 Name]: ..."]
            - main: "Indirect Competitors / Alternatives", subPoints: ["What other solutions might users employ instead?", "(Mention if *Contextual Products* sometimes serve as alternatives for specific tasks)."]
            - main: "Market Segment & Position", subPoints: ["Describe the specific market segment targeted by the [Primary Focus Product].", "Its perceived position (Leader, Challenger, etc.)."]
            - main: "Market Trends Impacting Ecosystem", subPoints: ["List 1-2 key industry trends affecting the [Primary Focus Product] and potentially the *Contextual Products*."]


    - Card 4: Strategy, News & Outlook
         # (Instructions as before)
        - title: "Strategy, News & Outlook"
        - summary: "Understand the strategic direction, recent developments, and future outlook for the primary product."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Latest News (Primary or Relevant)", subPoints: ["Identify the most recent relevant public announcement about the [Primary Focus Product] OR highly relevant company news impacting it.", "Summarize its key message.", "*If none found, state explicitly:* 'No specific recent public announcements found directly relating to [Primary Focus Product].'"]
            - main: "Inferred Vision/Goal", subPoints: ["Based on available info, what seems to be the long-term aspiration for the [Primary Focus Product]?"]
            - main: "Recent Strategic Shifts", subPoints: ["Have there been noticeable changes in focus for the [Primary Focus Product] in the last 6-12 months?"]
            - main: "Potential Future Directions (Ecosystem)", subPoints: ["Based on trends, what are plausible next steps for the [Primary Focus Product]?", "(Mention potential interplay or impact on *Contextual Products* if relevant)."]


    - Card 5: Key Features, Technology & Monetization
         # (Instructions as before)
        - title: "Key Features, Technology & Monetization"
        - summary: "Highlight defining features, relevant tech, integrations, and the business model for the primary product."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Defining Features & Value", subPoints: ["[Feature 1 Name]: Describe & explain its contribution to UVP.", "[Feature 2 Name]: ..."]
            - main: "Relevant Technology", subPoints: ["Mention tech only if strategically important (scalability, differentiation e.g., 'Proprietary AI')."]
            - main: "Integration Ecosystem", subPoints: ["Note key integrations, especially mentioning *Contextual Products* if they integrate tightly (e.g., 'Integrates natively with *[Contextual Product]* for Z')."]
            - main: "Monetization Strategy", subPoints: ["How is value captured for the [Primary Focus Product]?"]
            - main: "Pricing Structure (if known)", subPoints: ["Describe key tiers/structure for the [Primary Focus Product]."]


    - Card 6: SWOT Analysis (Primary Focus)
         # (Instructions as before)
        - title: "SWOT Analysis"
        - summary: "A strategic summary of the primary product's internal strengths/weaknesses and external opportunities/threats."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Strengths", subPoints: ["List 2-3 internal advantages of the [Primary Focus Product]."]
            - main: "Weaknesses", subPoints: ["List 2-3 internal disadvantages of the [Primary Focus Product]."]
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

Quick Summary Instructions:

    Generate a concise (3-4 sentence) overview.

    Explicitly state that this analysis is based only on the provided JD text.

    Synthesize the role's core purpose, the most critical skill/experience emphasized, the primary way success appears to be measured, and the main organizational context (reporting line or key collaborators).

---

Card 1: Core Role & Responsibilities

    Title: Core Role & Responsibilities

    Summary: Analysis of the main purpose of the role and key tasks specified in the JD, interpreted for their significance.

    Points:

        mainPoint: Primary Mission / Underlying Need

            subPoints: Based on the responsibilities and objectives listed, articulate the fundamental problem this role is hired to solve for the company or product team. Explain the significance of this mission and why it's likely a priority now, drawing inferences from the JD text.

        mainPoint: Key Responsibility Areas & PM Activities

            subPoints: Break down the main tasks mentioned in the JD into logical groupings (e.g., Product Strategy, Execution, GTM, Analysis). For each, explain what the JD says is required and why it's important for this specific role. Connect responsibilities to typical PM functions and translate jargon into actionable terms (e.g., "owning the roadmap" likely means defining priorities and communicating trade-offs).

        mainPoint: Areas of Specific Emphasis or Complexity

            subPoints: Identify any responsibility or task mentioned multiple times, listed first, or given particular detail/weight in the JD. Analyze why this area is likely a key focus for the hiring manager and what inherent complexities or challenges it might involve based on the JD's description.

Card 2: Required Skills & Experience

    Title: Required Skills & Experience

    Summary: Interpretation of the essential and preferred qualifications sought, explaining their relevance to the role's demands.

    Points:

        mainPoint: Essential Hard Skills / Technical Requirements

            subPoints: List specific technical skills, tools, methodologies, or domain knowledge explicitly required. If none are specific, state this clearly ("Specific required technical skills not listed"). For each required skill, explain how it directly applies to fulfilling the responsibilities listed in Card 1 and why it's critical for success in this specific role based on the JD.

        mainPoint: Critical Soft Skills & Attributes

            subPoints: List essential communication, collaboration, leadership, or other behavioral attributes mentioned. Analyze why these specific soft skills are crucial for success, connecting them to the team structure (Card 4), stakeholder interactions, or challenges implied by the JD.

        mainPoint: Required Experience Level & Domain

            subPoints: Specify the minimum years of experience, industry domain, or functional experience requested. Analyze what this requirement suggests about the expected level of autonomy, complexity, or specific challenges the candidate will need to handle.

        mainPoint: Preferred / Standout Qualifications

            subPoints: List any 'nice-to-have' qualifications. Analyze what these preferred items reveal about the ideal candidate profile, potential future needs of the team/role, or areas where a candidate could truly differentiate themselves.

Card 3: Defining Success & Measuring Impact

    Title: Defining Success & Measuring Impact

    Summary: Analysis of how performance will be measured and the expected tangible outcomes of the role, based on explicit and inferred JD points.

    Points:

        mainPoint: Explicitly Stated Success Metrics / KPIs

            subPoints: List any specific metrics, goals, or KPIs mentioned in the JD (e.g., "increase user engagement," "achieve revenue target," "deliver on time"). Clearly state if "Specific metrics/KPIs not explicitly listed." For any metrics found, explain how successful execution of the responsibilities listed in Card 1 would directly influence these metrics.

        mainPoint: Implied Success Indicators

            subPoints: Based on the responsibilities, objectives, and desired outcomes described, infer other ways performance will likely be judged, even without explicit metrics (e.g., quality of strategic input, effectiveness of collaboration, user satisfaction outcomes, successful feature adoption). Explain the reasoning for each inference drawn from the JD text.

        mainPoint: Expected Business / Product Impact

            subPoints: Synthesize the desired tangible outcomes of the role's success for the product, team, or the business as a whole, based on statements in the JD (e.g., market share growth, operational efficiency, user base expansion). Explain the significance of this impact from a strategic perspective.

        mainPoint: Connecting Success to Interview Examples

            subPoints: Based on the metrics, implied indicators, and expected impact, suggest the types of interview examples (using STAR method or similar) the candidate should prepare to demonstrate their ability to achieve these specific outcomes or deliver this kind of impact.

Card 4: Team, Collaboration & Reporting Structure

    Title: Team, Collaboration & Reporting Structure

    Summary: Analysis of the organizational context, including reporting lines, key partners, and the expected style and challenges of collaboration.

    Points:

        mainPoint: Reporting Structure

            subPoints: State who the role reports to, if specified. Clearly state if "Reporting structure not specified in JD." Analyze what this reporting line might mean for the role's level of autonomy, strategic alignment, and typical interactions (e.g., reporting to a Director might mean less day-to-day guidance, reporting to a Senior PM might imply mentorship).

        mainPoint: Key Internal Collaborators / Stakeholders

            subPoints: List specific internal teams or roles mentioned as partners (e.g., Engineering, Design, Marketing, Sales). For each, explain the nature of the collaboration implied by the JD's description of tasks (e.g., "collaborate closely with Engineering on technical feasibility and execution," "work with Marketing on GTM strategy and messaging").

        mainPoint: Key External Collaborators / Relationships

            subPoints: List any external groups mentioned (e.g., customers, partners, suppliers). Explain the purpose and type of interaction with these external parties based on the JD. State if "Key external collaborators not specified in JD."

        mainPoint: Implied Collaboration Style & Potential Challenges

            subPoints: Analyze the JD text for clues about the required collaboration style (e.g., highly cross-functional, consensus-driven, requiring significant influence without direct authority, global/distributed). Based on the number and type of collaborators, point out any potential challenges in managing dependencies, competing priorities, or communication that are suggested by the structure.

Card 5: Strategic Context & Role Significance

    Title: Strategic Context & Role Significance

    Summary: Places the role within the broader company and product strategy, interpreting why this position is important now and its potential impact.

    Points:

        mainPoint: The Company's Need for this Role

            subPoints: Synthesize why the company is hiring for this position specifically at this time, based on the problems the role is intended to solve or the initiatives it supports (Card 1 analysis). Explain what strategic gap or opportunity the role is designed to address according to the JD.

        mainPoint: Contribution to Broader Product / Company Strategy

            subPoints: Explain how successful execution of this role's responsibilities directly contributes to the company's overall product vision, business objectives, or strategic priorities mentioned or implied in the JD. Connect the specific tasks to the bigger picture.

        mainPoint: Potential Strategic Challenges or Opportunities

            subPoints: Identify any strategic challenges (e.g., competitive intensity, market maturity, technological shifts) or significant opportunities (e.g., untapped market segment, new platform adoption) that the role is intended to navigate, address, or capitalize on, as suggested by the JD.

        mainPoint: Role Autonomy and Influence Level

            subPoints: Based on the responsibilities (Card 1), required experience level (Card 2), reporting structure (Card 4), and strategic context, infer the expected level of autonomy the person in this role will have and their potential for influencing product decisions and cross-functional teams.

Card 6: Key Themes & Interview Angles

    Title: Key Themes & Interview Angles

    Summary: Synthesizes overarching themes from the JD and suggests areas to focus on during interview preparation and discussion.

    Points:

        mainPoint: Overarching Themes & Priorities

            subPoints: Identify 2-3 major themes that appear repeatedly or are given significant weight throughout the JD (e.g., "Execution Focus," "Customer Obsession," "Data-Driven Decision Making," "Cross-functional Leadership," "Innovation"). Explain how these themes are reflected across the responsibilities and requirements.

        mainPoint: Areas Likely to be Deeply Probed

            subPoints: Based on the required skills, areas of emphasis, and potential challenges identified in the previous cards, highlight specific topics or experiences the candidate should be prepared to discuss in detail. This is where the interviewer will likely probe for depth.

        mainPoint: How to Align Your Experience

            subPoints: Provide actionable guidance on how the candidate should frame their past experiences to align directly with the core requirements, skills, and strategic context identified in this analysis. Suggest focusing examples (e.g., using STAR) on the most emphasized responsibilities and demonstrating the required skills and impact.

        mainPoint: Insightful Questions to Ask

            subPoints: Generate 3-5 potential questions the candidate could ask their interviewers, derived directly from ambiguities, strategic points, potential challenges, or missing information identified during this JD analysis. Frame these as questions that show thoughtful engagement with the role and its context.

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
        "title": "Core Role & Responsibilities",
"completed":false,
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "Primary Mission / Underlying Need",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Key Responsibility Areas & PM Activities",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Areas of Specific Emphasis or Complexity",
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
        "title": "Required Skills & Experience",
"completed":false,
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "Essential Hard Skills / Technical Requirements",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Critical Soft Skills & Attributes",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Required Experience Level & Domain",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
             {
            "main": "Preferred / Standout Qualifications",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Defining Success & Measuring Impact",
"completed":false,
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "Explicitly Stated Success Metrics / KPIs",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Implied Success Indicators",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Expected Business / Product Impact",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Connecting Success to Interview Examples",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Team, Collaboration & Reporting Structure",
"completed":false,
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "Reporting Structure",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Key Internal Collaborators / Stakeholders",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Key External Collaborators / Relationships",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Implied Collaboration Style & Potential Challenges",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Strategic Context & Role Significance",
"completed":false,
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "The Company's Need for this Role",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Contribution to Broader Product / Company Strategy",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Potential Strategic Challenges or Opportunities",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Role Autonomy and Influence Level",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
         {
        "title": "Key Themes & Interview Angles",
"completed":false,
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "Overarching Themes & Priorities",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Areas Likely to be Deeply Probed",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "How to Align Your Experience",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Insightful Questions to Ask",
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

def recruiter_screen_preparation_fun(data):
    recruiter_screen_preparation = '''
    Analyse this entire
    '''+data+'''
    ----
   Act as an expert career coach specializing in early-stage interview 
preparation. Analyze the provided Job Description (JD) and typical 
recruiter screen objectives to generate a comprehensive guide for this
role candidate's first call with a recruiter. Focus on 
interpreting the JD in the context of this screening stage, predicting 
likely questions tailored to the JD, suggesting effective ways to 
approach answers, and providing insightful questions for the candidate 
to ask, all within a 4-card JSON structure.

**Constraints for JSON Output:**

- Generate **exactly 4** sub_modules (cards) as detailed below.
- Keep the content field empty ("") for all sub_modules.
- Use the provided JD text as a key source for tailoring typical recruiter
screen topics, predicting questions, and extracting quick facts. If
Resume is also provided as input, use it *only* for guidance in crafting the "Tell me about yourself" pitch (Card 2), *not* for tailoring other questions or facts derived *from the JD*.
- Maintain a clear Product Management candidate's perspective.
- For subPoints, include specific examples of *predicted questions*, *suggested strategies/talking points*, and *insightful questions to ask*.
- Clearly state when information for a specific quick fact (like salary range or location/remote status) is *not found* or is ambiguous in the provided JD.
- Ensure the complexity of questions and suggested answers is appropriate for an initial recruiter screening call (generally higher level than
technical/panel interviews).

*Module Title:* Recruiter Screen Prep

*Key Interview Prep Snapshot (Quick Summary)*

- **Instruction:** Generate a concise (3-4 sentence) quick summary for the quick_summary JSON field.
- **Content:** Briefly state the purpose of the recruiter screen (basic fit,
qualifications check, logistics) and how this module helps (call
objectives, quick facts, predicted questions, questions to ask).
Explicitly state that this preparation is tailored based on the provided JD (and Resume, if used).

*Card 1: Call Rubric & Quick Facts*

- **Instruction:** Generate the JSON object for the first sub_module.
- *Title:* Call Rubric & Quick Facts
- *Summary Preview:* What the recruiter is screening for in this round and key logistical details from the JD.
- *Expanded Details:* (These become the mainPoints in the JSON points array)
    - Purpose of the Recruiter Screen: [Explain the main objectives from the
    recruiter's perspective (e.g., verify basic qualifications match JD,
    assess communication skills, gauge enthusiasm/fit signals, confirm
    logistics). Interpret *how* the recruiter will likely evaluate the candidate at this stage based on typical practices.]
    - Key Evaluation Areas: [Summarize the core things the recruiter will likely
    be listening for (e.g., clarity in communication, relevant experience
    keywords aligning with JD, demonstrated interest, alignment on key
    requirements like location/salary, basic cultural fit signals).]
    - Salary Information from JD: [State explicitly if a salary range or specific
    salary information was provided in the JD. If yes, state the
    information. If no, state "Salary information not provided in the JD."]
    - Location & Remote Status from JD: [State explicitly what the JD says about
    location requirements or remote work options. If it's ambiguous or not
    mentioned, state this clearly ("Location/remote status unclear from JD"
    or "Not specified in JD").]
    - Other Logistical Details in JD: [Mention any other logistical requirements
    explicitly stated (e.g., travel requirement, specific certification
    needed for legal/compliance reasons mentioned in JD). State if none
    specified.]

---

*Card 2: Craft Your Introduction*

- **Instruction:** Generate the JSON object for the second sub_module.
- *Title:* Craft Your Introduction
- *Summary Preview:* Guidance on creating a compelling "Tell me about yourself" pitch tailored to this specific role.
- *Expanded Details:* (These become the mainPoints)
    - Strategy for Tailoring Your Pitch: [Explain the importance of tailoring the
    "Tell me about yourself" answer to the specific JD. Advise connecting
    past experience directly to the required skills and responsibilities
    mentioned in the JD (reference key areas from JD analysis if available,
    otherwise infer from typical PM responsibilities). Explain the
    'Past-Present-Future' framework commonly used.]
    - Key Elements to Highlight (Based on JD): [Suggest specific types of
    experiences or skills from a typical PM background (or the candidate's
    resume if provided) that are most relevant to *this specific role* based on keywords, responsibilities, and required qualifications in the JD. Provide examples like "Highlight experience managing [type of
    project from JD]," "Emphasize your skills in [specific required skill
    from JD]."]
    - Connecting Your Experience to the Role's Needs: [Advise using language from the
    JD. For instance, if the JD emphasizes "cross-functional collaboration," suggest framing experiences using similar terms. If it mentions
    "driving impact," suggest concluding points by summarizing the positive
    outcomes of past work.]
    - Practice and Timing: [Advise practicing the pitch to be concise, ideally 2-3
    minutes long, focusing on clarity and enthusiasm, not rushing through
    details.]

---

*Card 3: Predicted Recruiter Questions*

- **Instruction:** Generate the JSON object for the third sub_module.
- *Title:* Predicted Recruiter Questions
- *Summary Preview:* Likely questions you'll be asked, tailored based on the JD and common screening topics.
- *Expanded Details:* (These become the mainPoints, each containing tailored question examples as subPoints)
    - Background and Experience Questions: [Generate 5-6 questions. Tailor these
    questions to probe the candidate's relevant past roles, industry
    experience (if specified or preferred in JD), and how their overall
    background aligns with the basic qualifications listed in the JD.]
    - Role-Specific & Foundational PM Questions: [Generate 4-5 questions. Tailor these
    questions to touch upon the key responsibilities, specific required
    skills/tools/methodologies, and domain expertise mentioned in the JD
    (linking to key areas from JD analysis if available). Keep these at a
    recruiter-level (higher level) check, not deep technical dives.]
    - Teamwork & Collaboration Questions: [Generate 4-5 questions. Tailor these
    questions based on the team structure, reporting lines, and implied
    collaboration style described in the JD (linking to key areas from JD
    analysis if available). Focus on how the candidate interacts with
    others.]
    - Motivation & Company/Product Interest Questions: [Generate 4-5 questions.
    Tailor these questions to ask about the candidate's specific interest in this role, the company, its products, and how their career goals align
    (linking to key areas from JD analysis if available).]
    - General & Logistical Questions: [Generate 3-5 questions. Include standard
    logistical questions not covered in Card 1 (e.g., "What are you looking
    for in terms of company culture?") and wrap up any other general
    questions relevant for screening.]

---

*Card 4: Insightful Questions to Ask*

- **Instruction:** Generate the JSON object for the fourth sub_module.
- *Title:* Insightful Questions to Ask
- *Summary Preview:* Recommended questions to ask the recruiter, tailored to the JD, to show engagement and gather information.
- *Expanded Details:* (These become the mainPoints, each containing tailored question examples as subPoints)
    - Questions About the Role & Team: [Generate 3-4 thoughtful questions about the day-to-day of the role, immediate priorities, team dynamics, or
    specific responsibilities mentioned in the JD that could use
    clarification. Frame these as questions a recruiter *can* likely answer and that show the candidate has thought about the role.]
    - Questions About the Interview Process: [Generate 2-3 essential questions about
    the next steps, number of rounds, timeline, and what the candidate
    should expect in subsequent interviews.]
    - Questions About Company/Team Culture from Recruiter's View: [Generate 2-3
    questions that leverage the recruiter's perspective on the company or
    product team culture, work environment, or values. Tailor if the JD
    hints at a specific culture or way of working (e.g., asking about
    collaboration style if the JD emphasizes it).]
    - Clarifying JD Details or Strategic Context: [Generate 1-2 questions specifically
    designed to clarify something potentially ambiguous or strategic
    mentioned in the JD (linking to key areas from JD analysis if
    available). Frame these as questions stemming from the candidate's
    analysis of the role.]

    ----
    Give me response in this JSON format only:
    {
    "quick_summary": "Very long information description that summarizes all of these cards or sub modules",
    "sub_modules": [
        {
        "title": "Call Rubric & Quick Facts",
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
        "title": "Craft Your Introduction",
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
        "title": "Predicted Recruiter Questions",
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
        "title": "Insightful Questions to Ask",
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
    return recruiter_screen_preparation

def favorite_product_question_fun(data):
    favorite_product_question = '''
    Analyse this entire
    '''+data+'''
    ----
   Card 1: What’s Your Favorite Product?
    - title: "🧠 Overview: “What’s Your Favorite Product?” Interview Question"
    - summary: "A breakdown of one of the most common product management interview questions, why it’s asked, what to expect, variations, and how to answer effectively."
    - details (Map to 'points' array using 'main'/'subPoints'):
        - main: "✅ Summary", subPoints: [
            "This is one of the most common product management interview questions. It seems casual, but it's designed to assess how you think about products, empathize with users, and communicate clearly.",
            "In this module, you’ll learn:",
            "- Why interviewers ask this question",
            "- What to expect during the interview",
            "- Common variations of the question",
            "- Tips for choosing a great product",
            "- An example of how to suggest an improvement"
        ]
        - main: "🤔 Why Do Interviewers Ask This?", subPoints: [
            "This question acts as a low-pressure warm-up to help the interviewer evaluate:",
            "- Your product thinking and user empathy",
            "- Your ability to analyze strengths, weaknesses, and tradeoffs",
            "- Your communication skills and enthusiasm for product work",
            "It’s also a fun way for them to get to know your interests and how you see the world."
        ]
        - main: "📋 What to Expect", subPoints: [
            "- This is often the first real question in a PM interview.",
            "- The conversation usually lasts 5–10 minutes.",
            "- Expect a casual tone, but be ready for deeper follow-ups.",
            "Common follow-up questions include:",
            "- “How would you improve it?”",
            "- “What’s a product you dislike?”",
            "- “How would you measure its success?”",
            "- “What if you were the CEO — what would you change?”"
        ]
        - main: "🔁 Common Variants", subPoints: [
            "Interviewers may tweak the question to test your flexibility. Examples include:",
            "- “What’s your favorite Google product?”",
            "- “What’s your favorite non-tech product?”",
            "- “What are your top 3 favorite products?”",
            "- “What’s a product you hate that others love?”",
            "- “What’s a product with untapped potential?”"
        ]
        - main: "💡 How to Choose a Good Product", subPoints: [
            "Pick something that reflects your:",
            "- Passion — You enjoy using it and have real opinions about it.",
            "- Perspective — You understand its strengths and limitations.",
            "- Personality — It gives insight into how you think and work.",
            "Tips:",
            "✅ You can choose something popular — just add depth to your take.",
            "✅ Obscure products are fine — explain them clearly.",
            "❌ Avoid direct competitors of the company you’re interviewing with.",
            "❌ Avoid products that are too simple to discuss for 5–10 minutes."
        ]
        - main: "✏️ Example Product Improvement", subPoints: [
            "> “One thing I’d improve about Notion is its search experience. Right now, it’s hard to retrieve notes across pages. I’d introduce a lightweight tagging system, like #econ or #design, that automatically groups tagged content into a dynamic dashboard for easier synthesis.”"
        ]
---
Card 2: Favorite Product Answer Framework
    - title: "📘 Title: Answering the “Favorite Product” Interview Question"
    - summary: "Learn a proven 5-step framework to confidently answer the PM interview question: 'What is your favorite product and how would you improve it?'"
    - details (Map to 'points' array using 'main'/'subPoints'):
        - main: "🧠 Subtitle", subPoints: [
            "Use this 5-step framework to stand out with confidence"
        ]
        - main: "🧩 Summary", subPoints: [
            "You’ll learn how to:",
            "- Select the right product (and what to avoid)",
            "- Give a sharp one-sentence intro",
            "- Identify and personalize customer segments",
            "- Tie features to pain points using the PAINO method",
            "- Suggest thoughtful, strategic improvements"
        ]
        - main: "✅ 1. Pick the Right Product", subPoints: [
            "- Choose 3 digital and 1 physical product in advance",
            "- Avoid:",
            "  - Culturally niche tools (e.g., WeChat, rice cookers)",
            "  - Overused answers (e.g., Spotify, Netflix)",
            "- Select products your interviewer likely uses or knows"
        ]
        - main: "🧭 2. Intro in One Sentence", subPoints: [
            "Briefly describe what the product does.",
            "Example:",
            "> “Waze helps users navigate from point A to B using real-time traffic data.”"
        ]
        - main: "👥 3. Define Customer Segments", subPoints: [
            "List 3–4 user types and highlight which one you identify with.",
            "Example:",
            "> “As a new parent, I use Waze to avoid long drives with a crying baby.”"
        ]
        - main: "💢 4. Pain-Driven Features", subPoints: [
            "For each of 3 pain points, follow this formula:",
            "Pain → App Feature → Outcome",
            "- Tie real, emotional user needs to key features",
            "Example:",
            "> “Pain: Traffic stresses me out with kids in the car",
            "> → Feature: Waze reroutes in real time",
            "> → Outcome: I stay calm and get there faster.”"
        ]
        - main: "🔧 5. Suggest Improvements", subPoints: [
            "Use one or more of these 4 angles:",
            "1. 🎯 Align with the company’s mission",
            "2. 🚫 Address unmet user needs",
            "3. 🤖 Add tech-based value (e.g., AI-powered suggestions)",
            "4. 🎧 Improve the end-to-end journey (e.g., music/podcast integrations)"
        ]



    ----
    Give me response in this JSON format only:
    {
    "quick_summary": "Very long information description that summarizes all of these cards or sub modules",
    "sub_modules": [
        {
        "title": "What’s Your Favorite Product?",
"completed":false,
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "Summary",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Why Do Interviewers Ask This?",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "What to Expect",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Common Variants",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "How to Choose a Good Product",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Example Product Improvement",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Answering the 'Favorite Product' Interview Question",
"completed":false,
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "Summary",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "1. Pick the Right Product",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "2. Intro in One Sentence",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "3. Define Customer Segments",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "4. Pain-Driven Features",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "5. Suggest Improvements",
            "subPoints": ["information description 1", "information description 2", "..."]
            }
            "..."
        ]
        }
    ]
    }

    '''
    return favorite_product_question

def product_design_fun(data):
    product_design = '''
    Analyse this entire
    '''+data+'''
    ----
   **Quick Summary**

Please provide a summary of the key learnings from [card 1] [card 2]

---

**Card 1: Overview of Product Design Questions**

**Summary**

Please provide a quick summary of the key learnings from the product design overview.

*Key Points* 

**What to Expect:**
*Describe the typical format of a product design question (e.g., open-ended, problem-solving).
*   List common types of product design questions (e.g., "Design X for Y," "Improve Z," "How would you measure success for W?").
*   Explain the general flow you should follow when answering (mentioning a process like the one we discussed previously, e.g., Clarify, User, Pain Points, Solution, Metrics).

**What Interviewers are Looking For:**

- Explain the core skills and mindsets that interviewers assess through these questions (e.g., Product Sense, User Empathy, Structured Thinking, Problem Solving, Creativity, Communication, Prioritization, Technical Feasibility awareness).
- Describe *how* they look for these qualities during your answer (e.g., through your clarifying questions, your user analysis, the structure of your response, the range of solutions considered, how you justify your choices).

**Sample Answers: "Good" vs. "Great":**

- Choose a single, representative sample product design question (e.g., "Design a product to help people find a hiking trail").
- Provide a "Good" answer to this question. This answer should follow a basic structure but might lack depth, strong rationale, or clear prioritization.
- Provide a "Great" answer to the *same* question. This answer should follow a structured framework rigorously, demonstrate deeper user understanding, stronger rationale for choices, consideration of trade-offs, clearer prioritization, and better communication.
- *Crucially*, provide a clear explanation highlighting the specific differences between the "Good" and the "Great" answer, pointing out *why* the "Great" answer is superior based on the criteria mentioned in the "What Interviewers are Looking For" section.

**Why do companies ask Product Design questions:**

- Explain the purpose of these questions from the company's perspective. Why is this a necessary part of the interview process? (e.g., To simulate real-world problem-solving, assess how candidates think under pressure, see their structured approach, evaluate communication skills, gauge passion for product).Provide any short historical context for such interview question.

**Evaluation Rubric:**

- Outline a hypothetical rubric that interviewers might use to evaluate candidates' answers.
- Break down the evaluation into key criteria (similar to the skills mentioned in section 2, e.g., Problem Framing, User Focus, Solutioning, Communication, Structure).
- For each criterion, briefly describe what different performance levels might look like (e.g., Poor, Good, Great, or similar levels). Provide tangible examples of what demonstrates "Good" vs. "Great" performance for each criterion *within the context of answering a product design question*.

---

**Card 2: How to Answer Product Design Questions**

- Sample LLM response
    
    ![Screen Shot 2025-05-05 at 2.31.44 AM.png](attachment:b212eadf-ffb9-44c1-a3fe-980e47889b5a:Screen_Shot_2025-05-05_at_2.31.44_AM.png)
    

**Summary**

Please provide a summary of the key learnings from the product design framework for answering product design questions

**Optional Instructions**

Act as an instructor explaining "Card 2: How to Answer Product Design Questions".

Teach me the step-by-step framework provided below. For EACH step in the framework, please include the specific examples, advice, rationale, frameworks, and sound bites mentioned in the list under that step.

Explain each step clearly before moving to the next, providing the requested details for each.

**Key points** 

Framework:

- Clarify and get context
    - (Include sample clarifying questions)
- Mission/Vision
    - (Include advice for known company mission)
    - (Include advice for unknown company mission)
- Define Personas (user groups)
    - (Include an example of user groups)
    - (Include advice on identifying groups)
    - (Include an example of prioritization rationale)
    - (Include advice on prioritizing groups)
- User Journey
    - (Include an example of a user journey)
    - (Include advice on articulating the journey)
- Identify User Pain Points and Opportunity Areas
    - (Include example/advice on finding pain points from journey)
    - (Include advice on prioritizing pain points for MVP)
- Brainstorm possible solutions
    - (Include advice on brainstorming a spectrum)
    - (Include advice on evaluating/prioritizing solutions for MVP)
- Define a product vision
    - (Include an example of a product/new feature vision)
- Prioritize features
    - (Include framework/advice on prioritizing features)
- Success Metrics
    - (Include sound bites/advice on defining success metrics)
- draft
    
    Summary
    
    Provide a summary of main takeaways for the product design questions framework below
    
    *Key Points* 
    
    Framework
    
    - Clarify and get context
        - provide sample clarifying questions
    - Mission/Vision
        - provide users advice on how to define the mission of the company if they know the company
        - provide users advice on how to define the mission of the company if they don’t know much about the company
    - Define Personas (user groups)
        - provide an example of defining user groups
        - provide advice on how to think through identifying the user groups
        - provide example of rationale on how to prioritize/choose a user group
        - provide advice on how to prioritize/choose a user group
    - User Journey
        - Provide an example of a user journey
        - Provide advice how to articulate user journey
    - Identify User Pain Points and Opportunity Areas
        - Provide example/advice on how to identify user pain points from the user journey
        - Provide advice on how prioritize pain points for the MVP
    - Brainstorm possible solutions
        - Provide advice on how to brainstorm a spectrum of solutions for the problem
        - Provide advice on how to evaluate prioritize solution (e.g., mission/vision, impact metrics)for the MVP
    - Define a product vision
        - Provide an example of a product/new feature vision
    - Prioritize features
        - Provide framework/advice on how to priortize features (e.g., pros/cons)
    - Success Metrics
        - Provide sound bites on how to define success metric for this new feature/product design
        

---

**Card 3: Sample product design question for [company]**

Based on the [job description] create a mock product design interview question that would be suitable for a candidate applying for this role.

**Card 4: Sample product design question for [company]**

Create a mock product design interview question that would be suitable for a candidate applying for this role focused on the industry based on the [company].

or 

Generate ONE open-ended product design question that:

1. Is highly relevant to the **[Industry Name] industry**.
2. Connects meaningfully to **[Company]** context (even if not directly about their most famous product feature).
3. Aligns with the **focus area, key responsibilities, and target user group** mentioned in the job description context.
4. Requires the candidate to think through a standard product design process (understanding users/problems, brainstorming solutions, considering trade-offs/feasibility, defining success metrics).

    ----
    Give me response in this JSON format only:
    {
    "quick_summary": "Very long information description that summarizes all of these cards or sub modules",
    "sub_modules": [
        {
        "title": "Overview of Product Design Questions",
"completed":false,
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "What to Expect",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "What Interviewers are Looking For",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Sample Answers: "Good" vs. "Great"",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Why do companies ask Product Design questions",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Evaluation Rubric",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "How to Answer Product Design Questions",
"completed":false,
        "summary": "a full summary text of some long length that summarizes all these modules",
        "content": "some full long information text",
        "points": [
            {
            "main": "Clarify and get context",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Mission/Vision",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Define Personas (user groups)",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "User Journey",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Identify User Pain Points and Opportunity Areas",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Brainstorm possible solutions",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Define a product vision",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Prioritize features",
            "subPoints": ["information description 1", "information description 2", "..."]
            },
            {
            "main": "Success Metrics",
            "subPoints": ["information description 1", "information description 2", "..."]
            }
            "..."
        ]
        },
        {
        "title": "Sample product design question for [company]",
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
        "title": "..",
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
    return product_design
