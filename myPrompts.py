
def company_research_fun(data):
    # Consider adding role description here if available:
    # role_context = "The target role is a Product Manager focused on ML platforms."
    # Add role_context to the initial instruction if used.

    company_research = '''
 You are an expert research assistant helping a user prepare for a job interview.
Your task is to analyze the provided Job Description (JD), identify the company, research it thoroughly, and generate a detailed JSON output containing key information relevant for interview preparation.

    '''+data+'''
    ----
1.  Identify Company: Use the company name provided by the user as the primary target for research. If a company website URL is also provided (which is optional), use it as the most definitive source to confirm the specific company. Analyze the Job Description (JD) (and the website if provided) to gain crucial contextual understanding (industry, products, location) that helps confirm the specific company, especially for common names or if the website is not available, and guides the subsequent research focus.
2.  Research: Using the identified company, leverage your knowledge base and search capabilities to gather comprehensive information for all the points listed under "Required Information Categories" below. Prioritize information from official company sources (website, LinkedIn, press releases) and reputable business news outlets for accuracy, especially for details like founders, leadership, financials, and key events.
3.  Output Style:
    *   Generate the response exclusively in the JSON format specified at the end. Do not include any text before or after the JSON object.
    *   Populate the quick_summary field with a concise, high-impact overview of the company (~1-2 minutes of talking points). This should provide a rapid understanding of the company's core identity and key activities.
    *   For each sub_module, first populate the subPoints within the points array.
    *   Crucially: Write the content for each item in the subPoints arrays as complete, informative sentences or concise bullet points where a list format is natural (e.g., listing names, competitors, features). Do not write instructions or descriptions like "List the founders" within the subPoints values; instead, provide the actual information (e.g., "The company was founded by Jane Doe and John Smith.").
    *   If specific information for a point cannot be found after searching (especially for founders, specific financials, key leadership, etc.), explicitly state "Information not found" or "Specific details not publicly available" for that subPoint.
    *   After populating the points, generate a concise 2-3 sentence summary for each sub_module that synthesizes the key findings from its points.
    *   Ensure the completed flag remains false in the output JSON structure.

REQUIRED INFORMATION CATEGORIES (Map these to the JSON structure):

*   Quick Summary: A concise, high-impact overview providing a rapid understanding of the company. It should cover: Concise description of the company, Core mission/vision, primary product/service & differentiator, key customer segment & problem solved, and top 1-2 competitors.
*   Company Overview:
    *   Company Snapshot: Concise description of the company.
    *   Origins & Founders: Founding date, location, key founder(s), original vision/inspiration. Actively seek founder names and founding details from reliable sources.
    *   Product & Services Portfolio: Comprehensive list and summary of all products, services, and solutions offered by the company.
*   Target Market & Customers:
    *   Primary Customer Segments: B2B/B2C segments, defining characteristics.
    *   Key Customer Challenges Solved: Problems/needs addressed by products/services.
    *   Key Reasons Customers Choose: Top 2-3 USPs/differentiators.
    *   Key Industries Served: Primary verticals, areas of strategic focus.
    *   Notable Clients: 5-7 significant clients (publicly known), brief interview relevance (e.g., 'Validates enterprise readiness').
*   Competitive Landscape:
    *   Main Competitors: 5-7 significant competitors (or fewer if appropriate), their focus.
    *   Key Differentiators (USPs): 1-3 points making the company stand out.
    *   Competitive Strengths: 1-3 core advantages (e.g., technology, brand).
    *   Potential Weaknesses/Challenges: 1-3 potential vulnerabilities relative to competitors.
*   Org Structure, Leadership & Culture:
    *   Size, Status & Location: Approx Employee Count, Public/Private, HQ, Key Offices.
    *   Organizational Structure: Parent Company, Key Subsidiaries/Divisions, recent restructuring.
    *   Key Leadership: Identify and list the names of key leadership roles: CEO, Head of Product (e.g., CPO), Head of Engineering (e.g., CTO), and other relevant VPs or divisional heads. Actively search company websites, official press releases, and credible professional profiles (like LinkedIn) for these names. State 'Information not found' if a name cannot be definitively identified from reliable sources.
    *   Financial Health & Funding: Recent Funding (Round/Amount/Date/Investors). State 'No recent funding information found' if applicable.","Sentence on Profitability/Revenue trends, if public. State 'Financials not publicly available' if applicable.","Sentence noting other growth signals, if observed.",...]

    ----
    Give me response in this JSON format only. Adhere strictly to the structure provided:
    {
    "quick_summary": "Generated ~2-minute, high-impact overview hitting key interview talking points: mission, product/value, customers, competitors, recent development & implication.",
    "sub_modules": [
        {
        "title": "Company Overview",
"completed":false,
        "summary": "[A generated 2-3 sentence summary of the Company Overview based on its populated points will appear here.]",
        "content": "Detailed textual information synthesized from the points below, forming a coherent narrative about the company's overview.",
        "points": [
            {
            "main": "Company Snapshot",
            "subPoints": ["Complete sentence describing the company."]
            },
            {
            "main": "Origins & Founders",
            "subPoints": ["Sentence about founding date and location","Sentence listing key founder(s) names. State 'Founder information not found' if applicable","Sentence about the original vision or inspiration",...]
            },
            {
            "main": "Product & Services Portfolio",
            "subPoints": ["Sentence(s) describing the range of products/services","Sentence highlighting key offerings or innovation areas",...]
            },
            {
            "main": "Revenue Model",
            "subPoints": ["Sentence explaining the primary revenue generation method","Sentence describing pricing or monetization strategy, if known","Sentence identifying primary income streams, if distinct",...]
            }
        ]
        },
        {
        "title": "Target Market & Customers",
"completed":false,
        "summary": "Generated 2-3 sentence summary of Target Market findings.",
        "content": "Detailed textual information synthesized from the points below, forming a coherent narrative about the company's target market and customers.",
        "points": [
            {
            "main": "Primary Customer Segments",
            "subPoints": ["Sentence describing primary B2B/B2C segments","Sentence highlighting key characteristics/firmographics",...]
            },
            {
            "main": "Key Customer Challenges Solved",
            "subPoints": ["Sentence listing specific problems/needs solved","Sentence describing the core value proposition from the customer view",...]
            },
            {
            "main": "Key Reasons Customers Choose the Company",
            "subPoints": ["Sentence listing the top 2-3 reasons/USPs",...]
            },
            {
            "main": "Key Industries Served",
            "subPoints": ["Sentence listing primary industries/verticals","Sentence noting any strategic focus or significant market share by industry",...]
            },
            {
            "main": "Notable Clients",
            "subPoints": ["List 5-7 significant, publicly known clients as bullet points or sentences. State 'Few notable clients publicly listed' if applicable","Sentence on the potential interview relevance of these clients",...]
            }
        ]
        },
        {
        "title": "Competitive Landscape",
"completed":false,
        "summary": "[Generated 2-3 sentence summary of Competitive Landscape findings.]",
        "content": "Detailed textual information synthesized from the points below, forming a coherent narrative about the company's competitive landscape.",
        "points": [
            {
            "main": "Main Competitors",
            "subPoints": ["List of 5-7 significant competitors (or as many as publicly available) and their primary focus areas.",...]
            },
            {
            "main": "Key Differentiators (USPs)",
            "subPoints": ["What makes the company stand out (1-3 points).",...]
            },
            {
            "main": "Competitive Strengths",
            "subPoints": ["1-3 core advantages of the company.",...]
            },
            {
            "main": "Potential Weaknesses/Challenges",
            "subPoints": ["1-3 potential vulnerabilities relative to competitors.",...]
            }
        ]
        },
        {
        "title": "Org Structure, Leadership & Culture",
"completed":false,
        "summary": "[Generated 2-3 sentence summary of Org Structure, Leadership & Culture findings.]",
        "content": "Detailed textual information synthesized from the points below, forming a coherent narrative about the company's org structure, leadership, and culture.",
        "points": [
            {
            "main": "Size, Status & Location",
            "subPoints": ["Sentence with Approx Employee Count","Sentence with Public/Private Status","Sentence with HQ Location","Sentence with Other Key Office Locations, if relevant",...]
            },
            {
            "main": "Organizational Structure",
            "subPoints": ["Sentence about Parent Company, if any","Sentence about Key Subsidiaries/Divisions, if any","Sentence noting recent restructuring, if known",...]
            },
            {
            "main": "Key Leadership",
            "subPoints": ["CEO: Name or 'Information not found'","CPO/Head of Product: [Name or 'Information not found'","CTO/Head of Engineering: Name or 'Information not found'","Other relevant VPs/Heads: Name or 'Information not found'",...]
            },
            {
            "main": "Financial Health & Funding",
            "subPoints": ["Sentence about Recent Funding (Amount/Date/Investors). State 'No recent funding information found' if applicable.","Sentence on Profitability/Revenue trends, if public. State 'Financials not publicly available' if applicable.","Sentence noting other growth signals, if observed.",...]
            },
            {
            "main": "Company Culture",
            "subPoints": [ "Sentence describing 1-2 inferred cultural aspects based on research","Sentence providing justification/example for the inferred aspects","State 'Limited public information on culture' if necessary",...]
            }
        ]
        },
        {
        "title": "Recent News & Key Developments",
"completed":false,
        "summary": "[A generated 1-2 sentence summary of the key recent events (e.g., funding, launches) based on its populated points will appear here.]",
        "content": "Detailed textual information synthesized from the points below, forming a coherent narrative about recent news and developments.",
        "points": [
            {
            "main": "Key Events",
            "subPoints": [
                 "Factual sentence summarizing Event 1 (e.g., funding, launch, acquisition).","Factual sentence summarizing Event 2","Factual sentence summarizing Event 3","Add up to 2 more relevant recent events, if found","State 'Few major recent events found' if applicable",...
                ]
            }
        ]
        },
        {
        "title": "Industry Context & Company Fit",
"completed":false,
        "summary": "Generated 2-3 sentence summary of Industry Context findings.",
        "content": "Detailed textual information synthesized from the points below, forming a coherent narrative about the industry context and company fit.",
        "points": [
            {
            "main": "Key Industry Trends Impacting the Company",
            "subPoints": [
                "Sentence describing Trend 1","Sentence explaining Trend 1's specific effect on this company","Sentence describing Trend 2","Sentence explaining Trend 2's specific effect on this company",...
                ]
            },
            {
            "main": "Strategic Opportunities",
            "subPoints": ["Sentence identifying 1-2 key growth opportunities based on trends/strengths.",...]
            },
            {
            "main": "Potential Headwinds/Risks",
            "subPoints": ["Sentence identifying 1-2 key risks/challenges based on trends/weaknesses",...]
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
   Primary Goal: Generate a deep analysis of the product ecosystem most relevant to the this role described, tailored for a PM interview perspective, consolidated into 6 insightful cards. The key is to intelligently determine the most likely product focus.

    Step 1: Identify Mentioned Products:
    - Carefully read the Job Description (and Resume) to identify ALL specific products, product lines, platforms, or teams mentioned (e.g., "Search", "Maps", "Assistant", "Cloud Platform"). List them internally.

    Step 2: Determine Primary Focus Product & Contextual Products (PM Role Context):
    - Analyze the JD for PM Responsibility Signals: Look specifically within the "Responsibilities", "What You'll Do", or similar sections for keywords indicating direct ownership or primary focus for the PM role. Prioritize products associated with phrases like:
        - "own the roadmap for [Product X]"
        - "define the strategy for [Product X]"
        - "responsible for the success of [Product X]"
        - "drive the development of [Product X]"
        - "manage the lifecycle of [Product X]"
        - "gather requirements for [Product X]"
    - Identify Primary Focus based on Signals:
        - If one product is clearly associated with these PM responsibility keywords/phrases, designate it as the Primary Focus Product. List any other mentioned products as **Contextual Products.
    - If No Clear Ownership Signal, Analyze JD Emphasis & Resume Alignment:
        - If multiple products are mentioned without clear ownership keywords:
            - Assess which product receives the most emphasis or detailed description within the core responsibilities section of the JD.
            - If a resume is provided, assess if the candidate's experience (e.g., industry, technology, past product types) aligns more strongly with one mentioned product over the others.
            - Prioritize based on this hierarchy: (1st) Strong emphasis in JD Responsibilities, (2nd) Clear alignment with Resume Experience. Designate the product identified via this analysis as the Primary Focus Product. List others as **Contextual Products.
    - Handle Single Mention:
        - If only one product is mentioned throughout the JD, it is the Primary Focus Product.
    - Fallback Logic (If No Specific Product Identified Above):
        - If no specific product is mentioned OR the JD remains vague despite the analysis above:
            - Attempt to identify the company's single main/flagship/core product from General Company Info. Designate it as the Primary Focus Product (Fallback).
            - If no single flagship is clear, identify the relevant product category/business line (e.g., "Cloud Data Services"). Designate this category as the Primary Focus (Category Fallback).

    Step 3: Generate Analysis (Primary Focus + Comparative Mentions):
    - Populate the requested 6-card JSON structure below.
    - The deep analysis in each card should center on the Primary Focus Product/Category determined in Step 2.
    - Crucially: Where relevant within the subPoints for the Primary Focus Product, briefly mention the Contextual Products (identified in Step 2) to provide comparison or show interplay (e.g., "integrates with [Contextual Product]", "unlike [Contextual Product] which focuses on X"). Do not dedicate separate points just for contextual products.
    - *Writing Style Guidance:*
        - *Clarity and Professionalism:* Ensure all output is written in clear, concise, and professional business language.
        - *Descriptive Language:* Instead of very terse points, aim for descriptive phrasing that elaborates slightly to provide better understanding. Use strong verbs and precise terminology.
        - *Complete Thoughts:* Even within bullet points (subPoints), aim for complete thoughts or sentences where appropriate, rather than just keywords, to enhance readability.
        - *Engaging Tone:* While maintaining professionalism, strive for a tone that is informative and engaging for someone preparing for an interview.
        - *Impact-Oriented:* When describing features, benefits, or differentiators, try to convey the impact or "so what?" for the user or customer.

    # Module 2 - Know the Product (Analyze the Key Offering & Ecosystem)

    1. Quick Summary (Executive Overview & Context):

    - Purpose: Provide a concise summary of the analysis below, explicitly stating the context and the reasoning for the product identification strategy used.
    - Content (Populate the 'quick_summary' field in the JSON):
        - Start with the identification statement: Clearly state the Primary Focus Product/Category and specifically explain the reasoning based on Step 2 (e.g., "The JD emphasizes PM ownership ('owning the roadmap') for Search, designating it as the primary focus...", "Multiple products (Search, Maps) were mentioned; **Search is selected as the primary focus due to greater emphasis in the role's responsibilities...", "Based on the candidate's AI background in the resume aligning with mentions of AI features, Search AI initiatives are inferred as the primary focus...", "As no specific product was clearly defined for PM ownership, this analysis focuses on the flagship [Fallback Product Name]...", "JD vague, focusing analysis on the *[Category Fallback]* category...").
        - If Contextual Products exist, list them: (e.g., "...while acknowledging the role interacts with Maps and Assistant.").
        - Summarize Key Findings: Briefly cover the Primary Focus Product's core function & problem solved, target user, key differentiator/USP, market position, latest news/release, and monetization, synthesizing info from the 6 cards.

    6-Card Structure Guidance (Primary Focus + Comparative Mentions):
    For each card below, the 'summary' field should be a dynamically generated 3-5 sentence paragraph. This paragraph must summarize the key findings and main takeaways detailed within that specific card's 'points' (main points and their subPoints) for the [Primary Focus Product].

    - Card 1: Product Identity & Value
        - title: "Product Identity & Value"
        - summary: "Generate a 3-5 sentence summary of this card's key findings regarding the [Primary Focus Product]'s core function, the problems it solves, its unique value proposition, and key differentiators, based on the details provided in the 'points' section of this card."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Core Function", subPoints: ["Clearly articulate the primary purpose and functionality of the [Primary Focus Product].", "Elaborate on the core capability it delivers to users."]
            - main: "Problems Solved", subPoints: ["Detail the top 2-3 specific user pain points or business challenges the [Primary Focus Product] effectively addresses.", "Explain how it alleviates these issues."]
            - main: "Unique Value Proposition (UVP)", subPoints: ["Concisely explain the most compelling reason customers choose the [Primary Focus Product] over alternatives.", "If possible, highlight quantifiable benefits or unique outcomes that underscore its value."]
            - main: "Key Differentiators", subPoints: ["Identify and describe 2-3 distinct aspects or features that clearly differentiate the [Primary Focus Product] in the market.", "Where relevant, briefly illustrate its advantages by comparing with Contextual Products or key competitors (e.g., '...unlike [Contextual Product] which serves X, [Primary Focus Product] excels in Y due to...')."]

    - Card 2: Target Audience & Key Use Cases
        - title: "Target Audience & Key Use Cases"
        - summary: "Generate a 3-5 sentence summary of this card's key findings regarding the [Primary Focus Product]'s target user personas, primary use cases or workflows, and the core 'jobs-to-be-done', based on the details provided in the 'points' section of this card."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Target User Personas", subPoints: ["Provide a clear description of the primary user segment(s) or ideal customer profile for the [Primary Focus Product].", "Include key characteristics or needs relevant to the product."]
            - main: "Key Use Cases / Workflows", subPoints: ["Illustrate the top 2-3 common tasks or workflows where users engage with the [Primary Focus Product].", "Explain how the product facilitates these processes, and note any common integrations or handoffs with Contextual Products (e.g., '...users typically leverage [Primary Focus Product] for initial analysis, then transition to [Contextual Product] for advanced reporting.')."]
            - main: "Jobs-To-Be-Done (JTBD)", subPoints: ["Articulate the fundamental 'job' or underlying need that users are 'hiring' the [Primary Focus Product] to fulfill from their perspective."]

    - Card 3: Market Landscape & Positioning
        - title: "Market Landscape & Positioning"
        - summary: "Generate a 3-5 sentence summary of this card's key findings regarding the [Primary Focus Product]'s direct and indirect competitors, its target market segment and perceived position, and key market trends impacting its ecosystem, based on the details provided in the 'points' section of this card."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Direct Competitors", subPoints: ["For 2-3 key direct competitors: State their name, briefly outline their primary strength or market focus, and explain how the [Primary Focus Product] differentiates itself.", "Example format: '[Competitor Name]: Known for [strength/focus]. [Primary Focus Product] differentiates by [key difference].'"]
            - main: "Indirect Competitors / Alternatives", subPoints: ["Identify other types of solutions or alternative approaches users might consider instead of the [Primary Focus Product].", "Note if Contextual Products might serve as partial alternatives for specific niches or functionalities."]
            - main: "Market Segment & Position", subPoints: ["Clearly define the specific market segment the [Primary Focus Product] targets.", "Describe its perceived market position (e.g., Leader, Challenger, Niche Specialist), citing any supporting evidence if readily available."]
            - main: "Market Trends Impacting Ecosystem", subPoints: ["Discuss 1-2 significant industry or technological trends and explain how they are influencing the [Primary Focus Product] and potentially its related Contextual Products."]

    - Card 4: Strategy, News & Outlook
        - title: "Strategy, News & Outlook"
        - summary: "Generate a 3-5 sentence summary of this card's key findings regarding recent significant news or developments for the [Primary Focus Product], its inferred vision/goal, recent strategic shifts, and potential future directions, based on the details provided in the 'points' section of this card."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Recent Significant News & Developments", subPoints: ["Highlight the most significant recent (last 6-12 months) public announcement, product launch, or impactful company news related to the [Primary Focus Product].", "Summarize its key message and potential implications. If no major specific news, state this clearly."]
            - main: "Inferred Vision/Goal", subPoints: ["Based on public statements, product evolution, and market positioning, articulate what appears to be the long-term strategic vision or aspiration for the [Primary Focus Product]."]
            - main: "Recent Strategic Shifts", subPoints: ["Describe any discernible changes in the [Primary Focus Product]'s strategic direction, target market, or feature development priorities observed in the past 6-12 months."]
            - main: "Potential Future Directions (Ecosystem)", subPoints: ["Speculate on 1-2 plausible future developments or strategic moves for the [Primary Focus Product], considering market trends.", "Explain how these might involve or impact Contextual Products within the ecosystem."]

    - Card 5: Key Features, Technology & Monetization
        - title: "Key Features, Technology & Monetization"
        - summary: "Generate a 3-5 sentence summary of this card's key findings regarding the [Primary Focus Product]'s defining features and their value, strategically important technology, integration ecosystem, and its monetization and pricing strategy, based on the details provided in the 'points' section of this card."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Defining Features & Value", subPoints: ["Showcase 2-3 standout or 'hero' features of the [Primary Focus Product]. For each, briefly describe the feature and clearly explain its contribution to the product's UVP or how it solves a critical user problem."]
            - main: "Relevant Technology", subPoints: ["Discuss any underlying technology that is a core differentiator or strategic asset for the [Primary Focus Product] (e.g., 'Leverages a proprietary AI engine for predictive analytics,' 'Built on a highly scalable serverless architecture enabling global reach'). Avoid generic mentions."]
            - main: "Integration Ecosystem", subPoints: ["Identify key third-party integrations crucial for the [Primary Focus Product]'s functionality or market appeal.", "Emphasize any tight integrations with Contextual Products and the value this provides (e.g., '[Primary Focus Product] offers seamless data synchronization with [Contextual Product], enabling a unified workflow for X and Y.')."]
            - main: "Monetization & Pricing Strategy", subPoints: ["Clearly explain the primary way(s) the [Primary Focus Product] generates revenue (e.g., tiered subscriptions, usage-based billing).", "Provide a brief overview of its pricing model or common tiers."]

    - Card 6: SWOT Analysis (Primary Focus)
        - title: "SWOT Analysis"
        - summary: "Generate a 3-5 sentence summary of this card's key findings regarding the [Primary Focus Product]'s internal strengths, weaknesses, external opportunities, and threats, based on the details provided in the 'points' section of this card."
        - details (Map to 'points' array using 'main'/'subPoints'):
            - main: "Strengths", subPoints: ["Identify and briefly explain 2-3 key internal advantages or core competencies of the [Primary Focus Product] (e.g., 'Strong brand equity and customer loyalty,' 'Proprietary technology offering a significant performance edge')."]
            - main: "Weaknesses", subPoints: ["Identify and briefly explain 2-3 internal limitations or areas for improvement for the [Primary Focus Product] (e.g., 'Perceived high price point compared to emerging competitors,' 'Reliance on a complex legacy system for certain functionalities')."]
            - main: "Opportunities", subPoints: ["Outline 1-2 significant external market opportunities that the [Primary Focus Product] is well-positioned to capitalize on.", "(Consider potential synergies with Contextual Products or emerging market needs)."]
            - main: "Threats", subPoints: ["Describe 1-2 key external threats or challenges that could negatively impact the [Primary Focus Product]'s market position or growth.", "(Consider competitive pressures, including those involving Contextual Products, or shifting technological landscapes)."]
    ----
    in each sub module the completed must be false only
    ----
    Give me response in this JSON format only:
    {
    "quick_summary": "Very long information description that summarizes all of these cards or sub modules",
    "sub_modules": [
        {
        "title": "Product Identity & Value",
"completed":false,
        "summary": "A 3-5 sentence summary of the key findings detailed within this card's 'points' concerning the [Primary Focus Product]. For example: InnovateX Platform primarily serves as a B2B SaaS for project management, solving issues of fragmented data. Its UVP lies in AI-driven analytics, differentiating it through predictive capabilities and a highly customizable workflow unlike basic task managers.",
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
        },
        {
        "title": "Target Audience & Key Use Cases",
"completed":false,
        "summary": "A 3-5 sentence summary of this card's key findings related to its target users, common workflows, and the core problems it solves for them.",
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
            }
        ]
        },
        {
        "title": "Market Landscape & Positioning",
"completed":false,
        "summary": "A 3-5 sentence summary of this card's analysis on the competitive environment, market segment, and relevant trends.",
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
        },
        {
        "title": "Strategy, News & Outlook",
"completed":false,
        "summary": "A 3-5 sentence summary of this card's insights into recent developments, strategic goals, and future potential.",
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
        },
        {
        "title": "Key Features, Technology & Monetization",
"completed":false,
        "summary": "A 3-5 sentence summary of this card's details on defining features, core technology, and business model.",
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
        },
        {
        "title": "SWOT Analysis",
"completed":false,
        "summary": "A 3-5 sentence summary of this card's SWOT analysis (strengths, weaknesses, opportunities, threats).",
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
----
in each sub module the completed must be false only

---
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
