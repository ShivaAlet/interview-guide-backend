from flask import Flask, request, jsonify
import requests
import json
from flask_cors import CORS
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
CORS(app)

api_key = os.getenv("API_KEY")

# API_KEY_1 = os.getenv("API_KEY_1")
# CX_KEY =os.getenv("CX_KEY")
# GOOGLE_API_URL = os.getenv("GOOGLE_API_URL")

# @app.route('/search')
# def search():
#     query = request.args.get('q')
#     if not query:
#         return jsonify({"error": "Query parameter 'q' is required"}), 400

#     params = {
#         'q': query+" linkedin",
#         'key': API_KEY_1,
#         'cx': CX_KEY
#     }

#     response = requests.get(GOOGLE_API_URL, params=params)
#     resultsTitle = []
#     # for item in response.json().items:
#     #     resultsTitle.append(item.title)
#     # resultsWithOnlyTitle = [text for text in resultsTitle if " | LinkedIn" in text]
#     return jsonify({"company_names":response.json()["items"]})

@app.route('/company_research', methods=['POST'])
def company_research():
    required_keys = ["company_name", "job_role", "job_description"]
    data = request.json
    if all(key in data for key in required_keys):
        pass   
    else:
        return {"error": "Missing keys"}, 400
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer "+api_key,
            # "HTTP-Referer": "<YOUR_SITE_URL>",
            # "X-Title": "<YOUR_SITE_NAME>",
        },
        data=json.dumps({
            "model": "google/gemini-2.5-flash-preview",
            "messages": [
                # {"role": "user", "content": "Analyze the provided Company Name ("+data['company_name']+") and the context from the Job Description ("+data["job_description"]+"). Your goal is to generate a comprehensive yet concise research dossier tailored for a ("+data["job_role"]+") role preparing for an interview at this specific company. Please gather information from reliable public sources (like the company's official website, reputable news outlets, financial reports if public). And do not add information that is half information like if url is not provided then do not add info related to the url, if something that is don't know about company then do not add or give false informat. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly but not false information. Result should contain all sub modules and it is fixed : Company Overview, Mission & Culture, Target Market & Customers, Size & Structure, Leadership, Competitive Landscape, Recent News & Developments, Industry Trends, Funding/Financial Health. And give me output only in this JSON format only and this is JSON data of 'COMPANY RESEARCH' only and provide me entire full json data and not half:[{title:'Company Overview',summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Mission & Culture',summary:'',content:'',points:[]}\\}..."}
                {"role": "user", "content": "Analyze the provided Company Name ("+data['company_name']+") and the context from the Job Description ("+data["job_description"]+"). Your goal is to generate a comprehensive yet concise research dossier tailored for a "+data["job_role"]+" role preparing for an interview at this specific company. Please gather information from reliable public sources (like the company's official website, reputable news outlets, financial reports if public).Structure the output into the distinct sections listed below. Present detailed information using bullet points or short paragraphs as appropriate. Ensure the output is cleanly formatted and ready to populate UI cards.---REQUIRED SECTIONS:1. Company Overview • Summary of the company in 1 line • What are their main products/services? • What's their core business model and value proposition? • When were they founded, and what are some key historical milestones? • What's their current market position? 2. Mission & Culture • What are the company's official mission and vision statements? • What are their stated core values? 3. Target Market & Customers • Who are their primary customers (B2B, B2C, specific industries)? • What industries/verticals do they serve? • Any notable public clients?  4. Size & Structure • Approximately how many employees? • Estimated revenue (if public)? • Are they public or private? • Do they have parent companies or subsidiaries? 5. Leadership • Who are the key executives (especially CEO, CPO/Head of Product)? 6. Competitive Landscape • 3–5 main competitors? • What is the company's Unique Selling Proposition or key differentiator? • What are their competitive advantages? 7. Recent News & Developments • Major announcements, product updates, M&A, or partnerships in the last 6–12 months? 8. Industry Trends • What key trends affect the sector they operate in? • How might these represent opportunities or threats?9. Funding/Financial Health • Recent funding history (if private)?• General financial health (if public)?.also search on the entire web and Result should contain all sub modules and it is fixed : Company Overview, Mission & Culture, Target Market & Customers, Size & Structure, Leadership, Competitive Landscape, Recent News & Developments, Industry Trends, Funding/Financial Health. And give me output only in this JSON format only and this is JSON data of 'COMPANY RESEARCH' only and provide me entire full json data and not half:[{title:'Company Overview',summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Mission & Culture',summary:'',content:'',points:[]}\\}..."}
            ]
        })
    )

    return jsonify(json.loads(response.json()["choices"][0]["message"]["content"][8:-4]))

@app.route('/product_research', methods=['POST'])
def product_research():
    required_keys = ["company_name", "job_role", "job_description"]
    data = request.json
    if all(key in data for key in required_keys):
        pass   
    else:
        return {"error": "Missing keys"}, 400
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer "+api_key,
            # "HTTP-Referer": "<YOUR_SITE_URL>",
            # "X-Title": "<YOUR_SITE_NAME>",
        },
        data=json.dumps({
            "model": "google/gemini-2.0-flash-001",
            "messages": [
                {"role": "user", "content": "Analyze the product or service mentioned in the provided Job Description ("+data["job_description"]+") for the company ("+data["company_name"]+"). Your goal is to generate a structured, comprehensive analysis to help a "+data["job_role"]+" role prepare for an interview related to this product."+" .And do not add information that is half information like if url is not provided then do not add info related to the url, if something that is don't know about company then do not add or give false informat. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly but not false information. Result should contain all sub modules and it is fixed : Core Offering, Market Position, Technical Foundation, Business Approach. And give me output only in this JSON format only and this is JSON data of 'PRODUCT RESEARCH' only and provide me entire full json data and not half:[{title:'Core Offering',summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Market Position',summary:'',content:'',points:[]}\\}..."}
            ]
        })
    )

    return jsonify(json.loads(response.json()["choices"][0]["message"]["content"][8:-4]))

@app.route('/job_description_analysis', methods=['POST'])
def job_description_analysis():
    required_keys = ["company_name", "job_role", "job_description"]
    data = request.json
    if all(key in data for key in required_keys):
        pass   
    else:
        return {"error": "Missing keys"}, 400
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer "+api_key,
            # "HTTP-Referer": "<YOUR_SITE_URL>",
            # "X-Title": "<YOUR_SITE_NAME>",
        },
        data=json.dumps({
            "model": "google/gemini-2.0-flash-001",
            "messages": [
                {"role": "user", "content": "Analyze the provided Job Description ("+data["job_description"]+") for the company ("+data["company_name"]+")"+". Your goal is to provide a structured analysis of the role's key elements to help a "+data["job_role"]+" role  understand the specific requirements and expectations for the job"+" .And do not add information that is half information like if url is not provided then do not add info related to the url, if something that is don't know about company then do not add or give false informat. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly but not false information. Result should contain all sub modules and it is fixed : Core Responsibilities, Required Skills, Preferred Qualifications, Success Metrics, Team Structure. And give me output only in this JSON format only and this is JSON data of 'Job Description Analysis' only and provide me entire full json data and not half:[{title:'Core Responsibilities',summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Required Skills',summary:'',content:'',points:[]}\\}..."}
            ]
        })
    )

    return jsonify(json.loads(response.json()["choices"][0]["message"]["content"][8:-4]))

@app.route('/recruiter_screen_preparation', methods=['POST'])
def recruiter_screen_preparation():
    required_keys = ["company_name", "job_role", "job_description","resume"]
    data = request.json
    if all(key in data for key in required_keys):
        pass   
    else:
        return {"error": "Missing keys"}, 400
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer "+api_key,
            # "HTTP-Referer": "<YOUR_SITE_URL>",
            # "X-Title": "<YOUR_SITE_NAME>",
        },
        data=json.dumps({
            "model": "google/gemini-2.0-flash-001",
            "messages": [
                {"role": "user", "content": "Generate a recruiter interview preparation guide tailored for "+data["job_role"]+" position, based on the provided Job Description ("+data["job_description"]+") and Candidate Resume "+data["resume"]+" .And do not add information that is half information like if url is not provided then do not add info related to the url, if something that is don't know about company then do not add or give false informat. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly but not false information. Result should contain all sub modules and it is fixed : Background and Experience, Technical Knowledge, Role-Specific Competencies, Leadership and Collaboration, Company & Product Knowledge Section, Career Vision, General Questions, Questions for Recruiter on Team Structure, Questions for Recruiter on Role Responsibilities, Questions for Recruiter on Company Environment, Questions for Recruiter on Role Purpose, Questions for Recruiter on JD Points. And give me output only in this JSON format only and this is JSON data of 'Recruiter Screen Preparation' only and provide me entire full json data and not half:[{title:'Background and Experience',summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Technical Knowledge',summary:'',content:'',points:[]}\\}..."}
            ]
        })
    )

    return jsonify(json.loads(response.json()["choices"][0]["message"]["content"][8:-4]))

@app.route('/hiring_manager_round', methods=['POST'])
def hiring_manager_round():
    required_keys = ["job_role", "job_description","resume"]
    data = request.json
    if all(key in data for key in required_keys):
        pass   
    else:
        return {"error": "Missing keys"}, 400
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer "+api_key,
            # "HTTP-Referer": "<YOUR_SITE_URL>",
            # "X-Title": "<YOUR_SITE_NAME>",
        },
        data=json.dumps({
            "model": "google/gemini-2.0-flash-001",
            "messages": [
                {"role": "user", "content": "Generate a tailored set of potential interview questions for a "+data["job_role"]+" role Hiring Manager round, based on the provided Job Description "+data["job_description"]+") and Candidate Resume "+data["resume"]+" .And do not add information that is half information like if url is not provided then do not add info related to the url, if something that is don't know about company then do not add or give false informat. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly but not false information. Result should contain all sub modules and it is fixed : Phase 1: Introduction & Background, Phase 2: Product Experience Deep Dives, Phase 3: Product Methodology Assessment, Phase 4: Cross-Functional Collaboration, Phase 5: Strategic Thinking, Phase 6: Technical Understanding, Phase 7: Role-Specific Challenges. And give me output only in this JSON format only and this is JSON data of 'Recruiter Screen Preparation' only and provide me entire full json data and not half:[{title:'Phase 1: Introduction & Background',summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Phase 2: Product Experience Deep Dives',summary:'',content:'',points:[]}\\}..."}
            ]
        })
    )

    return jsonify(json.loads(response.json()["choices"][0]["message"]["content"][8:-4]))

@app.route('/behavioral_interview', methods=['POST'])
def behavioral_interview():
    required_keys = ["job_role", "job_description","resume"]
    data = request.json
    if all(key in data for key in required_keys):
        pass   
    else:
        return {"error": "Missing keys"}, 400
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer "+api_key,
            # "HTTP-Referer": "<YOUR_SITE_URL>",
            # "X-Title": "<YOUR_SITE_NAME>",
        },
        data=json.dumps({
            "model": "google/gemini-2.0-flash-001",
            "messages": [
                {"role": "user", "content": "Generate 15 behavioral questions that focus on: leadership, conflict resolution, failure recovery, crossfunctional collaboration, Decision Making, Communication style, prioritization style for this job description "+data["job_description"]+") Do not mention the category just the questions"+" .And do not add information that is half information like if url is not provided then do not add info related to the url, if something that is don't know about company then do not add or give false informat. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly but not false information. Result should contain all sub modules and it is fixed : STAR Method for Behavioral Questions,Essential Behavioral Interview Questions Decision Making & Problem Solving, Taking Initiative, Customer/Client Focus, Teamwork & Collaboration, Leadership, Adaptability, Results & Accountability, Innovation & Creativity, Communication, Integrity & Ethics. And give me output only in this JSON format only and this is JSON data of 'Behavioral Interview' only and provide me entire full json data and not half:[{title:'STAR Method for Behavioral Questions',summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Essential Behavioral Interview Questions Decision Making & Problem Solving',summary:'',content:'',points:[]}\\}..."}
            ]
        })
    )

    return jsonify(json.loads(response.json()["choices"][0]["message"]["content"][8:-4]))

@app.route('/resume_experience_to_highlight_to_stand_out', methods=['POST'])
def resume_experience_to_highlight_to_stand_out():
    required_keys = [ "job_description","resume"]
    data = request.json
    if all(key in data for key in required_keys):
        pass   
    else:
        return {"error": "Missing keys"}, 400
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer "+api_key,
            # "HTTP-Referer": "<YOUR_SITE_URL>",
            # "X-Title": "<YOUR_SITE_NAME>",
        },
        data=json.dumps({
            "model": "google/gemini-2.0-flash-001",
            "messages": [
                {"role": "user", "content": "Analyze the resume ("+data["resume"]+") and JD ("+data["job_description"]+") and identify the best experiences or skill to highlight to stand out and show the interviewer that you are good fit for the job"+" .And do not add information that is half information like if url is not provided then do not add info related to the url, if something that is don't know about company then do not add or give false informat. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly but not false information. And give me output only in this JSON format only and this is JSON data of 'Resume Experience to highlight To stand out' only and provide me entire full json data and not half:[{title:'some important title..',summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'some important title...',summary:'',content:'',points:[]}\\}..."}
            ]
        })
    )

    return jsonify(json.loads(response.json()["choices"][0]["message"]["content"][8:-4]))

@app.route('/favorite_product_question', methods=['POST'])
def favorite_product_question():
    required_keys = [ ]
    data = request.json
    if all(key in data for key in required_keys):
        pass   
    else:
        return {"error": "Missing keys"}, 400
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer "+api_key,
            # "HTTP-Referer": "<YOUR_SITE_URL>",
            # "X-Title": "<YOUR_SITE_NAME>",
        },
        data=json.dumps({
            "model": "google/gemini-2.0-flash-001",
            "messages": [
                {"role": "user", "content": "You're being asked 'What is your favorite product?' and 'How would you improve your favorite product?' in an interview setting. Your goal is to provide insightful answers that showcase your analytical skills, user-centric thinking, and potential for innovation"+" .And do not add information that is half information like if url is not provided then do not add info related to the url, if something that is don't know about company then do not add or give false informat. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly but not false information. Result should contain all sub modules and it is fixed : Choose Thoughtfully,Explain Your Choice, Focus on Improvement, Justify Your Suggestions, Keep it Concise and Positive. And give me output only in this JSON format only and this is JSON data of 'Favorite Product Question' only and provide me entire full json data and not half:[{title:'Choose Thoughtfully',summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Explain Your Choice',summary:'',content:'',points:[]}\\}..."}
            ]
        })
    )

    return jsonify(json.loads(response.json()["choices"][0]["message"]["content"][8:-4]))

@app.route('/product_design', methods=['POST'])
def product_design():
    required_keys = ["job_role","job_description"]
    data = request.json
    if all(key in data for key in required_keys):
        pass   
    else:
        return {"error": "Missing keys"}, 400
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer "+api_key,
            # "HTTP-Referer": "<YOUR_SITE_URL>",
            # "X-Title": "<YOUR_SITE_NAME>",
        },
        data=json.dumps({
            "model": "google/gemini-2.0-flash-001",
            "messages": [
                {"role": "user", "content": "Generate 5 Product Design type question for a ("+data["job_role"]+") interview based on the company’s industry or product type mentioned in the JD (."+data["job_description"]+")"+" .And do not add information that is half information like if url is not provided then do not add info related to the url, if something that is don't know about company then do not add or give false informat. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly but not false information. And give me output only in this JSON format only and this is JSON data of 'Product Design' only and provide me entire full json data and not half:[{title:'Important title text',summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Important title text',summary:'',content:'',points:[]}\\}..."}
            ]
        })
    )

    return jsonify(json.loads(response.json()["choices"][0]["message"]["content"][8:-4]))


@app.route('/product_sense', methods=['POST'])
def product_sense():
    required_keys = ["job_role","company_name","job_description"]
    data = request.json
    if all(key in data for key in required_keys):
        pass   
    else:
        return {"error": "Missing keys"}, 400
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer "+api_key,
            # "HTTP-Referer": "<YOUR_SITE_URL>",
            # "X-Title": "<YOUR_SITE_NAME>",
        },
        data=json.dumps({
            "model": "google/gemini-2.0-flash-001",
            "messages": [
                {"role": "user", "content": "Generate 4-6 analytical interview questions suitable for a "+data["job_role"]+" role at a company "+data["company_name"]+" and job description ("+data["job_description"]+"). The questions should be composed of: **2-3 Analytical Questions:**, **2-3 A/B Testing Scenarios:**"+" .And do not add information that is half information like if url is not provided then do not add info related to the url, if something that is don't know about company then do not add or give false informat. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly but not false information.And give me output only in this JSON format only and this is JSON data of 'Product Sense' only and provide me entire full json data and not half:[{title:'Important title text',summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Important title text',summary:'',content:'',points:[]}\\}..."}
            ]
        })
    )

    return jsonify(json.loads(response.json()["choices"][0]["message"]["content"][8:-4]))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)