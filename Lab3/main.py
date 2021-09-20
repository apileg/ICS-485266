# Took the console menu from https://pypi.org/project/console-menu/
# Import the necessary packages
from consolemenu import *
from consolemenu.items import *

import excel_opener
from excel_reader import read_file

# Create the menu
menu = ConsoleMenu("Laboratory work", "File path")

# A FunctionItem runs a Python function when selected
# TODO: To prevent the window from closing; now workaround
function_item = FunctionItem("Call a Python function", read_file, args=None, kwargs=None, menu=ConsoleMenu,
                             should_exit=False)

# Once we're done creating them, we just add the items to the menu
menu.append_item(function_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()
