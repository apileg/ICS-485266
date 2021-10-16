# Took the console menu from https://pypi.org/project/console-menu/
# Import the necessary packages
from consolemenu import *
from consolemenu.items import *

# Import variables and functions from root files
import excel_opener
from excel_reader import *

from make_plot import *

# Variables
column = get_all_columns()


# Functions TODO: change string "File path.." to real file path
def console_menu_subtitle(subtitle: str):
    return ConsoleMenu("Laboratory work", subtitle)


# Create the menu
menu = ConsoleMenu("Laboratory work", excel_opener.get_file_path())

# A FunctionItem runs a Python function when selected
# TODO: To prevent the window from closing; now workaround
print_excel_table = FunctionItem("Print excel table", read_file, args=None, kwargs=None, menu=ConsoleMenu,
                                 should_exit=False)

print_excel_table_column = FunctionItem("Print excel column", read_file_column, args=None, kwargs=None,
                                        menu=ConsoleMenu, should_exit=False)

create_line_plot_from_table = FunctionItem("Show line plot", create_line_pot, args=None, kwargs=None,
                                           menu=ConsoleMenu, should_exit=False)

create_bar_plot_from_table = FunctionItem("Show bar plot", create_bar_pot, args=None, kwargs=None,
                                          menu=ConsoleMenu, should_exit=False)

# Once we're done creating them, we just add the items to the menu
menu.append_item(print_excel_table)
menu.append_item(print_excel_table_column)
menu.append_item(create_line_plot_from_table)
menu.append_item(create_bar_plot_from_table)

# Finally, we call show to show the menu and allow the user to interact
menu.show()
