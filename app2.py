import streamlit as st


st.title("Welcome to basic streamlit app")
name = st.text_input("Enter you name")
age = st.slider("Select your age", 0,100)
city = st.selectbox("select your city",["Delhi","Nashik","Pune","Mumbai","Nagpur"])

if st.button("show Details"):
    st.write("Age:",age)
    st.write("City:" , city )
    st.write("Name is :" , name)    