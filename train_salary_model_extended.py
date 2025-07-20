# train_salary_model_extended.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib

# Extended dataset
DATA = {
    "Experience": [0, 1, 2, 3, 5, 7, 10, 12, 15, 1, 2, 3, 5, 7, 10, 2, 4, 6, 8, 11],
    "Education": [0, 1, 1, 1, 2, 2, 2, 3, 3, 1, 1, 1, 2, 2, 3, 1, 2, 2, 3, 3],
    "Role": [
        0, 0, 1, 1, 1, 2, 2, 3, 3, 4,
        4, 4, 5, 5, 5, 6, 6, 7, 8, 9
    ],
    "Salary": [
        250000, 300000, 400000, 500000, 700000, 900000, 1200000, 1500000, 1800000,
        320000, 400000, 480000, 600000, 850000, 1100000, 650000, 800000, 700000,
        750000, 900000
    ]
}

# Load into DataFrame
df = pd.DataFrame(DATA)

# Features and Target
X = df[["Experience", "Education", "Role"]]
y = df["Salary"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Evaluate performance
y_pred = model.predict(X)

r2 = r2_score(y, y_pred)
mae = mean_absolute_error(y, y_pred)
rmse = mean_squared_error(y, y_pred, squared=False)

print("✅ Model trained and evaluated.")
print(f"📊 R² Score: {r2:.2f}")
print(f"📉 MAE: ₹{mae:,.0f}")
print(f"📉 RMSE: ₹{rmse:,.0f}")

# Save model
joblib.dump(model, "salary_model.pkl")
print("💾 Model saved as salary_model.pkl")
