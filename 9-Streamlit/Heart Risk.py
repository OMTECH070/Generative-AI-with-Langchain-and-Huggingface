import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Heart Attack Data Dashboard",
    page_icon="❤️",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("❤️ Heart Attack Data Dashboard")
st.write("A simple healthcare dataset dashboard built using Streamlit.")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Dataset",
        "Dataset Information",
        "Statistics",
        "Missing Values",
        "Duplicate Values",
        "Column Explorer",
        "Filter Data",
        "Search by Age",
        "Download Dataset"
    ]
)

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is None:
    st.info("Please upload a CSV dataset from the sidebar.")
    st.stop()

df = pd.read_csv(uploaded_file)

# -----------------------------
# HOME
# -----------------------------
if page == "Home":

    st.header("Project Overview")

    st.write("""
This dashboard provides basic analysis of a Heart Attack dataset.

Features:
- Dataset Preview
- Dataset Information
- Statistics
- Missing Values
- Duplicate Values
- Column Explorer
- Filter Records
- Search by Age
- Download Dataset
""")

    st.success("Dataset Loaded Successfully!")

# -----------------------------
# DATASET
# -----------------------------
elif page == "Dataset":

    st.header("Dataset Preview")

    rows = st.slider(
        "Number of Rows",
        5,
        len(df),
        10
    )

    st.dataframe(df.head(rows))

# -----------------------------
# INFORMATION
# -----------------------------
elif page == "Dataset Information":

    st.header("Dataset Information")

    st.subheader("Shape")

    col1, col2 = st.columns(2)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])

    st.subheader("Column Names")
    st.write(df.columns.tolist())

    info = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum().values
    })

    st.subheader("Column Information")
    st.dataframe(info)

# -----------------------------
# STATISTICS
# -----------------------------
elif page == "Statistics":

    st.header("Statistical Summary")

    st.dataframe(df.describe())

# -----------------------------
# MISSING VALUES
# -----------------------------
elif page == "Missing Values":

    st.header("Missing Values")

    missing = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum()
    })

    st.dataframe(missing)

# -----------------------------
# DUPLICATES
# -----------------------------
elif page == "Duplicate Values":

    st.header("Duplicate Values")

    duplicate_count = df.duplicated().sum()

    st.metric("Duplicate Rows", duplicate_count)

    if duplicate_count > 0:
        if st.button("Show Duplicate Rows"):
            st.dataframe(df[df.duplicated()])

# -----------------------------
# COLUMN EXPLORER
# -----------------------------
elif page == "Column Explorer":

    st.header("Column Explorer")

    column = st.selectbox(
        "Select Column",
        df.columns
    )

    st.subheader("Column Data")

    st.write(df[column])

    st.subheader("Unique Values")

    st.write(df[column].unique())

    st.subheader("Value Counts")

    st.write(df[column].value_counts())

# -----------------------------
# FILTER
# -----------------------------
elif page == "Filter Data":

    st.header("Filter Dataset")

    column = st.selectbox(
        "Select Column",
        df.columns
    )

    values = sorted(df[column].astype(str).unique())

    selected = st.selectbox(
        "Select Value",
        values
    )

    filtered = df[df[column].astype(str) == selected]

    st.write("Filtered Records:", len(filtered))

    st.dataframe(filtered)

# -----------------------------
# SEARCH AGE
# -----------------------------
elif page == "Search by Age":

    st.header("Search Patient by Age")

    if "age" in df.columns:

        age = st.number_input(
            "Enter Age",
            min_value=int(df["age"].min()),
            max_value=int(df["age"].max()),
            value=int(df["age"].min())
        )

        result = df[df["age"] == age]

        st.write("Records Found:", len(result))

        st.dataframe(result)

    else:
        st.error("No 'age' column found.")

# -----------------------------
# DOWNLOAD
# -----------------------------
elif page == "Download Dataset":

    st.header("Download Dataset")

    csv = df.to_csv(index=False)

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="heart_attack_dataset.csv",
        mime="text/csv"
    )

st.sidebar.markdown("---")
st.sidebar.write("Made with ❤️ using Streamlit")                                                           