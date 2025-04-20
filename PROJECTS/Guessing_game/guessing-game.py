import streamlit as st
import random 

st.markdown("<h1 style='color:purple;'>Number Guessing Game🔣</h1>", unsafe_allow_html=True)

# Initialize session state
if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randrange(50, 100)
if "guess_counter" not in st.session_state:
    st.session_state.guess_counter = 0
if "chance" not in st.session_state:
    st.session_state.chance = 5

# Input for user's guess
guess = st.number_input("Enter your guess number:", min_value=50, max_value=100, step=1)

# Check the guess
if st.button("Submit Guess"):
    st.session_state.guess_counter += 1
    
    if guess == st.session_state.number_to_guess:
        st.success(f"🎉 Correct! The number is {st.session_state.number_to_guess} and you found it in {st.session_state.guess_counter} attempts!")
        st.session_state.number_to_guess = random.randrange(50, 100)
        st.session_state.guess_counter = 0

    elif st.session_state.guess_counter >= st.session_state.chance:
        st.error(f"❌ Game Over! The number was {st.session_state.number_to_guess}. Try again!")
        st.session_state.number_to_guess = random.randrange(50, 100)
        st.session_state.guess_counter = 0

    elif guess < st.session_state.number_to_guess:
        st.warning("Your guess is too low, try again.")
    else:
        st.warning("Your guess is too high, try again.")
