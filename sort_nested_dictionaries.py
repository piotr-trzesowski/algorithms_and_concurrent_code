import pandas as pd

# Example DataFrame
data = {
    'Details': [
        {'value1': "A", 'value2': 2, 'value3': "B"},
        {'value1': "B", 'value2': 3, 'value3': "C"},
        {'value1': "C", 'value2': 1, 'value3': "A"},
    ]
}

df = pd.DataFrame(data)

# Sort the list of dictionaries by 'value2'
sorted_details = sorted(df['Details'], key=lambda x: x['value2'])

# Replace the original column with the sorted list
df['Details'] = sorted_details

print(df)