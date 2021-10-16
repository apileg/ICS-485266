from excel_reader import *
import pandas as pd
import numpy as np
import hashlib
from numpy import *

from excel_reader import *


def sort_data():
    # Print available columns
    print(f"Available columns: {get_all_columns()}\n")

    # Input
    column = input("Enter column: ")
    value = input("Enter value: ")
    # Variables
    # get data from our table
    df = get_data()
    # standardizing our df type to dictionary
    df_dict = df.to_dict()
    result_arr = {}

    for i in df_dict:
        # Column - i
        if i == column:
            # Column - i, Value - j
            for j in df_dict[i]:
                # Hashing data for comparison
                if hashlib.md5(str(df_dict[i][j]).encode()).hexdigest() == hashlib.md5(str(value).encode()).hexdigest():
                    try:
                        # ar[i][j] - Try to add to the dictionary keys with values
                        result_arr[i].append(df_dict[i][j])
                    except KeyError:
                        # ar[i][j] - In case of failure create keys with values for the dictionary
                        result_arr[i] = [df_dict[i][j]]
    # Print DataFrame with our columns and rows
    print(pd.DataFrame(result_arr))
