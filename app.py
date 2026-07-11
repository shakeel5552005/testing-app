import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Data Analysis Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Data Analysis Assistant")
st.write("Upload a CSV file to begin analysis.")

# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

# -----------------------------
# Read Dataset
# -----------------------------
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("✅ Dataset Loaded Successfully!")

    # Preview
    st.subheader("Dataset Preview")
    st.dataframe(df)

    # Dataset Information
    st.subheader("Dataset Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric("Missing Values", df.isnull().sum().sum())

    # Column Names
    st.subheader("Column Names")
    st.write(list(df.columns))

    # Data Types
    st.subheader("Data Types")
    st.dataframe(df.dtypes.astype(str).reset_index().rename(
        columns={"index": "Column", 0: "Data Type"}
    ))