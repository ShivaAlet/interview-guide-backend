from flask import Flask, request, jsonify
import threading
from multiprocessing import Process, Manager
import utils
from flask_cors import CORS
from google.oauth2 import id_token
from google.auth.transport import requests
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
SECRET_KEY=os.getenv("SECRET_KEY")

YOUR_GOOGLE_CLIENT_ID=os.getenv("YOUR_GOOGLE_CLIENT_ID")
client = MongoClient(os.getenv("MONGO_URI"))
db = client["Interview_Guide"]
googleAuth = db["googleAuth"]

# Temporary folder to save PDFs
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/generate_guide', methods=['POST'])
def ask_questions():
    access_key = request.headers.get('x-api-key')

    if access_key != ACCESS_KEY:
        return jsonify({"status": "Not Ok", "error": "Missing or invalid access key"}), 400

    try:
        required_keys = ["company_name", "job_role", "job_description", "token"]
        data = request.form

        if not all(key in data for key in required_keys) or "resume" not in request.files:
            return jsonify({"error": "Missing keys or resume file"}), 400

        resume_file = request.files["resume"]
        if resume_file.filename == '':
            return jsonify({"error": "No selected PDF file"}), 400

        # Save the file
        filename = secure_filename(resume_file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        resume_file.save(file_path)

        # Extract text from the resume
        reader = PyPDF2.PdfReader(file_path)
        resume_text = ''
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

        # Add extracted resume text to data
        updated_data = dict(data)
        updated_data["resume"] = resume_text

        prompts = utils.generatePrompts(updated_data)

        # Using multiprocessing to get responses
        manager = Manager()
        results = manager.list([None] * len(prompts))
        errorJsons = manager.list([None] * len(prompts))
        processes = []

        for i, prompt in enumerate(prompts):
            process = Process(target=utils.get_response, args=(prompt, results, errorJsons, i))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        idd = str(uuid.uuid4())
        newGuide = utils.structureGuide(list(results), updated_data, idd)

        history = user.get("history", [])
        history.append(newGuide)

        result = googleAuth.update_one({"email": user_email}, {"$set": {"history": history}})

        if result.matched_count:
            return jsonify({"status": "Ok", "message": "User updated", "history": history, "guide": newGuide})
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
        return jsonify({"status":"Ok","message": "Login Successful", "user":utils.convert_objectid(user)})
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
            if guide:
                return jsonify({"status":"Ok","guide":guide}), 200
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)