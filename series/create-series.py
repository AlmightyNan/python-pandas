# import pandas and numpy
import pandas as pd
import numpy as np 

# create a list/dict/tuple and store it in a var
emptySeriesVar = pd.Series()
listVar = pd.Series(data=[1, 2, 3, 4, 5], index=None)
dictVar = pd.Series(data={0:1, 1:2, 2:3, 3:4, 4:5})
tupleVar = pd.Series(data=(1, 2, 3, 4, 5), index=['a', 'b', 'c', 'd', 'e'])
nparangeVar = pd.Series(data=np.arange(1, 6, 1), index=np.arange(10, 60, 10))
nparrayVar = pd.Series(data=np.array([1, 2, 3, 4, 5]))
nplinspaceVar = pd.Series(data=np.linspace(10, 50, 4), index=[1, 2, 3, 4])
scalarVar = pd.Series(data=1, index=['a'])
nanValueVar = pd.Series(data=[1, np.NaN, 3, 4, 5])

# use the created dtypes to generate a series
print("==================== empty series created via None ================")
print(emptySeriesVar)
print("===================================================================")

print("=================== series created using list =====================")
print(listVar)
print("===================================================================")

print("==================== series created using dict ====================")
print(dictVar)
print("===================================================================")

print("==================== series created using tuple ===================")
print(tupleVar)
print("===================================================================")

print("================= series created using np.arange() ================")
print(nparangeVar)
print("===================================================================")

print("================== series created using np.array() ================")
print(nparrayVar)
print("===================================================================")

print("================= series created using np.linspace() ==============")
print(nplinspaceVar)
print("===================================================================")

print("================= series created using scalar value ===============")
print(scalarVar)
print("===================================================================")

print("================== series created using NaN value =================")
print(nanValueVar)
print("===================================================================")

# NOTE:
# You can also specify index and data without the series parameters
# Here is an example:
# pd.Series(['a', 'b', 'c'], [1, 2, 3])
# list ['a', 'b', 'c'] will be taken as data
# list [1, 2, 3'] will be taken as indexes

# ------------------------------------------------------------------

# @ https://almightynan.cc