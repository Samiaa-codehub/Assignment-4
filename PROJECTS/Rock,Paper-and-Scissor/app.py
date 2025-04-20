import streamlit as st
import random

st.set_page_config(page_title="Rock Paper and Scissors", page_icon="🕹", layout="wide")

st.markdown("<h1 style= color:purple;>Rock Paper and Scissors✊✂📑</h1>", unsafe_allow_html=True)
st.markdown("<h4 style= color:purple;>A simple game to play with your friends</h4>", unsafe_allow_html=True)
st.markdown("<h6 style= color:purple;>Choose your weapon and let the game begin!</h6>", unsafe_allow_html=True)

choices = ["Rock ✊", "Paper 📑", "Scissors ✂"]
emoji_map = {
    "Rock": "✊",
    "Paper": "📑",
    "Scissors": "✂"
}

user_choice = st.selectbox("Select your choice:", choices)

if st.button("Play Game Now!"):
    computer_choice = random.choice(choices)

    st.write("You chose:", user_choice)
    st.write("Computer chose:", computer_choice)
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Rock✊ " and computer_choice == "Scissors ✂") or
        (user_choice == "Paper 📑" and computer_choice == "Rock ✊") or
        (user_choice == "Scissors ✂" and computer_choice == "Paper 📑")
    ):
        result = "🎉 You win!"
        st.balloons()
    else:
        result = "😢 Computer wins!"

    st.markdown(f"### {result}")

    if st.button("Play again"):
        st.rerun()

st.markdown("---")
st.markdown("<h5 style= color:purple;>Made with ❤️ by Samia Ali</h5>", unsafe_allow_html=True)
