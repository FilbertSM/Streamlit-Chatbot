import streamlit as st
from components.upload import render_uploader
from components.history_download import render_history_download
from components.chatUI import render_chat
from components.sidebar_logo import render_sidebar_logo
from components.sidebar_message import render_sidebar_message

st.set_page_config(page_title="GAIA", layout="wide")

# Main App
st.title("Chatbot")

# Sidebar
render_sidebar_logo()
# render_sidebar_message()

render_uploader()
render_chat()
render_history_download()