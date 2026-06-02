import streamlit as st
from agents.suspect_agent import rank_suspects

st.title("👤 Suspect Ranking")

if "case_text" not in st.session_state:

    st.warning("Please upload documents on Home Page.")

else:

    with st.spinner("Ranking suspects..."):

        suspects = rank_suspects(
            st.session_state["case_text"]
        )

    st.markdown(suspects)