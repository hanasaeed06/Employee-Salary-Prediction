# 💼 Employee Salary Predictor

This is a machine learning-based web application that predicts an employee's salary using their resume details like experience, education level, role, and skills. It also recommends missing skills and visualizes salary trends for the selected role.

---

## 📌 Project Summary

This project helps users understand what salary they might expect based on their background. After uploading a resume and selecting relevant information, the system predicts salary using a trained machine learning model. It also shows which key skills are missing and displays a graph of future salary trends.

---

## 🔧 Tech Stack

- **Python**, **Flask** – Backend logic & API
- **HTML**, **Bootstrap 5**, **AOS.js** – Frontend UI
- **Scikit-learn** – Machine Learning (Linear Regression)
- **Matplotlib** – Salary trend graphs
- **Pandas**, **NumPy** – Data handling

---

## 🧠 Machine Learning

- **Model:** Linear Regression
- **Input:** Experience, Education, Role (encoded numerically)
- **Output:** Predicted annual salary
- **Model Accuracy:** R² = 0.91
- **Average Error (MAE):** ₹82,157  
- **Root Mean Square Error (RMSE):** ₹1,19,233

---

## 🚀 How to Run

1. Clone the repo:
   git clone https://github.com/your-username/employee-salary-predictor
   cd employee-salary-predictor
   
2. Install dependencies:
   pip install -r requirements.txt

3. Train the model (if not already):
   python train_salary_model_extended.py

4. Start the Flask app:
   python main.py
   
5. Open in browser:
   http://127.0.0.1:5000

---

## ✨ Features

- 📄 Upload a resume and auto-fill form fields
- 💼 Select role, skills, and education level
- 💰 Predict salary based on ML model
- 🎯 Recommend missing skills for the selected role
- 📈 Visualize salary trend by experience (2025–2029)

---

## 📂 Project Structure

employee-salary-predictor/
│
├── app/
│ ├── model.py
│ ├── resume_parser.py
│ ├── skill_recommender.py
│ └── salary_trend.py
│
├── templates/
│ └── index.html
│
├── static/
│ └── graphs/
│
├── salary_model.pkl
├── main.py
├── train_salary_model_extended.py
├── requirements.txt
└── README.md


---

## 🔮 Future Scope

- Use real-world datasets (Glassdoor, LinkedIn, etc.)
- Integrate NLP-based resume parsing
- Improve model using Random Forest or XGBoost
- Deploy app online (Render, Heroku, AWS)
- Add login, profile history, and admin dashboard

---





