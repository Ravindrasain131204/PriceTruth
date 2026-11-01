import pandas as pd

# Load dataset
df = pd.read_parquet("data/raw/train.parquet")

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Show rows where price or rating is missing
missing_data = df[df["product_price"].isnull() | df["Rate"].isnull()]

print("\nRecords with Missing Price or Rating:")
print(missing_data)

# Remove records with missing price or rating
clean_df = df.dropna(subset=["product_price", "Rate"])

# Check missing values again
print("\nMissing Values After Cleaning:")
print(clean_df.isnull().sum())

print("\nOriginal Dataset Shape:", df.shape)
print("Cleaned Dataset Shape:", clean_df.shape)

# Check duplicate records
duplicate_count = clean_df.duplicated().sum()

print("\nDuplicate Records:", duplicate_count)

# Display duplicate records
duplicates = clean_df[clean_df.duplicated()]

print("\nSample Duplicate Records:")
print(duplicates.head())

# Remove duplicate records
clean_df = clean_df.drop_duplicates()

# Check duplicates again
print("\nDuplicates After Cleaning:")
print(clean_df.duplicated().sum())

# Check final dataset size
print("\nFinal Dataset Shape:", clean_df.shape)

# Check data types
print("\nData Types:")
print(clean_df.dtypes)

# Check invalid prices
print("\nInvalid Prices:")
print(clean_df[clean_df["product_price"] <= 0])

# Check invalid ratings
print("\nInvalid Ratings:")
print(clean_df[(clean_df["Rate"] < 1) | (clean_df["Rate"] > 5)])


# Save cleaned dataset

clean_df.to_parquet(
    "data/processed/cleaned_flipkart_reviews.parquet",
    index=False
)

print("\nCleaned dataset saved successfully!")
print("Final Dataset Shape:", clean_df.shape)