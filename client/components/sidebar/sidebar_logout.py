import streamlit as st

def logout_button():
    with st.sidebar:
        if st.button(
            label = "Logout",
            type = "primary"
        ):
            st.text("Logout")