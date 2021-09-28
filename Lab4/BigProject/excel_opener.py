# Import the necessary packages
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Variables
tkinter_hide_window = Tk().withdraw()
filepath = askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])


def open_file():
    """
    :return: Return String
    """
    try:
        # Hide tkinter root window
        tkinter_hide_window
        # Filepath window dialog
        return filepath
    except FileNotFoundError:
        print("Oops! File open error.")


def get_file_path():
    return filepath
