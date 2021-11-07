import csv
import pandas as pd
import numpy as np

df = pd.read_csv('census.csv')

stname = list(df['STNAME']) # creat a list of 'STNAME'

stncountdict = {}

for i in stname:

    stncountdict[i] = stname.count(i)


comdf = pd.Series(stncountdict)

comdd=comdf.sort_values()
print(str(comdd.index[-1]))
