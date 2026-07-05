import os

from dotenv import load_dotenv
from google import genai

from ai.prompts import (
    RESUME_REVIEW_PROMPT,
    JD_MATCH_PROMPT,
    SKILL_GAP_PROMPT,
    COVER_LETTER_PROMPT
)

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ==========================================================
# Generic Gemini Function
# ==========================================================

def ask_gemini(prompt: str):

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"""
# ❌ Gemini Error

{e}
"""


# ==========================================================
# AI Resume Review
# ==========================================================

def review_resume(resume_text):

    prompt = RESUME_REVIEW_PROMPT.format(
        resume_text
    )

    return ask_gemini(prompt)


# ==========================================================
# AI JD Matcher
# ==========================================================

def review_jd_match(
    resume_text,
    job_description
):

    prompt = JD_MATCH_PROMPT.format(
        resume_text,
        job_description
    )

    return ask_gemini(prompt)


# ==========================================================
# AI Skill Gap Analyzer
# ==========================================================

def analyze_skill_gap(
    resume_text,
    job_description
):

    prompt = SKILL_GAP_PROMPT.format(
        resume_text,
        job_description
    )

    return ask_gemini(prompt)


# ==========================================================
# AI Cover Letter Generator
# ==========================================================

def generate_cover_letter(
    resume_text,
    company,
    role,
    job_description
):

    prompt = COVER_LETTER_PROMPT.format(
        resume_text,
        company,
        role,
        job_description
    )

    return ask_gemini(prompt)