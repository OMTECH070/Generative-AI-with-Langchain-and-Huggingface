import streamlit as st
import numpy as np
import pandas as pd

## Title of the application

st.title("Anime Data Analysis") 

## Display a Simple text
st.write("This application allows you to analyze anime data using Streamlit.")

df=pd.read_csv("E:\\Generative AI with Langchain and Huggingface\\9-Streamlit\\Pandas\\anime.csv")  
st.write(df)

## Creat a line chart to visualize the data
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=["A","B","C"]
)
st.line_chart(chart_data)