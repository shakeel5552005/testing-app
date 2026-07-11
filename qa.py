
import pandas as pd

def answer_question(df, question):

    question = question.lower()

    # Highest Sales Product
    if "highest sales" in question or "maximum sales" in question:

        row = df.loc[df["Sales"].idxmax()]

        return f"{row['Product']} generated the highest sales of {row['Sales']}."

    # Average Sales
    elif "average sales" in question:

        return f"Average Sales = {df['Sales'].mean():,.2f}"

    # Maximum Orders City
    elif "maximum orders" in question or "highest orders" in question:

        city = df["City"].value_counts().idxmax()

        count = df["City"].value_counts().max()

        return f"{city} has the highest number of orders ({count})."

    # Most Frequent Category
    elif "category" in question and "frequently" in question:

        cat = df["Category"].value_counts().idxmax()

        return f"{cat} is the most frequent category."

    else:

        return "Sorry! I don't know the answer."