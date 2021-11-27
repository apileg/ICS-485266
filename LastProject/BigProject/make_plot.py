import pandas as pd
import matplotlib.pyplot as plt

from threading import Thread
from excel_reader import get_data
from excel_reader import get_all_columns


# I can not avoid repeating the code, because the cleft hand person who created the menu could not normally pass the
# function arguments to FunctionItem(args), because it returns FOUR args, but should ONE
# You can just pass 'plot_type' to function args and use this variable in df.plot(x=...,y=...,kind=plot_type)

def create_line_pot():
    # Variables
    get_all_columns_arr = get_all_columns()
    # Print all columns of table
    print(f"Available columns: {get_all_columns()}\n")
    # Input variables for plot
    f_column = input("Enter name of the first column: ")
    s_column = input("Enter name of the second column: ")

    try:
        # If get_all_columns string array has f_column and s_column - make action
        if f_column and s_column in get_all_columns_arr:
            # df = select columns from excel data
            df = pd.DataFrame(get_data(), columns=[f_column, s_column])
            # Create plot, using f_column, s_column, figsize=(width, height) - figure size (inch)
            # kind='...' - type of plot line|bar
            df.plot(x=f_column, y=s_column, figsize=(8, 8), kind='line')
            # Show plot
            plt.show()
    except ArithmeticError:
        print("Invalid field name")


def create_bar_pot():
    get_all_columns_arr = get_all_columns()
    print(f"Available columns: {get_all_columns()}\n")
    f_column = input("Enter name of the first column: ")
    s_column = input("Enter name of the second column: ")
    try:
        if f_column and s_column in get_all_columns_arr:
            df = pd.DataFrame(get_data(), columns=[f_column, s_column])
            df.plot(x=f_column, y=s_column, figsize=(8, 8), kind='bar')
            plt.show()
    except ArithmeticError:
        print("Invalid field name")

