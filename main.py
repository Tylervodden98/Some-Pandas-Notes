import pandas as pd

nums_pd = pd.Series([1,5,6,7,8,9,3,4])
print(nums_pd)
print(nums_pd.describe())
print(nums_pd.value_counts())

names_pd = pd.Series(['Bob', 'Joe', 'Tyler'])

combined_series = pd.concat([nums_pd,names_pd], ignore_index=True)
print(combined_series)