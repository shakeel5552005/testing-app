import streamlit as st
import plotly.express as px


def create_chart(df):

    st.header("📊 Data Visualization")

    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()

    categorical_columns = df.select_dtypes(include=["object"]).columns.tolist()

    if len(numeric_columns) == 0:
        st.warning("No numeric columns found.")
        return

    chart_type = st.selectbox(
        "Select Chart Type",
        ["Bar Chart", "Line Chart", "Pie Chart", "Histogram", "Scatter Plot"]
    )

    if chart_type == "Bar Chart":

        x = st.selectbox("X Axis", categorical_columns)
        y = st.selectbox("Y Axis", numeric_columns)

        fig = px.bar(df, x=x, y=y, color=x, title=f"{y} by {x}")

    elif chart_type == "Line Chart":

        x = st.selectbox("X Axis", df.columns)
        y = st.selectbox("Y Axis", numeric_columns)

        fig = px.line(df, x=x, y=y, title=f"{y} Trend")

    elif chart_type == "Pie Chart":

        names = st.selectbox("Category", categorical_columns)
        values = st.selectbox("Values", numeric_columns)

        fig = px.pie(df, names=names, values=values)

    elif chart_type == "Histogram":

        x = st.selectbox("Column", numeric_columns)

        fig = px.histogram(df, x=x)

    elif chart_type == "Scatter Plot":

        x = st.selectbox("X Axis", numeric_columns)
        y = st.selectbox("Y Axis", numeric_columns)

        fig = px.scatter(df, x=x, y=y)

    st.plotly_chart(fig, use_container_width=True)