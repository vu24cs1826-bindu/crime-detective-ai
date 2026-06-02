import streamlit as st
from agents.contradiction_agent import find_contradictions

st.title("⚠️ Contradiction Analysis")

if "case_text" not in st.session_state:

    st.warning("Please upload documents on Home Page.")

else:

    with st.spinner("Finding contradictions..."):

        contradictions = find_contradictions(
            st.session_state["case_text"]
        )

    st.markdown(contradictions)