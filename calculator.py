import streamlit as st

# Streamlit app title
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0.0, step=1.0)
num2 = st.number_input("Enter the second number", value=0.0, step=1.0)

# Dropdown for selecting operation
operation = st.selectbox("Select an operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Perform calculation based on selected operation
result = None
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is not allowed!")

    # Display the result
    if result is not None:
        st.success(f"The result is: {result}")