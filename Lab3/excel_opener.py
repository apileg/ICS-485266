from tkinter import Tk
from tkinter.filedialog import askopenfilename


def open_file():
    Tk().withdraw()
    filename = askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
    return filename
