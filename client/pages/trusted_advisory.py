import streamlit as st
# from PIL import Image
from components.sidebar.sidebar_message import render_sidebar_message
from components.sidebar.sidebar_logout import logout_button

st.title("Explore all the Trusted Advisory")
st.markdown("Practice real-world scenario through immersive roleplays or personalized tutoring.")
st.text_input(label = "Search for tutors", label_visibility = "collapsed", width = 600, icon = ":material/search:", placeholder = "Search for tutors")
st.divider()
st.subheader("Trusted Advisory")
row = st.columns(3)


dummy_advisor = {
    "Title": [
        "Product Knowledge",
        "Business Relationship",
        "Management",
        "Risk Assessment",
        "Compliance Training",
        "Customer Service"
    ],
    "Description": [
        "Master key banking products and services through interactive real-world scenarios.",
        "Develop essential skills to build trust, communicate effectively, and grow client relationships.",
        "Enhance leadership and decision-making abilities for team management and strategic planning.",
        "Identify, evaluate, and mitigate financial risks using industry best practices.",
        "Stay updated on regulatory requirements and compliance standards through engaging.",
        "Deliver exceptional customer experiences by learning effective communication."
    ],
    "Image Path": [
        "./assets/roleplay/PK.png",
        "./assets/roleplay/BR.png",
        "./assets/roleplay/BL.png",
        "./assets/roleplay/RA.png",
        "./assets/roleplay/CT.png",
        "./assets/roleplay/CS.png",
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
                        if st.button(label = ":speech_balloon: Chat", key = [card_idx], width = "stretch", type = "primary"):
                            st.switch_page("pages/trusted_advisory_chatbot.py")

#######################
# Sidebar
render_sidebar_message()
logout_button()