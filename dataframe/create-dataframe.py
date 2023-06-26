import pandas as pd
import numpy as np

data_dict = {
    "Name": ["John", "Joseph", "George", "Thekkumootil"],
    "Age": [25, 28, 30, 27],
    "City": ["New York", "London", "Dallas", "Sydney"],
}
df_dict = pd.DataFrame(data_dict)
print("====================== dataframe object via dict ==================")
print(df_dict)
print("===================================================================")


data_list = [
    ["John", 25, "New York"],
    ["Joseph", 28, "London"],
    ["George", 30, "Dallas"],
    ["Thekkumootil", 27, "Sydney"],
]
columns = ["Name", "Age", "City"]
df_list = pd.DataFrame(data_list, columns=columns)
print("====================== dataframe object via lists =================")
print(df_list)
print("===================================================================")

data_array = np.array(
    [
        ["John", 25, "New York"],
        ["Joseph", 28, "London"],
        ["George", 30, "Dallas"],
        ["Thekkumootil", 27, "Sydney"],
    ]
)

df_array = pd.DataFrame(data_array, columns=columns)
print("====================== dataframe object via numpy =================")
print(df_array)
print("===================================================================")

# ------------------------------------------------------------------

# @ https://almightynan.cc