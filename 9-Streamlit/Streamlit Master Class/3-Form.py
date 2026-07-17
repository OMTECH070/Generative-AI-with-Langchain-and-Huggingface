import streamlit as st
import pandas as pd
from datetime import datetime

form_values={
    "name":None,
    "height":None,
    "age":None,
    "gender":None,
    "dob":None,
    "location":None
}
min_date=datetime(1900,1,1)
max_date=datetime.now()


st.title("User Info Form")

with st.form(key="user_info_form"):
    form_values["name"]=st.text_input("Enter your name:")
    form_values["age"]=st.number_input("Enter your age:")
    form_values["height"]=st.number_input("Enter your height (cm):")
    form_values["gender"]=st.selectbox("Gender",["Male","Female","Other"])
    form_values["dob"]=st.date_input("Enter your Date of birthday:",min_value=min_date,max_value=max_date)

    
    submit_button=st.form_submit_button(label="Submit")
if submit_button:
    if form_values["name"].strip() == "":
        st.warning("Please enter your name.")
    elif form_values["age"] <= 0:
        st.warning("Please enter a valid age.")
    elif form_values["height"] <= 0:
        st.warning("Please enter a valid height.")
    else:
        st.balloons()
        st.write("### INFO ###")
        for key, value in form_values.items():
            st.write(f"{key}: {value}")









