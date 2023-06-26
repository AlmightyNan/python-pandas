# import pandas and numpy (numpy is optional in this case)
import pandas as pd
import numpy as np 

# sample series 
s = pd.Series(data=np.arange(1, 11), index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
s.index.name = 'idx'
s.name = 'seriesObject'

# list of attributes supported by a series object:

objIndex = s.index # returns the indexes of the object 
objIndexName = s.index.name # returns the name of the index 
objValues = s.values # returns the values of the object
objDtype = s.dtype # returns the data type of the object
objShape = s.shape # returns the shape of the object in a tuple
objnBytes = s.nbytes # returns the no. of bytes in the object
objnDim = s.ndim # returns the no. of dimensions in the object in a tuple
objSize = s.size # returns the size of the object
objHasNaNs = s.hasnans # returns True if the object has NaN values
objEmpty = s.empty # returns True if the object is empty
objName = s.name # returns the name of the object

# use the created dtypes to generate a series
print("======================= existing series object ====================")
print(s)
print("===================================================================")
print("===================== series object's attributes ==================")
print('<obj>.index:       ', objIndex)
print('<obj>.index.name:  ', objIndexName)
print('<obj>.values:      ', objValues)
print('<obj>.dtype:       ', objDtype)
print('<obj>.shape:       ', objShape)
print('<obj>.nbytes:      ', objnBytes)
print('<obj>.ndim:        ', objnDim)
print('<obj>.size:        ', objSize)
print('<obj>.hasnans:     ', objHasNaNs)
print('<obj>.empty:       ', objEmpty)
print('<obj>.name:        ', objName)
print("===================================================================")

# ------------------------------------------------------------------

# @ https://almightynan.cc