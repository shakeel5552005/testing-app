import streamlit as st

st.set_page_config(page_title="Test")

st.title("✅ Streamlit is working on Python 3.14")
st.write("If you can see this, Python 3.14 is working correctly.")
from analysis import get_summary, numeric_summary, categorical_summary

# -----------------------------
# Dataset Summary
# -----------------------------

summary = get_summary(df)

st.header("📊 Dataset Summary")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Rows", summary["Rows"])
c2.metric("Columns", summary["Columns"])
c3.metric("Missing", summary["Missing Values"])
c4.metric("Duplicates", summary["Duplicate Rows"])

# -----------------------------
# Numeric Statistics
# -----------------------------

st.header("📈 Numerical Statistics")

st.dataframe(numeric_summary(df))

# -----------------------------
# Category Distribution
# -----------------------------

st.header("📋 Category Distribution")

categories = categorical_summary(df)

for column, values in categories.items():

    st.subheader(column)

    st.dataframe(values)