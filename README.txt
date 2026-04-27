# Resume Analyzer + Job Matcher

## Overview
This project is a full-stack web application that analyzes resumes and matches them with job descriptions using Natural Language Processing (NLP).

It calculates a similarity score and provides suggestions to improve the resume based on missing keywords and skills.

---

## Features
- Upload resume in PDF format
- Extract text automatically from resume
- Match resume with job description
- Generate similarity score (percentage)
- Provide improvement suggestions
- Identify missing skills

---

## Tech Stack
- Backend: Python, Flask
- NLP: Scikit-learn (TF-IDF, Cosine Similarity)
- Frontend: HTML, CSS, JavaScript

---

## Project Structure
resume-analyzer-job-matcher/
│
├── backend/
│ ├── app.py
│ ├── model.py
│ ├── utils.py
│ ├── requirements.txt
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ ├── script.js
│
├── sample_data/
│ ├── sample_resume.pdf
│ ├── job_description.txt
│
├── README.md
├── LICENSE
└── .gitignore





---

## How to Run

### 1. Clone the repository
git clone https://github.com/ARGHA2204/Resume-Analyzer-Job-Matcher

cd resume-analyzer-job-matcher


### 2. Setup backend

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py


### 3. Run frontend
Open a new terminal:

cd frontend
python -m http.server 5500
Then open in browser:

http://localhost:5500



## Sample Test

Use the files provided in the sample_data folder:
- sample_resume.pdf
- job_description.txt

---

## Sample Output


Score: 75%
Suggestion: Good match!
Missing Skills: docker, kubernetes