import joblib

model = joblib.load('salary_model.pkl')

# Mapping used during training
EDUCATION_MAP = {'High School': 0, 'Bachelor': 1, 'Master': 2, 'PhD': 3}
ROLE_MAP = {
    'Data Scientist': 0,
    'Software Engineer': 1,
    'Project Manager': 2,
    'HR': 3,
    'Frontend Developer': 4,
    'Backend Developer': 5,
    'DevOps Engineer': 6,
    'UI/UX Designer': 7,
    'Business Analyst': 8,
    'Cybersecurity Analyst': 9
}

def predict_salary(experience, education_level, role):
    edu_encoded = EDUCATION_MAP.get(education_level, 1)
    role_encoded = ROLE_MAP.get(role, 0)
    features = [[experience, edu_encoded, role_encoded]]
    predicted = model.predict(features)[0]

    # Clamp salary range between ₹2L and ₹20L
    predicted = max(200000, min(predicted, 2000000))
    return predicted

