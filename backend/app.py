from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from utils import extract_resume_text
from model import calculate_similarity

app = Flask(__name__)
CORS(app)  # 👈 IMPORTANT (fixes your error)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    job_desc = request.form['job_desc']

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    resume_text = extract_resume_text(file_path)
    score = calculate_similarity(resume_text, job_desc)

    if score > 70:
        suggestion = "Good match!"
    else:
        suggestion = "Improve skills & keywords"

    return jsonify({
        "score": score,
        "suggestion": suggestion
    })

if __name__ == '__main__':
    app.run(debug=True)