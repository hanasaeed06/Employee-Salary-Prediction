import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Simple dummy dataset
DATA = {
    "Experience": [0, 1, 3, 5, 7, 10],
    "Education": [0, 1, 1, 2, 2, 3],  # 0=High School, 1=Bachelor, 2=Master, 3=PhD
    "Role": [0, 0, 1, 1, 2, 3],       # 0=DS, 1=SE, 2=PM, 3=HR
    "Salary": [250000, 350000, 500000, 700000, 1000000, 1400000]
}

df = pd.DataFrame(DATA)

X = df[["Experience", "Education", "Role"]]
y = df["Salary"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "salary_model.pkl")
print("✅ New salary_model.pkl trained and saved.")
