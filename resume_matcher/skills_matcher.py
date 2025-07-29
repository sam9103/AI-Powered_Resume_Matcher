# resume_matcher/skills_matcher.py

import re

# Example skill list – you can expand this
SKILL_KEYWORDS = [
    # Programming Languages
    "python", "java", "c++", "c", "c#", "javascript", "typescript", "go", "ruby", "swift", "r", "php", "matlab",
    
    # Web Development
    "html", "css", "javascript", "react", "vue", "angular", "node.js", "express.js", "next.js", "bootstrap", "tailwind css","django",

    # Backend / Frameworks
    "flask", "django", "spring boot", "fastapi", "laravel", ".net", "asp.net", "gin", "rails",

    # Databases
    "mysql", "postgresql", "sqlite", "mongodb", "firebase", "oracle", "redis", "dynamodb",

    # Data Science & Analytics
    "numpy", "pandas", "matplotlib", "seaborn", "scikit-learn", "plotly", "statsmodels", "power bi", "tableau", "excel", "looker",

    # Machine Learning / AI
    "machine learning", "deep learning", "supervised learning", "unsupervised learning", "reinforcement learning",
    "computer vision", "nlp", "natural language processing", "recommendation systems", "clustering", "classification", "regression",

    # DL Frameworks
    "tensorflow", "keras", "pytorch", "transformers", "openai", "langchain", "huggingface", "bert", "gpt", "yolov5",

    # DevOps & Cloud
    "aws", "azure", "google cloud", "gcp", "heroku", "docker", "kubernetes", "jenkins", "terraform", "github actions", "cloud computing", "ci/cd",

    # Version Control / VCS
    "git", "github", "bitbucket", "gitlab",

    # Testing & Agile
    "selenium", "pytest", "unit testing", "test automation", "jira", "agile", "scrum", "kanban",

    # Operating Systems / Tools
    "linux", "ubuntu", "windows", "bash", "shell scripting", "terminal", "vim", "command line",

    # Mobile Development
    "android", "kotlin", "java", "flutter", "react native", "swift", "ios",

    # Big Data & Streaming
    "hadoop", "spark", "kafka", "hive", "pig",

    # APIs / Integration
    "rest api", "graphql", "postman", "api testing", "json", "xml",

    # Soft Skills / Business
    "communication", "teamwork", "leadership", "problem solving", "critical thinking", "collaboration", "time management", "adaptability", "creativity",

    # Misc / Bonus
    "data engineering", "data warehousing", "etl", "airflow", "snowflake", "dbt", "salesforce", "sap", "figma", "ui/ux design", "automation", "prompt engineering"
]

def extract_skills(text):
    
    found_skills = []
    for skill in SKILL_KEYWORDS:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text.lower()):
            found_skills.append(skill.lower())
    return sorted(set(found_skills))


def match_skills(jd_skills, resume_skills):
    matched = list(set(jd_skills) & set(resume_skills))
    missing = list(set(jd_skills) - set(resume_skills))
    return sorted(matched), sorted(missing)
