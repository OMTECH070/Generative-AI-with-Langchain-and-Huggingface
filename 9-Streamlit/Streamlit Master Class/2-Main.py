import streamlit as st
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

st.title("Streamlit Chart Demo")

chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=["A","B","C"]
)

st.dataframe(chart_data)

st.subheader("Area Chat Section")

st.area_chart(chart_data)

st.subheader("Bar Chat Section")

st.bar_chart(chart_data)

st.subheader("Line Graph Section")

st.line_chart(chart_data)

st.subheader("Scatter Plot Section")

scatter_data=pd.DataFrame({
    "x":np.random.randn(100),
    "y":np.random.randn(100)
})

st.scatter_chart(scatter_data)

st.subheader("Map")

map=pd.DataFrame(
    np.random.randn(100,2) /[50,50] + [18.5204,73.8567],
    columns=["lat","lon"]
)

st.map(map)







