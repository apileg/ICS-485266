# Import the necessary packages
import pandas as pd
from excel_opener import open_file

# Read excel file from open_file function
data = pd.read_excel(fr'{open_file()}')


def read_file():
    try:
        # Make table data structure
        df = pd.DataFrame(data)
        print(df)
    except FileNotFoundError:
        print("Oops! I can't find the file.")


def read_file_column(column: str):
    try:
        # Make table data structure
        df = pd.DataFrame(data, columns=[column])
        print(df)
    except FileNotFoundError:
        print("Oops! I can't find the file.")


def get_all_columns():
    """
    :return: String
    """
    return data.columns.values
