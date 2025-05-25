from flask import Flask, request, jsonify
import threading
from multiprocessing import Process, Manager
import utils
from datetime import datetime
from flask_cors import CORS
from google.oauth2 import id_token
# from google.auth.transport import requests
import requests
from pymongo import MongoClient
import uuid
from werkzeug.utils import secure_filename
from datetime import datetime
import PyPDF2
import jwt
import json
from bson.json_util import dumps
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import os
from bson import ObjectId
from datetime import datetime, timezone,timedelta
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
CORS(app)

ACCESS_KEY = os.getenv("accessKey")
UPDATE_CSV_KEY = os.getenv("UPDATE_CSV_KEY")
SECRET_KEY=os.getenv("SECRET_KEY")
api_key = os.getenv("API_KEY")

YOUR_GOOGLE_CLIENT_ID=os.getenv("YOUR_GOOGLE_CLIENT_ID")
client = MongoClient(os.getenv("MONGO_URI"))
db = client["Interview_Guide"]
googleAuth = db["googleAuth"]
userNotes = db["userNotes"]

# Temporary folder to save PDFs
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/generate_guide', methods=['POST'])
def all_modules():
    access_key = request.headers.get('x-api-key')

    if access_key != ACCESS_KEY:
        return jsonify({"status": "Not Ok", "error": "Missing or invalid access key"}), 400

    try:
        required_keys = ["company_name", "job_role", "job_description", "token"]
        data = request.form

        if not all(key in data for key in required_keys):
            return jsonify({"error": "Missing keys"}), 400
        
        resume_text = ''
        

        if "resume" in request.files and request.files["resume"].filename != '':
            resume_file = request.files["resume"]

            # Save the file
            filename = secure_filename(resume_file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            resume_file.save(file_path)

            # Extract text from the resume
            reader = PyPDF2.PdfReader(file_path)
            for page in reader.pages:
                resume_text += page.extract_text()

            # Delete the uploaded file after processing
            os.remove(file_path)

        # Use request.form to get 'token'
        token = data.get('token')
        idinfo = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        idinfo = idinfo["idinfo"]
        user_email = idinfo['email']

        user = googleAuth.find_one({"email": user_email})

        if user is None:
            return jsonify({"error": "User not found"}), 404

        if "resume" not in request.files or request.files["resume"].filename == '':
            userHistory=json.loads(dumps(user))["history"]
            existsResumes = []
            for history in userHistory:
                if "companyData" in history and "resume" in history["companyData"] and history["companyData"]["resume"]!="":
                    existsResumes.append(history["companyData"]["resume"])
            if len(existsResumes)==0:
                return jsonify({"status":"Not Ok","error":"Existing resume not found"}),200
            resume_text = existsResumes[-1]

        # Add extracted resume text to data
        updated_data = dict(data)
        updated_data["resume"] = resume_text

        prompts = utils.generatePrompts(updated_data)

        # Using multiprocessing to get responses
        manager = Manager()
        results = manager.list([None] * len(prompts))
        citations = manager.list([None] * len(prompts))
        errorJsons = manager.list([None] * len(prompts))
        processes = []

        for i, prompt in enumerate(prompts):
            process = Process(target=utils.get_response, args=(prompt, results, errorJsons,citations, i))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        idd = str(uuid.uuid4())
        newGuide = utils.structureGuide(list(results),list(citations), updated_data, idd)

        history = user.get("history", [])
        history.append(newGuide)

        result = googleAuth.update_one({"email": user_email}, {"$set": {"history": history}})
        notes = {"guideId":idd,"company_research":[],"product_research":[],"job_description_analysis":[],"resume_experience_to_highlight_to_stand_out":[],"hiring_manager_round":[],"behavioral_interview":[],"recruiter_screen_preparation":[],"favorite_product_question":[],"product_design":[],"product_sense":[],"product_strategy":[],"analytical_estimation":[],"technical":[],"leadership":[]}
        userNotes.insert_one(notes)
        if result.matched_count:
            return jsonify({"status": "Ok", "message": "User updated", "history": history, "guide": newGuide,"notes":utils.convert_objectid(notes)})
        else:
            return jsonify({"error": "Failed to update user history"}), 500
    
    except ExpiredSignatureError:
        if 'file_path' in locals() and os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({"status":"Not Ok",'error': 'Token has expired'}), 401
    except InvalidTokenError:
        if 'file_path' in locals() and os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({"status":"Not Ok",'error': 'Invalid token'}), 401
    except Exception as e:
        if 'file_path' in locals() and os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({"status": "Not Ok", "error": str(e)}), 400

@app.route('/save_guide', methods=['POST'])
def save_guide():
    access_key = request.headers.get('x-api-key')

    if access_key != ACCESS_KEY:
        return jsonify({"status": "Not Ok", "error": "Missing or invalid access key"}), 400

    try:
        required_keys = ["company_name", "job_role", "job_description", "token","guideId"]
        data = request.form

        if not all(key in data for key in required_keys):
            return jsonify({"error": "Missing keys"}), 400
        
        resume_text = ''
        

        if "resume" in request.files and request.files["resume"].filename != '':
            resume_file = request.files["resume"]

            # Save the file
            filename = secure_filename(resume_file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            resume_file.save(file_path)

            # Extract text from the resume
            reader = PyPDF2.PdfReader(file_path)
            for page in reader.pages:
                resume_text += page.extract_text()

            # Delete the uploaded file after processing
            os.remove(file_path)

        # Use request.form to get 'token'
        token = data.get('token')
        idinfo = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        idinfo = idinfo["idinfo"]
        user_email = idinfo['email']

        user = googleAuth.find_one({"email": user_email})

        if user is None:
            return jsonify({"error": "User not found"}), 404

        if "resume" not in request.files or request.files["resume"].filename == '':
            userHistory=json.loads(dumps(user))["history"]
            existsResumes = []
            for history in userHistory:
                if "companyData" in history and "resume" in history["companyData"] and history["companyData"]["resume"]!="":
                    existsResumes.append(history["companyData"]["resume"])
            if len(existsResumes)==0:
                return jsonify({"status":"Not Ok","error":"Existing resume not found"}),200
            resume_text = existsResumes[-1]

        # Add extracted resume text to data
        guide = {"id":data["guideId"],"datetime":datetime.now(),"result":{}}
        guide["companyData"] = dict(data)
        del guide["companyData"]["token"]
        del guide["companyData"]["guideId"]
        guide["companyData"]["resume"] = resume_text

        history = user.get("history", [])
        history.append(guide)

        googleAuth.update_one({"email": user_email}, {"$set": {"history": history}})

        return jsonify({"status":"Ok","message":"Guide Saved Successfully"})
    
    except ExpiredSignatureError:
        if 'file_path' in locals() and os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({"status":"Not Ok",'error': 'Token has expired'}), 401
    except InvalidTokenError:
        if 'file_path' in locals() and os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({"status":"Not Ok",'error': 'Invalid token'}), 401
    except Exception as e:
        if 'file_path' in locals() and os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({"status": "Not Ok", "error": str(e)}), 400

@app.route('/generate_guide/<module_name>', methods=['POST'])
def single_module(module_name):
    access_key = request.headers.get('x-api-key')

    if access_key != ACCESS_KEY:
        return jsonify({"status": "Not Ok", "error": "Missing or invalid access key"}), 400

    try:
        required_keys = ["token","guideId"]
        data = request.form

        if not all(key in data for key in required_keys):
            return jsonify({"error": "Missing keys"}), 400
        
        module_names = ["company_research","product_research","job_description_analysis","resume_experience_to_highlight_to_stand_out","hiring_manager_round","behavioral_interview","recruiter_screen_preparation","favorite_product_question","product_design","product_sense","product_strategy","analytical_estimation","technical","leadership"]
        
        if module_name not in module_names:
            return jsonify({"status": "Not Ok", "error": "incorrect module name"})
            

        # Use request.form to get 'token'
        token = data.get('token')
        idinfo = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        idinfo = idinfo["idinfo"]
        user_email = idinfo['email']

        user = googleAuth.find_one({"email": user_email})

        if user is None:
            return jsonify({"error": "User not found"}), 404

        history = user.get("history", [])
        guide = {}
        for historyObj in history:
            if "id" in historyObj and historyObj["id"]==data["guideId"]:
                guide = historyObj
                break
            elif history[-1]==historyObj:
                return jsonify({"status":"Not Ok","error":"guide not found with this id"})


        prompt = utils.generateCompanyResearchPrompt(guide["companyData"],module_name)

        guide["result"][f'{module_name}']=utils.get_single_response(prompt)

        history = user.get("history", [])
        updatedHistory = []
        for historyObj in history:
            if historyObj["id"]==guide["id"]:
                updatedHistory.append(guide)
            else:   
                updatedHistory.append(historyObj)

        result = googleAuth.update_one({"email": user_email}, {"$set": {"history": updatedHistory}})

        if result.matched_count:
            return jsonify({"status": "Ok", "message": "User updated", "history": history, f"{module_name}": guide["result"][f'{module_name}']})
        else:
            return jsonify({"error": "Failed to update user history"}), 500
    
    except ExpiredSignatureError:
        return jsonify({"status":"Not Ok",'error': 'Token has expired'}), 401
    except InvalidTokenError:
        return jsonify({"status":"Not Ok",'error': 'Invalid token'}), 401
    except Exception as e:
        return jsonify({"status": "Not Ok", "error": str(e)}), 400

@app.route('/check_resume', methods=['POST'])
def check_resume():
    access_key = request.headers.get('x-api-key')

    if access_key != ACCESS_KEY:
        return jsonify({"status": "Not Ok", "error": "Missing or invalid access key"}), 400

    try:
        required_keys = ["token"]
        data = request.form

        if not all(key in data for key in required_keys):
            return jsonify({"error": "Missing keys"}), 400
        
        resume_text = ''
        
        # Use request.form to get 'token'
        token = data.get('token')
        idinfo = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        idinfo = idinfo["idinfo"]
        user_email = idinfo['email']

        user = googleAuth.find_one({"email": user_email})

        if user is None:
            return jsonify({"error": "User not found"}), 404

        if "resume" not in request.files or request.files["resume"].filename == '':
            userHistory=json.loads(dumps(user))["history"]
            existsResumes = []
            for history in userHistory:
                if "companyData" in history and "resume" in history["companyData"] and history["companyData"]["resume"]!="":
                    existsResumes.append(history["companyData"]["resume"])
            if len(existsResumes)==0:
                return jsonify({"status":"Not Ok","message":"Existing resume not found"}),200
        return jsonify({"status":"Ok","message":"Resume exists"}),200

    except ExpiredSignatureError:
        return jsonify({"status":"Not Ok",'error': 'Token has expired'}), 401
    except InvalidTokenError:
        return jsonify({"status":"Not Ok",'error': 'Invalid token'}), 401
    except Exception as e:
        return jsonify({"status": "Not Ok", "error": str(e)}), 400
 
@app.route('/google-login', methods=['POST'])
def google_login():
    access_key = request.headers.get('x-api-key')

    if access_key!=ACCESS_KEY:
        return jsonify({"status":"Not Ok","error": "missing or invalid access key"}), 400

    token = request.json.get('token')
    try:
        idinfo = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        idinfo = idinfo["idinfo"]
        user_email = idinfo['email']
        user_name = idinfo['name']
        user = googleAuth.find_one({"email": user_email})
        if user is None:
            user={"name":user_name,"email":user_email,"credits":100,"history":[],"createdAt":datetime.now()}
            googleAuth.insert_one(user)
        uNotes = []
        for notes in userNotes.find({}):
            if len(notes['company_research'])>0 or len(notes['product_research'])>0 or len(notes['job_description_analysis'])>0 or len(notes['resume_experience_to_highlight_to_stand_out'])>0 or len(notes['leadership'])>0 or len(notes['behavioral_interview'])>0 or len(notes['recruiter_screen_preparation'])>0 or len(notes['favorite_product_question'])>0 or len(notes['product_design'])>0 or len(notes['product_sense'])>0 or len(notes['product_strategy'])>0 or len(notes['analytical_estimation'])>0 or len(notes['technical'])>0:
                uNotes.append({"guideId":notes["guideId"],"haveNotes":True})
            else:
                uNotes.append({"guideId":notes["guideId"],"haveNotes":False})
        filteredNotes = []
        for uNote in user["history"]:
            filteredNotes.append(uNote["id"])

        haveNotes = []
        for note in uNotes:
            if note["guideId"] in filteredNotes:
                haveNotes.append(note)

        return jsonify({"status":"Ok","message": "Login Successful", "user":utils.convert_objectid(user),"uNotes":haveNotes})
    except ExpiredSignatureError:
        return jsonify({"status":"Not Ok",'error': 'Token has expired'}), 401
    except InvalidTokenError:
        return jsonify({"status":"Not Ok",'error': 'Invalid token'}), 401
    except Exception as e:
        return jsonify({"status":"Not Ok","error": str(e)}), 400

@app.route('/generate-token', methods=['POST'])
def generate_token():
    # Normally, you'd first verify the Google token here.
    # Let's assume you verified and have the user info:
    access_key = request.headers.get('x-api-key')

    if access_key != ACCESS_KEY:
        return jsonify({"status": "Not Ok", "error": "Missing or invalid access key"}), 400
    # Create your own payload
    payload = {
        'idinfo': request.json,
        'exp': datetime.now(timezone.utc) + timedelta(days=7),  # Token expires in 7 days
        'iat': datetime.now(timezone.utc)  # Issued at
    }

    # Encode the token
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return jsonify({"status":"Ok","token": token})

@app.route("/guide/<id>",methods=['GET'])
def get_guide(id):
    access_key = request.headers.get('x-api-key')

    if access_key!=ACCESS_KEY:
        return jsonify({"status":"Not Ok","error": "missing or invalid access key"}), 400
    try:        
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(" ")[1] 
            idinfo = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            idinfo = idinfo["idinfo"]
            user_email = idinfo['email']
            user = googleAuth.find_one({"email": user_email})
            if user is None:
                return jsonify({"error": "User not found"}), 404
            history = user["history"]
            guide=next((g for g in history if g["id"] == id), None)
            uNotes = userNotes.find_one({"guideId":id})
            if guide:
                notes = {"guideId":id,"company_research":[],"product_research":[],"job_description_analysis":[],"resume_experience_to_highlight_to_stand_out":[],"hiring_manager_round":[],"behavioral_interview":[],"recruiter_screen_preparation":[],"favorite_product_question":[],"product_design":[],"product_sense":[],"product_strategy":[],"analytical_estimation":[],"technical":[],"leadership":[]}
                if uNotes is None:
                    userNotes.insert_one(notes)
                else:
                    notes=uNotes
                return jsonify({"status":"Ok","guide":guide,"notes":utils.convert_objectid(notes)}), 200
            else:
                return jsonify({"status":"Not Ok",'error': 'Guide not found with this id'}), 401
        else:
            return jsonify({"status":"Not Ok",'error': 'Authorization header missing'}), 401
    except ExpiredSignatureError:
        return jsonify({"status":"Not Ok",'error': 'Token has expired'}), 401
    except InvalidTokenError:
        return jsonify({"status":"Not Ok",'error': 'Invalid token'}), 401
    except Exception as e:
        return jsonify({"status":"Not Ok","error": "Invalid token","error":str(e)}), 400
    
@app.route("/get_notes/<id>",methods=['GET'])
def get_notes(id):
    access_key = request.headers.get('x-api-key')

    if access_key!=ACCESS_KEY:
        return jsonify({"status":"Not Ok","error": "missing or invalid access key"}), 400
    try:        
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(" ")[1] 
            idinfo = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            idinfo = idinfo["idinfo"]
            user_email = idinfo['email']
            user = googleAuth.find_one({"email": user_email})
            if user is None:
                return jsonify({"error": "User not found"}), 404
            uNotes = userNotes.find_one({"guideId":id})
            return jsonify({"status":"Ok","notes":utils.convert_objectid(uNotes)}), 200
        else:
            return jsonify({"status":"Not Ok",'error': 'Authorization header missing'}), 401
    except ExpiredSignatureError:
        return jsonify({"status":"Not Ok",'error': 'Token has expired'}), 401
    except InvalidTokenError:
        return jsonify({"status":"Not Ok",'error': 'Invalid token'}), 401
    except Exception as e:
        return jsonify({"status":"Not Ok","error": "Invalid token","error":str(e)}), 400
    
@app.route("/save_note/<guideId>/<moduleName>",methods=['POST'])
def save_note(guideId,moduleName):
    access_key = request.headers.get('x-api-key')

    if access_key!=ACCESS_KEY:
        return jsonify({"status":"Not Ok","error": "missing or invalid access key"}), 400
    try:   
        required_keys = ["note"]
        data = request.json

        if not all(key in data for key in required_keys):
            return jsonify({"error": "Missing keys"}), 400     
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(" ")[1] 
            idinfo = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            idinfo = idinfo["idinfo"]
            user_email = idinfo['email']
            user = googleAuth.find_one({"email": user_email})
            if user is None:
                return jsonify({"error": "User not found"}), 404
            uNotes = userNotes.find_one({"guideId":guideId})
            if uNotes is None:
                 return jsonify({"status":"Not Ok","error":"Notes not found for this Id"}), 404
            notes = uNotes
            del notes["_id"]
            notes[moduleName]=data["note"]
            userNotes.update_one({"guideId":guideId},{"$set":notes})
            return jsonify({"status":"Ok","message":"Note Saved successfully"}), 200
        else:
            return jsonify({"status":"Not Ok",'error': 'Authorization header missing'}), 401
    except ExpiredSignatureError:
        return jsonify({"status":"Not Ok",'error': 'Token has expired'}), 401
    except InvalidTokenError:
        return jsonify({"status":"Not Ok",'error': 'Invalid token'}), 401
    except Exception as e:
        return jsonify({"status":"Not Ok","error": "Invalid token","error":str(e)}), 400
    
@app.route("/guide/<id>", methods=["DELETE"])
def delete_guide(id):
    access_key = request.headers.get('x-api-key')

    if access_key != ACCESS_KEY:
        return jsonify({"status": "Not Ok", "error": "missing or invalid access key"}), 400
    try:
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(" ")[1]
            idinfo = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            idinfo = idinfo["idinfo"]
            user_email = idinfo['email']
            user = googleAuth.find_one({"email": user_email})
            if user is None:
                return jsonify({"error": "User not found"}), 404
            history = user.get("history", [])
            guide_index = next((index for index, g in enumerate(history) if g["id"] == id), None)
            if guide_index is not None:
                # Remove the guide from history
                history.pop(guide_index)
                # Update the user's history in database
                googleAuth.update_one(
                    {"email": user_email},
                    {"$set": {"history": history}}
                )
                uNotes = userNotes.find_one({"guideId":id})
                if uNotes is not None:
                    userNotes.delete_one({"guideId":id})
                return jsonify({"status": "Ok", "message": "Guide deleted successfully"}), 200
            else:
                return jsonify({"status": "Not Ok", "error": "Guide not found with this id"}), 401
        else:
            return jsonify({"status": "Not Ok", "error": "Authorization header missing"}), 401
    except ExpiredSignatureError:
        return jsonify({"status": "Not Ok", "error": "Token has expired"}), 401
    except InvalidTokenError:
        return jsonify({"status": "Not Ok", "error": "Invalid token"}), 401
    except Exception as e:
        return jsonify({"status": "Not Ok", "error": str(e)}), 400

@app.route("/markcomplete/<guideId>/<mainModule>/<subModuleInd>",methods=["PUT"])
def mark_as_complete(guideId,mainModule,subModuleInd):
    access_key = request.headers.get('x-api-key')

    if access_key != ACCESS_KEY:
        return jsonify({"status": "Not Ok", "error": "missing or invalid access key"}), 400
    try:
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(" ")[1]
            idinfo = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            idinfo = idinfo["idinfo"]
            user_email = idinfo['email']
            user = googleAuth.find_one({"email": user_email})
            if user is None:
                return jsonify({"error": "User not found"}), 404
            history = user.get("history", [])
            guide=next((g for g in history if g["id"] == guideId), None)
            if guide:
                if mainModule not in guide["result"]:
                    return jsonify({"status":"Not Ok",'error': 'Module not found with this id'}), 401
                if int(subModuleInd) >= len(guide["result"][mainModule]["sub_modules"]):
                    return jsonify({"status":"Not Ok",'error': 'index overlaps'}), 401
                for myGuide in history:
                    if myGuide["id"]==guide["id"]:
                        myGuide["result"][mainModule]["sub_modules"][int(subModuleInd)]["completed"]=True
                        break
                googleAuth.update_one({"email":user_email},{"$set":{"history":history}})
                return jsonify({"status": "Ok","message": "Sub Module marked successfully"}), 200
            else:
                return jsonify({"status":"Not Ok",'error': 'Guide not found with this id'}), 401
        else:
            return jsonify({"status": "Not Ok", "error": "Authorization header missing"}), 401
    except ExpiredSignatureError:
        return jsonify({"status": "Not Ok", "error": "Token has expired"}), 401
    except InvalidTokenError:
        return jsonify({"status": "Not Ok", "error": "Invalid token"}), 401
    except Exception as e:
        return jsonify({"status": "Not Ok", "error": str(e)}), 400

@app.route('/update-csv', methods=['GET'])
def update_csv():
    updatecsvkey = request.args.get('updatecsvkey')
    if not updatecsvkey:
        return jsonify({'error': 'Missing required parameter: updatecsvkey'}), 400
    
    if updatecsvkey!=UPDATE_CSV_KEY:
        return jsonify({'error': 'incorrect csv key'}), 400

    file_path = utils.fetch_data_and_convert_to_csv(googleAuth)
    utils.upload_csv_to_drive(file_path)
    return {"message": "CSV updated in Google Drive successfully!"}, 200

# @app.route("/test_response",methods=['POST'])
# def test_response():
#     try:
#         data1=request.form
        
#         response = requests.post(
#                     url="https://openrouter.ai/api/v1/chat/completions",
#                     headers={
#                         "Authorization": "Bearer " + api_key,
#                     },
#                     data=json.dumps({
#                         "model": "google/gemini-2.5-flash-preview",
#                         "plugins": [{ "id": "web","max_results":10 }],
#                         "messages": [
#                             {"role": "user", "content": (f'''
#    You are an expert research assistant helping a user prepare for a job interview.
# Your task is to identify the company, research it thoroughly, and generate a detailed JSON output containing key information relevant for interview preparation.
#     {str(data1)}'''
#     '''
#     ----
# *INSTRUCTIONS:*

# 1. Identify Company:
#     - Start with the 'COMPANY NAME' provided in the input as the primary candidate.
#     - **Crucially, use the 'COMPANY WEBSITE' (if available in the input) to disambiguate this name.** Analyze its domain to distinguish this specific company from others that might share a similar name. This step is vital for pinpointing the exact entity the user is referring to.
#     - Further refine and confirm the specific company identity by analyzing the 'JOB DESCRIPTION'. Look for contextual clues (industry, services mentioned, specific technologies, location if relevant) that align with the website information and the provided company name, helping to resolve any remaining ambiguity.
#     - Your objective is to accurately determine and confirm the single, specific company entity intended by the user for subsequent research.

# Research: **Using the identified company name, leverage your general knowledge base for a foundational understanding of the company (e.g., its industry, general product categories, common perceptions). However, to ensure the highest accuracy and up-to-date information for specific factual and potentially time-sensitive details, you **must prioritize and actively employ your searching grounding (searching the internet) capabilities.** Aim for comprehensive information, using search to validate, update, or find details that are likely to be current or highly specific.This approach is especially critical for gathering precise information on:

# - Mission & Values
# - Founding Team - Company founding date & Key founder(s)
# - Products & Services Offered
# - Business Model & Market Footprint
# - Recent funding rounds (including amounts, dates, and key investors, if publicly available)
# - Key recent events (e.g., significant news, major product launches, acquisitions, strategic partnerships, ideally within the last 1-2 years)
# - Current key leadership roles and names (e.g., CEO, CPO, CTO)
# - Specific financial details (e.g., revenue trends if public, latest valuation if reported)
# - Notable clients/customers (verifying publicly acknowledged relationships)

# -----

# REQUIRED INFORMATION CATEGORIES (Map these to the JSON structure):

# - ***Quick Summary:*** High-impact overview (~2 mins) covering: What the company does, its primary product/service, key customer segment & problem solved & company's advantage
# - **Company Overview:**
#     - **Company Snapshot:** 3–4 sentence summary explaining what the company does, its core product or service, key innovation, and why it matters in its industry
#     - **Mission & Values: Instruction - This information should not be inferred or guessed, it should be searched on the web for the most accurate result**
#         - Mission: 1 sentence stating the mission of the company if available
#         - Vision: 1 sentence stating the vision of the company if available
#         - Values: List all the values of the company
#     - **Founding Team:** String (In 1-2 sentences, state the *year* Alloy was founded and list *all the names* *e.g. name(job title)* of its founders entirely from web search) e.g. *The founders of company_name are name1(job title), name2(job title), name3(job title),etc.*
# - **Products & Services Offered: Instruction:** Identify and list the company's key, distinct products and/or service lines. Aim to list all major offerings unless the company's portfolio is significantly smaller or larger (in which case, adjust to accurately represent their main offerings). For each offering, provide a concise 1-2 line description of what the product or service is and what it does. Information should be sourced primarily from searching the internet - the company's official website (e.g., "Products," "Services," "Solutions" pages) or your own knowledge base (if its up to date)
#     - [Product/Service Name 1:** [Concise 1-2 sentence description of Product/Service 1.]
#     - [Product/Service Name 2:** [Concise 1-2 sentence description of Product/Service 2.] ad keep repeat for all offerings found
# - **Business Model & Company Financials:**
#     - **Business Model & Monetization: 1- 3 points outlining what is the b primary business model of the company**
#     - **Financials & Funding:** Recent Funding (Round/Amount/Date/Investors). Instruction - Focus on the last [n] funding round and focus on getting the latest data.
#     - **Revenue:** *Please provide the latest funding amount, date, and valuation for company_name entirely from web search*.
# - **Target Market & Customers:**
#     - Primary Customer Segments: Provide a 3-5 sentence summary of key industries, sectors or target market that the company serves, if they serve multiple industries then focus on the main industry they serve with the product mentioned in the job description. A
#     - Key Customer Challenges Solved: Problems/needs addressed by products/services.
#     - Key Reasons Customers Choose: Top 2-3 USPs/differentiators.
#     - Notable Clients: 5-7 significant clients that the company has worked with (publicly known)
# - **Competitive Landscape:**
#     - Main Competitors: List 5-7 significant competitors. These can be direct or indirect competitors
#     - Key Differentiators (USPs): 1-3 points making the differentiates the company from its competitors. Focus on the things that the company does that sets it apart from its competitors and is the reason companies prefer the company over the competitors
#     - Competitive Strengths: 1-3 core advantages (e.g., technology, brand).
#     - Potential Weaknesses/Challenges: 1-3 potential vulnerabilities relative to competitors.
# - **Org Structure and Leadership:**
#     - Size, Status & Location: Approx Employee Count, Public/Private, HQ, Key Offices.
#     - Organizational Structure: Parent Company, Key Subsidiaries/Divisions, recent restructuring.
#     - Key Leadership: CEO, CPO/Product Head, CTO/Engineering Head, other relevant VPs/Heads (provide names).
# - **Industry Context, News & Outlook**
#     - **Key Industry Trends:** List all the key trends in the company’s primary industry that the company
#     - **Recent News & Key Developments:** 3-5 significant events from the last ~2 years (funding, product launches, acquisitions, partnerships, milestones reached etc.). Summarize each factually in one sentence (e.g., "Acquired Company Y, specializing in Z technology, in Q3 2023.")
#     -----

#     **The JSON Output should be in this format only and ensure atleast `2 subPoints` should,must be filled in each object of sub_modules and the 'completed' must be 'false' only:**
#     {
#   "quick_summary": "[A comprehensive 5–6 paragraph overview covering what the company does, its products/services, customer segments, problems solved, competitive advantage, recent momentum, and industry relevance.]",
#   "sub_modules": [
#     {
#       "title": "Company Overview",
#       "completed": false,
#       "summary": "string (Engaging paragraph summarizing the company overview section) atleast of 54 words",
#       "content": "string (3–4 fluent sentences explaining the scope and value of this module) ",
#       "points": [
#         {
#           "main": "Company Snapshot",
#           "subPoints": [
#             "String (3–4 sentence summary explaining what the company does, core product/service, key innovation, and relevance)",
#             ...
#           ]
#         },
#         {
#           "main": "Mission & Values",
#           "subPoints": [
#             "Mission: string (Mission of the company. Must be sourced, not inferred.)",
#             "Vision: string (Vision of the company. Must be sourced, not inferred.)",
#             "Values: [string, string, string] (List of values; must be sourced)",
#             ...
#           ]
#         },
#         {
#           "main": "Founding Team",
#           "subPoints": [
#             "String (In 1-2 sentences, state the *year* Alloy was founded and list *all the names* *e.g. name(job title)* of its founders entirely from web search) e.g. *The founders of company_name are name1(job title), name2(job title), name3(job title),etc.*",
#             ...
#           ]
#         }
#       ]
#     },
#     {
#       "title": "Products & Services Offered",
#       "completed": false,
#       "summary": "string (Summary explaining the company's product/service range and importance) ",
#       "content": "string (3–4 fluent sentences describing key offerings and how they help customers) ",
#       "points": [
#         {
#           "main": "Product & Service List",
#           "subPoints": [
#             "Product/Service A: string (Concise 1-2 sentence description of what it is and does)",
#             "Product/Service B: string (Same format, repeat as needed)",
#             ...
#           ]
#         }
#       ]
#     },
#     {
#       "title": "Business Model & Company Financials",
#       "completed": false,
#       "summary": "string (Summary explaining how the company makes money, growth trajectory, and financial standing) ",
#       "content": "string (3–4 fluent sentences on business model, recent funding, and revenue highlights) ",
#       "points": [
#         {
#           "main": "Business Model & Monetization",
#           "subPoints": [
#             "String (e.g., 'Subscription-based SaaS platform for enterprise analytics')",
#             "String (e.g., 'Freemium pricing for individual users with tiered enterprise plans')",
#             ...
#           ]
#         },
#         {
#           "main": "Financials & Funding",
#           "subPoints": [
#             "Recent Funding (Round/Amount/Date/Investors). Instruction - Focus on the last [n] funding round and focus on getting the latest data. e.g. Recent Funding Round 1: string (e.g., 'Series C – $120M – May 2023 – led by Sequoia')",
#             "Recent Funding (Round/Amount/Date/Investors). Instruction - Focus on the last [n] funding round and focus on getting the latest data. e.g. Recent Funding Round 2: string (e.g., 'Series B – $80M – Feb 2022 – led by Accel')",
#             ...
#           ]
#         },
#         {
#           "main": "Revenue",
#           "subPoints": [
#             "*Please provide the latest funding amount, date, and valuation for company_name entirely from web search*",
#             ...
#           ]
#         }
#       ]
#     },
#     {
#       "title": "Target Market & Customers",
#       "completed": false,
#       "summary": "string (Summary of target market, customer needs, and how the company addresses them) ",
#       "content": "string (3–4 sentences describing customers, problems solved, and value delivered) ",
#       "points": [
#         {
#           "main": "Primary Customer Segments",
#           "subPoints": [
#             "String (3–5 sentences on key industries, sectors, or personas served)",
#             ...
#           ]
#         },
#         {
#           "main": "Key Customer Challenges Solved",
#           "subPoints": [
#             "String (List of core problems solved by the company’s products/services)",
#             ...
#           ]
#         },
#         {
#           "main": "Key Reasons Customers Choose",
#           "subPoints": [
#             "String (1–2 sentence point on USP 1)",
#             "String (USP 2)",
#             "String (USP 3, if applicable)",
#             ...
#           ]
#         },
#         {
#           "main": "Notable Clients",
#           "subPoints": [
#             "Client 1",
#             "Client 2",
#             "Client 3",
#             "Client 4",
#             "Client 5",
#             "Client 6",
#             "Client 7",
#             ...
#           ]
#         }
#       ]
#     },
#     {
#       "title": "Competitive Landscape",
#       "completed": false,
#       "summary": "string (Summary outlining competitors and what gives the company an edge or poses a risk) ",
#       "content": "string (3–4 sentences describing competitors, strengths, differentiators, and risks) ",
#       "points": [
#         {
#           "main": "Main Competitors",
#           "subPoints": [
#             "Competitor A",
#             "Competitor B",
#             "Competitor C",
#             "Competitor D",
#             "Competitor E",
#             "Competitor F",
#             "Competitor G",
#             ...
#           ]
#         },
#         {
#           "main": "Key Differentiators (USPs)",
#           "subPoints": [
#             "String (Point 1)",
#             "String (Point 2)",
#             ...
#           ]
#         },
#         {
#           "main": "Competitive Strengths",
#           "subPoints": [
#             "String (e.g., 'Proprietary AI engine that automates analysis 30% faster')",
#             ...
#           ]
#         },
#         {
#           "main": "Potential Weaknesses/Challenges",
#           "subPoints": [
#             "String (e.g., 'Limited geographic reach compared to global competitors')",
#             ...
#           ]
#         }
#       ]
#     },
#     {
#       "title": "Org Structure and Leadership",
#       "completed": false,
#       "summary": "string (Summary describing size, structure, and leadership team of the company) ",
#       "content": "string (3–4 sentences about leadership, company structure, and global footprint) ",
#       "points": [
#         {
#           "main": "Size, Status & Location",
#           "subPoints": [
#             "String (e.g., 'Approx 1,500 employees, private company, HQ in San Francisco, regional offices in London and Bangalore')",
#             ...
#           ]
#         },
#         {
#           "main": "Organizational Structure",
#           "subPoints": [
#             "String (e.g., 'Wholly-owned subsidiary of XYZ Group, with 3 business divisions: Consumer, Enterprise, Research')",
#             ...
#           ]
#         },
#         {
#           "main": "Key Leadership",
#           "subPoints": [
#             "CEO: Full Name",
#             "CPO: Full Name",
#             "CTO: Full Name",
#             "Other Key Heads: Role – Name",
#             ...
#           ]
#         }
#       ]
#     },
#     {
#       "title": "Industry Context, News & Outlook",
#       "completed": false,
#       "summary": "string (Summary highlighting industry trends, company alignment, and recent developments) ",
#       "content": "string (3–4 sentences about the market environment and what the company has recently done to adapt or lead) ",
#       "points": [
#         {
#           "main": "Key Industry Trends",
#           "subPoints": [
#             "Trend 1",
#             "Trend 2",
#             "Trend 3",
#             ...
#           ]
#         },
#         {
#           "main": "Recent News & Key Developments",
#           "subPoints": [
#             "Event 1: string (e.g., 'Acquired Company Y, specializing in Z, in Q3 2023')",
#             "Event 2",
#             "Event 3",
#             "Event 4",
#             "Event 5",
#             ...
#           ]
#         }
#       ]
#     }
#   ]
# }''')
#     }
#                         ],
#                         "tools": [
#             {
#     "type": "function",
#     "function": {
#       "name": "structured_module_output",
#       "description": "",
#       "parameters": {
#         "type": "object",
#         "properties": {
#           "quick_summary": {
#             "type": "string",
#             "description": ""
#           },
#           "sub_modules": {
#             "type": "array",
#             "items": {
#               "type": "object",
#               "properties": {
#                 "title": {
#                   "type": "string",
#                   "description": ""
#                 },
#                 "completed": {
#                   "type": "boolean",
#                   "description": ""
#                 },
#                 "summary": {
#                   "type": "string",
#                   "description": ""
#                 },
#                 "content": {
#                   "type": "string",
#                   "description": ""
#                 },
#                 "points": {
#                   "type": "array",
#                   "items": {
#                     "type": "object",
#                     "properties": {
#                       "main": {
#                         "type": "string",
#                         "description": ""
#                       },
#                       "subPoints": {
#                         "type": "array",
#                         "items": {
#                           "type": "string"
#                         },
#                         "description": ""
#                       }
#                     },
#                     "required": ["main", "subPoints"]
#                   }
#                 }
#               },
#               "required": ["title", "completed", "summary", "content", "points"]
#             }
#           }
#         },
#         "required": ["quick_summary", "sub_modules"]
#       }
#     }
#   }
#         ],
#         "tool_choice": {
#             "type": "function",
#             "function": {
#                 "name": "structured_module_output"
#             }
#         }
#                     })
#                 )
#         citations=[]
#         for citation in response.json()["choices"][0]["message"]["annotations"]:
#             del citation["url_citation"]["start_index"]
#             del citation["url_citation"]["end_index"]
#             citation=citation["url_citation"]
#             citations.append(citation)
#         return jsonify({"ans":citations})
#     except Exception as e:
#         return jsonify({"error":str(e)})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)