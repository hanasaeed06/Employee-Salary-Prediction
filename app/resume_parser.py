import docx2txt
import pdfplumber
import spacy
import re
import os

nlp = spacy.load("en_core_web_sm")

SKILL_KEYWORDS = [
    'Python', 'Java', 'C++', 'SQL', 'Machine Learning', 'Deep Learning', 'Data Analysis',
    'NLP', 'Pandas', 'NumPy', 'Excel', 'TensorFlow', 'Keras', 'Tableau', 'Power BI'
]

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text

    elif ext == ".docx":
        return docx2txt.process(file_path)

    else:
        return ""

def parse_resume(file_path):
    text = extract_text(file_path)
    doc = nlp(text)

    # --- Name Extraction ---
    name = "Unknown"
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text.strip()
            break

    # --- Experience Extraction ---
    experience = 0
    exp_matches = re.findall(r'(\d{1,2})\s+(?:year|years)', text.lower())
    if exp_matches:
        exp_nums = [int(e) for e in exp_matches if 0 < int(e) < 40]
        if exp_nums:
            experience = max(exp_nums)

    # --- Education Detection ---
    education_level = 'High School'
    lowered = text.lower()
    if 'phd' in lowered:
        education_level = 'PhD'
    elif 'master' in lowered or 'msc' in lowered:
        education_level = 'Master'
    elif 'bachelor' in lowered or 'bsc' in lowered:
        education_level = 'Bachelor'

    # --- Skill Extraction ---
    detected_skills = [skill for skill in SKILL_KEYWORDS if skill.lower() in text.lower()]

    return name, experience, education_level, detected_skills
