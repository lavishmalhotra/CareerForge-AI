import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from utils.resume_parser import parse_resume
from utils.resume_score import calculate_ats_score
from utils.session import save_resume

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.caption("Upload your resume and get an ATS analysis report.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    # ---------------- PDF Parsing ----------------

    resume_text = extract_text_from_pdf(uploaded_file)

    # ---------------- Resume Parsing ----------------

    info = parse_resume(resume_text)

    # Save for all pages
    save_resume(info)
    info["Raw_Text"] = resume_text
    # ---------------- ATS ----------------

    score, strengths, weaknesses, suggestions = calculate_ats_score(
        info,
        resume_text
    )

    st.success("Resume Parsed Successfully ✅")

    st.divider()

    # ============================================================
    # Candidate Information
    # ============================================================

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

    # ============================================================
    # Skills
    # ============================================================

    st.subheader("💻 Skills")

    if info["Skills"]:

        cols = st.columns(3)

        for i, skill in enumerate(info["Skills"]):

            with cols[i % 3]:
                st.success(skill)

    else:

        st.warning("No skills detected.")

    st.divider()

    # ============================================================
    # Education
    # ============================================================

    st.subheader("🎓 Education")

    if info["Education"]:

        for edu in info["Education"]:
            st.info(edu)

    else:

        st.warning("Education section not found.")

    st.divider()

    # ============================================================
    # Projects
    # ============================================================

    st.subheader("📂 Projects")

    if info["Projects"]:

        for project in info["Projects"]:
            st.success(project)

    else:

        st.warning("Projects not found.")

    st.divider()

    # ============================================================
    # Certifications
    # ============================================================

    st.subheader("📜 Certifications")

    if info["Certifications"]:

        for cert in info["Certifications"]:
            st.info(cert)

    else:

        st.warning("No certifications detected.")

    st.divider()

    # ============================================================
    # Experience
    # ============================================================

    st.subheader("💼 Experience")

    if "Experience" in info and info["Experience"]:

        for exp in info["Experience"]:
            st.success(exp)

    else:

        st.warning("No experience detected.")

    st.divider()

    # ============================================================
    # ATS Score
    # ============================================================

    st.subheader("🎯 ATS Score")

    st.progress(score / 100)

    st.metric(
        label="Overall ATS Score",
        value=f"{score}/100"
    )

    st.divider()

    # ============================================================
    # Strengths & Weaknesses
    # ============================================================

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

    # ============================================================
    # Suggestions
    # ============================================================

    st.subheader("💡 Improvement Suggestions")

    if suggestions:

        for item in suggestions:
            st.warning(item)

    else:

        st.success("Excellent Resume! 🎉")

    st.divider()

    # ============================================================
    # Raw Resume
    # ============================================================

    with st.expander("📄 View Extracted Resume Text"):

        st.text(resume_text)

else:

    st.info("Upload a PDF resume to start the analysis.")