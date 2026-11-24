# AI Resume Analyzer

A beginner-friendly Python project that analyzes PDF resumes and identifies academic information, work experience, extracurricular activities, and skills.

## Features

- Extracting text from PDF resumes.
- Identifing academic-related keywords.
- Detecting work experience and internship-related keywords.
- Identifing extracurricular activities and volunteering related keywords
- Extracting skills using keyword matching.
- Comparing resume skills with required job skills.
- Calculating a basic job skill match score.

## Technologies Used

- Python
- PyPDF
- Regular Expressions
- Streamlit (planned for future web app development)
- Pandas
- Scikit-learn

## Project Structure

```text
AI-Resume-Analyzer/
│
├── main.py
├── resume_parser.py
├── academic_analyzer.py
├── experience_analyzer.py
├── eca_analyzer.py
├── skill_extractor.py
├── job_matcher.py
├── profile_evaluator.py
├── requirements.txt
├── README.md
│
├── data/
├── sample_resumes/
└── reports/
```

## Installation

1. Clone this repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Open the project folder.

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the project using Python:

```bash
python -c "from main import analyze_resume; f=open('sample_resumes/sample.pdf','rb'); print(analyze_resume(f, ['Python', 'Java', 'Linux']))"
```

## Current Limitations

- Skill extraction uses predefined keywords.
- Academic and experience analysis identifies keywords rather than extracting all detailed information.
- Job matching uses basic text matching.
- The project does not provide admission or scholarship predictions.

## Future Improvements

- Improved resume information extraction.
- More flexible skill detection.
- Natural Language Processing integration.
- Streamlit-based web interface.

## Project Status

Version 1.0 – Beginner-friendly Python prototype.

## Author

Samonty Hasan Shrestha
GitHub:https://github.com/samontyhasan-hub