import streamlit as st

def model_selection(disabled = False):
    model_options = ["GPT-4.1", "Google Gemini 3", "Claude Sonnet 4", "Grok Code Fast 1"]
    with st.sidebar:
        ai_model = st.selectbox(
            label = "Select a model:",
            options = model_options,
            disabled = disabled
        )