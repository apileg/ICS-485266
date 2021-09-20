# Import the necessary packages
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def open_file():
    """
    :return: Return String
    """
    try:
        # Hide tkinter root window
        Tk().withdraw()
        # Filepath window dialog
        filepath = askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
        return filepath
    except Warning:
        print("Oops! File open error.")
