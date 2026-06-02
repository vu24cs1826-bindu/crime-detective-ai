import streamlit as st
from graph_builder import create_graph

st.title("🕸️ Crime Relationship Network")

if "case_text" not in st.session_state:

    st.warning("Please upload documents on Home Page.")

else:

    fig = create_graph(
        st.session_state["case_text"]
    )

    st.pyplot(fig)