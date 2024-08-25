import pandas as pd

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    data = data.dropna()
    data = data.drop_duplicates()
    return data

def normalize_data(data: pd.DataFrame) -> pd.DataFrame:
    return (data - data.min()) / (data.max() - data.min())