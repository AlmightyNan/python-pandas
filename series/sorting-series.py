# import pandas and numpy (numpy is optional in this case)
import pandas as pd
import numpy as np 

# sample series 
data = {'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50}
series = pd.Series(data)

# Display the original Series
print("======================= existing series object ====================")
print(series)
print("===================================================================")

# Sort the Series by values in ascending order
print("================== sorting values in ascending order ==============")
sorted_series = series.sort_values()
print(sorted_series)
print("===================================================================")

# Sort the Series by values in descending order
print("================= sorting values in descending order ==============")
sorted_series = series.sort_values(ascending=False)
print(sorted_series)
print("===================================================================")

# Sort the Series by index in ascending order
print("================= sorting index in ascending order ================")
sorted_series = series.sort_index()
print(sorted_series)
print("===================================================================")

# Sort the Series by index in descending order
print("================= sorting index in descending order ===============")
sorted_series = series.sort_index(ascending=False)
print(sorted_series)
print("===================================================================")

# ------------------------------------------------------------------

# @ https://almightynan.cc