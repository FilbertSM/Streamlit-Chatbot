import streamlit as st

st.set_page_config(page_title="GAIA", layout="wide")

#######################
# Routes
# pages = [
#     st.Page("./pages/chatbot.py", title="💬 Chatbot"),
#     st.Page("./pages/chatbot_onprem.py", title="🗨️ Chatbot_OnPrem"),
    
#     st.Page("./pages/vision_chatbot.py", title="👁️ Vision_Chatbot"),
#     st.Page("./pages/multimodal_chatbot.py", title="🌐 Mulitmodal Chatbot"),
#     st.Page("./pages/multimodal_chatbot_onprem.py", title="🌐 Multimodal_Chatbot_OnPrem"),
#     st.Page("./pages/html_generator.py", title="🖥️ HTML Generator.py"),
#     st.Page("./pages/image_generation.py", title="🖼️ Image Generation"),
#     st.Page("./pages/deep_research.py", title="🔬 Deep Research"),
#     st.Page("./pages/feedback.py", title="✍🏻 Feedback"),
#     st.Page("./pages/dashboard.py", title="📊 Dashboard"),
# ]
pages = {
    "": [
        st.Page("./pages/chatbot.py", title="💬 Chatbot"),
        st.Page("./pages/dashboard.py", title="📊 Dashboard"),
        st.Page("./pages/database.py", title="⚙️ Database"),
    ],
    "👤 Roleplay & Tutor": [
        st.Page("./pages/trusted_advisory.py", title="Trusted Advisory"),
        st.Page("./pages/bca_leader.py", title="BCA Leader+"),
        st.Page("./pages/design_thinking.py", title="Design Thinking"),
        st.Page("./pages/magang_bakti.py", title="Magang Bakti"),
        
    ],
    "🖥️ Other Chatbot": [
        st.Page("./pages/chatbot_onprem.py", title="🗨️ Chatbot_OnPrem"),
        st.Page("./pages/vision_chatbot.py", title="👁️ Vision_Chatbot"),
        st.Page("./pages/multimodal_chatbot.py", title="🌐 Mulitmodal Chatbot"),
        st.Page("./pages/multimodal_chatbot_onprem.py", title="🌐 Multimodal_Chatbot_OnPrem"),
        st.Page("./pages/html_generator.py", title="🖥️ HTML Generator.py"),
        st.Page("./pages/image_generation.py", title="🖼️ Image Generation"),
        st.Page("./pages/deep_research.py", title="🔬 Deep Research"),
        st.Page("./pages/feedback.py", title="✍🏻 Feedback"),
        st.Page("./pages/trusted_advisory_chatbot.py", title="Trusted Advisory Chatbot")
    ]
}

pg = st.navigation(pages)
pg.run()