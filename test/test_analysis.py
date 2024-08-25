import pandas as pd

def analyze_data(data: pd.DataFrame) -> dict:
    analysis_results = {
        'mean': data.mean(),
        'median': data.median(),
        'std': data.std()
    }
    return analysis_results