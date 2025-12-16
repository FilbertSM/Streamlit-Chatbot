import streamlit as st

def suggestion_button(question):
    st.markdown("**Examples**")


    # button_suggestions = question if question else [
    #     "How do I process a loan application?"
    # ]
    # Set how many buttons per row
    # buttons_row = 2

    # for i in range(0, len(button_suggestions), buttons_row):
    #     cols = st.columns(buttons_row)
    #     for idx, suggestion in enumerate(button_suggestions[i:i+buttons_row]):
    #         with cols[idx]:
    #             if st.button(
    #                 label = suggestion,
    #                 type = "secondary",
    #                 use_container_width= False
    #             ):
    #                 st.write("Nice") # The text will be placed on placeholder of chat
    
    if st.button(
        label = question,
        type = "secondary",
        use_container_width= False
    ):
        st.write("Nice") # The text will be placed on placeholder of chat
