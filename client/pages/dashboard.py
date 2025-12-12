import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from numpy.random import default_rng as rng
from components.sidebar.sidebar_logo import render_sidebar_logo
from components.sidebar.sidebar_message import render_sidebar_message
from components.sidebar.sidebar_logout import logout_button

#######################
# Main App
avg_competency_score, roleplay_completion_rate, avg_session_duration, total_user = st.columns(4)
st.divider()
skill_gap_radar, sentiment_analysis_chart, activity_heatmap = st.columns(3)
difficulty_chart, attention_table = st.columns(2)


#######################
# Styling
st.markdown('''
<style>
    [data-testid="stMainBlockContainer"] {
        max-width: 100rem;
    }
    [data-testid="stMetric"] {
        min-width: 200px;
        width: auto;
        background-color: #272630;
    }
    [data-testid="stMetric"] div {
        text-align: center;
        align-items: center;
        justify-content: center;
        width: auto;        
    }
    [data-testid="stMetricLabel"] {
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    [data-testid="stMetricLabel"] p {
        font-size: 1.2rem;
        font-weight: medium;
        white-space: nowrap;
    }
    [data-testid="stMetricValue"] {
        text-align: center;
        font-weight: bold;
        font-size: 4rem;
    }
    [data-testid="stMetricDelta"] {
        font-size: 1rem;
    }
    [data-testid="stMarkdownContainer"] h4 {
        position: relative;
        width: fit-content;
        z-index: 10;
    }
    [data-testid="stPlotlyChart"] {
        margin-top: -4rem;        
        z-index: 1;
    }
    [data-testid="stColumn"] {
        height: "10rem";
    } 
    [data-testid="stTableStyledTable"] tbody tr div {
        text-align: left;
    }
</style>
''', unsafe_allow_html=True)

#######################
# Visualization
avg_competency_score.metric(
    label = "Average Competency Score",
    value = "78%",
    delta = "2%",
    border = True
)

roleplay_completion_rate.metric(
    label = "Roleplay Completion Rate",
    value = "85%",
    delta = "3%",
    border = True
)

avg_session_duration.metric(
    label = "Average Session Duration",
    value = "12m 30s",
    delta = "-24s",
    border = True
)

total_user.metric(
    label = "Total User",
    value = 5892,
    delta = 14,
    border = True
)

skills = ["Empathy", "Skills", "Compliance", "Clarity ", "Handling", "Knowledge"]
scores = [80, 65, 70, 90, 60, 30]

# Radar chart requires the first value to be repeated at the end to close the shape
skills += [skills[0]]
scores += [scores[0]]

skill_fig = go.Figure(
        data = [
            go.Scatterpolar(
                r = scores,
                theta = skills,
                fill = "toself",
                name = "Skill Gap Analysis",
                
            )
        ],
        layout = go.Layout(
            polar = dict(
                radialaxis = dict(
                    visible = True,
                    range = [0, 100],
                    gridcolor = "gray",
                    showticklabels = False                    
                ),
                angularaxis=dict(
                    gridcolor="gray"
                )
            ),
            font = dict(
                size = 16,
                weight = "bold"
            ),
            showlegend = False,
            
        )
    )

with skill_gap_radar:
    with st.container(border=True, height="stretch"):
        st.markdown("#### Skill Gap Analysis Employee")
        st.plotly_chart(skill_fig, use_container_width=True)

generator = np.random.default_rng()
sentiment_analysis_data = pd.DataFrame(
    {
        "Week": list(range(20)),
        "Positive": generator.integers(30, 51, size=20),
        "Neutral": generator.integers(10, 21, size=20),
        "Negative": generator.integers(5, 11, size=20)
    }
)

with sentiment_analysis_chart:
    with st.container(border = True, height="stretch"):
        st.markdown("#### Sentiment Analysis Over Time")
        st.area_chart(sentiment_analysis_data, x="Week", y=["Positive", "Neutral", "Negative"], color=["#639754", "#FFD301", "#E03C32"])

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hours = []
for h in range(24):
    if h == 0:
        hours.append("12AM")
    elif h < 12:
        hours.append(f"{h}AM")
    elif h == 12:
        hours.append("12PM")
    else:
        hours.append(f"{h-12}PM")

activity_fig = go.Figure(
    data = go.Heatmap(
        z = np.random.poisson(size=(len(days), len(hours))),
        x = hours,
        y = days,
        colorscale = "blues"
    )
)

with activity_heatmap:
    with st.container(border=True, height="stretch"):
        st.markdown("#### Activity Heatmap (Day/Time)")
        st.plotly_chart(activity_fig, use_container_width=True)

difficulty_data = pd.DataFrame(
    {
        "Difficulty": list(range(0, 101, 10)),
        "Pass Rate%": generator.integers(0, 101, size=11),
        "Pass Rate2%": generator.integers(0, 101, size=11),
    }
)

size = generator.integers(20, 101, size=11)

difficulty_fig = go.Figure(
    data = go.Scatter(
        x = list(range(0, 101, 10)),
        y = generator.integers(0, 101, size=11),
        mode = "markers",
        marker = dict(
            size = size,
            sizemode = "area",
            sizeref = 2*max(size)/(40.**2),
            sizemin = 4
        )
    ),
    layout = go.Layout(
        xaxis = dict(title="Scenario Difficulty (Easy -> Hard)"),
        yaxis = dict(title="Pass Rate %")
    )
)


with difficulty_chart:
    with st.container(border=True, height="stretch"):
        st.markdown("#### Scenario Difficulty vs Success Rate")
        # st.scatter_chart(difficulty_data, x="Difficulty", y="Pass Rate%")
        st.plotly_chart(difficulty_fig, use_container_width=True)

dummy_username = ["Alex", "Nicole", "Sara", "Etienne", "Chelsea", "Jody", "Marianne", "Chris", "Taylor", "Jordan"]
dummy_dept = [
    "Retail Banking", "Corporate Banking", "Risk Management", "Compliance",
    "Wealth Management", "IT", "Customer Service", "Treasury", "Audit", "Operations"
]
dummy_score_temp = [62, 55, 48, 60, 58, 53, 50, 47, 59, 56]
dummy_score = []
for score in dummy_score_temp:
    if score >= 60:
        dummy_score.append(f':yellow[{score}]')
    else:
        dummy_score.append(f':red[{score}]')
dummy_weakness = [
    "Poor customer engagement",
    "Limited product knowledge",
    "Weak risk assessment",
    "Regulatory gaps",
    "Insufficient financial planning",
    "System downtime",
    "Slow response time",
    "Cash flow errors",
    "Audit trail issues",
    "Process inefficiency"
]

attention_data = pd.DataFrame({
    "User Name": dummy_username,
    "Department": dummy_dept,
    "Last Score": dummy_score,
    "Weakness": dummy_weakness,
})

with attention_table:
    with st.container(border=True, height="stretch"):
        st.markdown("#### Need Attention List (Priority)")
        st.table(attention_data)

#######################
# Sidebar
render_sidebar_message()
logout_button()