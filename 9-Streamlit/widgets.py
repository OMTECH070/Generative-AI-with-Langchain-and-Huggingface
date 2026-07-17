import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit Widgets Example")


name=st.text_input("Enter your name:")
options=["Python","Java","C++","JavaScript"]
choice=st.selectbox("Select your favorite programming language:",options)
st.write(f"You selected: {choice}")

age=st.slider("Select your age:",0,100,25)
if name:
    st.write(f"Hello, {name}!")
    st.write(f"You are {age} years old.")

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [25, 30, 28, 35, 27],
    "City": ["New York", "London", "Mumbai", "Sydney", "Toronto"],
    "Salary": [55000, 62000, 48000, 75000, 59000]
}

df1 = pd.DataFrame(data)
st.write(df1)

uploader=st.file_uploader("Upload a CSV file", type="csv")

if uploader is not None:
    uploaded_df=pd.read_csv(uploader)
    st.write(uploaded_df)