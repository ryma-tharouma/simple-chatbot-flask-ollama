from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"  # Or "llama2", etc.

@app.route("/")
def home():
    # Serve index.html automatically
    return send_from_directory('.', 'index.html')

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message", "")
        print(f"[User message received]: {user_message}")

        payload = {
            "model": MODEL_NAME,
            "prompt": user_message,
            "stream": False
        }
        print(f"[Sending payload to Ollama]: {payload}")

        response = requests.post(OLLAMA_API_URL, json=payload)

        print(f"[Ollama HTTP Status]: {response.status_code}")
        print(f"[Ollama Response Text]: {response.text}")

        if response.status_code != 200:
            return jsonify({"reply": "Error: Ollama returned a non-200 status."}), 500

        data = response.json()

        if "response" not in data:
            print("[Warning]: 'response' key not found in Ollama reply.")
            return jsonify({"reply": "Error: Unexpected Ollama response format."}), 500

        reply = data["response"]
        print(f"[Reply to User]: {reply}")

        return jsonify({"reply": reply})

    except Exception as e:
        print(f"[Exception]: {e}")
        return jsonify({"reply": "Error: Server crashed."}), 500


if __name__ == "__main__":
    app.run(debug=True)
