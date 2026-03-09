from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)

UPLOAD_FOLDER = "../uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

uploads_data = []  
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["image"]
    if file.filename == "":
        return "No file selected", 400

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    if random.random() > 0.5:
        result = "Defective Exhibit Detected"
    else:
        result = "Exhibit is OK"

    uploads_data.append({'filename': file.filename, 'result': result})

    image_url = "/uploads/" + file.filename
    return render_template("result.html", result=result, image_url=image_url)

@app.route("/admin")
def admin_dashboard():
    return render_template("admin.html", uploads=uploads_data)

if __name__ == "__main__":
    app.run(debug=True)
