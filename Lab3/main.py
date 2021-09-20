# Took the console menu from https://pypi.org/project/console-menu/
# Import the necessary packages
from consolemenu import *
from consolemenu.items import *

# Import variables and functions from root files
import excel_opener
from excel_reader import *

# Variables
filepath = None


# Functions TODO: change string "File path.." to real file path
def console_menu_subtitle(subtitle: str):
    return ConsoleMenu("Laboratory work", subtitle)


# Create the menu
menu = console_menu_subtitle("File path will be here!")

# A FunctionItem runs a Python function when selected
# TODO: To prevent the window from closing; now workaround
print_excel_table = FunctionItem("Print excel table", read_file, args=None, kwargs=None, menu=ConsoleMenu,
                                 should_exit=False)

# Once we're done creating them, we just add the items to the menu
menu.append_item(print_excel_table)

# Finally, we call show to show the menu and allow the user to interact
menu.show()
