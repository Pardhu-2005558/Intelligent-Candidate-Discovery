import pandas as pd

df = pd.read_csv("sample_submission.csv")

print("Columns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())