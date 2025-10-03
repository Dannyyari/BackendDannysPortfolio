import os
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)


CORS(app)

@app.route("/api/contact", methods=["POST", "OPTIONS"])
def contact_api():

    if request.method == "OPTIONS":
        return '', 200

    data = request.get_json()

    print("Data received:", data ["name"], data["email"], data ["subject"], data ["message"])
    
    name = data.get("name", "N/A")
    email = data.get("email", "N/A")
    subject = data.get("subject", "N/A")
    message = data.get("message", "N/A")

    print(f"Data received: {name}, {email}, {subject}, {message}", flush=True)
    app.logger.info(f"Data received: {name}, {email}, {subject}, {message}")
    return jsonify({"status": "success", "message": "Contact form submitted successfully!"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port)
