import streamlit as st

def clearsave_button(user_input):
    if user_input:
        with st.sidebar:
            labels = ["🗑️ Clear", "📥 Save"]
            actions = ["Cleared", "Saved"]
            cols = st.columns(2)
            for i, label in enumerate(labels):
                with cols[i]:
                    if st.button(label):
                        st.text(actions[i])