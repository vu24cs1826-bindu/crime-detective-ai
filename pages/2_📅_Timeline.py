import streamlit as st
from agents.timeline_agent import create_timeline

st.title("📅 Investigation Timeline")

if "case_text" not in st.session_state:

    st.warning("Please upload documents on Home Page.")

else:

    with st.spinner("Generating timeline..."):

        timeline = create_timeline(
            st.session_state["case_text"]
        )

    st.markdown(timeline)