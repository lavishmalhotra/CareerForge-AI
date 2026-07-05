import streamlit as st

from ai.llm import analyze_skill_gap
from utils.session import has_resume, get_resume
from database.db import save_history
from utils.pdf_generator import create_pdf

st.set_page_config(
    page_title="Skill Gap Analyzer",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Skill Gap Analyzer")
st.caption("Analyze missing skills between your Resume and Job Description.")

# ==========================================================
# Resume Check
# ==========================================================

if not has_resume():

    st.warning("⚠ Please upload your Resume first.")

    st.stop()

# ==========================================================
# Load Resume
# ==========================================================

resume = get_resume()

resume_text = resume["Raw_Text"]

skills = resume["Skills"]

# ==========================================================
# Resume Summary
# ==========================================================

st.subheader("📄 Current Resume")

c1, c2 = st.columns(2)

with c1:

    st.write(f"**👤 Name:** {resume['Name']}")
    st.write(f"**📧 Email:** {resume['Email']}")

with c2:

    st.write(f"**💻 Skills:** {len(skills)}")
    st.write(f"**📂 Projects:** {len(resume['Projects'])}")

st.divider()

# ==========================================================
# Skills
# ==========================================================

st.subheader("💻 Detected Skills")

if skills:

    cols = st.columns(3)

    for i, skill in enumerate(skills):

        with cols[i % 3]:

            st.success(skill)

else:

    st.warning("No Skills Detected")

st.divider()

# ==========================================================
# Job Description
# ==========================================================

job_description = st.text_area(

    "📋 Paste Job Description",

    height=300,

    placeholder="Paste complete Job Description here..."

)

# ==========================================================
# Analyze
# ==========================================================

if st.button(

    "🚀 Analyze Skill Gap",

    use_container_width=True

):

    if job_description.strip() == "":

        st.error("Please paste a Job Description.")

        st.stop()

    with st.spinner(

        "🤖 AI is analyzing your Skill Gap..."

    ):

        report = analyze_skill_gap(

            resume_text,

            job_description

        )

    save_history(

        report_type="Skill Gap",

        title=resume["Name"],

        content=report

    )

    st.success("✅ Report Saved")

    st.divider()

    st.subheader("📚 AI Skill Gap Report")

    st.markdown(report)
        # ======================================================
    # PDF Download
    # ======================================================

    pdf_file = create_pdf(
        "AI Skill Gap Report",
        report,
        "skill_gap_report.pdf"
    )

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="⬇ Download Skill Gap Report",
            data=file,
            file_name="Skill_Gap_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

# ==========================================================
# Career Tips
# ==========================================================

st.divider()

st.subheader("💡 Career Tips")

st.info("""
- Compare your resume with every Job Description before applying.
- Learn the high-priority missing skills first.
- Build at least one project using every important missing technology.
- Update your resume after learning new skills.
""")

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "🚀 CareerForge AI • AI Powered Skill Gap Analysis"
)