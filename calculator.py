import streamlit as st

st.set_page_config(page_title="Pro Calculator", page_icon="🧮")

st.title("🧮 Smart Calculator")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", value=0.0)
with col2:
    num2 = st.number_input("Enter second number", value=0.0)

# Operation 
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

st.markdown("---")

if st.button("Calculate Result", use_container_width=True):
    result = None
    
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
            st.error("Error: Cannot divide by zero!")

    # Result 
    if result is not None:
        st.success(f"### The result is: **{result}**")
        st.balloons() # Thoda fun element!