<<<<<<< HEAD
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Get Groq API key from .env
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# 🔍 Log API Key status (only for debug)
print("✅ Using Groq API Key:", "Loaded" if GROQ_API_KEY else "❌ NOT LOADED")

@app.route('/generate', methods=['POST'])
def generate_proposal():
    data = request.json

    name = data.get("name")
    skills = data.get("skills")
    platform = data.get("platform")
    tone = data.get("tone")
    job = data.get("job")

    # 💡 Build prompt for proposal
    prompt = f"""
You are an expert freelance writer creating proposals for platforms like {platform}.
Write a {tone.lower()} and professional proposal for this job:

Job Description: {job}

Freelancer Name: {name}
Skills: {skills}

Structure the proposal with a greeting, explanation of skills, why you're a fit, and a call to action.
Avoid generic buzzwords. Keep it focused and custom.
"""

    # 🧾 Headers for Groq API
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    # 📦 Payload sent to Groq
    payload = {
    "model": "llama3-70b-8192",
    "messages": [
        {"role": "system", "content": "You are a helpful proposal-writing assistant."},
        {"role": "user", "content": prompt}
    ],
    "max_tokens": 500,
    "temperature": 0.7
}

    # 🔎 Log payload for debug
    print("🚀 Sending Payload to Groq:")
    print(payload)

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()

        # ✅ Extract the proposal text
        proposal_text = response.json()['choices'][0]['message']['content'].strip()
        return jsonify({"proposal": proposal_text})

    # 🔥 Specific HTTP error handling from Groq
    except requests.exceptions.HTTPError as http_err:
        print("🔥 HTTP ERROR:", http_err.response.text)
        return jsonify({"error": http_err.response.text}), 500

    # 🔥 Any other unexpected error
    except Exception as e:
        print("🔥 OTHER ERROR:", e)
        return jsonify({"error": str(e)}), 500

# 🟢 Start Flask server
if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Get Groq API key from .env
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# 🔍 Log API Key status (only for debug)
print("✅ Using Groq API Key:", "Loaded" if GROQ_API_KEY else "❌ NOT LOADED")

@app.route('/generate', methods=['POST'])
def generate_proposal():
    data = request.json

    name = data.get("name")
    skills = data.get("skills")
    platform = data.get("platform")
    tone = data.get("tone")
    job = data.get("job")

    # 💡 Build prompt for proposal
    prompt = f"""
You are an expert freelance writer creating proposals for platforms like {platform}.
Write a {tone.lower()} and professional proposal for this job:

Job Description: {job}

Freelancer Name: {name}
Skills: {skills}

Structure the proposal with a greeting, explanation of skills, why you're a fit, and a call to action.
Avoid generic buzzwords. Keep it focused and custom.
"""

    # 🧾 Headers for Groq API
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    # 📦 Payload sent to Groq
    payload = {
    "model": "llama3-70b-8192",
    "messages": [
        {"role": "system", "content": "You are a helpful proposal-writing assistant."},
        {"role": "user", "content": prompt}
    ],
    "max_tokens": 500,
    "temperature": 0.7
}

    # 🔎 Log payload for debug
    print("🚀 Sending Payload to Groq:")
    print(payload)

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()

        # ✅ Extract the proposal text
        proposal_text = response.json()['choices'][0]['message']['content'].strip()
        return jsonify({"proposal": proposal_text})

    # 🔥 Specific HTTP error handling from Groq
    except requests.exceptions.HTTPError as http_err:
        print("🔥 HTTP ERROR:", http_err.response.text)
        return jsonify({"error": http_err.response.text}), 500

    # 🔥 Any other unexpected error
    except Exception as e:
        print("🔥 OTHER ERROR:", e)
        return jsonify({"error": str(e)}), 500

# 🟢 Start Flask server
if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 74fc07ea5efd77b7835f9ab7be4c66cca8cec472
