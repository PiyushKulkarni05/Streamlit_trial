import streamlit as st
 
st.title("Basic Calculator")
ans = 0
num1 = st.number_input("Enter your 1st no. ")
num2 = st.number_input("Enter your 2st no. ")

if st.button(" Add "):
    ans = num1 + num2
elif st.button(" Sub "):
    ans = num1 - num2 
elif st.button(" Mul "):
    ans = num1 * num2 
elif st.button(" div "):
    ans = num1 / num2 

st.write("Ans is :", ans)