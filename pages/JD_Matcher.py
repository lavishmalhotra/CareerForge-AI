import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from utils.resume_parser import parse_resume, COMMON_SKILLS
from utils.jd_matcher import extract_skills, match_resume_with_jd

st.set_page_config(
    page_title="JD Matcher",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Job Description Matcher")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

if st.button("Analyze Match"):

    if uploaded_file is None:
        st.error("Please upload a resume.")
        st.stop()

    if job_description.strip() == "":
        st.error("Please paste the Job Description.")
        st.stop()

    # Resume Parsing
    resume_text = extract_text_from_pdf(uploaded_file)
    resume_info = parse_resume(resume_text)

    resume_skills = resume_info["Skills"]

    jd_skills = extract_skills(
        job_description,
        COMMON_SKILLS
    )

    result = match_resume_with_jd(
        resume_skills,
        jd_skills
    )

    st.divider()

    st.subheader("🎯 Match Score")

    st.progress(result["percentage"] / 100)

    st.metric(
        "Resume Match",
        f"{result['percentage']}%"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matched Skills")

        if result["matched"]:

            for skill in result["matched"]:
                st.success(skill.title())

        else:

            st.warning("No matched skills.")

    with col2:

        st.subheader("❌ Missing Skills")

        if result["missing"]:

            for skill in result["missing"]:
                st.error(skill.title())

        else:

            st.success("Excellent!")

    st.divider()

    st.subheader("💡 Recommendations")

    if result["recommendations"]:

        for item in result["recommendations"]:
            st.info(item)

    else:

        st.success("Excellent Match 🎉")