
def company_research_fun(data):
    company_research = '''
    Analyse this entire
    '''+data+'''
    ----
    # Module 1 - **Know the Company**

    **1. Quick Summary (New Feature):**

    - **Purpose:** A ~2-minute overview hitting the absolute must-knows.
    - **Content:**
        - Company's 1-line description.
        - Core product/service category & primary value proposition.
        - Primary target customer type (B2B/B2C, key industry).
        - Top 1-2 competitors.
        - One major recent development (e.g., major launch, acquisition, funding).
    - **UI Implementation:** A prominent button/section at the top of Module 1, perhaps labeled "**View Quick Summary**" or "Key Highlights".

    **Revised Card Structure:**

    - **Card 1: Core Business & Strategy** (Combines Overview aspects + Mission)
        - **title**: "Core Business & Strategy"
        - **summary**: "Understand the company's main offerings, business model, market position, and driving mission."
        - **details**:
            - point: "Company Snapshot", value: [1-line summary]
            - point: "Main Products/Services", value: [List of key offerings]
            - point: "Core Business Model & Value Prop", value: [How they make money, what makes them valuable]
            - point: "Mission Statement", value: [Official mission]
            - point: "Current Market Position", value: [e.g., Leader, Challenger, Niche player in X market]
            - point: "Key Milestones", value: [Brief! e.g., Founded Year, 1-2 major historical points if relevant]
        
    - **Card 2: Target Market & Customers**
        - **title**: "Target Market & Customers"
        - **summary**: "Identify who the company serves and the industries it operates in."
        - **details**:
            - point: "Primary Customers", value: [B2B/B2C, specific segments/personas if known]
            - point: "Industries Served", value: [Key verticals]
            - point: "Notable Clients/Partners", value: [Examples if public, shows validation]
        
    - **Card 3: Competitive Landscape**
        - **title**: "Competitive Landscape"
        - **summary**: "Analyze key competitors and the company's unique positioning."
        - **details**:
            - point: "Main Competitors", value: [List top 3-5 rivals]
            - point: "USP / Key Differentiators", value: [What makes them stand out]
            - point: "Competitive Advantages", value: [e.g., Network effects, tech, brand]

    - **Card 4: Company Vitals**
        - **title**: "Company Vitals"
        - **summary**: "Key facts about the company's size, status, leadership, and financial health."
        - **details**:
            - point: "Size & Status", value: ["Approx X employees", "Public/Private", "HQ: Location"]
            - point: "Structure Notes", value: ["Parent: [Name]" or "Key Subsidiaries: [List]" if relevant, else "Standalone"]
            - point: "Key Leadership", value: ["CEO: [Name]", "Head of Product/CPO: [Name]"]
            - point: "Financial Snapshot", value: ["Recent Funding: [Round/Amount/Date]" or "General health indication"]
    - **Card 5: Recent News & Developments**
        - **title**: "Recent News & Developments"
        - **summary**: "Stay updated on major announcements, product updates, and strategic moves."
        - **details**:
            - point: "Key Recent Events (6-12 mo)", value: [Bullet list: Major product launches, M&A, partnerships, significant news]
        
    - **Card 6: Industry Context**
        - **title**: "Industry Context"
        - **summary**: "Understand the broader market trends affecting the company."
        - **details**:
            - point: "Key Industry Trends", value: [List 2-3 major trends impacting their sector]
            - point: "Opportunities/Threats", value: [How these trends might represent chances or risks for the company]
    ----
    Give me response in this JSON format only:
    {
    "quick_summary": "",
    "sub_modules": [
        {
        "title": "Core Business & Strategy",
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Target Market & Customers",
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Competitive Landscape",
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Company Vitals",
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Recent News & Developments",
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Industry Context",
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
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
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Market Position",
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Product Strategy & Tech",
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Key Trends",
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
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
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Skills & Experience Needed",
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "How Your Impact Will Be Measured",
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Team Structure",
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
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
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Potential Gaps & How to Address",
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            "..."
        ]
        },
        {
        "title": "Standout Experiences to Highlight",
        "summary": "some summary text",
        "content": "some long information text",
        "points": [
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
            },
            {
            "main": "some main title",
            "subPoints": ["information text 1", "information text 2", "..."]
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
