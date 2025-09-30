import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app, origins="https://danny-portfolio-devops.netlify.app", allow_headers=["Content-Type"])

@app.route("/api/contact", methods=["POST"])
def contact_api():
    data = request.get_json()
    print ("Data received:", data["name"], data["email"], data["subject"], data["message"])
    return jsonify({"status": "success", "message": "Contact form submitted successfully!"})



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Railway tilldelar port via miljövariabel
    app.run(host="0.0.0.0", port=port)