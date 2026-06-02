import streamlit as st
from agents.evidence_agent import analyze_evidence

st.title("🔍 Evidence Analysis")

if "case_text" not in st.session_state:

    st.warning("Please upload documents on Home Page.")

else:

    with st.spinner("Analyzing evidence..."):

        result = analyze_evidence(
            st.session_state["case_text"]
        )
    

with st.expander("📋 Investigation Findings", expanded=True):
    st.markdown(result)
    st.success("Analysis Completed")