import pandas as pd

def read_excel(file_path=None):
    if file_path is None:
        file_path = 'D:/CDMI/AED/exercicios/dolar.xlsx'
    df = pd.read_excel(file_path)
    return df