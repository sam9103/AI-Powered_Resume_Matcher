# app.py

import streamlit as st
from pipeline import run_pipeline
import os
from datetime import datetime

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="AI Resume Matcher", layout="centered")

# ---------- HEADER ----------
st.markdown(
    """
    <h1 style='text-align: center; color: #6495ED;'>AI-Powered Resume Matcher</h1>
    <p style='text-align: center; font-size: 18px;'>Upload a Job Description and Resume to get an instant skill match and similarity score.</p>
    """,
    unsafe_allow_html=True
)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.header("📄 File Upload")
    jd_file = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])
    resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    st.markdown("---")

# ---------- MAIN AREA ----------
if jd_file and resume_file:
    if st.button(" Match Resume"):
        with st.spinner("Analyzing resume..."):

            # Ensure folders exist
            os.makedirs("data/job_description", exist_ok=True)
            os.makedirs("data/resume", exist_ok=True)

            # Save uploaded files to 'data/' folder
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            jd_path = f"data/job_description/JD_{timestamp}.pdf"
            resume_path = f"data/resume/Resume_{timestamp}.pdf"

            with open(jd_path, "wb") as f:
                f.write(jd_file.read())

            with open(resume_path, "wb") as f:
                f.write(resume_file.read())

            # Run the analysis pipeline
            result = run_pipeline(jd_path, resume_path)

        # ---------- OUTPUTS ----------
        st.success("✅ Analysis Complete!")

        # Similarity Score
        st.subheader(" Resume - JD Similarity")
        st.metric("Similarity Score", f"{result['similarity_score']}%")

        # Matched Skills
        st.subheader("✅ Matched Skills")
        if result["matched_skills"]:
            st.success(", ".join(result["matched_skills"]))
        else:
            st.warning("No matched skills found.")

else:
    st.info("👈 Please upload both a Job Description and Resume PDF to get started.")
