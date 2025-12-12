import streamlit as st
from components.sidebar.sidebar_message import render_sidebar_message
from components.sidebar.sidebar_model import model_selection
from components.sidebar.sidebar_advance_options import advance_options
from components.sidebar.sidebar_logout import logout_button
from components.sidebar.sidebar_clearsave_button import clearsave_button
from utils.api import ask_question_api

st.set_page_config(page_title="GAIA", layout="wide")

#######################
# Main App
st.markdown("""
<div style="
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 60px;
">
    <div style="
        overflow: hidden;
        background-color: rgba(0, 0, 0, 0);
        border: 0px solid black;
        box-sizing: border-box;
        width: 150px;
        height: 150px;
        border-radius: 100%;
        position: relative;
        display: flex;
        flex-direction: column;
    ">
        <div style="width: 150px; height: 150px; position: relative;">
            <img 
                src="https://images.pexels.com/photos/7691662/pexels-photo-7691662.jpeg"
                alt=""
                loading="lazy"
                decoding="async"
                style="
                    object-position: left 50% top 50%;
                    width: 100%;
                    height: 100%;
                    position: absolute;
                    top: 0px;
                    left: 0px;
                    object-fit: cover;
                    border-radius: 100%;
                "
            >
        </div>
    </div>
    <div>
        <h1>Product Knowledge</h1>
    </div>
    <div style="margin-bottom: 32px; color: #aaa; font-size: 15px; text-align: center; max-width: 320px;">
        Master key banking products and services through interactive real-world scenarios.
    </div>
</div>
""", unsafe_allow_html=True)

#######################
# Session Variable
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render existing chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Chatbot
user_input = st.chat_input("Hi! Ask me anything...")
role_id = "product-knowledge"
if user_input:
    # Show user input to chat
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # API Call to Backend
    response = ask_question_api(user_input, role_id)

    if response.status_code == 200:
        # Extract the answer and sources
        data = response.json()
        answer = data
        # sources = data.get("sources", [])
        
        # Display AI Response
        st.chat_message("assistant").markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
    else:
        st.error(f"Error: {response.text}")

#######################
# Sidebar
render_sidebar_message()
model_selection(disabled = True)
clearsave_button(user_input)
advance_options()
logout_button()