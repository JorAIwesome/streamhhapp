import streamlit as st

# Title of the app
st.title("🔢 Power Calculator")

# User input for base and exponent
base = st.number_input("Enter the base number:", value=2)
exponent = st.number_input("Enter the exponent:", value=3)

# Compute and display result
if st.button("Calculate"):
    result = base ** exponent
    st.success(f"{base} raised to the power of {exponent} is {result}")
