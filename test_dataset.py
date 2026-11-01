import pandas as pd
file_path ="data/raw/train.parquet"
df = pd.read_parquet(file_path)
print("\nDATASET LOADED SUCCESSFULLY!")
df.head()

df.shape

print("\nColumn Names:")
print(df.columns.tolist())