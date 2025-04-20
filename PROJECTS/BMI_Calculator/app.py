import streamlit as st


st.set_page_config(
    page_title="BMI Calculator App",
    page_icon="💡",
    layout="wide"
)

#Title of the app
st.title("BMI Calculator App")
#Subtitle of the app
st.subheader("Calculate your Body Mass Index (BMI)")
#Description of the app
st.write("This app calculates your Body Mass Index (BMI) based on your height and weight.")
#Instructions
#Input feilds for height and weight
height = st.number_input("Enter your height in meters (m):",min_value=0.0, max_value=3.0, value=0.00, step=0.01)
#
weight = st.number_input("Enter your weight in kilograms (kg):",min_value=0.0, max_value=500.0, value=0.00, step=0.1)
#Button to calculate BMI
if st.button("Calculator BMI"):
    #Check if height and weight are valid
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")
    else:
        st.error("Height must be greater than zero.")
        st.stop()
        st.write("Please enter a valid height.")
        st.ballon("🎈")
st.write("----")    
st.write(" Build by samia ali❤")   
    