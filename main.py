import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)


CORS(app, origins=["https://danny-portfolio-devops.netlify.app"], supports_credentials=True)

@app.route("/api/contact", methods=["POST", "OPTIONS"])
def contact_api():
    if request.method == "OPTIONS":
        return '', 200
    try:
    
        data = request.get_json()
        print("Data received:", data)
        
        if not data:
            return jsonify({"status": "error", "message": "No JSON data received"}), 400
        
        required_fields = ["name", "email", "subject", "message"]
        for field in required_fields:
            if field not in data:
                return jsonify({"status": "error", "message": f"Missing field: {field}"}), 400
        return jsonify({"status": "success", "message": "Contact form submitted successfully!"})
        
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"status": "error", "message": "Server error"}), 500

#@app.route("/api/contact", methods=["POST", "OPTIONS"])
#@cross_origin(origins=["https://danny-portfolio-devops.netlify.app"])
#def contact_api():
#    try:
 #       data = request.get_json()
  #      
   #     if not data:
    #        return jsonify({"status": "error", "message": "No JSON data received"}), 400
     #   
      #  required_fields = ["name", "email", "subject", "message"]
       # for field in required_fields:
        #    if field not in data:
         #       return jsonify({"status": "error", "message": f"Missing field: {field}"}), 400
        
      #  print("Data received:", data)
       # return jsonify({"status": "success", "message": "Contact form submitted successfully!"})
        
   # except Exception as e:  # Denna rad måste ha samma indentation som try
   #     print("Error:", str(e))
    #    return jsonify({"status": "error", "message": "Server error"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway tilldelar port via miljövariabel
    app.run(host="0.0.0.0", port=port)



    #if request.method == "OPTIONS":
     #   return"", 200

    #if request.method == "POST":
     #   data = request.get_json()
      #  print ("Data received:", data, data["name"], data["email"], data["subject"], data["message"])
       # return jsonify({"status": "success", "message": "Contact form submitted successfully!"})