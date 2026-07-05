import streamlit as st

from database.db import (
    get_history,
    get_report
)

st.set_page_config(
    page_title="History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 AI Report History")
st.caption("View all previously generated AI reports.")

history = get_history()

if not history:

    st.info("No reports found.")

    st.stop()

for index, item in enumerate(history):

    report_type = item[0]
    title = item[1]
    created_at = item[2]

    with st.expander(
        f"{report_type} • {title} • {created_at}"
    ):

        report = get_report(index + 1)

        if report:

            st.markdown(report[3])

        else:

            st.error("Unable to load report.")