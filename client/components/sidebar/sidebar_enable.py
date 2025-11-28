import streamlit as st

def enable_button():
    with st.sidebar:
        st.toggle(
            label = "Enable Web Searching",
            help = "test"
        )
        st.toggle(
            label = "Enable Map Searching",
            help = "test"
        )
        st.toggle(
            label = "Enable URL Detection",
            help = "test"
        )