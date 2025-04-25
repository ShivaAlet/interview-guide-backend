from flask import Flask, request, jsonify
import threading
from multiprocessing import Process, Manager
import utils
from flask_cors import CORS
from google.oauth2 import id_token
from google.auth.transport import requests
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
CORS(app)

YOUR_GOOGLE_CLIENT_ID=os.getenv("YOUR_GOOGLE_CLIENT_ID")
client = MongoClient(os.getenv("MONGO_URI"))
db = client["Interview_Guide"]
googleAuth = db["googleAuth"]

@app.route('/generate_guidee', methods=['POST'])
def ask_questionss():
    required_keys = ["company_name","company_website", "job_role", "job_description","resume","company_location"]
    data = request.json
    if all(key in data for key in required_keys):
        pass  
    else:
        return {"error": "Missing keys"}, 400
    
    prompts = utils.generatePrompts(data)
    
    results = [None, None,None,None,None,None, None,None,None,None,None, None,None,None]
    errorJsons = [None, None,None,None,None,None, None,None,None,None,None, None,None,None]
    threads = []

    for i, prompt in enumerate(prompts):
        thread = threading.Thread(target=utils.get_response, args=(prompt, results,errorJsons, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return jsonify(utils.structureGuide(results,data))

    # return jsonify({"error":errorJsons})

@app.route('/generate_guide', methods=['POST'])
def ask_questions():
    try:
        required_keys = ["company_name","company_website", "job_role", "job_description","resume","company_location","token"]
        data = request.json
        if all(key in data for key in required_keys):
            pass  
        else:
            return {"error": "Missing keys"}, 400
        
        token = request.json.get('token')
        idinfo = id_token.verify_oauth2_token(token, requests.Request(),YOUR_GOOGLE_CLIENT_ID )
        user_email = idinfo['email']
        user = googleAuth.find_one({"email": user_email})

        if user is None:
            return jsonify({"error": "User not found"}), 404

        prompts  = utils.generatePrompts(data)

        results = [None, None,None,None,None,None, None,None,None,None,None, None,None,None]
        errorJsons = [None, None,None,None,None,None, None,None,None,None,None, None,None,None]
        manager = Manager()
        results = manager.list([None] * len(prompts))  # Shared list across processes
        errorJsons = manager.list([None] * len(prompts))  # Shared list across processes
        processes = []

        for i, prompt in enumerate(prompts):
            process = Process(target=utils.get_response, args=(prompt, results,errorJsons, i))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        errorJsons = list(errorJsons)
        results = list(results)

        history = user["history"]
        history.append(utils.structureGuide(results,data))
        
        result = googleAuth.update_one({"email": user_email}, {"$set": {"history":history}})
        if result.matched_count:
            return jsonify({"status":"Ok","message": "User updated","history":history,"guide":utils.structureGuide(results,data)})
    except Exception as e:
        return jsonify({"status":"Not Ok","error": "Invalid token","error":str(e)}), 400

    # return jsonify({"error":errorJsons})

@app.route('/google-login', methods=['POST'])
def google_login():
    token = request.json.get('token')
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(),YOUR_GOOGLE_CLIENT_ID )
        user_email = idinfo['email']
        user_name = idinfo['name']
        user = googleAuth.find_one({"email": user_email})
        if user is None:
            user={"name":user_name,"email":user_email,"credits":100,"history":[]}
            googleAuth.insert_one(user)
        return jsonify({"status":"Ok","message": "Login Successful", "user":utils.convert_objectid(user)})
    except Exception as e:
        return jsonify({"status":"Not Ok","error": "Invalid token"}), 400



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)