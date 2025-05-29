import streamlit as st

st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧮 Simple Calculator</h1>", unsafe_allow_html=True)

# Input numbers
num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:", format="%.2f")

# Operation choice
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate on button click
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero.")
            result = None

    if result is not None:
        st.success(f"Result = {result:.2f}")
