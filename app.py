import streamlit as st
import pandas as pd

# -----------------------
# Page Config
# -----------------------

st.set_page_config(
    page_title="Smart Excel Analyzer",
    page_icon="📊",
    layout="wide"
)

# -----------------------
# Load CSS
# -----------------------

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------
# Sidebar
# -----------------------

st.sidebar.title("📂 Navigation")

menu = st.sidebar.radio(
    "Choose Option",
    [
        "Dashboard",
        "Upload Excel",
        "About"
    ]
)

# -----------------------
# Header
# -----------------------

st.markdown(
    "<p class='main-title'>📊 Smart Excel Analyzer Pro</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='sub-title'>Analyze Excel files with interactive dashboard.</p>",
    unsafe_allow_html=True
)

st.divider()

# -----------------------
# Dashboard
# -----------------------

if menu == "Dashboard":

    col1, col2, col3 = st.columns(3)

    col1.metric("📄 Files", 0)

    col2.metric("📊 Rows", 0)

    col3.metric("📈 Columns", 0)

    st.info("Upload an Excel file from the sidebar.")

# -----------------------
# Upload
# -----------------------

elif menu == "Upload Excel":

    uploaded_file = st.file_uploader(
        "Upload Excel File",
        type=["xlsx", "xls", "csv"]
    )

    if uploaded_file:

        if uploaded_file.name.endswith(".csv"):

            df = pd.read_csv(uploaded_file)

        else:

            df = pd.read_excel(uploaded_file)

        st.success("File uploaded successfully!")

        st.dataframe(df, use_container_width=True)

# -----------------------
# About
# -----------------------

else:

    st.header("About")

    st.write("""
    Smart Excel Analyzer Pro

    Developed using:

    ✔ Streamlit

    ✔ Pandas

    ✔ Plotly

    ✔ Python1
    """)