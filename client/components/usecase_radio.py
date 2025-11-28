import streamlit as st

def usecase_radio():
    st.radio(
        label="Usecase presets",
        options = ["chatting", "text summarization", "code generation", "creative writing"],
        help = "Select a use case to optimize the chatbot for your specific task.",
        horizontal = True
    )