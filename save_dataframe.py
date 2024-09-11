import pandas as pd

# Create a sample DataFrame
data = {'column1': [1, 2, 3], 'column2': ['a', 'b', 'c']}
df = pd.DataFrame(data)

df.to_csv('data.csv', index=False)
df.to_parquet('data.parquet', engine='pyarrow')
# df.to_excel('data.xlsx', index=False)
