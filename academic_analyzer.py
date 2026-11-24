def analyze_academic_info(text):

    academic_keywords = [
        "education",
        "ssc",
        "hsc",
        "bachelor",
        "university",
        "college",
        "gpa",
        "cgpa",
        "degree"
    ]

    found_info = []

    for keyword in academic_keywords:
        if keyword.lower() in text.lower():
            found_info.append(keyword)

    return found_info