import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_data_distribution(data: pd.DataFrame, column: str) -> None:
    sns.histplot(data[column], kde=True)
    plt.show()

def plot_correlation_matrix(data: pd.DataFrame) -> None:
    corr_matrix = data.corr()
    sns.heatmap(corr_matrix, annot=True)
    plt.show()