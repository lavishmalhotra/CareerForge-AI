import streamlit as st

from ai.llm import generate_cover_letter
from utils.session import has_resume, get_resume
from database.db import save_history
from utils.pdf_generator import create_pdf

st.set_page_config(
    page_title="Cover Letter Generator",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Cover Letter Generator")
st.caption("Generate an ATS Friendly Cover Letter using AI.")

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

# ==========================================================
# Resume Summary
# ==========================================================

st.subheader("📄 Current Resume")

c1, c2 = st.columns(2)

with c1:

    st.write(f"**👤 Name:** {resume['Name']}")
    st.write(f"**📧 Email:** {resume['Email']}")

with c2:

    st.write(f"**💻 Skills:** {len(resume['Skills'])}")
    st.write(f"**📂 Projects:** {len(resume['Projects'])}")

st.divider()

# ==========================================================
# Input
# ==========================================================

company = st.text_input(
    "🏢 Company Name"
)

role = st.text_input(
    "💼 Job Role"
)

job_description = st.text_area(
    "📋 Job Description",
    height=250,
    placeholder="Paste complete Job Description here..."
)

# ==========================================================
# Generate
# ==========================================================

if st.button(
    "🚀 Generate Cover Letter",
    use_container_width=True
):

    if (
        company.strip() == ""
        or role.strip() == ""
        or job_description.strip() == ""
    ):

        st.error("Please fill all fields.")

        st.stop()

    with st.spinner(
        "🤖 AI is generating your Cover Letter..."
    ):

        letter = generate_cover_letter(
            resume_text,
            company,
            role,
            job_description
        )

    save_history(
        report_type="Cover Letter",
        title=f"{company} - {role}",
        content=letter
    )

    st.success("✅ Cover Letter Saved")

    st.divider()

    st.subheader("📄 Generated Cover Letter")

    st.markdown(letter)
        # ======================================================
    # PDF Download
    # ======================================================

    pdf_file = create_pdf(
        "AI Cover Letter",
        letter,
        "cover_letter.pdf"
    )

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="⬇ Download Cover Letter",
            data=file,
            file_name="Cover_Letter.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    # ======================================================
    # Copy Button
    # ======================================================

    st.divider()

    st.subheader("📋 Copy Cover Letter")

    st.code(
        letter,
        language="text"
    )

    st.info(
        "💡 You can copy the cover letter from the box above and paste it into your job application."
    )

# ==========================================================
# Tips
# ==========================================================

st.divider()

st.subheader("💼 Cover Letter Tips")

st.success("""
✔ Keep your cover letter to one page.

✔ Mention the company name.

✔ Highlight your most relevant skills.

✔ Mention projects related to the role.

✔ End with a professional closing.
""")

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "🚀 CareerForge AI • AI Powered Cover Letter Generator"
)