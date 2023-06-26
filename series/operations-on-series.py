# import pandas and numpy (numpy is optional in this case)
import pandas as pd
import numpy as np 

# sample series 
s = pd.Series(data=np.arange(1, 11), index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
s.index.name = 'idx'
s.name = 'seriesObject'

# modifying elements in series object
print("==================== modifying elements in series =================")
s['a'] = 5
s['b'] = 6
s['c'] = 7
s['d'] = 8
s['e'] = 9
s['f'] = 10
print(s)
print("===================================================================")

# renaming indexes
print("=================== renaming index.name in series =================")
s.index.name = 'new_idx'
print(s)
print("===================================================================")

# vector operations on series object(s)
print("==================== vector operations on series ==================")
print(s + s)
print()
print(s / s)
print("===================================================================")

# ------------------------------------------------------------------

# @ https://almightynan.cc