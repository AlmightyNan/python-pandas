# import pandas and numpy (pandas is optional in this case)
import pandas as pd
import numpy as np 

# here is a list of numpy functions which we will be using from now

'''
np.arange()   - is the same as the builtin range function in python
np.array()    - seems like a list dtype but allows you to perform vector operations
np.linspace() - returns evenly spaced numbers. uses the following formula: (arg2 - arg1) / (arg3 - 1)
                if your function is np.linspace(1, 10, 6), formula will be: (10 - 1)/(6 - 1)

np.tile()     - repeats the given value by n times.
np.NaN()      - returns a NaN (Not a Number) value which is equivalent to null.
'''

arangeFn = np.arange(1, 6, 1) 
arrayFn = np.array([1, 2, 3, 4, 5]) 
linSpaceFn = np.linspace(1, 10, 6)
tileFn = np.tile([6, 2], 5)
nanFn = np.NaN

# use the created dtypes to generate a series
print("======================= list of numpy functions ===================")
print(f"np.arange() => {arangeFn}")
print(f"np.array() => {arrayFn}")
print(f"np.linspace() => {linSpaceFn}")
print(f"np.tile() => {tileFn}")
print(f"np.NaN => {nanFn}")
print("===================================================================")

# @ https://almightynan.cc