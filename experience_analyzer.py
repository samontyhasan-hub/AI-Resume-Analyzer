def analyze_experience(text):

    experience_keywords = [
        "experience",
        "internship",
        "intern",
        "volunteer",
        "employment",
        "work experience",
        "responsibilities"
    ]

    found_experience = []

    for keyword in experience_keywords:
        if keyword.lower() in text.lower():
            found_experience.append(keyword)

    return found_experience