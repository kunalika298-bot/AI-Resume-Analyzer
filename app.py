import streamlit as st
import matplotlib.pyplot as plt

from utils.pdf_extractor import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.job_matcher import match_jobs

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.write("Upload your resume and get AI-based job matches.")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text_from_pdf(uploaded_file)

    st.subheader("📌 Resume Text")
    st.write(text)

    skills = extract_skills(text)

    st.subheader("🛠 Detected Skills")

    if skills:
        st.write(skills)
        score = min(len(skills) * 10, 100)
        st.subheader("📊 Resume Score")
        st.progress(score)
        st.write(f"Resume Score: {score}/100")
        st.subheader("📈 Skills Distribution")

        fig, ax = plt.subplots()

        ax.pie(
            [1] * len(skills),
            labels=skills,
            autopct='%1.1f%%'
        )

        st.pyplot(fig)
    else:
        st.warning("No matching skills found.")

    matched_jobs = match_jobs(text)
    top_job = matched_jobs.iloc[0]

    required_skills = (
    top_job['description']
    .split()
    )

    missing_skills = []

    for skill in required_skills:
        if skill.lower() not in text.lower():
            missing_skills.append(skill)
    st.subheader("❌ Missing Skills")

    if missing_skills:
        st.write(missing_skills)
    else:
        st.success(
        "No missing skills! Great Resume 🎉"
    )
    st.subheader("💼 Job Match Scores")

    st.dataframe(
        matched_jobs[['job_title', 'match_score']]
    )