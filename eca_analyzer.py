def analyze_eca(text):

    eca_keywords = [
        "volunteering",
        "volunteer",
        "leadership",
        "community service",
        "club",
        "competition",
        "award",
        "research",
        "publication",
        "extracurricular"
    ]

    found_eca = []

    for keyword in eca_keywords:
        if keyword.lower() in text.lower():
            found_eca.append(keyword)

    return found_eca