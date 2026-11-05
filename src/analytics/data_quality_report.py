import pandas as pd


# Load Cleaned Dataset

df = pd.read_parquet("data/processed/cleaned_flipkart_reviews.parquet")


print("\n========== DATA QUALITY REPORT ==========")

# 1. Dataset Overview

print("\n1. DATASET OVERVIEW")

print("Total Records:", len(df))
print("Total Columns:", len(df.columns))
print("Total Unique Products:", df["product_name"].nunique())


# 2. Missing Values

print("\n2. MISSING VALUES")

missing_values = df.isnull().sum()

print(missing_values)

print("Total Missing Values:", missing_values.sum())


# 3. Duplicate Records

print("\n3. DUPLICATE RECORDS")

duplicate_count = df.duplicated().sum()

print("Total Duplicate Records:", duplicate_count)


# 4. Invalid Prices

print("\n4. PRICE VALIDATION")

invalid_prices = (df["product_price"] <= 0).sum()

print("Invalid Price Records:", invalid_prices)


# 5. Invalid Ratings

print("\n5. RATING VALIDATION")

invalid_ratings = (
    (df["Rate"] < 1) | (df["Rate"] > 5)
).sum()

print("Invalid Rating Records:", invalid_ratings)

# 6. Data Quality Score

total_checks = 5

passed_checks = 0

if missing_values.sum() == 0:
    passed_checks += 1

if duplicate_count == 0:
    passed_checks += 1

if invalid_prices == 0:
    passed_checks += 1

if invalid_ratings == 0:
    passed_checks += 1

if df["product_name"].nunique() > 0:
    passed_checks += 1

quality_score = (passed_checks / total_checks) * 100

print("\n6. DATA QUALITY SCORE")

print("Passed Checks:", passed_checks, "/", total_checks)

print("Overall Quality Score:", quality_score, "%")

# 7. Save Data Quality Report

quality_report = pd.DataFrame({
    "Metric": [
        "Total Records",
        "Total Columns",
        "Unique Products",
        "Missing Values",
        "Duplicate Records",
        "Invalid Prices",
        "Invalid Ratings",
        "Passed Checks",
        "Total Checks",
        "Data Quality Score"
    ],

    "Value": [
        len(df),
        len(df.columns),
        df["product_name"].nunique(),
        missing_values.sum(),
        duplicate_count,
        invalid_prices,
        invalid_ratings,
        passed_checks,
        total_checks,
        quality_score
    ]
})

quality_report.to_csv(
    "reports/data_quality_report.csv",
    index=False
)

print("\n7. REPORT SAVED SUCCESSFULLY!")
print("File: reports/data_quality_report.csv")