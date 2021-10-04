import pandas as pd
import matplotlib.pyplot as plt

from excel_reader import get_data
from excel_reader import get_all_columns


def create_pot():
    df = pd.DataFrame(get_data(), columns=['Дата', 'Картопля'])
    df.plot(x='Дата', y='Картопля', kind='line')
    plt.show()
