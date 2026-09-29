import streamlit as st
st.title("Welcome Tejuuu!!!")
name=st.text_input("Enter your name")
st.write("Hellooo..",name)
click=st.button("Click Mee!!!")
if click:
    st.write("Good Morning..",name)
    st.caption("Have a nice dayyyy...")
