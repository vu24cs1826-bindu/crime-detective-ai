import streamlit as st
from utils import extract_text

st.set_page_config(
    page_title="Crime Detective AI",
    page_icon="🕵️",
    layout="wide"
)

# Header
st.title("🕵️ Crime Detective AI")

st.markdown("""
### AI-Powered Crime Investigation Platform

Upload case files and investigate evidence using AI-powered forensic tools.
""")

st.divider()

# Investigation Cards
st.subheader("🚔 Investigation Modules")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🔍 Evidence Analysis")

with col2:
    st.info("📅 Timeline Generation")

with col3:
    st.info("⚠️ Contradiction Detection")

col4, col5, col6 = st.columns(3)

with col4:
    st.info("👤 Suspect Ranking")

with col5:
    st.info("🕸️ Crime Network")

with col6:
    st.info("📄 Final Report")

st.divider()

# Upload Section
uploaded_files = st.file_uploader(
    "📂 Upload Case Documents",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    all_text = ""

    for file in uploaded_files:
        all_text += extract_text(file)

    st.session_state["case_text"] = all_text

    st.success("🟢 Case Loaded and Ready for Investigation")

    st.progress(100)

    st.info("🕵️ Investigation System Ready")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📄 Documents", len(uploaded_files))

    with col2:
        st.metric("👤 Suspects", "Detected")

    with col3:
        st.metric("📍 Locations", "Detected")

    with col4:
        st.metric("🚗 Vehicles", "Detected")

    with st.expander("📄 Document Preview"):

        st.text_area(
            "Case Content",
            all_text[:2000],
            height=250
        )

else:

    st.info(
        "Upload one or more PDF case files to begin the investigation."
    )