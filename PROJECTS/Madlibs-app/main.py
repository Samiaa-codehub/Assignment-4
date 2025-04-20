import streamlit as st
import random
st.set_page_config(
    page_title="Madlibs Generator App",
    page_icon="📝",
    layout="centered",
)
st.markdown("<h1 style= color:#98FF98;>Madlibs Generator App📑</h1>", unsafe_allow_html=True)
st.markdown("<h2 style= color:#87CEEB;>Fill in the blanks to create a fun story!</h2>", unsafe_allow_html=True)
st.markdown("<h6 style= color:#87CEEB;>Click the button below to generate a random story.</h6>", unsafe_allow_html=True)
place = st.text_input("Enter  a place:")
adjective = st.text_input("Enter an adjective:")
animal = st.text_input("Enter an animal:")
verb = st.text_input("Enter a verb:")
story = [f"Once upon a time in {place}, there was a {adjective} {animal} who loved to {verb}. One day, it decided to go on an adventure and explore the world. It met many friends along the way and had a lot of fun. In the end, it returned home with amazing stories to tell.",
                 f"One day in {place}, a {adjective} {animal} woke up and decided to {verb}. It packed its bags and set off on an adventure. Along the way, it met many interesting creatures and had a lot of fun. When it returned home, it had so many stories to share with its friends.",
                f"There was a {adjective} {animal} living in {place}. It loved to {verb} all day long. One day, it met a new friend who joined in on the fun. Together, they explored the world and had many adventures. They learned that friendship is the greatest adventure of all.",
                f"Once upon a time in {place}, there was a {adjective} {animal} who loved to {verb}. It went on many adventures and met many friends. One day, it discovered a hidden treasure that changed its life forever. It learned that the greatest treasure of all is friendship.",]
button_style = """
    <style>
    div.stButton>button {
        background-color: #98FF98;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        cursor: pointer;
        }
        div.stButton>button:hover {
        background-color: #98FF87;
        color:#FFFFFF;
        }"""
st.markdown(button_style,unsafe_allow_html=True)
if st.button("Generate Story"):
    if place and adjective and animal and verb:
        selected_story = random.choice(story)
        story = selected_story.format(
            place=place,
            adjective=adjective,
            animal=animal,
            verb=verb,
        )      
        st.markdown("<h5 style= color:#87CEEB;>Here's your story:</h5>", unsafe_allow_html=True)
        st.write(story)
    else:
        st.warning("Please fill in all the feilds to generate a story.")
st.write("---")
st.markdown("<h6 style= color:#87ECCB;>Develop by ❤ Samia Ali..</h6>",unsafe_allow_html=True)