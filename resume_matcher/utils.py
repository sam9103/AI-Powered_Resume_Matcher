# resume_matcher/utils.py

from pdfminer.high_level import extract_text
import re


def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF using pdfminer.six
    """
    try:
        text = extract_text(pdf_path)
        return text
    except Exception as e:
        print(f"[ERROR] Failed to extract text from {pdf_path}: {e}")
        return ""


def clean_text(text):
    """
    Cleans the extracted text for NLP processing.
    - Lowercases
    - Removes special characters
    - Removes extra whitespace
    """
    text = text.lower()
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.strip()
