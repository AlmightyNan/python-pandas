# import pandas and numpy
import pandas as pd
import numpy as np 

# sample series object 
data = np.array([10, 20, 30, 40, 50])
index = ['A', 'B', 'C', 'D', 'E']
series = pd.Series(data, index)

# Display the original Series
print("======================= existing series object ====================")
print(series)
print("===================================================================")

# Slicing using index labels
print("=================== slicing using positional index ================")
sliced_series = series['B':'D']
print(sliced_series)
print("===================================================================")

# Slicing using index positions
print("==================== slicing using default index ==================")
sliced_series = series[1:4]
print(sliced_series)
print("===================================================================")

# Slicing with a step size
print("===================== slicing using step_values ====================")
sliced_series = series[::2]
print(sliced_series)
print("===================================================================")

# ------------------------------------------------------------------

# @ https://almightynan.cc