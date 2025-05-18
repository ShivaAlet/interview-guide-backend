import requests
import json
from datetime import datetime
from dotenv import load_dotenv
import myPrompts
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import re
import base64
import os
load_dotenv()

api_key = os.getenv("API_KEY")

def generatePrompts(data):
    data1 = "{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")
    prompts = [
         myPrompts.company_research_fun("{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']),
         myPrompts.product_research_fun("{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']),
         myPrompts.job_description_analysis_fun(data1),
         myPrompts.resume_experience_to_highlight_to_stand_out_fun(data1),
        "{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")+".Your goal is to just Generate entire Output of 'Hiring Manager Round' Array Data. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly. Result should contain all sub modules and it is fixed : 'Phase 1: Introduction & Background', 'Phase 2: Product Experience Deep Dives', 'Phase 3: Product Methodology Assessment', 'Phase 4: Cross-Functional Collaboration', 'Phase 5: Strategic Thinking', 'Phase 6: Technical Understanding', 'Phase 7: Role-Specific Challenges'. And give me JSON data of 'Hiring Manager Round' only and 'STRICTLY do not include any silly mistake in this JSON OUTPUT e.g. brackets, comas, quatations,'\\n'','\\t',etc.' and completed must be 'false' only so provide me entire full JSON Data in this exact JSON format only:{quick_summary:'',sub_modules:[{title:'Phase 1: Introduction & Background',completed:false,summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Phase 2: Product Experience Deep Dives',completed:false,summary:'',content:'',points:[]}\\}...]}",
        "{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")+".Generate 15 behavioral questions that focus on: leadership, conflict resolution, failure recovery, crossfunctional collaboration, Decision Making, Communication style, prioritization style for this job description. Mention all the questions"+". Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly. Result should contain all sub modules and it is fixed : STAR Method for Behavioral Questions,Essential Behavioral Interview Questions Decision Making & Problem Solving, Taking Initiative, Customer/Client Focus, Teamwork & Collaboration, Leadership, Adaptability, Results & Accountability, Innovation & Creativity, Communication, Integrity & Ethics. And give me JSON data of 'Behavioral Interview' only and 'STRICTLY do not include any silly mistake in this JSON OUTPUT e.g. brackets, comas, quatations,'\\n'','\\t',etc.' and completed must be 'false' only so provide me entire full JSON Data in this  exact JSON format only:{quick_summary:'',sub_modules:[{title:'...',completed:false,summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'',completed:false,summary:'',content:'',points:[]}\\}...]}",
        myPrompts.recruiter_screen_preparation_fun(data1),        
        myPrompts.favorite_product_question_fun(data1),
        # "You're being asked 'What is your favorite product?' and 'How would you improve your favorite product?',etc questions. in an interview setting. Your goal is to provide insightful answers that showcase your analytical skills, user-centric thinking, and potential for innovation"+" .Your goal is to just Generate entire Output of 'Favourite Product Questions' Array Data. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly. And give me JSON data of 'Favorite Product Questions' only and 'STRICTLY do not include any silly mistake in this JSON OUTPUT e.g. brackets, comas, quatations,'\\n'','\\t',etc.' and completed must be 'false' only so provide me entire full JSON Data in this exact JSON format only:{quick_summary:'',sub_modules:[{title:'Choose Thoughtfully',completed:false,summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Explain Your Choice',completed:false,summary:'',content:'',points:[]}\\}...]}",
        myPrompts.product_design_fun(data1),
        # "{\\n company_name:'"+data['company_name']+"',\\n company_website:'"+data['company_website']+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")+".Generate 5 Product Design type question for this job role interview based on the company’s industry or product type mentioned in the JD. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly. And give me JSON data of 'Product Design' only and 'STRICTLY do not include any silly mistake in this JSON OUTPUT e.g. brackets, comas, quatations,'\\n'','\\t',etc.' and completed must be 'false' only so provide me entire full JSON Data in this exact JSON format only:{quick_summary:'',sub_modules:[{title:'Important title text',completed:false,summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Important title text',completed:false,summary:'',content:'',points:[]}\\}...]}",
        "{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")+". The questions should be composed of: **2-3 Analytical Questions:**, **2-3 A/B Testing Scenarios:**"+" .  Your goal is to just Generate entire Output of 'Product Sense' Array Data. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly.And give me JSON data of 'Product Sense' only and 'STRICTLY do not include any silly mistake in this JSON OUTPUT e.g. brackets, comas, quatations,'\\n'','\\t',etc.' and *completed must be 'false' only so provide me entire full JSON Data in this exact JSON format only ensure atleast `2 subPoints` should,must be filled in each object of sub_modules*:{quick_summary:'',sub_modules:[{title:'Important title text',completed:false,summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Important title text',completed:false,summary:'',content:'',points:[]}\\}...]}",
        "{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")+".Generate 7 strategic product questions for a this role at this company. Company:... Product: ... Industry: ... Competitors: ... Mix of question types: - Product investment: 'Why should this company continue investing in product?' - Competitive strategy: 'How would you respond to competitor's new features?' - Market expansion: 'Should this company enter new market?' - Metrics & goals: 'What metrics would you track for product?' - Industry trends: 'How should this company adapt to industry trend ?' Make questions specific to real products, competitors, and industry challenges. '+' . Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly.  'STRICTLY do not include any silly mistake in this JSON OUTPUT e.g. brackets, comas, quatations,'\\n'','\\t',etc.' and completed must be 'false' only so provide me entire full JSON Data in this  exact JSON format only:{quick_summary:'',sub_modules:[{title:'some important title..',completed:false,summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'some important title...',completed:false,summary:'',content:'',points:[]}\\}...]}",
        "{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")+".Generate a list of market sizing interview questions that test a candidate's estimation and analytical skills. 'Guidelines • Focus on strategic understanding and market potential, • Cover diverse industries and technologies', 'Question Types 1. Total Addressable Market (TAM) estimates, 2. Revenue potential calculations, 3. User base or adoption rate projections,4. Infrastructure and operational cost estimations'"+" . Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly. And give me JSON data of 'Analytical Estimation' only and 'STRICTLY do not include any silly mistake in this JSON OUTPUT e.g. brackets, comas, quatations,'\\n'','\\t',etc.' and completed must be 'false' only so provide me entire full JSON Data in this  exact JSON format only:{quick_summary:'',sub_modules:[{title:'some important title..',completed:false,summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'some important title...',completed:false,summary:'',content:'',points:[]}\\}...]}",
        "{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")+".Generate a comprehensive list of technical interview questions that probe the candidate's expertise in key areas mentioned in the job description. Question types: high level understanding based questions on key technical concepts mentioned in JD Experience-based scenario questions based on resume, The candidate’s experience collaborating with engineers, Their understanding of technical trade-offs, implementation complexity, or API design Probing questions about past projects that demonstrate proficiency"+" . Add more points,values, etc. as per your understanding and I want entire json data to be more so add accordingly. And give me JSON data of 'Technical' only and 'STRICTLY do not include any silly mistake in this JSON OUTPUT e.g. brackets, comas, quatations,'\\n'','\\t',etc.' and completed must be 'false' only so provide me entire full JSON Data in this  exact JSON format only:{quick_summary:'',sub_modules:[{title:'some important title..',completed:false,summary:'...',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'some important title...',completed:false,summary:'',content:'',points:[]}\\}...]}",
        "{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")+".Generate a list of 15 leadership interview questions that assess the candidate's ability to lead and influence. Question types: Strategic vision and alignment with company goals Experience managing crossfunctional stakeholders Decision-making and prioritization approaches Team leadership and development capabilities Communication and influence strategies Handling organizational challenges and change"+" . Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly.'STRICTLY do not include any silly mistake in this JSON OUTPUT e.g. brackets, comas, quatations,'\\n'','\\t',etc.' and completed must be 'false' only so provide me entire full JSON Data in this  exact JSON format only:{quick_summary:'',sub_modules:[{title:'some important title..',completed:false,summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'some important title...',completed:false,summary:'',content:'',points:[]}\\}...]}"
        ]
    return prompts

def generateCompanyResearchPrompt(data,module):
    data1 = "{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")
    
    company_research=myPrompts.company_research_fun(data1)
    product_research=myPrompts.product_research_fun(data1)
    job_description_analysis=myPrompts.job_description_analysis_fun(data1)
    resume_experience_to_highlight_to_stand_out=myPrompts.resume_experience_to_highlight_to_stand_out_fun(data1)
    hiring_manager_round="{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")+".Your goal is to just Generate entire Output of 'Hiring Manager Round' Array Data. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly. Result should contain all sub modules and it is fixed : 'Phase 1: Introduction & Background', 'Phase 2: Product Experience Deep Dives', 'Phase 3: Product Methodology Assessment', 'Phase 4: Cross-Functional Collaboration', 'Phase 5: Strategic Thinking', 'Phase 6: Technical Understanding', 'Phase 7: Role-Specific Challenges'. And give me JSON data of 'Hiring Manager Round' only and 'STRICTLY do not include any silly mistake in this JSON OUTPUT e.g. brackets, comas, quatations,'\\n'','\\t',etc.' and completed must be 'false' only so provide me entire full JSON Data in this exact JSON format only:{quick_summary:'',sub_modules:[{title:'Phase 1: Introduction & Background',completed:false,summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Phase 2: Product Experience Deep Dives',completed:false,summary:'',content:'',points:[]}\\}...]}"
    behavioral_interview="{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")+".Generate 15 behavioral questions that focus on: leadership, conflict resolution, failure recovery, crossfunctional collaboration, Decision Making, Communication style, prioritization style for this job description. Mention all the questions"+". Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly. Result should contain all sub modules and it is fixed : STAR Method for Behavioral Questions,Essential Behavioral Interview Questions Decision Making & Problem Solving, Taking Initiative, Customer/Client Focus, Teamwork & Collaboration, Leadership, Adaptability, Results & Accountability, Innovation & Creativity, Communication, Integrity & Ethics. And give me JSON data of 'Behavioral Interview' only and 'STRICTLY do not include any silly mistake in this JSON OUTPUT e.g. brackets, comas, quatations,'\\n'','\\t',etc.' and completed must be 'false' only so provide me entire full JSON Data in this  exact JSON format only:{quick_summary:'',sub_modules:[{title:'...',completed:false,summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'',completed:false,summary:'',content:'',points:[]}\\}...]}"
    recruiter_screen_preparation=myPrompts.recruiter_screen_preparation_fun(data1)
    favorite_product_question=myPrompts.favorite_product_question_fun(data1)
    product_design=myPrompts.product_design_fun(data1)
    product_sense="{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")+". The questions should be composed of: **2-3 Analytical Questions:**, **2-3 A/B Testing Scenarios:**"+" .  Your goal is to just Generate entire Output of 'Product Sense' Array Data. Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly.And give me JSON data of 'Product Sense' only and 'STRICTLY do not include any silly mistake in this JSON OUTPUT e.g. brackets, comas, quatations,'\\n'','\\t',etc.' and completed must be 'false' only so provide me entire full JSON Data in this exact JSON format only:{quick_summary:'',sub_modules:[{title:'Important title text',completed:false,summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'Important title text',completed:false,summary:'',content:'',points:[]}\\}...]}",
    product_strategy="{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")+".Generate 7 strategic product questions for a this role at this company. Company:... Product: ... Industry: ... Competitors: ... Mix of question types: - Product investment: 'Why should this company continue investing in product?' - Competitive strategy: 'How would you respond to competitor's new features?' - Market expansion: 'Should this company enter new market?' - Metrics & goals: 'What metrics would you track for product?' - Industry trends: 'How should this company adapt to industry trend ?' Make questions specific to real products, competitors, and industry challenges. '+' . Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly.  'STRICTLY do not include any silly mistake in this JSON OUTPUT e.g. brackets, comas, quatations,'\\n'','\\t',etc.' and completed must be 'false' only so provide me entire full JSON Data in this  exact JSON format only:{quick_summary:'',sub_modules:[{title:'some important title..',completed:false,summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'some important title...',completed:false,summary:'',content:'',points:[]}\\}...]}"
    analytical_estimation="{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")+".Generate a list of market sizing interview questions that test a candidate's estimation and analytical skills. 'Guidelines • Focus on strategic understanding and market potential, • Cover diverse industries and technologies', 'Question Types 1. Total Addressable Market (TAM) estimates, 2. Revenue potential calculations, 3. User base or adoption rate projections,4. Infrastructure and operational cost estimations'"+" . Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly. And give me JSON data of 'Analytical Estimation' only and 'STRICTLY do not include any silly mistake in this JSON OUTPUT e.g. brackets, comas, quatations,'\\n'','\\t',etc.' and completed must be 'false' only so provide me entire full JSON Data in this  exact JSON format only:{quick_summary:'',sub_modules:[{title:'some important title..',completed:false,summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'some important title...',completed:false,summary:'',content:'',points:[]}\\}...]}"
    technical="{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")+".Generate a comprehensive list of technical interview questions that probe the candidate's expertise in key areas mentioned in the job description. Question types: high level understanding based questions on key technical concepts mentioned in JD Experience-based scenario questions based on resume, The candidate’s experience collaborating with engineers, Their understanding of technical trade-offs, implementation complexity, or API design Probing questions about past projects that demonstrate proficiency"+" . Add more points,values, etc. as per your understanding and I want entire json data to be more so add accordingly. And give me JSON data of 'Technical' only and 'STRICTLY do not include any silly mistake in this JSON OUTPUT e.g. brackets, comas, quatations,'\\n'','\\t',etc.' and completed must be 'false' only so provide me entire full JSON Data in this  exact JSON format only:{quick_summary:'',sub_modules:[{title:'some important title..',completed:false,summary:'...',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'some important title...',completed:false,summary:'',content:'',points:[]}\\}...]}"
    leadership="{\\n company_name:'"+data['company_name']+(f",\n company_website:{data.get('company_website', '')}" if data.get("company_website") else "")+"',\\n job_role:'"+data['job_role']+"',\\n job_description:'"+data['job_description']+("',\\n resume:'"+data['resume']+"'\\n }" if data['resume'] else "")+".Generate a list of 15 leadership interview questions that assess the candidate's ability to lead and influence. Question types: Strategic vision and alignment with company goals Experience managing crossfunctional stakeholders Decision-making and prioritization approaches Team leadership and development capabilities Communication and influence strategies Handling organizational challenges and change"+" . Add more points,values, etc. as per your understanding and I want json data to be more so add accordingly.'STRICTLY do not include any silly mistake in this JSON OUTPUT e.g. brackets, comas, quatations,'\\n'','\\t',etc.' and completed must be 'false' only so provide me entire full JSON Data in this  exact JSON format only:{quick_summary:'',sub_modules:[{title:'some important title..',completed:false,summary:'',content:'some text content only',points:[{main:'title of point can be short text or little long short text',subPoints:['value1 can be text only','value2',..]},{main:'',subPoints:['value1',..]},..]},{title:'some important title...',completed:false,summary:'',content:'',points:[]}\\}...]}"
    
    if module=="company_research":
        return company_research
    if module=="product_research":
        return product_research    
    if module=="job_description_analysis":
        return job_description_analysis    
    if module=="resume_experience_to_highlight_to_stand_out":
        return resume_experience_to_highlight_to_stand_out    
    if module=="hiring_manager_round":
        return hiring_manager_round    
    if module=="behavioral_interview":
        return behavioral_interview    
    if module=="recruiter_screen_preparation":
        return recruiter_screen_preparation    
    if module=="favorite_product_question":
        return favorite_product_question    
    if module=="product_design":
        return product_design    
    if module=="product_sense":
        return product_sense    
    if module=="product_strategy":
        return product_strategy    
    if module=="analytical_estimation":
        return analytical_estimation    
    if module=="technical":
        return technical    
    if module=="leadership":
        return leadership    
    return "none"



def get_response(question, results,errorJsons,citations1, index):
    model = "google/gemini-2.5-flash-preview"
    plugins = [{ "id": "web","max_results":10 }] if index == 0 or index == 1 else []
    print(index,model,plugins)
    jdumps = json.dumps({
                        "model": model,
                        "plugins": plugins,
                        "messages": [
                            {"role": "user", "content":question}
                        ],
                        "tools": [
  {
    "type": "function",
    "function": {
      "name": "structured_module_output",
      "description": "",
      "parameters": {
        "type": "object",
        "properties": {
          "quick_summary": {
            "type": "string",
            "description": ""
          },
          "sub_modules": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "title": {
                  "type": "string",
                  "description": ""
                },
                "completed": {
                  "type": "boolean",
                  "description": ""
                },
                "summary": {
                  "type": "string",
                  "description": ""
                },
                "content": {
                  "type": "string",
                  "description": ""
                },
                "points": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "main": {
                        "type": "string",
                        "description": ""
                      },
                      "subPoints": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        },
                        "description": ""
                      }
                    },
                    "required": ["main", "subPoints"]
                  }
                }
              },
              "required": ["title", "completed", "summary", "content", "points"]
            }
          }
        },
        "required": ["quick_summary", "sub_modules"]
      }
    }
  }
],
        "tool_choice": {
            "type": "function",
            "function": {
                "name": "structured_module_output"
            }
        }
                    })
    while True:
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": "Bearer " + api_key,
                },
                data=jdumps
            )
            if index==0 or index==1:
                citations=[]
                for citation in response.json()["choices"][0]["message"]["annotations"]:
                    del citation["url_citation"]["start_index"]
                    del citation["url_citation"]["end_index"]
                    citation=citation["url_citation"]
                    citations.append(citation)
                citations1[index]=citations
            results[index]=json.loads(response.json()["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"])
            break
        except Exception as e:
            # errorJsons[index] = response.json()["choices"][0]["message"]["content"][8:-4]
            print(f"Error occurred: {e}. Retrying in 2 seconds...")

def get_single_response(question):
    while True:
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": "Bearer " + api_key,
                },
                data=json.dumps({
                    "model": "google/gemini-2.0-flash-001",
                    "messages": [
                        {"role": "user", "content": question}
                    ]
                })
            )
            

            return json.loads(response.json()["choices"][0]["message"]["content"][8:-4])
            break  # success, exit loop
        except Exception as e:
            print(f"Error occurred: {e}. Retrying in 2 seconds...")

def checkPromptsResponseData(question):
    try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": "Bearer " + api_key,
                },
                data=json.dumps({
                    "model": "google/gemini-2.0-flash-001",
                    "messages": [
                        {"role": "user", "content": question}
                    ]
                })
            )
            
            print(response.json()["choices"][0]["message"]["content"][8:-4])  # success, exit loop
    except Exception as e:
           print(response.json()["choices"][0]["message"]["content"][8:-4])


# checkPromptsResponseData("Get all interview questions of role Product Manager only in Google only from Glassdoor only")
# checkPromptsResponseData("Provide me all most and recent minimum or more than 50-60 interview questions that are posted from current date to past dates  in glassdoor only of Product Manager Role and Google company in json format only [{quesiton'',date:''\\},{quesiton'',date:''\\},...]")

def structureGuide(results,citations,companyData,id):
    return {
        "id":id,
        "datetime":datetime.now(),
        "companyData":companyData,
        "citations":{
        "company_research": citations[0],
        "product_research": citations[1],
        "job_description_analysis": [],
        "resume_experience_to_highlight_to_stand_out": [],
        "hiring_manager_round": [],
        "behavioral_interview": [],
        "recruiter_screen_preparation": [],
        "favorite_product_question": [],
        "product_design": [],
        "product_sense": [],
        "product_strategy": [],
        "analytical_estimation": [],
        "technical": [],
        "leadership":[]
        },
        "result":{
        "company_research": results[0],
        "product_research": results[1],
        "job_description_analysis": results[2],
        "resume_experience_to_highlight_to_stand_out": results[3],
        "hiring_manager_round": results[4],
        "behavioral_interview": results[5],
        "recruiter_screen_preparation": results[6],
        "favorite_product_question": results[7],
        "product_design": results[8],
        "product_sense": results[9],
        "product_strategy": results[10],
        "analytical_estimation": results[11],
        "technical": results[12],
        "leadership": results[13]
        }
    }

def convert_objectid(obj):
    if "_id" in obj:
        obj["_id"] = str(obj["_id"])
    return obj


def save_service_account_file():
    b64_creds = os.environ.get("GOOGLE_CREDENTIALS_BASE64")
    if not b64_creds:
        raise Exception("Missing GOOGLE_CREDENTIALS_BASE64 environment variable")

    decoded = base64.b64decode(b64_creds)
    file_path = "service_account.json"

    with open(file_path, "wb") as f:
        f.write(decoded)

    return file_path

def fetch_data_and_convert_to_csv(collection):
        # Fetch only the required fields
    cursor = collection.find({}, {'_id': 0, 'name': 1, 'email': 1, 'createdAt': 1})
    data = list(cursor)

    # Convert each document's 'createdAt' to the desired format
    for doc in data:
        if 'createdAt' in doc and isinstance(doc['createdAt'], datetime):
            doc['createdAt'] = doc['createdAt'].strftime('%d %b, %Y %H:%M:%S')
        elif 'createdAt' in doc:
            # In case it's a string from MongoDB, parse it first
            try:
                doc['createdAt'] = datetime.fromisoformat(str(doc['createdAt']).replace('Z', '+00:00')).strftime('%d %b, %Y %H:%M:%S')
            except:
                doc['createdAt'] = ''
    df = pd.DataFrame(data)

    csv_path = "data.csv"
    df.to_csv(csv_path, index=False)
    return csv_path

SCOPES = [os.getenv("GOOGLEAPIDRIVE")]
SERVICE_ACCOUNT_FILE = save_service_account_file()
FOLDER_ID = os.getenv("FOLDER_ID")
CSV_FILE_ID = os.getenv("CSV_FILE_ID")

def upload_csv_to_drive(file_path):
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': 'data.csv',
        'mimeType': 'application/vnd.google-apps.spreadsheet',
        'parents': [FOLDER_ID],
    }

    media = MediaFileUpload(file_path, mimetype='text/csv')

    # If file exists, update it
    if CSV_FILE_ID:
        service.files().update(fileId=CSV_FILE_ID, media_body=media).execute()
    else:
        file = service.files().create(
            body=file_metadata, media_body=media, fields='id'
        ).execute()
        print(f"Uploaded CSV File ID: {file.get('id')}")