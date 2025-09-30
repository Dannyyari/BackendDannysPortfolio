from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

@app.route("/api/contact", methods=["POST"])
@cross_origin(origins="https://python-flask-devops.netlify.app")
def contact_api():
    data = request.get_json()
    print ("Data received:", data.name, data.email, data.subject, data.message)
    return jsonify({"status": "success", "message": "Contact form submitted successfully!"})



if __name__ == "__main__":
    app.run(debug=True)