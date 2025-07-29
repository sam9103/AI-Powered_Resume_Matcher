# resume_matcher/pipeline.py

from utils import extract_text_from_pdf, clean_text
from skills_matcher import extract_skills, match_skills
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def process_documents(jd_path, resume_path):
    # Extract text
    jd_text_raw = extract_text_from_pdf(jd_path)
    resume_text_raw = extract_text_from_pdf(resume_path)

    # Clean text
    jd_text = clean_text(jd_text_raw)
    resume_text = clean_text(resume_text_raw)

    return jd_text, resume_text


def calculate_similarity(jd_text, resume_text):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([jd_text, resume_text])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(similarity[0][0] * 100, 2)  # Return percentage


def run_pipeline(jd_path, resume_path):
    jd_text, resume_text = process_documents(jd_path, resume_path)
    similarity_score = calculate_similarity(jd_text, resume_text)

    jd_skills = extract_skills(jd_text)
    resume_skills = extract_skills(resume_text)
    matched_skills, unmatched_skills = match_skills(jd_skills, resume_skills)

    result = {
        "similarity_score": similarity_score,
        "jd_skills": jd_skills,
        "resume_skills": resume_skills,
        "matched_skills": matched_skills,
        "missing_skills": unmatched_skills
    }

    return result
