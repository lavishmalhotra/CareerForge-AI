# ============================
# CareerForge AI - Dashboard.py
# ============================

import os
import json
import time
import random
from datetime import datetime

import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="CareerForge AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

...

.stButton>button{
    width:100%;
    border-radius:10px;
    height:45px;
    font-weight:bold;
}

/* 👇 YE YAHAN PASTE KAR */

div[data-testid="stMetric"]{
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}

div[data-testid="stMetric"] > div{
    background: transparent !important;
}

div[data-testid="metric-container"]{
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

</style>
""", unsafe_allow_html=True)
    
# -----------------------------
# SESSION STATE
# -----------------------------
defaults = {

    "resume_score":78,
    "ats_score":82,
    "profile_completion":65,
    "interview_score":71,
    "skills_score":69,

    "goal":"Software Engineer",

    "completed_courses":5,
    "pending_courses":7,

    "completed_tasks":12,
    "pending_tasks":9,

    "applications":8,
    "interviews":2,
    "offers":0,

    "notifications":[
        "Resume analyzed successfully.",
        "New internship recommendations available.",
        "Your ATS score improved."
    ]
}

for k,v in defaults.items():
    if k not in st.session_state:
        st.session_state[k]=v

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:

    st.markdown("""
    <h2 style="text-align:center;color:#4F46E5;">
        🚀 CareerForge AI
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("📊 Profile Progress")

    st.progress(
        st.session_state.profile_completion / 100
    )

    st.caption(
        f"{st.session_state.profile_completion}% Completed"
    )

    st.markdown("---")

    st.subheader("🎯 Career Goal")

    st.info(
        st.session_state.goal
    )

    st.markdown("---")

    st.subheader("📈 Quick Stats")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Resume",
            st.session_state.resume_score
        )

    with c2:
        st.metric(
            "ATS",
            st.session_state.ats_score
        )

    c3, c4 = st.columns(2)

    with c3:
        st.metric(
            "Apps",
            st.session_state.applications
        )

    with c4:
        st.metric(
            "Interviews",
            st.session_state.interviews
        )

    st.markdown("---")

    st.success("🚀 Keep Improving Every Day!")

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<h1 style="
font-size:52px;
font-weight:800;
color:#4F46E5;
margin-top:20px;
margin-bottom:10px;
line-height:1.3;
">
🚀 CareerForge AI Dashboard
</h1>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="sub-title">Your Personal AI Career Companion</div>',
    unsafe_allow_html=True
)

st.write("")

# -----------------------------
# TOP METRICS
# -----------------------------
c1,c2,c3,c4,c5=st.columns(5)

with c1:
    st.markdown('<div class="metric-card">',unsafe_allow_html=True)
    st.metric(
        "Resume",
        st.session_state.resume_score,
        "+4"
    )
    st.markdown("</div>",unsafe_allow_html=True)

with c2:
    st.markdown('<div class="metric-card">',unsafe_allow_html=True)
    st.metric(
        "ATS",
        st.session_state.ats_score,
        "+6"
    )
    st.markdown("</div>",unsafe_allow_html=True)

with c3:
    st.markdown('<div class="metric-card">',unsafe_allow_html=True)
    st.metric(
        "Skills",
        st.session_state.skills_score,
        "+3"
    )
    st.markdown("</div>",unsafe_allow_html=True)

with c4:
    st.markdown('<div class="metric-card">',unsafe_allow_html=True)
    st.metric(
        "Interview",
        st.session_state.interview_score,
        "+8"
    )
    st.markdown("</div>",unsafe_allow_html=True)

with c5:
    st.markdown('<div class="metric-card">',unsafe_allow_html=True)
    st.metric(
        "Completion",
        f"{st.session_state.profile_completion}%"
    )
    st.markdown("</div>",unsafe_allow_html=True)

st.write("")

# -----------------------------
# CHART DATA
# -----------------------------
progress_df=pd.DataFrame({

    "Week":[
        "W1",
        "W2",
        "W3",
        "W4",
        "W5",
        "W6",
        "W7",
        "W8"
    ],

    "Progress":[
        18,
        24,
        31,
        45,
        56,
        68,
        77,
        86
    ]

})

skill_df=pd.DataFrame({

    "Skill":[
        "Python",
        "Java",
        "SQL",
        "AI",
        "DSA",
        "Communication"
    ],

    "Score":[
        90,
        74,
        68,
        83,
        72,
        64
    ]

})

application_df=pd.DataFrame({

    "Status":[
        "Applied",
        "Interview",
        "Rejected",
        "Offer"
    ],

    "Count":[
        18,
        6,
        9,
        1
    ]

})

# -----------------------------
# ROW 1
# -----------------------------
left, right = st.columns([2,1])

with left:

    st.markdown("### 📈 Career Progress")

    fig = px.line(
        progress_df,
        x="Week",
        y="Progress",
        markers=True
    )

    fig.update_layout(
        height=350,
        margin=dict(
            l=10,
            r=10,
            t=30,
            b=10
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        xaxis=dict(
            showgrid=False,
            zeroline=False
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(255,255,255,0.08)",
            zeroline=False
        )
    )

    fig.update_traces(
        line=dict(width=4),
        marker=dict(size=10)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    st.markdown("### 🎯 Overall Progress")

    gauge = go.Figure(go.Indicator(

        mode="gauge+number",

        value=st.session_state.profile_completion,

        gauge={
            "axis":{"range":[0,100]},
            "bar":{"thickness":0.3},
            "steps":[
                {"range":[0,40],"color":"#FCA5A5"},
                {"range":[40,70],"color":"#FCD34D"},
                {"range":[70,100],"color":"#86EFAC"}
            ]
        }

    ))

    gauge.update_layout(
        height=350,
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white")
    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )
    # ============================
# CareerForge AI - Dashboard.py
# PART 2 / 4
# Append below Part 1
# ============================

# -----------------------------
# ROW 2
# -----------------------------
left, right = st.columns([1.2, 1])

with left:

    st.markdown("### 💡 Skill Analysis")

    fig = px.bar(
        skill_df,
        x="Skill",
        y="Score",
        text="Score",
        color="Score",
        color_continuous_scale="blues"
    )

    fig.update_layout(
        height=370,
        coloraxis_showscale=False,
        margin=dict(l=10, r=10, t=30, b=10)
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    st.markdown("### 📨 Job Applications")

    pie = px.pie(
        application_df,
        names="Status",
        values="Count",
        hole=.55
    )

    pie.update_layout(
        height=370,
        margin=dict(l=10, r=10, t=20, b=20)
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

# -----------------------------
# ROW 3
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    st.markdown("### ✅ Daily Career Checklist")

    resume = st.checkbox("Update Resume")

    lc = st.checkbox("Solve 2 LeetCode Problems")

    project = st.checkbox("Work on AI Project")

    linkedin = st.checkbox("Post on LinkedIn")

    apply = st.checkbox("Apply to 3 Jobs")

    learn = st.checkbox("Study 1 Hour")

    completed = sum([
        resume,
        lc,
        project,
        linkedin,
        apply,
        learn
    ])

    percent = int(completed / 6 * 100)

    st.progress(percent / 100)

    st.success(f"Today's Progress : {percent}%")

with col2:

    st.markdown("### 🔥 Weekly Goals")

    st.write("Resume Optimization")
    st.progress(.82)

    st.write("DSA Practice")
    st.progress(.68)

    st.write("AI Projects")
    st.progress(.75)

    st.write("Mock Interviews")
    st.progress(.55)

    st.write("LinkedIn Growth")
    st.progress(.61)

    st.write("Job Applications")
    st.progress(.46)

# -----------------------------
# AI INSIGHTS
# -----------------------------
st.markdown("---")
st.markdown("## 🤖 AI Career Insights")

insight1, insight2, insight3 = st.columns(3)

with insight1:

    st.info(
        """
### Resume

Your resume is strong.

Improve ATS keywords.

Add quantified achievements.

Keep it one page.
"""
    )

with insight2:

    st.warning(
        """
### Skill Gap

Focus on:

• SQL

• System Design

• Communication

• Backend Development
"""
    )

with insight3:

    st.success(
        """
### Recommendation

Apply for:

• SDE Intern

• AI Engineer

• ML Intern

• Python Developer
"""
    )

# -----------------------------
# JOB TRACKER
# -----------------------------
st.markdown("---")
st.markdown("## 💼 Application Tracker")

tracker = pd.DataFrame({

    "Company":[
        "Google",
        "Microsoft",
        "Amazon",
        "Adobe",
        "Infosys",
        "TCS",
        "NVIDIA",
        "OpenAI"
    ],

    "Role":[
        "SWE Intern",
        "AI Intern",
        "ML Engineer",
        "Backend",
        "Associate",
        "Developer",
        "AI Engineer",
        "Research Intern"
    ],

    "Status":[
        "Applied",
        "Interview",
        "Rejected",
        "Applied",
        "OA",
        "Applied",
        "Wishlist",
        "Wishlist"
    ]

})

st.dataframe(
    tracker,
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# ROADMAP
# -----------------------------
st.markdown("---")
st.markdown("## 🛣️ Career Roadmap")

roadmap = [

    "Complete Resume",

    "Improve ATS Score",

    "Master Python",

    "Master DSA",

    "Build 3 AI Projects",

    "Complete SQL",

    "Practice Interviews",

    "Apply Daily",

    "Improve LinkedIn",

    "Get Internship"

]

for i, item in enumerate(roadmap, start=1):

    st.write(f"**{i}.** {item}")

# -----------------------------
# ACHIEVEMENTS
# -----------------------------
st.markdown("---")
st.markdown("## 🏆 Achievements")

a1, a2, a3, a4 = st.columns(4)

with a1:
    st.metric("Projects", "7")

with a2:
    st.metric("Certificates", "11")

with a3:
    st.metric("LeetCode", "320")

with a4:
    st.metric("Hackathons", "5")
    # ============================
# CareerForge AI - Dashboard.py
# PART 3 / 4
# Append below Part 2
# ============================

# -----------------------------
# LEARNING DASHBOARD
# -----------------------------
st.markdown("---")
st.markdown("## 📚 Learning Progress")

course_df = pd.DataFrame({

    "Course":[
        "Python",
        "Machine Learning",
        "Deep Learning",
        "SQL",
        "DSA",
        "System Design",
        "GenAI",
        "Prompt Engineering"
    ],

    "Completion":[
        100,
        85,
        62,
        78,
        71,
        35,
        90,
        95
    ]

})

fig = px.bar(
    course_df,
    x="Completion",
    y="Course",
    orientation="h",
    text="Completion",
    color="Completion",
    color_continuous_scale="greens"
)

fig.update_layout(
    height=450,
    coloraxis_showscale=False,
    margin=dict(
        l=10,
        r=10,
        t=20,
        b=10
    )
)

fig.update_traces(textposition="outside")

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# MOCK INTERVIEW
# -----------------------------
st.markdown("---")
st.markdown("## 🎤 Mock Interview")

question_bank = [

    "Tell me about yourself.",

    "Explain OOPs.",

    "Difference between Process and Thread?",

    "What is Machine Learning?",

    "Explain CNN.",

    "What is Gradient Descent?",

    "Difference between Stack and Queue?",

    "Explain Binary Search.",

    "Difference between SQL and NoSQL?",

    "What are APIs?"

]

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(question_bank)

st.info(st.session_state.current_question)

if st.button("Next Interview Question"):

    st.session_state.current_question = random.choice(question_bank)

    st.rerun()

answer = st.text_area(
    "Write your answer",
    height=180
)

if st.button("Evaluate Answer"):

    score = random.randint(65, 98)

    st.success(f"Interview Score : {score}/100")

    if score >= 90:

        st.success("Excellent Answer!")

    elif score >= 75:

        st.warning("Good Answer. Add more technical depth.")

    else:

        st.error("Needs Improvement.")

# -----------------------------
# RESUME IMPROVER
# -----------------------------
st.markdown("---")
st.markdown("## 📄 Resume Improvement Suggestions")

resume_suggestions = [

    "Add measurable achievements.",

    "Increase ATS keywords.",

    "Keep resume under one page.",

    "Highlight AI projects.",

    "Improve project descriptions.",

    "Add GitHub links.",

    "Add LinkedIn profile.",

    "Mention technologies clearly."

]

for item in resume_suggestions:

    st.write("✅", item)

# -----------------------------
# PRODUCTIVITY
# -----------------------------
st.markdown("---")
st.markdown("## ⚡ Productivity")

productivity = pd.DataFrame({

    "Day":[
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ],

    "Hours":[
        3,
        5,
        6,
        4,
        7,
        8,
        5
    ]

})

fig = px.area(
    productivity,
    x="Day",
    y="Hours"
)

fig.update_layout(
    height=350,
    margin=dict(
        l=10,
        r=10,
        t=20,
        b=10
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# NOTIFICATIONS
# -----------------------------
st.markdown("---")
st.markdown("## 🔔 Notifications")

for note in st.session_state.notifications:

    st.success(note)

# -----------------------------
# RECENT ACTIVITY
# -----------------------------
st.markdown("---")
st.markdown("## 🕒 Recent Activity")

activity = [

    "Resume analyzed successfully.",

    "Completed Deep Learning Module.",

    "Applied to Microsoft.",

    "Improved ATS score by 6%.",

    "Solved 5 LeetCode problems.",

    "Completed AI Project.",

    "Updated LinkedIn profile."

]

for item in activity:

    st.write("•", item)

# -----------------------------
# AI RECOMMENDATIONS
# -----------------------------
st.markdown("---")
st.markdown("## 🧠 AI Recommendations")

recommendations = [

    "Practice SQL joins this week.",

    "Build one full-stack AI project.",

    "Revise DBMS interview questions.",

    "Practice OOP concepts.",

    "Increase GitHub contributions.",

    "Participate in one hackathon.",

    "Publish one LinkedIn post.",

    "Apply to 5 companies today."

]

for rec in recommendations:

    st.info(rec)
    # ============================
# CareerForge AI - Dashboard.py
# PART 4 / 4
# Append below Part 3
# ============================

# -----------------------------
# PROFILE SUMMARY
# -----------------------------
st.markdown("---")
st.markdown("## 👤 Profile Summary")

profile_col1, profile_col2 = st.columns([1, 2])

with profile_col1:

    st.metric("Resume Score", st.session_state.resume_score)
    st.metric("ATS Score", st.session_state.ats_score)
    st.metric("Interview Score", st.session_state.interview_score)
    st.metric("Skill Score", st.session_state.skills_score)

with profile_col2:

    st.write("### Career Goal")
    st.success(st.session_state.goal)

    st.write("### Progress")

    st.progress(st.session_state.profile_completion / 100)

    st.write(
        f"Overall Completion : **{st.session_state.profile_completion}%**"
    )

# -----------------------------
# EXPORT REPORT
# -----------------------------
st.markdown("---")
st.markdown("## 📤 Export Report")

report = {
    "Resume Score": st.session_state.resume_score,
    "ATS Score": st.session_state.ats_score,
    "Interview Score": st.session_state.interview_score,
    "Skills Score": st.session_state.skills_score,
    "Profile Completion": st.session_state.profile_completion,
    "Applications": st.session_state.applications,
    "Interviews": st.session_state.interviews,
    "Offers": st.session_state.offers,
    "Goal": st.session_state.goal,
    "Generated On": datetime.now().strftime("%d-%m-%Y %H:%M")
}

json_report = json.dumps(report, indent=4)

st.download_button(
    label="⬇ Download Career Report (JSON)",
    data=json_report,
    file_name="careerforge_report.json",
    mime="application/json"
)

csv_df = pd.DataFrame([report])

csv = csv_df.to_csv(index=False)

st.download_button(
    label="⬇ Download Career Report (CSV)",
    data=csv,
    file_name="careerforge_report.csv",
    mime="text/csv"
)

# -----------------------------
# QUICK ACTIONS
# -----------------------------
st.markdown("---")
st.markdown("## ⚙ Quick Actions")

action1, action2, action3, action4 = st.columns(4)

with action1:

    if st.button("Improve Resume"):

        st.success("Resume optimization started.")

with action2:

    if st.button("Find Jobs"):

        st.success("Searching latest opportunities...")

with action3:

    if st.button("Start Mock Interview"):

        st.success("Launching interview module...")

with action4:

    if st.button("Generate Roadmap"):

        st.success("Career roadmap generated.")

# -----------------------------
# DAILY QUOTE
# -----------------------------
st.markdown("---")
st.markdown("## 💬 Daily Motivation")

quotes = [

    "Success comes from consistent effort.",

    "Every interview is practice for your dream job.",

    "Build projects that solve real problems.",

    "Small progress every day becomes big success.",

    "Keep learning. Keep building. Keep applying.",

    "Your future is created by today's actions.",

    "Consistency beats motivation."

]

st.info(random.choice(quotes))

# -----------------------------
# FOOTER STATS
# -----------------------------
st.markdown("---")

footer1, footer2, footer3, footer4 = st.columns(4)

with footer1:
    st.metric("Courses Completed", st.session_state.completed_courses)

with footer2:
    st.metric("Pending Courses", st.session_state.pending_courses)

with footer3:
    st.metric("Completed Tasks", st.session_state.completed_tasks)

with footer4:
    st.metric("Pending Tasks", st.session_state.pending_tasks)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")

st.markdown(
    """
<div style="text-align:center;padding:20px;">

<h3>🚀 CareerForge AI</h3>

<p>
Your Personal AI Career Companion
</p>

<p>
Resume Analysis • ATS Optimization • Skill Gap Detection •
Learning Roadmap • Mock Interviews • Career Analytics
</p>

<p style="color:gray;">
Built with ❤️ using Streamlit & Plotly
</p>

</div>
""",
    unsafe_allow_html=True
)

# -----------------------------
# AUTO REFRESH CLOCK
# -----------------------------
placeholder = st.empty()

current_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

placeholder.caption(f"Last Updated : {current_time}")

# -----------------------------
# END OF DASHBOARD
# -----------------------------