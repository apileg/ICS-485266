# Import the necessary packages
import pandas as pd
from excel_opener import open_file

# Read excel file from open_file function
data = pd.read_excel(fr'{open_file()}')

def get_data():
    return data

def read_file():
    try:
        # Make table data structure
        df = pd.DataFrame(data)
        print(df)
    except FileNotFoundError:
        print("Oops! I can't find the file.")


def read_file_column():
    print(f"Available columns: {get_all_columns()}\n")
    # Variables
    column = input("Enter name of column: ")

    if column in get_all_columns():
        # Make table data structure
        df = pd.DataFrame(data, columns=[column])
        print(df)
    else:
        print("Oops! I can't find the column.")


def get_all_columns():
    """
    :return: String
    """
    return data.columns.values
