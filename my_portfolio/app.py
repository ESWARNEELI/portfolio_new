import os
MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)

from flask import Flask, request, render_template, send_from_directory
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb+srv://djexo:Eswarneeli2005@portfolio.jwaij2g.mongodb.net/?retryWrites=true&w=majority&appName=portfolio")
db = client["portfolio"]
collection = db["contacts"]

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        # Insert into MongoDB
        
        #   name:name;
        #   email:email;
        #   message:message;
            
        collection.insert_one({"name": name, "email": email,"message" : message})
        return render_template("contact.html",msg=True)
    return render_template("contact.html",msg=False)
    
@app.route("/")
def serve_index():
    return send_from_directory('.', 'index.html')
# Serve static pages like index.html, about.html, etc.
@app.route("/<path:filename>")
def static_pages(filename):
    return send_from_directory(".", filename)

if __name__ == "__main__":
    app.run(debug=True) 
