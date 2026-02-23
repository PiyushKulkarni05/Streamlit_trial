import streamlit as st

st.markdown("""
<style>
            .stButton > button 
            {
            background-color:red;
            color : white;
            border: 2px solid black
            }

           span {
    color: red;
}

label {
    color: red !important;
}
            p{
            color : blue;
            }
</style>











""",unsafe_allow_html=True)


st.title("Welcome to basic streamlit app")
fname = st.text_input("Enter your First name")
lname = st.text_input("Enter your last name")
age = st.slider("Select your age", 0,100)
city = st.selectbox("select your city",["Nashik","Delhi","Pune","Mumbai","Nagpur"])

if st.button("show Details"):
    st.write("First name : ", fname)
    st.write("Last name : ", lname)
    st.write("Age:",age)
    st.write("City:" , city )
  