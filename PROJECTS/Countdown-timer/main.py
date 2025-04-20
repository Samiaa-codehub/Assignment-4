import streamlit as st
import time

st.set_page_config(
    page_title="Countdown Timer",
    page_icon="⏳",
    layout="centered",
)

# Initialize session states
if "running" not in st.session_state:
    st.session_state.running = False
if "remaining_time" not in st.session_state:
    st.session_state.remaining_time = 10

def countdown_timer():
    st.session_state.running = True
    placeholder = st.empty()
    while st.session_state.remaining_time > 0 and st.session_state.running:
        mins, secs = divmod(st.session_state.remaining_time, 60)
        placeholder.markdown(
            f"<h1 style='color:#ff7766;'>{mins:02d}:{secs:02d}</h1>", unsafe_allow_html=True
        )
        time.sleep(1)
        st.session_state.remaining_time -= 1

    if st.session_state.running:
        placeholder.success("🎇 Time up! The countdown has finished!")
    else:
        placeholder.warning("⏳ Timer stopped! Click 'Start' to resume.")

# UI
st.markdown("<h1 style='color:#A52A2A;'>Countdown Timer ⏳</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#8B0000;'>Set a countdown timer and watch it tick down!</h3>", unsafe_allow_html=True)
if not st.session_state.running:
    st.session_state.remaining_time = st.number_input(
       "Enter time in seconds:", min_value=1, step=1,
        value=st.session_state.remaining_time, format="%d",
        key="time_input"
    )
button_style = """
    <style>
    div.stButton>button {
        background-color: #A52A2A;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        cursor: pointer;
    }
    div.stButton>button:hover {
        background-color: #8B0000;
        color: white;
    }"""
st.markdown(button_style, unsafe_allow_html=True)
col1,col2 = st.columns(2)
with col1:
    if st.button("Start Timer"):
       countdown_timer()
with col2:
    if st.button("Stop Timer"):
       st.session_state.running = False

st.write("---")
st.markdown("<h6 style='color:#A52A2A;'>Developed by Samia Ali</h6>", unsafe_allow_html=True)
