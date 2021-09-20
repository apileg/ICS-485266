import pandas as pd
from excel_opener import open_file


def read_file():
    try:
        data = pd.read_excel(fr'{open_file()}')
        df = pd.DataFrame(data)
        return df
    except FileNotFoundError:
        print("Oops! I can't find the file")
