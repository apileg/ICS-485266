# Took the console menu from https://pypi.org/project/console-menu/
# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
from excel_reader import read_file

# Create the menu
menu = ConsoleMenu("Title", "Subtitle")

# A FunctionItem runs a Python function when selected
function_item = FunctionItem("Call a Python function", read_file())

# Once we're done creating them, we just add the items to the menu
menu.append_item(function_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()
