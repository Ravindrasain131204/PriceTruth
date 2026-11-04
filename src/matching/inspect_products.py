import pandas as pd

# Load cleaned dataset
df = pd.read_parquet(
    "data/processed/cleaned_flipkart_reviews.parquet"
)

# Get unique product names
products = df["product_name"].drop_duplicates()

print("Total Unique Products:", len(products))

print("\nFirst 20 Product Names:")

for index, product in enumerate(products.head(20), start=1):
    print(f"{index}. {product}")

# Count corrupted product names
corrupted_products = products[
    products.str.contains(r"\?", na=False)
]

print("\nProducts Containing Question Marks:")
print(len(corrupted_products))


# Create a separate cleaned product name
df["clean_product_name"] = (
    df["product_name"]
    .str.replace(r"\?+", " ", regex=True)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

print("\nOriginal vs Cleaned Product Names:")

comparison = df[
    ["product_name", "clean_product_name"]
].drop_duplicates()

print(comparison.head(20).to_string(index=False))

print("\nOriginal Unique Products:",
      df["product_name"].nunique())

print("Cleaned Unique Product Names:",
      df["clean_product_name"].nunique())


# Check product name collisions
collision_counts = (
    df[["product_name", "clean_product_name"]]
    .drop_duplicates()
    .groupby("clean_product_name")["product_name"]
    .nunique()
)

collisions = collision_counts[collision_counts > 1]

print("\nProduct Name Collisions:")
print("Total Collisions:", len(collisions))

if len(collisions) > 0:
    print(collisions)
else:
    print("No product name collisions found.")