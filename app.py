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

# ----------------------------------
# File Upload
# ----------------------------------
uploaded_file = st.file_uploader(
    "Choose a CSV File",
    type=["csv"]
)

# ----------------------------------
# Read CSV
# ----------------------------------
if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        st.success("✅ CSV Loaded Successfully!")
        create_chart(df)
        # ----------------------------------
        # Preview
        # ----------------------------------
        st.header("📄 Dataset Preview")
        st.dataframe(df, use_container_width=True)

        # ----------------------------------
        # Summary
        # ----------------------------------
        st.header("📊 Dataset Summary")

        total_rows = df.shape[0]
        total_columns = df.shape[1]
        missing_values = df.isnull().sum().sum()
        duplicate_rows = df.duplicated().sum()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Rows", total_rows)
        col2.metric("Columns", total_columns)
        col3.metric("Missing Values", missing_values)
        col4.metric("Duplicate Rows", duplicate_rows)

        # ----------------------------------
        # Column Names
        # ----------------------------------
        st.header("📌 Column Names")
        st.write(list(df.columns))

        # ----------------------------------
        # Data Types
        # ----------------------------------
        st.header("📋 Data Types")

        datatype_df = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str)
        })

        st.dataframe(datatype_df, use_container_width=True)

        # ----------------------------------
        # Missing Values
        # ----------------------------------
        st.header("❗ Missing Values")

        missing_df = pd.DataFrame({
            "Column": df.columns,
            "Missing Values": df.isnull().sum()
        })

        st.dataframe(missing_df, use_container_width=True)

        # ----------------------------------
        # Numerical Statistics
        # ----------------------------------
        numeric_df = df.select_dtypes(include=["number"])

        if not numeric_df.empty:

            st.header("📈 Numerical Statistics")

            st.dataframe(
                numeric_df.describe(),
                use_container_width=True
            )

        # ----------------------------------
        # Category Distribution
        # ----------------------------------
        categorical_columns = df.select_dtypes(include=["object"]).columns

        if len(categorical_columns) > 0:

            st.header("📊 Category Distribution")

            for column in categorical_columns:

                st.subheader(column)

                frequency = df[column].value_counts().reset_index()

                frequency.columns = [column, "Count"]

                st.dataframe(
                    frequency,
                    use_container_width=True
                )

    except Exception as e:

        st.error("❌ Error Reading CSV File")

        st.exception(e)

else:

    st.info("⬆ Please upload a CSV file to continue.")
