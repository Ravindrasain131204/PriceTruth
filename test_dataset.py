import pandas as pd
import matplotlib.pyplot as plt
import textwrap

df = pd.read_parquet("data/processed/cleaned_flipkart_reviews.parquet")

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

print("\nDuplicate Records:")
print(df[df.duplicated()].head(10).to_string())

print("\nMissing Price Records:")
print(df[df["product_price"].isnull()])

print("\nMissing Rating Records:")
print(df[df["Rate"].isnull()])

print("\nTotal Unique Products:")
print(df["product_name"].nunique())

print("\nProduct Price Summary:")
product_data = df.groupby("product_name").agg(
    review_count=("product_name", "count"),
    average_price=("product_price", "mean"),
    minimum_price=("product_price", "min"),
    maximum_price=("product_price", "max")
)

print(product_data.head(10))

print("\nMost Reviewed Products:")
print(df["product_name"].value_counts().head(10))

print("\nProducts with Multiple Recorded Prices:")

multiple_prices = df.groupby("product_name")["product_price"].nunique()

print(multiple_prices[multiple_prices > 1])

print("\nTotal Products with Multiple Recorded Prices:")
print((multiple_prices > 1).sum())


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

product_labels = [
    textwrap.fill(name, width=50)
    for name in top_products.index
]

plt.figure(figsize=(13, 7))

plt.barh(product_labels, top_products.values)

plt.title("Top 10 Most Reviewed Products", fontsize=13)
plt.xlabel("Number of Reviews", fontsize=10)

plt.tick_params(axis="y", labelsize=8)

plt.subplots_adjust(left=0.42, hspace=0.4)

plt.savefig(
    "reports/top_reviewed_products.png",
    dpi=200,
    bbox_inches="tight"
)

plt.show()

# Product Price Distribution

# Product-level Price Distribution

product_prices = df.groupby("product_name")["product_price"].median()

plt.figure(figsize=(8, 5))
product_prices.plot(kind="hist", bins=30)

plt.title("Product-Level Price Distribution")
plt.xlabel("Median Product Price (INR)")
plt.ylabel("Number of Products")

plt.tight_layout()
plt.savefig("reports/price_distribution.png")
plt.show()