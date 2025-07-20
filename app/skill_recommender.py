REQUIRED_SKILLS_BY_ROLE = {
    "Data Scientist": ["Python", "Machine Learning", "SQL", "Pandas"],
    "Software Engineer": ["Java", "C++", "Git", "APIs"],
    "Project Manager": ["Excel", "Power BI", "Team Management"],
    "HR": ["Excel", "Power BI", "Communication"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript", "React"],
    "Backend Developer": ["Node.js", "MongoDB", "APIs", "Python"],
    "DevOps Engineer": ["Docker", "Kubernetes", "AWS", "CI/CD"],
    "UI/UX Designer": ["Figma", "Adobe XD", "Wireframing", "Design Systems"],
    "Business Analyst": ["Excel", "SQL", "Tableau", "Critical Thinking"],
    "Cybersecurity Analyst": ["Networking", "Firewalls", "Linux", "Threat Analysis"]
}


def get_missing_skills(user_skills, role):
    expected = REQUIRED_SKILLS_BY_ROLE.get(role, [])
    user_skills_lower = [skill.lower() for skill in user_skills]
    missing = [skill for skill in expected if skill.lower() not in user_skills_lower]
    return missing
