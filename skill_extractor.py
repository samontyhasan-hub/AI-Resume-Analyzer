def extract_skills(text):

    skills = [
        "python",
        "java",
        "c++",
        "c",
        "html",
        "css",
        "javascript",
        "machine learning",
        "artificial intelligence",
        "linux",
        "networking",
        "communication",
        "leadership",
        "problem solving",
        "teamwork"
    ]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills