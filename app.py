import streamlit as st
import pandas as pd
from charts import create_chart
from qa import answer_question

# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="AI Data Analysis Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Data Analysis Assistant")
st.write("Upload a CSV file to analyze your data.")

