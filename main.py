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
    
    name = data.get("name")
    email = data.get("email")
    subject = data.get("subject")
    message = data.get("message")

    print("Data received","Name: ", name, "Email: ", email, "Subject: ", subject, "Message:", message )

    return jsonify({"status": "success", "message": "Contact form submitted successfully!"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port)
