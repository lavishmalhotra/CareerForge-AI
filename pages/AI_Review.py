import streamlit as st

from utils.session import has_resume, get_resume
from ai.llm import review_resume
from database.db import save_history
from utils.pdf_generator import create_pdf

st.set_page_config(
    page_title="AI Resume Review",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Review")

# ==========================================================
# Check Resume
# ==========================================================

if not has_resume():

    st.warning("Please upload a resume first.")

    st.stop()

# ==========================================================
# Load Resume
# ==========================================================

resume = get_resume()

resume_text = resume["Raw_Text"]

# ==========================================================
# Resume Summary
# ==========================================================

st.subheader("📄 Resume Summary")

col1, col2 = st.columns(2)

with col1:

    st.write(f"**👤 Name:** {resume['Name']}")
    st.write(f"**📧 Email:** {resume['Email']}")

with col2:

    st.write(f"**💻 Skills:** {len(resume['Skills'])}")
    st.write(f"**📂 Projects:** {len(resume['Projects'])}")

st.divider()

# ==========================================================
# Skills
# ==========================================================

st.subheader("💻 Skills")

if resume["Skills"]:

    cols = st.columns(3)

    for i, skill in enumerate(resume["Skills"]):

        with cols[i % 3]:

            st.success(skill)

else:

    st.warning("No skills detected.")

st.divider()

# ==========================================================
# Generate AI Review
# ==========================================================

if st.button(
    "🚀 Generate AI Review",
    use_container_width=True
):

    with st.spinner("🤖 AI is reviewing your resume..."):

        review = review_resume(
            resume_text
        )

    # ------------------------------------------------------
    # Save History
    # ------------------------------------------------------

    save_history(
        report_type="AI Resume Review",
        title=resume["Name"],
        content=review
    )

    st.success("✅ Report Saved")

    st.divider()

    st.subheader("🤖 AI Resume Review")

    st.markdown(review)

    # ======================================================
    # PDF Download
    # ======================================================

    pdf_file = create_pdf(
        "AI Resume Review",
        review,
        "resume_review.pdf"
    )

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="⬇ Download PDF",
            data=file,
            file_name="AI_Resume_Review.pdf",
            mime="application/pdf",
            use_container_width=True
        )