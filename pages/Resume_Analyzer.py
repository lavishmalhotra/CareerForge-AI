import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from utils.resume_parser import parse_resume
from utils.resume_score import calculate_ats_score

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Your Resume",
    type=["pdf"]
)

if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)

    info = parse_resume(resume_text)

    score, strengths, weaknesses, suggestions = calculate_ats_score(
        info,
        resume_text
    )

    st.success("Resume Parsed Successfully ✅")

    st.divider()

    st.subheader("👤 Candidate Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Name:** {info['Name']}")
        st.write(f"**Email:** {info['Email']}")
        st.write(f"**Phone:** {info['Phone']}")

    with col2:
        st.write(f"**GitHub:** {info['GitHub']}")
        st.write(f"**LinkedIn:** {info['LinkedIn']}")

    st.divider()

    st.subheader("💻 Skills")

    if info["Skills"]:

        cols = st.columns(3)

        for i, skill in enumerate(info["Skills"]):

            with cols[i % 3]:
                st.success(skill)

    else:

        st.warning("No Skills Found")

    st.divider()

    st.subheader("🎯 ATS Score")

    st.progress(score / 100)

    st.metric(
        "Overall ATS Score",
        f"{score}/100"
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Strengths")

        if strengths:

            for item in strengths:
                st.success(item)

        else:

            st.info("No strengths detected.")

    with col2:

        st.subheader("❌ Weaknesses")

        if weaknesses:

            for item in weaknesses:
                st.error(item)

        else:

            st.success("No weaknesses detected.")

    st.divider()

    st.subheader("💡 Improvement Suggestions")

    if suggestions:

        for item in suggestions:
            st.warning(item)

    else:

        st.success("Excellent Resume! 🎉")

    with st.expander("📄 View Extracted Resume"):

        st.text(resume_text)