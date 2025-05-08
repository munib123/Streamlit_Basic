import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI using the formula: weight (kg) / (height (m) ^ 2)."""
    return weight / (height ** 2)
def classify_bmi(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
# Streamlit UI
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")
st.title("BMI Calculator")
st.write("Use this app to calculate your Body Mass Index (BMI) and understand your health status.")
# Input fields
st.sidebar.header("Input Your Details")
weight = st.sidebar.number_input("Enter your weight (kg):", min_value=1.0, step=0.1, format="%.1f")
height = st.sidebar.number_input("Enter your height (m):", min_value=0.1, step=0.01, format="%.2f")
if st.sidebar.button("Calculate BMI"):
    if height > 0:
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        st.success(f"Your BMI is: {bmi:.2f}")
        st.info(f"Category: {category}")
    else:
        st.error("Height must be greater than 0.")
else:
    st.write("Enter your details in the sidebar and click 'Calculate BMI' to see the results.")