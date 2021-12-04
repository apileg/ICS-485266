import numpy as np

from excel_reader import get_data


def to_text():
    data = get_data()
    numpy_to_list = data.values.tolist()

    open_file = open('./to_text.txt', 'w')
    for row in numpy_to_list:
        np.savetxt(open_file, row, fmt="%s")
    open_file.close()
