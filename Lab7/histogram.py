from collections import Counter
from matplotlib import pyplot as plt
import numpy as np

def create_histogram(text: str):
    counts = Counter(text.replace(" ", ""))
    for i in text:
        plt.bar(i, counts[i])
        plt.savefig('plot.png')
    plt.show()



create_histogram("ssomme ttexxt")
