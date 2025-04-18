import express from "express";
import Anthropic from "@anthropic-ai/sdk";
import dotenv from "dotenv";
import cors from "cors";
dotenv.config()

const app = express();
app.use(cors())
app.use(express.json());
app.use(express.urlencoded({extended:true}))

// Initialize Anthropic client
const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});


app.post('/api/company_research', async (req, res) => {
  try {
    const { company_name,job_role,resume,job_description } = req.body;
    
    if (!company_name || !job_role || !resume || !job_description) {
      return res.status(400).json({ error: 'Company name, job role, resume and job description are required fields' });
    }

  let  question = `Analyze the provided Company Name ('${company_name}') and the context from the Job Description ('${job_description}') and my resume is "${resume}". Your goal is to generate a comprehensive yet concise research dossier tailored for a ('${job_role}') role preparing for an interview at this specific company. Please gather information from reliable public sources (like the company's official website, reputable news outlets, financial reports if public). And do not add information that is half information like if url is not provided then do not add info related to the url, if something that is don't know about company then do not add or give false informat. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly but not false information. Result should contain all sub modules and it is fixed : Company Overview, Mission & Culture, Target Market & Customers, Size & Structure, Leadership, Competitive Landscape, Recent News & Developments, Industry Trends, Funding/Financial Health. And give me output only in this JSON format only and this is JSON data of 'COMPANY RESEARCH' only and provide me entire full json data and not half:[{title:'Company Overview',summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Mission & Culture',summary:'',content:'',points:[]}}...`;

     const response = await anthropic.messages.create({
      model: "claude-3-7-sonnet-20250219",
      max_tokens: 4096,
      messages: [{ role: "user", content: question }],
      stream: true
    });

    let fullAnswer = '';

    // Process the stream
    for await (const chunk of response) {
      const chunkText = chunk.delta?.text || "";
      fullAnswer += chunkText;
      
      // Optional: If you want to show progress as it comes in
      // process.stdout.write(chunkText);
    }
    
    // Process the answer like you were doing before
    if (fullAnswer.startsWith('```json')) {
      fullAnswer = fullAnswer.substring(8);
      if (fullAnswer.endsWith('```')) {
        fullAnswer = fullAnswer.slice(0, -3);
      }
    }

    const parsedAnswer = JSON.parse(fullAnswer);
    res.json(parsedAnswer);

  //   let answer =[
  //     {
  //         "title": "Company Overview",
  //         "summary": "HiSurat.com is a Surat-based digital services company offering web development and technology solutions.",
  //         "content": "HiSurat.com provides digital services and expert solutions for businesses and individuals in Surat, India. They appear to be a relatively small technology company offering web development services with a focus on Node.js and JavaScript technologies. The company aims to blend cutting-edge services with expert solutions tailored to meet evolving business needs.",
  //         "points": [
  //             {
  //                 "main": "Service Offerings",
  //                 "subPoints": [
  //                     "Web development services with Node.js specialization",
  //                     "Digital solutions for businesses and individuals",
  //                     "Professional consultancy services",
  //                     "Custom technology solutions"
  //                 ]
  //             },
  //             {
  //                 "main": "Technology Focus",
  //                 "subPoints": [
  //                     "Node.js and JavaScript development",
  //                     "Express.js framework implementation",
  //                     "Database expertise (MongoDB, MySQL, PostgreSQL)",
  //                     "RESTful API development"
  //                 ]
  //             },
  //             {
  //                 "main": "Location & Presence",
  //                 "subPoints": [
  //                     "Based in Surat, Gujarat, India",
  //                     "Likely serves local businesses in the Surat region",
  //                     "May have an online presence to reach broader markets"
  //                 ]
  //             }
  //         ]
  //     },
  //     {
  //         "title": "Mission & Culture",
  //         "summary": "HiSurat.com aims to provide cutting-edge services and expert solutions while maintaining a modern work environment.",
  //         "content": "The company states they are 'dedicated to providing a unique blend of cutting-edge services and expert solutions tailored to meet the evolving needs of businesses and individuals.' Their workplace culture appears to prioritize a casual environment with a standard five-day workweek.",
  //         "points": [
  //             {
  //                 "main": "Company Mission",
  //                 "subPoints": [
  //                     "Providing tailored technology solutions",
  //                     "Meeting evolving needs of clients",
  //                     "Delivering expert digital services",
  //                     "Helping clients achieve success through technology"
  //                 ]
  //             },
  //             {
  //                 "main": "Workplace Environment",
  //                 "subPoints": [
  //                     "Informal dress code - suggesting a casual work atmosphere",
  //                     "5-day work week - standard work schedule",
  //                     "Likely startup or small business atmosphere",
  //                     "Focus on professional service delivery"
  //                 ]
  //             },
  //             {
  //                 "main": "Values & Approach",
  //                 "subPoints": [
  //                     "Emphasis on expertise and professional solutions",
  //                     "Customer-centric service approach",
  //                     "Focus on innovation and cutting-edge technology",
  //                     "Commitment to meeting specific client needs"
  //                 ]
  //             }
  //         ]
  //     },
  //     {
  //         "title": "Target Market & Customers",
  //         "summary": "HiSurat.com appears to target local businesses and individuals in Surat requiring web development and digital services.",
  //         "content": "Based on the company name and job description, HiSurat.com likely focuses on serving businesses and individuals in the Surat region who need web development, digital services, and technology solutions. Their emphasis on Node.js suggests they create modern web applications and services.",
  //         "points": [
  //             {
  //                 "main": "Primary Customer Segments",
  //                 "subPoints": [
  //                     "Local businesses in Surat requiring web solutions",
  //                     "Startups and SMEs needing digital transformation",
  //                     "Individuals requiring professional web services",
  //                     "Organizations seeking Node.js based applications"
  //                 ]
  //             },
  //             {
  //                 "main": "Service Areas",
  //                 "subPoints": [
  //                     "Web application development",
  //                     "Database design and implementation",
  //                     "API development and integration",
  //                     "Digital consultancy services"
  //                 ]
  //             },
  //             {
  //                 "main": "Geographic Focus",
  //                 "subPoints": [
  //                     "Primary focus on Surat, Gujarat",
  //                     "Potentially expanding to nearby regions",
  //                     "May serve remote clients through digital channels"
  //                 ]
  //             }
  //         ]
  //     },
  //     {
  //         "title": "Size & Structure",
  //         "summary": "HiSurat.com appears to be a small company currently hiring for growth.",
  //         "content": "Based on the job posting for a Node.js Developer position, HiSurat.com seems to be a small-sized company looking to expand its development team. The salary range and job requirements suggest they are hiring entry to mid-level professionals.",
  //         "points": [
  //             {
  //                 "main": "Company Size Indicators",
  //                 "subPoints": [
  //                     "Currently hiring for at least one Node.js Developer position",
  //                     "The relatively modest salary range (₹3,60,000 - 7,20,000) suggests a small or growing company",
  //                     "Seeking developers with only 1 year of minimum experience, indicating potentially limited resources for senior hires",
  //                     "Likely has a small team structure common in tech startups or boutique service providers"
  //                 ]
  //             },
  //             {
  //                 "main": "Organizational Structure",
  //                 "subPoints": [
  //                     "Likely has a flat organizational hierarchy typical of small tech companies",
  //                     "Probably maintains a small development team with specific technology focuses",
  //                     "May operate with developers handling multiple responsibilities",
  //                     "Could be organized around project-based teams"
  //                 ]
  //             },
  //             {
  //                 "main": "Growth Phase",
  //                 "subPoints": [
  //                     "Active hiring suggests a growth phase or expansion of services",
  //                     "The company appears to be building its technical capacity",
  //                     "The focus on modern technologies indicates preparation for future projects"
  //                 ]
  //             }
  //         ]
  //     },
  //     {
  //         "title": "Leadership",
  //         "summary": "No specific information is available about HiSurat.com's leadership team.",
  //         "content": "The job posting and available information do not provide details about the company's founders, CEO, or management team. As a seemingly small company in Surat, it may have a simple leadership structure.",
  //         "points": [
  //             {
  //                 "main": "Leadership Structure",
  //                 "subPoints": [
  //                     "Likely has a founder/owner-operated structure common in small businesses",
  //                     "May have a small management team overseeing operations",
  //                     "Could be led by technology professionals with development backgrounds"
  //                 ]
  //             },
  //             {
  //                 "main": "Management Style",
  //                 "subPoints": [
  //                     "The informal dress code suggests a potentially relaxed management approach",
  //                     "Five-day work week indicates standard business operations",
  //                     "Focus on specific technologies may reflect leadership's technical background"
  //                 ]
  //             }
  //         ]
  //     },
  //     {
  //         "title": "Competitive Landscape",
  //         "summary": "HiSurat.com competes in the web development and digital services market in Surat, Gujarat.",
  //         "content": "As a web development company specializing in Node.js in Surat, HiSurat.com likely competes with other local digital agencies, freelancers, and regional technology service providers. The competitive landscape in tier-2 Indian cities like Surat typically features numerous small to medium-sized web development agencies.",
  //         "points": [
  //             {
  //                 "main": "Local Competitors",
  //                 "subPoints": [
  //                     "Other Surat-based web development agencies and digital service providers",
  //                     "Freelance developers and small technology teams",
  //                     "Regional IT service companies extending services to Surat",
  //                     "Digital marketing agencies with web development offerings"
  //                 ]
  //             },
  //             {
  //                 "main": "Competitive Factors",
  //                 "subPoints": [
  //                     "Specialization in Node.js and modern JavaScript frameworks",
  //                     "Focus on providing tailored solutions for specific business needs",
  //                     "Pricing structure (based on the salary range, likely positions as mid-market)",
  //                     "Quality of service and expertise in specific technologies"
  //                 ]
  //             },
  //             {
  //                 "main": "Market Differentiation",
  //                 "subPoints": [
  //                     "Focus on modern technologies (Node.js, Express.js, MongoDB)",
  //                     "Potentially offering specialized consultancy services",
  //                     "Emphasis on meeting evolving business needs",
  //                     "Providing personalized service likely characteristic of smaller agencies"
  //                 ]
  //             }
  //         ]
  //     },
  //     {
  //         "title": "Recent News & Developments",
  //         "summary": "No specific recent news or developments are available for HiSurat.com.",
  //         "content": "The job posting indicates they are currently hiring for a Node.js Developer position, suggesting company growth or expansion of their development team. Beyond this hiring activity, no specific news or recent developments are publicly available.",
  //         "points": [
  //             {
  //                 "main": "Current Hiring Activities",
  //                 "subPoints": [
  //                     "Actively recruiting for a Node.js Developer position",
  //                     "Offering annual CTC of ₹3,60,000 - 7,20,000",
  //                     "Position posted 2 days prior to the job description date",
  //                     "Requiring minimum 1 year of experience"
  //                 ]
  //             },
  //             {
  //                 "main": "Business Focus",
  //                 "subPoints": [
  //                     "Continued emphasis on Node.js and JavaScript technologies",
  //                     "Maintaining focus on web development services",
  //                     "Expanding technical capabilities through hiring"
  //                 ]
  //             }
  //         ]
  //     },
  //     {
  //         "title": "Industry Trends",
  //         "summary": "HiSurat.com operates in the rapidly evolving web development industry focusing on modern JavaScript technologies.",
  //         "content": "The company's focus on Node.js, Express.js, and MongoDB aligns with current industry trends toward JavaScript-based full-stack development. These technologies are particularly relevant for building modern, scalable web applications and microservices architecture.",
  //         "points": [
  //             {
  //                 "main": "Technology Stack Relevance",
  //                 "subPoints": [
  //                     "Node.js continues to be a popular choice for backend development",
  //                     "NoSQL databases like MongoDB are increasingly used for flexible data storage",
  //                     "RESTful APIs remain the standard for web service architecture",
  //                     "JavaScript's dominance in web development continues to grow"
  //                 ]
  //             },
  //             {
  //                 "main": "Market Demand Trends",
  //                 "subPoints": [
  //                     "Increasing demand for full-stack JavaScript developers",
  //                     "Growing need for web applications with real-time features (Node.js specialty)",
  //                     "Rising importance of API-first development approaches",
  //                     "Continued movement toward cloud-based application deployment"
  //                 ]
  //             },
  //             {
  //                 "main": "Regional Industry Context",
  //                 "subPoints": [
  //                     "Growth of technology services in tier-2 Indian cities like Surat",
  //                     "Increasing digital transformation among local businesses",
  //                     "Rising competition among service providers in smaller markets",
  //                     "More businesses seeking custom web applications rather than template solutions"
  //                 ]
  //             }
  //         ]
  //     },
  //     {
  //         "title": "Funding/Financial Health",
  //         "summary": "No specific funding or financial information is publicly available for HiSurat.com.",
  //         "content": "As what appears to be a small service-based company, HiSurat.com likely operates on a service revenue model without disclosed external funding. The salary range offered suggests a small to medium-sized operation with stable but limited financial resources.",
  //         "points": [
  //             {
  //                 "main": "Business Model Indicators",
  //                 "subPoints": [
  //                     "Service-based revenue model typical of web development agencies",
  //                     "Likely operates on project-based billing or retainer contracts",
  //                     "Salary offerings suggest a sustainable but modest financial position",
  //                     "Focus on technical expertise rather than scale suggests boutique service approach"
  //                 ]
  //             },
  //             {
  //                 "main": "Growth Indicators",
  //                 "subPoints": [
  //                     "Current hiring activity suggests business growth or increased project demands",
  //                     "Focus on specific technical skills indicates targeted service expansion",
  //                     "Investment in modern technologies suggests forward-looking financial planning"
  //                 ]
  //             },
  //             {
  //                 "main": "Company Stability",
  //                 "subPoints": [
  //                     "Five-day work week and structured compensation suggest stable operations",
  //                     "Blend of fixed and variable pay in salary structure indicates performance-based financial model",
  //                     "Offering annual contracts with benefits indicates sustainable business operations"
  //                 ]
  //             }
  //         ]
  //     }
  // ]

  // res.json(answer)

  } catch (error) {
    console.error('Error calling Claude API:', error);
    res.status(500).json({ error: 'Failed to get response from Claude' });
  }
});

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});