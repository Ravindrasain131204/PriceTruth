import pandas as pd
import matplotlib.pyplot as plt


# Load cleaned dataset
df = pd.read_parquet(
    "data/processed/cleaned_flipkart_reviews.parquet"
)


# Create clean product names for display
df["display_product_name"] = (
    df["product_name"]
    .str.replace(r"\?+", " ", regex=True)
    .str.strip()
)

print("\nClean Product Names:")
print(
    df[["display_product_name", "Rate"]]
    .head(10)
    .to_string(index=False)
)


# Calculate overall average rating
average_rating = df["Rate"].mean()

print("\nOverall Average Rating:", average_rating)


# Calculate average rating for each product
product_ratings = df.groupby(
    "display_product_name"
)["Rate"].mean()

print("\nProduct-wise Average Ratings:")
print(product_ratings.head(10))


# Product rating and review count
product_analysis = df.groupby("display_product_name").agg(
    average_rating=("Rate", "mean"),
    total_reviews=("Rate", "count")
)

print("\nProduct Rating and Review Count:")
print(product_analysis.head(10))


# Filter products with at least 20 reviews
reliable_products = product_analysis[
    product_analysis["total_reviews"] >= 20
]


# Sort products by average rating
top_rated_products = reliable_products.sort_values(
    by="average_rating",
    ascending=False
)

print("\nTop 10 Reliable Rated Products:")
print(top_rated_products.head(10))


# Select Top 10 Products
top_10 = top_rated_products.head(10)


# Create Bar Chart
plt.figure(figsize=(12, 7))

top_10["average_rating"].sort_values().plot(
    kind="barh"
)

plt.title("Top 10 Highest Rated Products")
plt.xlabel("Average Rating")
plt.ylabel("Product Name")

plt.xlim(0, 5)

plt.tight_layout()

# Save graph
plt.savefig(
    "reports/top_10_rated_products.png",
    dpi=300,
    bbox_inches="tight"
)

# Display graph
plt.show()


# Check original product names containing question marks
print("\nProduct Names Containing Question Marks:")

question_mark_products = df[
    df["product_name"].str.contains(r"\?", na=False)
]

print(
    question_mark_products["product_name"]
    .drop_duplicates()
    .head(10)
    .to_string(index=False)
)

print(
    "\nTotal Products with Question Marks:",
    question_mark_products["product_name"].nunique()
)