import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv('model_training/salary_data.csv')

# Encode categorical columns manually
df['education_level'] = df['education_level'].map({'High School': 0, 'Bachelor': 1, 'Master': 2, 'PhD': 3})
df['role'] = df['role'].astype('category').cat.codes

# Features and label
X = df[['experience', 'education_level', 'role']]
y = df['salary']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'salary_model.pkl')
print("Model trained and saved.")
