from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv

# ✅ Load environment variables from .env file (local only)
load_dotenv()

# ✅ Get Groq API key securely from env vars
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# ✅ Initialize Flask app and allow CORS
app = Flask(__name__)
CORS(app)

# ✅ Debugging line to confirm API Key is loaded
print("✅ Using Groq API Key:", "Loaded" if GROQ_API_KEY else "❌ NOT LOADED")

@app.route('/generate', methods=['POST'])
def generate_proposal():
    data = request.json

    name = data.get("name")
    skills = data.get("skills")
    platform = data.get("platform")
    tone = data.get("tone")
    job = data.get("job")

    # 🧠 Build prompt for AI
    prompt = f"""
You are an expert freelance writer creating proposals for platforms like {platform}.
Write a {tone.lower()} and professional proposal for this job:

Job Description: {job}

Freelancer Name: {name}
Skills: {skills}

Structure the proposal with a greeting, explanation of skills, why you're a fit, and a call to action.
Avoid generic buzzwords. Keep it focused and custom.
"""

    # 📦 Request to Groq API
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful proposal-writing assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,
        "temperature": 0.7
    }

    # 🚀 Log payload for debugging
    print("📤 Sending to Groq API...")
    print(payload)

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()

        # ✅ Extract response
        proposal_text = response.json()['choices'][0]['message']['content'].strip()
        return jsonify({"proposal": proposal_text})

    except requests.exceptions.HTTPError as http_err:
        print("🔥 HTTP ERROR:", http_err.response.text)
        return jsonify({"error": http_err.response.text}), 500

    except Exception as e:
        print("🔥 ERROR:", str(e))
        return jsonify({"error": str(e)}), 500

# 🟢 Start Flask server
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Railway provides a dynamic port
    app.run(host='0.0.0.0', port=port, debug=True)  # Bind to 0.0.0.0 for external access