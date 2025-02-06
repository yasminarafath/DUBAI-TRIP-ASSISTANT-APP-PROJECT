import streamlit as st
import time

st.image("https://media.istockphoto.com/id/1333035210/photo/sunset-view-of-the-dubai-marina-and-jbr-area-and-the-famous-ferris-wheel-and-golden-sand.jpg?s=612x612&w=0&k=20&c=ONRt8hlovwg0m8f6Q3OG5Spavaer2JCaAioUE-XM_r8=")

st.title("Welcome To DXB NAVIGATOR")

name=st.text_input("Enter Your Name :")

if st.button("Say Hello"):
    st.write(f"Hello {name} , Welcome to DXB NAVIGATOR")

    time.sleep(3) 
    st.switch_page("pages/chatbot.py")  