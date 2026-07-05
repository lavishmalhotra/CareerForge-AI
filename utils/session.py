import streamlit as st


def save_resume(data):
    """
    Save parsed resume into session.
    """
    st.session_state["resume_data"] = data


def get_resume():
    """
    Return parsed resume if available.
    """
    return st.session_state.get("resume_data", None)


def has_resume():
    """
    Check whether resume exists.
    """
    return "resume_data" in st.session_state


def clear_resume():
    """
    Remove resume from session.
    """
    if "resume_data" in st.session_state:
        del st.session_state["resume_data"]