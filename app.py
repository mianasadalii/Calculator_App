import streamlit as st
import math

st.title("🧮 Advanced Calculator")

option = st.selectbox("Choose operation", [
    "Add", "Subtract", "Multiply", "Divide",
    "Square Root", "Log (base 10)", "Exponential"
])

if option in ["Add", "Subtract", "Multiply", "Divide"]:
    num1 = st.number_input("Enter first number")
    num2 = st.number_input("Enter second number")

    if st.button("Calculate"):
        if option == "Add":
            st.write(num1 + num2)
        elif option == "Subtract":
            st.write(num1 - num2)
        elif option == "Multiply":
            st.write(num1 * num2)
        elif option == "Divide":
            if num2 != 0:
                st.write(num1 / num2)
            else:
                st.error("Cannot divide by zero")

elif option == "Square Root":
    num = st.number_input("Enter number")
    if st.button("Calculate"):
        if num >= 0:
            st.write(math.sqrt(num))
        else:
            st.error("Invalid input")

elif option == "Log (base 10)":
    num = st.number_input("Enter number")
    if st.button("Calculate"):
        if num > 0:
            st.write(math.log10(num))
        else:
            st.error("Invalid input")

elif option == "Exponential":
    num = st.number_input("Enter number")
    if st.button("Calculate"):
        st.write(math.exp(num))
