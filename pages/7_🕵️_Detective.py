import streamlit as st
from agents.detective_agent import ask_detective
st.title("🕵️ Detective Assistant")

st.markdown(
    "Ask questions about the uploaded case documents."
)

if "case_text" not in st.session_state:

    st.warning(
        "Please upload documents on the Home Page."
    )

else:

    # Store chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    question = st.chat_input(
        "Ask the detective..."
    )

    if question:

        # Show user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.write(question)

        with st.spinner("Investigating case files..."):

            answer = ask_detective(
                question,
                st.session_state["case_text"]
            )

        with st.chat_message("assistant"):
            st.write(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )