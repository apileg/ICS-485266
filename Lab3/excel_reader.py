# Import the necessary packages
import pandas as pd
from excel_opener import open_file


def read_file():
    try:
        # Read excel file from open_file function
        data = pd.read_excel(fr'{open_file()}')
        # Make table data structure
        df = pd.DataFrame(data)
        print(df)
    except FileNotFoundError:
        print("Oops! I can't find the file.")

