from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()

filename = askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
print(filename)
