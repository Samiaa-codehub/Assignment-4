import streamlit as st
import pandas as pd
from datetime import date


st.set_page_config(
    page_title="Growth Tracker",
    page_icon="📈",
    layout="wide"
)


st.markdown("<h1 style='color:brown;'>💡Mindset Challenge App  By Samia Adnan</h1>",

unsafe_allow_html=True)
st.markdown("<h5 style='color:brown;'>🎖Track your personal growth goals and visualize progress .</h5>",
unsafe_allow_html=True)
 

if 'goals' not in st.session_state:
   st.session_state.goals =[]
    
with st.form("goals_form"):
    goals = st.text_input("Enter your goal:")
    submit = st.form_submit_button("Add Goals")
    if submit and goals:
     st.session_state.goals.append({"Goals":goals,"Date": date.today(),"Status": "In Progress"})
     st.success("Goal added successfully!")

if st.session_state.goals:
    df = pd.DataFrame(st.session_state.goals)
    st.markdown("<h1 style='color:brown;'>✍Today Goals</h1>",
    unsafe_allow_html=True)
    st.markdown("<h4>🎇Great things rarely come from sitting in comfort zones</h4>",
    unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)
    

    selected_goal = st.selectbox("👋Mark goal as completed:", [g["Goals"] for g in st.session_state.goals], index=None)
    if st.button("Mark as Completed") and selected_goal:
        for g in st.session_state.goals:
            if g["Goals"] == selected_goal:
                g["Status"] = "Completed"
        st.success(f"Goal '{selected_goal}' marked as completed!")
        st.success("💪A strong mindest can turn any challenge into an opportunity🎖")