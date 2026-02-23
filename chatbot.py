import streamlit as st

st.title("Simple Chatbot")

Question = st.text_input("Ask me anything")

if st.button("sent"):
    st.write("You asked ",Question)
    st.write("chatbot is processing...")