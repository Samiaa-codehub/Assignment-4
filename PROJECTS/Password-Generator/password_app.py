import streamlit as st
import random # Random module use for random choice
import string


st.set_page_config(
    page_title="Password Generate App",
    page_icon="💡",
    layout="wide",
)

def generate_password(length,use_digits,use_symbols):
    letters = string.ascii_letters
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''
    all_chars = letters + digits + symbols
    if not all_chars: 
        return "Please select at least one character type!"
    password = ''.join(random.choice(all_chars)for _ in range(length))
    return password

st.title("Password Generator App")
st.write("Generate a strong password easily!")
length = st.slider("Selected password lenght", min_value=4,max_value=50,value=12)
use_digits = st.checkbox("Include Numbers (0-9)", value=True)
use_symbols = st.checkbox("Include Symbols (!,@,#,$...)",value=True)
if st.button("Generate Password"):
    password = generate_password(length,use_digits,use_symbols)
    st.success(f"Your password:'{password}'")
    st.balloons()

st.write(".......................................................")


st.write("Build with ❤ by [Samia..](https://github.com/Samiaa-codehub)")