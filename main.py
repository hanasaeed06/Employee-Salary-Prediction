from flask import Flask, request, render_template
from app.salary_trend import generate_salary_trend_graph
from app.resume_parser import parse_resume
from app.skill_recommender import get_missing_skills
from app.model import predict_salary
import os

app = Flask(__name__)

# Global list of all possible skills for checkboxes
ALL_SKILLS = [
    'Python', 'Java', 'C++', 'SQL', 'Machine Learning', 'Deep Learning',
    'Data Analysis', 'NLP', 'Pandas', 'NumPy', 'Excel', 'TensorFlow',
    'Keras', 'Tableau', 'Power BI'
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")

        if action == "Parse Resume":
            uploaded_file = request.files["resume"]
            role = request.form.get("role")

            if not os.path.exists("uploads"):
                os.makedirs("uploads")
            file_path = os.path.join("uploads", uploaded_file.filename)
            uploaded_file.save(file_path)

            name, exp, edu, extracted_skills = parse_resume(file_path)

            return render_template(
                "index.html",
                parsed=True,
                name=name,
                experience=exp,
                education=edu,
                role=role,
                all_skills=ALL_SKILLS,
                user_skills=extracted_skills
            )

        elif action == "Predict Salary":
            name = request.form.get("name", "Unknown")
            exp = int(request.form['experience'])
            edu = request.form['education']
            role = request.form['role']
            user_skills = request.form.getlist('skills')

            # ✅ Handle other skills input
            other_skills_raw = request.form.get('other_skills', '')
            other_skills = [s.strip() for s in other_skills_raw.split(',') if s.strip()]
            user_skills.extend(other_skills)

            salary = predict_salary(exp, edu, role)
            missing_skills = get_missing_skills(user_skills, role)
            graph_path = generate_salary_trend_graph(role)  # ✅ NEW: Generate salary trend graph

            return render_template(
                "index.html",
                salary=salary,
                skills=missing_skills,
                parsed=True,
                name=name,
                experience=exp,
                education=edu,
                role=role,
                all_skills=ALL_SKILLS,
                user_skills=user_skills,
                graph_path=graph_path  # ✅ Pass graph to template
            )

    # Initial GET request
    return render_template(
        "index.html",
        parsed=False,
        all_skills=ALL_SKILLS,
        user_skills=[],
        role="Data Scientist"
    )

if __name__ == "__main__":
    app.run(debug=True)
