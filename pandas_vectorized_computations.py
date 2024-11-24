import pandas as pd
import numpy as np


# Sample data
data = {
    'A': np.random.randint(1, 100, 10),
    'B': np.random.randint(1, 100, 10),
    'C': np.random.random(10),
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Vectorized computations

# Adding two columns
df['Sum'] = df['A'] + df['B']

# Multiplying two columns
df['Product'] = df['A'] * df['B']

# Applying a mathematical function (e.g., square root) to a column
df['Sqrt_A'] = np.sqrt(df['A'])

# Conditional computation: Assign a value based on a condition
df['A_greater_50'] = df['A'] > 50

# Creating a new column with a combination of operations
df['Custom_Formula'] = df['A'] * df['C'] + df['B']

# Normalizing a column (min-max scaling)
df['Normalized_C'] = (df['C'] - df['C'].min()) / (df['C'].max() - df['C'].min())

# Using vectorized string operations (if applicable)
df['String_Example'] = ['item_' + str(i) for i in range(10)]
df['String_Length'] = df['String_Example'].str.len()

# Boolean Masking

# Mask rows where 'A' is greater than 50
mask_A_greater_50 = df['A'] > 50
df_masked_A = df[mask_A_greater_50]

# Mask rows where the normalized value of 'C' is below 0.5
mask_C_below_0_5 = df['Normalized_C'] < 0.5
df_masked_C = df[mask_C_below_0_5]

print("\nDataFrame after vectorized operations:")
print(df)

print("\nRows where 'A' > 50 (Boolean Masking):")
print(df_masked_A)

print("\nRows where normalized 'C' < 0.5 (Boolean Masking):")
print(df_masked_C)
