import matplotlib.pyplot as plt
import os
import numpy as np

# Given dataset
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

ROLE_MAP = {
    0: "Data Scientist",
    1: "Software Engineer",
    2: "Project Manager",
    3: "HR",
    4: "Frontend Developer",
    5: "Backend Developer",
    6: "DevOps Engineer",
    7: "UI/UX Designer",
    8: "Business Analyst",
    9: "Cybersecurity Analyst"
}

def generate_salary_trend_graph(role_name):
    # Get role number from name
    role_id = None
    for k, v in ROLE_MAP.items():
        if v == role_name:
            role_id = k
            break
    if role_id is None:
        return None

    # Filter salaries for the given role
    years = list(range(0, 16))  # 0 to 15 years experience
    avg_salaries = []

    for y in years:
        salaries = [
            DATA["Salary"][i]
            for i in range(len(DATA["Salary"]))
            if DATA["Role"][i] == role_id and DATA["Experience"][i] == y
        ]
        if salaries:
            avg_salaries.append(np.mean(salaries))
        else:
            avg_salaries.append(None)  # No data for that year

    # Plotting
    plt.figure(figsize=(8, 4))
    filtered_years = [y for y, s in zip(years, avg_salaries) if s is not None]
    filtered_salaries = [s for s in avg_salaries if s is not None]

    if not filtered_salaries:
        return None

    plt.plot(filtered_years, filtered_salaries, marker='o', linestyle='-', color='navy')
    plt.title(f'Salary Trend for {role_name} (by Experience)')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary (INR/year)')
    plt.grid(True)

    # Show labels
    for i, s in zip(filtered_years, filtered_salaries):
        plt.text(i, s + 10000, f"{int(s)//1000}k", ha='center', fontsize=8)

    # Save to static
    os.makedirs('static/graphs', exist_ok=True)
    path = f'static/graphs/{role_name.lower().replace(" ", "_")}_trend.png'
    plt.savefig(path)
    plt.close()
    return path
