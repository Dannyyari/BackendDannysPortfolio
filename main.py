import os
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
     # Use app.logger instead of print - this works better on Render
    app.logger.info(f"Contact form received - Name: {data.get('name')}, Email: {data.get('email')}")
    app.logger.info(f"Subject: {data.get('subject')}")
    app.logger.info(f"Message: {data.get('message')}")
    return jsonify({"status": "success", "message": "Contact form submitted successfully!"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port)
