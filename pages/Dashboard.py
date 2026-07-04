import streamlit as st

st.title("📊 Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("ATS Score", "0")
col2.metric("Interviews", "0")
col3.metric("Roadmaps", "0")
col4.metric("Applications", "0")

st.divider()

st.subheader("📄 Recent Activity")

st.info("No activity available.")