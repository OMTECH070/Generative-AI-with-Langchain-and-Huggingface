import streamlit as st
import numpy as np
import pandas as pd
import os

'''
st.title("This Is The Main Title")

st.header("This Is The Header")

st.subheader("This Is The Subheader")

st.markdown("This is a markdown text. You can use **bold**, *italic*, and other markdown features.")

st.caption("This is a caption text. It is usually used for additional information or context.")

code="""
name=input("Enter your name: ")
age=int(input("Enter your age: "))

print(f"Your {name} and your {age} year old.")

"""
st.code(code,language="python")

st.image(os.path.join(os.getcwd(),"static","BlackHole.jpg",))

'''

st.title("Streamlit Elements Demo")

st.subheader("DataFrame Section")
df=pd.DataFrame({"Name":["Om","Sai","Raj","Anyone"],
                 "Age":[19,13,22,1000],
                 "Weight":[40,50,60,100]})

st.dataframe(df)

st.subheader("Date Editor")

editable_dataframe=st.data_editor(df)

st.subheader("Static Table")

st.table(editable_dataframe)

st.subheader("Metrics")

st.metric(label="Total Rows",value=len(df))

st.metric(label="Averagev Age",value=round(df["Age"].mean(),1))

st.subheader("JSON and Dictionaries")

sample={"Name":["Om","Sai","Raj","Anyone"],
                 "Age":[19,13,22,1000],
                 "Weight":[40,50,60,100]}

st.json(sample)

st.write("Dictionary view:",sample)


