import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_parquet("data/raw/train.parquet")

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nPrice Details:")
print(df["product_price"].describe())

print("\nTotal Duplicate Rows:")
print(df.duplicated().sum())

print("\nDuplicate Records:")
print(df[df.duplicated()].head(10).to_string())

print("\nMissing Price Records:")
print(df[df["product_price"].isnull()])

print("\nMissing Rating Records:")
print(df[df["Rate"].isnull()])

print("\nTotal Unique Products:")
print(df["product_name"].nunique())

print("\nProduct Price Summary:")
product_data = df.groupby("product_name")["product_price"].agg(
    ["count", "mean", "min", "max"]
)

print(product_data.head(10))

print("\nMost Reviewed Products:")
print(df["product_name"].value_counts().head(10))

print("\nProducts with Different Prices:")

price_changes = df.groupby("product_name")["product_price"].nunique()

print(price_changes[price_changes > 1])

print("\nTotal Products with Different Prices:")
print((price_changes > 1).sum())


print("\nSentiment Distribution:")
print(df["labels"].value_counts())


print("\nRating Distribution:")
print(df["Rate"].value_counts().sort_index())


print("\nAverage Rating:")
print(df["Rate"].mean())

# Sentiment Distribution Graph

sentiment_count = df["labels"].value_counts()

plt.figure(figsize=(8, 5))
sentiment_count.plot(kind="bar")

plt.title("Customer Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

plt.tight_layout()
plt.savefig("reports/sentiment_distribution.png")
plt.show()


# Rating Distribution Graph

rating_count = df["Rate"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
rating_count.plot(kind="bar")

plt.title("Customer Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Reviews")

plt.tight_layout()
plt.savefig("reports/rating_distribution.png")
plt.show()


# Top 10 Most Reviewed Products

top_products = df["product_name"].value_counts().head(10)

plt.figure(figsize=(10, 7))
top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Most Reviewed Products")
plt.xlabel("Number of Reviews")
plt.ylabel("Product Name")

plt.tight_layout()
plt.savefig("reports/top_reviewed_products.png")
plt.show()


# Product Price Distribution

plt.figure(figsize=(8, 5))
df["product_price"].dropna().plot(kind="hist", bins=30)

plt.title("Product Price Distribution")
plt.xlabel("Price in INR")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("reports/price_distribution.png")
plt.show()