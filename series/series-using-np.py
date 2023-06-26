# import pandas and numpy
import pandas as pd
import numpy as np 

# create numpy datas to use for series creation

# arange()   - is the same as range but in numpy
# linspace() - uses a formula to calculate value: (2nd arg - 1st arg) / (3rd arg - 1)
# tile()     - repeats the value based on the 2nd argument
# NaN        - denotes an empty value in the series

arangeVar = np.arange(1, 6) 
arrayVar = np.array([1, 2, 3, 4, 5]) 
linSpaceVar = np.linspace(10, 50, 4) 
tileVar = np.tile([1, 2], 4) 
nanVar = np.NaN


print("====================== np{} variable values =======================")
print(f"Arange var: {arangeVar}")
print(f"Array var: {arrayVar}")
print(f"Linspace var: {linSpaceVar}")
print(f"Tile var: {tileVar}")
print("===================================================================")
print()
print("=================== series created using arange ===================")
print(pd.Series(arangeVar))
print("===================================================================")

print("=================== series created using array ====================")
print(pd.Series(arrayVar))
print("===================================================================")

print("================== series created using linspace ==================")
print(pd.Series(linSpaceVar))
print("===================================================================")

print("==================== series created using tile ====================")
print(pd.Series(tileVar))
print("===================================================================")

print("================ series created using NaN (thats me) ==============")
print(pd.Series(nanVar))
print("===================================================================")

# @ https://almightynan.cc