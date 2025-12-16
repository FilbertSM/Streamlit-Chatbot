import streamlit as st
import pandas as pd
import json 
# from components.sidebar.sidebar_logo import render_sidebar_logo
from components.sidebar.sidebar_message import render_sidebar_message
from components.sidebar.sidebar_logout import logout_button
from components.upload import render_uploader

#######################
# Main App
st.title("Database")
st.markdown(f"""
    <div style='display: flex; justify-content: flex-start; gap: 1rem; font-size: 1.5rem; margin-bottom: 1.5rem;'>
        <span style='background-color: #bbf7d1; color: #16a24b; font-weight: 600; border-radius: 6px; padding: 0.25rem 0.75rem; line-height: 2rem; flex: inline;'>Successfully Indexed: 4,480</span>
        <span style='background-color: #fecbcb; color: #dc2726; font-weight: 600; border-radius: 6px; padding: 0.25rem 0.75rem; line-height: 2rem; flex: inline;'>Processing: 17</span>
        <span style='background-color: #fef18a; color: #ca8b19; font-weight: 600; border-radius: 6px; padding: 0.25rem 0.75rem; line-height: 2rem; flex: inline;'>Failed: 8</span>
    </div>
""", unsafe_allow_html=True)

with st.container(border=True, height="stretch"):
    st.header("RAG Documents Database", width="stretch")

    with st.container(horizontal=True):
        st.text_input(label = "Search", label_visibility = "collapsed", placeholder = "Search", icon = ":material/search:", width = 500)
        st.selectbox(label = "Filter", label_visibility = "collapsed", options = ["Indexed", "Processing", "Failed"], width = 150)
        st.selectbox(label = "All Columns", label_visibility ="collapsed", options = ["All Columns", "Important"], width = 150)
    
    df = None
    with open("../server/data/database.json", "r", encoding="utf-8") as f:
        if f:            
            df = df = pd.DataFrame(json.load(f))

    if df not in st.session_state:
        st.session_state.df = pd.DataFrame(df)
    
    df.index = range(1, len(df) + 1)
    st.data_editor(
        df,
        column_config = {
            "RAG Status": st.column_config.MultiselectColumn(
                "RAG Status",
                options = ["Indexed", "Processing", "Failed"],
                color = ["#bbf7d1", "#fef18a", "#fecbcb"]
            ),
            "Actions": st.column_config.LinkColumn("Actions", display_text = "Edit Here")
        },
        height = 600
    )
    st.session_state.df.reset_index(drop=True, inplace=True)

#######################
# Sidebar
render_sidebar_message()
render_uploader()
logout_button()