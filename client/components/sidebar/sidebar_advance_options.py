import streamlit as st

temp_options = [f"{x * 0.1:.2f}" for x in range(11)]
token_options = list(range(100, 4001, 100))

def advance_options():
    with st.sidebar:
        with st.popover("⚙️ Advanced Options"):
            temperature = st.select_slider(
                label = "Temperature",
                options = temp_options,
                help = "Select the temperature",
                label_visibility = "visible"
            )

            token_output = st.select_slider(
                label = "Token Output",
                options = token_options,
                help = "Select the token output"
            )

            uploaded_conversation = st.file_uploader(
                label = "Load Conversation",
                type = "json",
                accept_multiple_files = "false",
                help = "Upload your conversation"
            )