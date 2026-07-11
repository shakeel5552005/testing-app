import pandas as pd

def get_summary(df):
    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum(),
        "Duplicate Rows": df.duplicated().sum()
    }

def numeric_summary(df):
    return df.describe()

def categorical_summary(df):
    cat_cols = df.select_dtypes(include="object").columns

    result = {}

    for col in cat_cols:
        result[col] = df[col].value_counts()

    return result