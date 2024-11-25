import  streamlit as st
Title = st.title(" Login Here ")
name = st.text_input("Enter your name:")
fathername = st.text_input("Enter your fathername:")
age = st.text_input("Enter your age:")
classdata = st.selectbox("Enter your classdata:", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
button = st.button("fuck off")
if button:
    st.markdown(f""" name :{name} age :{age} classdata :{classdata}""")
