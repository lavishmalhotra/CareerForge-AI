from database.db import create_tables
from utils.theme import load_css

import streamlit as st

create_tables()

st.set_page_config(
    page_title="CareerForge AI",
    page_icon="🚀",
    layout="wide"
)

# Load Custom CSS
load_css()

st.title("🚀 CareerForge AI")

st.markdown("""
# Welcome to CareerForge AI

### Your AI Powered Career Assistant

### 🚀 Features

- 📄 Resume Analyzer
- 🤖 AI Resume Review
- 💼 JD Matcher
- 📚 Skill Gap Analyzer
- 📄 Cover Letter Generator
- 🎯 ATS Score
- 📑 Resume Builder
- 🤖 AI Mock Interview
- 🗺️ AI Roadmap Generator

👈 Select a page from the sidebar to get started.
""")