import pandas as pd


# =====================================
# LOAD CLEANED DATASET
# =====================================

df = pd.read_parquet(
    "data/processed/cleaned_flipkart_reviews.parquet"
)

print("Dataset Loaded Successfully!")
print("Total Records:", len(df))


# =====================================
# CLEAN PRODUCT NAMES
# =====================================

df["clean_product_name"] = (
    df["product_name"]
    .str.replace(r"\?+", " ", regex=True)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)


# =====================================
# LOAD PRODUCT CATALOG
# =====================================

catalog = pd.read_csv("reports/product_catalog.csv")

df = df.merge(
    catalog[
        ["clean_product_name", "brand", "category"]
    ],
    on="clean_product_name",
    how="left"
)


# =====================================
# PRODUCT LEVEL ANALYSIS
# =====================================

product_data = df.groupby(
    "clean_product_name"
).agg(
    brand=("brand", "first"),
    category=("category", "first"),
    product_price=("product_price", "median"),
    average_rating=("Rate", "mean"),
    total_reviews=("Rate", "count")
).reset_index()

product_data["average_rating"] = (
    product_data["average_rating"].round(2)
)


# =====================================
# CATEGORY PRICE BENCHMARK
# =====================================

category_benchmark = product_data.groupby(
    "category"
)["product_price"].median()

product_data["category_median_price"] = (
    product_data["category"].map(category_benchmark)
)


# =====================================
# PRICE DIFFERENCE CALCULATION
# =====================================

product_data["price_difference_percent"] = (
    (
        product_data["product_price"]
        - product_data["category_median_price"]
    )
    / product_data["category_median_price"]
) * 100

product_data["price_difference_percent"] = (
    product_data["price_difference_percent"].round(2)
)


# =====================================
# PRICE POSITION
# =====================================

def classify_price(difference):

    if difference < -10:
        return "Below Category Benchmark"

    elif difference > 10:
        return "Above Category Benchmark"

    else:
        return "Near Category Benchmark"


product_data["price_position"] = (
    product_data["price_difference_percent"]
    .apply(classify_price)
)


# =====================================
# SAVE PRICE INTELLIGENCE REPORT
# =====================================

product_data = product_data.sort_values(
    "price_difference_percent"
)

product_data.to_csv(
    "reports/price_intelligence.csv",
    index=False
)


# =====================================
# DISPLAY RESULTS
# =====================================

print("\n========== PRICE INTELLIGENCE ==========")

print(
    product_data[
        [
            "clean_product_name",
            "brand",
            "category",
            "product_price",
            "category_median_price",
            "price_difference_percent",
            "price_position"
        ]
    ].head(10).to_string(index=False)
)

print("\nPrice Position Summary:")

print(
    product_data["price_position"].value_counts()
)

print("\nPrice Intelligence Report Saved Successfully!")