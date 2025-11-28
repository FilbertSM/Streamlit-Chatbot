import streamlit as st

#######################
# Main App
st.header("Dashboard")
st.markdown(f"""
    <div style='display: flex; justify-content: flex-start; gap: 1rem; font-size: 1.5rem; margin-bottom: 1.5rem;'>
        <span style='background-color: #bbf7d1; color: #16a24b; font-weight: 600; border-radius: 6px; padding: 0.25rem 0.75rem; line-height: 2rem; flex: inline;'>Successfully Indexed: 4,480</span>
        <span style='background-color: #fecbcb; color: #dc2726; font-weight: 600; border-radius: 6px; padding: 0.25rem 0.75rem; line-height: 2rem; flex: inline;'>Processing: 17</span>
        <span style='background-color: #fef18a; color: #ca8b19; font-weight: 600; border-radius: 6px; padding: 0.25rem 0.75rem; line-height: 2rem; flex: inline;'>Failed: 8</span>
    </div>
""", unsafe_allow_html=True)

with st.container(border=True, height="stretch"):
    st.title("RAG Documents Database", width="stretch")

    with st.container(horizontal=True):
        st.text_input(label = "Search", label_visibility = "collapsed", placeholder = "Search", icon = ":material/search:", width = 500)
        st.selectbox(label = "Filter", label_visibility = "collapsed", options = ["Successful", "Processing", "Failed"], width = 150)
        st.selectbox(label = "All Columns", label_visibility ="collapsed", options = ["All Columns", "Important"], width = 150)

    dummy_data = {
        "Document Name": [
            ":material/description: Loan Policy.pdf",
            ":material/description: Mortgage Guide.pdf",
            ":material/description: Credit Card Terms.pdf",
            ":material/description: Savings Account Info.pdf",
            ":material/description: AML Compliance.pdf",
            ":material/description: KYC Procedure.pdf",
            ":material/description: Treasury Report.pdf",
            ":material/description: Risk Assessment.pdf",
            ":material/description: Investment Portfolio.pdf",
            ":material/description: Audit Checklist.pdf",
            ":material/description: Customer Service SOP.pdf",
            ":material/description: Branch Operations.pdf",
            ":material/description: Mobile Banking FAQ.pdf",
            ":material/description: Wire Transfer Policy.pdf",
            ":material/description: Fraud Detection.pdf",
            ":material/description: Financial Statement.pdf",
            ":material/description: Employee Handbook.pdf",
            ":material/description: Regulatory Update.pdf",
            ":material/description: Business Banking.pdf",
            ":material/description: ATM Maintenance.pdf",
        ],
        "Document ID": [
            ":blue[Loan]", ":green[Mortgage]", ":violet[Credit Card]", ":blue[Savings]", ":red[Compliance]",
            ":green[KYC]", ":violet[Treasury]", ":blue[Risk]", ":green[Investment]", ":violet[Audit]",
            ":blue[Service]", ":green[Operations]", ":violet[Mobile]", ":blue[Transfer]", ":red[Fraud]",
            ":green[Statement]", ":violet[Handbook]", ":blue[Regulatory]", ":green[Business]", ":violet[ATM]"
        ],
        "Upload Date": [
            "2023-11-01", "2023-11-02", "2023-11-03", "2023-11-04", "2023-11-05",
            "2023-11-06", "2023-11-07", "2023-11-08", "2023-11-09", "2023-11-10",
            "2023-11-11", "2023-11-12", "2023-11-13", "2023-11-14", "2023-11-15",
            "2023-11-16", "2023-11-17", "2023-11-18", "2023-11-19", "2023-11-20"
        ],
        "RAG Status": [
            ":green[Indexed]", ":yellow[Processing]", ":green[Indexed]", ":red[Failed]", ":green[Indexed]",
            ":yellow[Processing]", ":green[Indexed]", ":red[Failed]", ":green[Indexed]", ":yellow[Processing]",
            ":green[Indexed]", ":red[Failed]", ":green[Indexed]", ":yellow[Processing]", ":green[Indexed]",
            ":red[Failed]", ":green[Indexed]", ":yellow[Processing]", ":green[Indexed]", ":red[Failed]"
        ],
        "File Size": [
            "365.2 MB", "43.9 MB", "48.2 MB", "39.9 MB", "32.5 MB",
            "8.32 MB", "26.8 MB", "33.3 MB", "56.2 MB", "5.5 MB",
            "109.7 MB", "21.4 MB", "67.8 MB", "12.3 MB", "92.1 MB",
            "75.6 MB", "18.9 MB", "54.3 MB", "29.7 MB", "80.5 MB"
        ],
        "Actions": list(range(1, 21))
    }
    st.table(dummy_data)