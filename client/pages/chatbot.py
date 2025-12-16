import streamlit as st
from components.sidebar.sidebar_message import render_sidebar_message
from components.sidebar.sidebar_model import model_selection
from components.sidebar.sidebar_advance_options import advance_options
from components.sidebar.sidebar_logout import logout_button
from components.sidebar.sidebar_enable import enable_button
from components.usecase_radio import usecase_radio
from components.suggestion_button import suggestion_button
from components.sidebar.sidebar_clearsave_button import clearsave_button
from utils.api import ask_question_api

st.set_page_config(page_title="GAIA", layout="wide")

#######################
# Main App
st.title("Chatbot")
st.markdown("""
Hello! Welcome to **GAIA Chatbot** by Filbert\n\n

A few tips:\n\n

1. **Upload your PDF files** using the sidebar before starting a chat.
2. **Ask clear and specific questions** for better answers.
3. **Download your chat history** anytime using the sidebar.
4. **Use the feedback button** to report issues or suggest improvements.
5. **Your data is private**—only you can see your uploaded documents and chat.

Enjoy chatting!
""")

usecase_radio()
suggestion_button("How do I process a loan application?")

#######################
# Session Variable
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render existing chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Chatbot
user_input = st.chat_input("Hi! Ask me anything...")
role_id = "chatbot"
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
        # placeholder = st.empty()
        # displayed = ""
        # for char in answer:
        #     displayed += char
        #     placeholder.markdown(displayed)
        #     time.sleep(0.005)

        # Adding sources to on the answer if exist
        # if sources:
        #     st.markdown("📃 **Sources:**")
        #     for src in sources:
        #         st.markdown(f"- `{src}`")
        
        # Save AI Response in Chat History
        st.session_state.messages.append({"role": "assistant", "content": answer})
    else:
        st.error(f"Error: {response.text}")

#######################
# Sidebar
render_sidebar_message()
model_selection()
clearsave_button(user_input)
enable_button()
advance_options()
logout_button()