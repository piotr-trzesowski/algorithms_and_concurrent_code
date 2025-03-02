import pandas as pd

# Example DataFrames
df1 = pd.DataFrame({
    "db": ["db1", "db2", "db3"],
    "table": ["table1", "table2", "table3"],
    "sum": [100, 200, 300, 200]
})

df2 = pd.DataFrame({
    "db": ["db1", "db2", "db4"],
    "table": ["table1", "table2", "table4"],
    "null": [10, 20, 40]
})

# Merge on columns "db" and "table"
merged_df = pd.merge(df1, df2, on=["db", "table"], how="outer")

print(merged_df)