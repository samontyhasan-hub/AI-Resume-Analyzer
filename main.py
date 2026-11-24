from resume_parser import extract_text_from_pdf
from academic_analyzer import analyze_academic_info
from experience_analyzer import analyze_experience
from eca_analyzer import analyze_eca
from skill_extractor import extract_skills
from profile_evaluator import evaluate_profile
from job_matcher import match_skills


def analyze_resume(file, required_skills=None):

    text = extract_text_from_pdf(file)

    academic = analyze_academic_info(text)
    experience = analyze_experience(text)
    eca = analyze_eca(text)
    skills = extract_skills(text)

    profile = evaluate_profile(
        academic,
        experience,
        eca,
        skills
    )

    if required_skills:
        profile["Job Matching"] = match_skills(
            skills, required_skills
        )

    return profile