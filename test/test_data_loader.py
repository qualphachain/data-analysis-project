import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def save_data(data: pd.DataFrame, file_path: str) -> None:
    data.to_csv(file_path, index=False)