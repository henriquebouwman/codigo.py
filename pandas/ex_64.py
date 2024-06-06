from pandas_datareader import data as pdr
from datetime import datetime

bdd = "GDP"

dado = pdr.get_data_fred(bdd, "1910-12-31", datetime.now())

print(dado)