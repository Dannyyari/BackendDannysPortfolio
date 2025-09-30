import os
from flask import Flask, request, jsonify
from flask_cors import cross_origin

app = Flask(__name__)

#CORS(app, origins=["https://danny-portfolio-devops.netlify.app"], methods=["POST", "OPTIONS"], allow_headers=["Content-Type"])


@app.route("/api/contact", methods=["POST", "OPTIONS"])
@cross_origin(origins=["https://danny-portfolio-devops.netlify.app/api/contact"])
def contact_api():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"status": "error", "message": "No JSON data received"}), 400
        
        required_fields = ["name", "email", "subject", "message"]
        for field in required_fields:
            if field not in data:
                return jsonify({"status": "error", "message": f"Missing field: {field}"}), 400
        
        print("Data received:", data)
        return jsonify({"status": "success", "message": "Contact form submitted successfully!"})
        
    except Exception as e:  # Denna rad måste ha samma indentation som try
        print("Error:", str(e))
        return jsonify({"status": "error", "message": "Server error"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Railway tilldelar port via miljövariabel
    app.run(host="0.0.0.0", port=port)



    #if request.method == "OPTIONS":
     #   return"", 200

    #if request.method == "POST":
     #   data = request.get_json()
      #  print ("Data received:", data, data["name"], data["email"], data["subject"], data["message"])
       # return jsonify({"status": "success", "message": "Contact form submitted successfully!"})