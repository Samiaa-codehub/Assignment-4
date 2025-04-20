import streamlit as st
import random

st.set_page_config(
    page_title="Hangman App",
    page_icon="🪄",
)



st.title("Hangman Game")
st.subheader("Guess the word, one letter at a time!")

words = ["python", "streamlit", "assignment", "hangman", "computer", "science"]

# Initialize session state
if "word" not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.guessed = []
    st.session_state.attempts = 6
    st.session_state.game_over = False

# Show blanks with guessed letters
def get_display_word():
    return " ".join([letter if letter in st.session_state.guessed else "_" for letter in st.session_state.word])

st.write("Word to guess:")
st.write(f"{get_display_word()}")

st.write(f"Attempts left: {st.session_state.attempts}")

# Input box for guessing
if not st.session_state.game_over:
    guess = st.text_input("Enter a letter:", max_chars=1).lower()

    if st.button("Submit Guess"):
        if guess in st.session_state.guessed:
            st.warning("You already guessed that letter.")
        elif guess in st.session_state.word:
            st.success(f"Good job! '{guess}' is in the word.")
            st.session_state.guessed.append(guess)
        else:
            st.error(f"Oops! '{guess}' is not in the word.")
            st.session_state.guessed.append(guess)
            st.session_state.attempts -= 1

# Check game status
    if all(letter in st.session_state.guessed for letter in st.session_state.word):
        st.success(f"You won! The word was '{st.session_state.word}'.")
        st.session_state.game_over = True

    elif st.session_state.attempts == 0:
        st.error(f"You lost! The word was '{st.session_state.word}'.")
        st.session_state.game_over = True

# Restart game
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.word = random.choice(words)
        st.session_state.guessed = []
        st.session_state.attempts = 6
        st.session_state.game_over = False
        st.experimental_rerun()

st.write("---")
st.caption("Built with love by Samia Ali")
