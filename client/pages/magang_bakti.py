import streamlit as st
# from PIL import Image
from components.sidebar.sidebar_message import render_sidebar_message
from components.sidebar.sidebar_logout import logout_button

st.title("Explore all the Magang Bakti")
st.markdown("Practice real-world scenario through immersive roleplays or personalized tutoring.")
st.text_input(label = "Search for tutors", label_visibility = "collapsed", width = 600, icon = ":material/search:", placeholder = "Search for tutors")
st.divider()
st.subheader("Magang Bakti")
row = st.columns(3)


dummy_advisor = {
    "Title": [
        "Customer Services",
        "Teller",
        "Customer Relationship Officer",
        "Personal Customer Relationship",
        "Compliance Training",
        "Branch Manager"
    ],
    "Description": [
        "Deliver exceptional customer experiences by learning effective communication.", # Master key banking products and services through interactive real-world scenarios.
        "Master cash handling, transaction processing, and customer interaction in a fast-paced environment.",
        "Build strong relationships with clients about banking solutions.",
        "Offer personalized financial advice and support to customer.",
        "Understand and apply banking regulations, anti-money laundering policies.",
        "Lead branch operations, manage teams, and drive business growth through strategic decision-making."
    ],
    "Image Path": [
        "./assets/roleplay/CS.png", # PK
        "./assets/roleplay/T.png",
        "./assets/roleplay/CRO.png",
        "./assets/roleplay/PCRO.png",
        "./assets/roleplay/CTs.png",
        "./assets/roleplay/PK.png",
    ]
}
    
num_cols = 3
num_cards = len(dummy_advisor["Title"])

for start in range(0, num_cards, num_cols):
    row = st.columns(num_cols)
    for idx, col in enumerate(row):
        card_idx = start + idx
        if card_idx < num_cards:
            with col:
                with st.container(border = True, height = "stretch"):
                    left, right = st.columns(2)
                    with left:
                        st.image(image = dummy_advisor["Image Path"][card_idx])
                    with right:
                        st.markdown(f"### {dummy_advisor['Title'][card_idx]}") 
                        st.markdown(dummy_advisor['Description'][card_idx])
                        st.button(label = "Read More", key = [card_idx], width = "stretch", type = "primary")

#######################
# Sidebar
render_sidebar_message()
logout_button()