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
    newarr = {}

    for i in df_dict:
        try:
            # ar[i][j] - Try to add to the dictionary keys with values
            result_arr[i].append("")
        except KeyError:
            # ar[i][j] - In case of failure create keys with values for the dictionary
            result_arr[i] = []
        # Column - i
        if i == column:
            # Column - i, Value - j
            for j in df_dict[i]:
                # Hashing data for comparison
                result_arr[i].append(df_dict[i])
                if hashlib.md5(str(df_dict[i][j]).encode()).hexdigest() != hashlib.md5(str(value).encode()).hexdigest():
                    newarr = remove_from_array(df_dict, j)

    for x in newarr.copy():
        for y in newarr[x].copy():
            if (newarr[x][y] == None):
                newarr[x].pop(y)
    # Print DataFrame with our columns and rows
    print(pd.DataFrame(newarr))


def remove_from_array(dictionary, idx):
    for i in dictionary:
        dictionary[i][idx] = None
    return dictionary
