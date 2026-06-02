import streamlit as st
from agents.evidence_agent import analyze_evidence
from agents.timeline_agent import create_timeline
from agents.contradiction_agent import find_contradictions
from agents.master_detective import generate_report

st.title("📄 Investigation Report")

if "case_text" not in st.session_state:

    st.warning("Please upload documents on Home Page.")

else:

    with st.spinner("Generating report..."):

        evidence = analyze_evidence(
            st.session_state["case_text"]
        )

        timeline = create_timeline(
            st.session_state["case_text"]
        )

        contradictions = find_contradictions(
            st.session_state["case_text"]
        )

        report = generate_report(
            evidence,
            timeline,
            contradictions
        )
    st.success("✅ Investigation Report Generated")

    st.markdown(report)

    st.download_button(
    "📥 Download Report",
    report,
    file_name="investigation_report.txt"
)