def match_skills(resume_skills, required_skills):

    matched = []
    missing = []

    for skill in required_skills:
        if skill.lower() in [s.lower() for s in resume_skills]:
            matched.append(skill)
        else:
            missing.append(skill)

    score = (
        len(matched) / len(required_skills) * 100
        if required_skills else 0
    )

    return {
        "matched": matched,
        "missing": missing,
        "match_score": round(score, 2)
    }