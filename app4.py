import streamlit as st
 
st.title("Basic Calculator")
ans = 0
num1 = st.input("Enter your 1st no. ")

num2 = st.number_input("Enter your 2st no. ")

choice = st.selectbox("Enter operation",["Add","Sub","Mul","Div"])


if st.button("Calculate"):
    if choice == "Add":
       ans = num1 + num2
    elif choice == "Sub":
       ans = num1 - num2 
    elif choice == "Mul":
      ans = num1 * num2 
    elif choice == "Div":
       if num2!=0 : 
           ans = num1 / num2 
       else :
          st.write("Cannot Write")

st.write("Ans is :", ans)