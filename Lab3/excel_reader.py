import pandas as pd
from excel_opener import open_file

data = pd.read_excel(fr'{open_file()}')
df = pd.DataFrame(data)
print(df)