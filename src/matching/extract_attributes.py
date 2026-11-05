import pandas as pd
import re

# Load cleaned dataset
df = pd.read_parquet(
    "data/processed/cleaned_flipkart_reviews.parquet"
)

# Get unique product names
products = (
    df["product_name"]
    .drop_duplicates()
    .reset_index(drop=True)
)

# Display all products
print("Total Unique Products:", len(products))

print("\nALL PRODUCT NAMES:\n")

for index, product in enumerate(products, start=1):
    print(f"{index}. {product}")



# Clean product names for attribute extraction
df["clean_product_name"] = (
    df["product_name"]
    .str.replace(r"\?+", " ", regex=True)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)


# Initial brand dictionary
brands = [
    "MAHARAJA WHITELINE",
    "Voltas Beko",
    "D&V ENGINEERING",
    "Flipkart SmartBuy",
    "the indian casa",
    "SQUARO ONLINE STORE",
    "F FERONS",
    "SportSoul",
    "ArrowMax",
    "OnePlus",
    "ZEBRONICS",
    "Crompton",
    "Hindware",
    "Eurodomo",
    "MOTOROLA",
    "SAMSUNG",
    "Siemens",
    "BLUECHIP",
    "Supreme Bazaar",
    "Value Adds",
    "Nextron",
    "WONDERCHEF",
    "Prestige",
    "Butterfly",
    "Seagate",
    "LUMINOUS",
    "Atomberg",
    "BAJAJ",
    "Inalsa",
    "HAVELLS",
    "PHILIPS",
    "Google",
    "VARDHMAN",
    "PRAGATI TRENDS",
    "Fashion Tree",
    "The Sharp Club",
    "Candes",
    "boAt",
    "Aroma",
    "Mivi",
    "Canon",
    "Faber",
    "Glen",
    "CEAT",
    "MRF",
    "VICTORY",
    "Rixen",
    "LURAGS",
    "IFB",
    "Midea",
    "BOSCH",
    "Hafele",
    "DALUCI",
    "Tata Sky",
    "Airtel",
    "7SEVEN",
    "Pigeon",
    "WD",
    "BAJAJ",
    "USHA",
    "KENT",
    "Joker",
    "Ozarro",
    "SSWW",
    "STYLERA",
    "AdroitZ",
    "Birdie",
    "Lakm",
    "etmax",
    "I Kall",
    "Sulfur Best Buy",
    "Whirlpool",
    "LG",
    "CHARDI KALA",
    "Adonai",
    "PUHBRHY",
    "Wishpool",
    "Glun",
    "konvio neer",
    "Qiisx",
    "kay1steel",
    "YUV",
    "F8WARES",
]

# Remove duplicate brand entries
brands = list(dict.fromkeys(brands))

# Match brand at the beginning of product name
brands_sorted = sorted(brands, key=len, reverse=True)

def extract_brand(product_name):
    product_name = str(product_name).strip()

    # Special case: MRF product with HF prefix
    if product_name.lower().startswith("hf mrf "):
        return "MRF"

    for brand in brands_sorted:
        if product_name.lower().startswith(brand.lower()):
            return brand

    return "Unknown"


# Extract brands
df["brand"] = df["clean_product_name"].apply(extract_brand)

print("\nBrand Extraction Results:")

print(
    df[["clean_product_name", "brand"]]
    .drop_duplicates()
    .head(30)
    .to_string(index=False)
)

print("\nBrand-wise Product Count:")

print(
    df[["clean_product_name", "brand"]]
    .drop_duplicates()["brand"]
    .value_counts()
)

print("\nProducts with Unknown Brand:")

unknown_products = df[
    df["brand"] == "Unknown"
]["clean_product_name"].drop_duplicates()

print(unknown_products.to_string(index=False))

# Product Category Extraction

def extract_category(product_name):
    name = str(product_name).lower()

    category_rules = [
        ("Air Cooler", ["air cooler"]),
       ("Headphones", ["headphone", "headset", "earphone", "earbud", "neckband"]),
        ("Speaker", ["speaker", "soundbar", "home theatre"]),
        ("Camera", ["camera", "dslr"]),
        ("Kitchen Chimney", ["chimney"]),
        ("Dishwasher", ["dishwasher"]),
        ("Voltage Stabilizer", ["stabilizer"]),
        ("Cricket Equipment", ["cricket bat", "cricket ball", "cricket", "stumps"]),
        ("Electric Kettle", ["electric kettle", "kettle"]),
        ("Rice Cooker", ["rice cooker"]),
        ("Pressure Cooker", ["pressure cooker"]),
        ("External Hard Drive", ["hard disk", "hard drive"]),
        ("Ceiling Fan", ["ceiling fan"]),
        ("Exhaust Fan", ["exhaust fan"]),
        ("Food Processor", ["food processor"]),
        ("LED Bulb", ["bulb", "led light"]),
        ("Wall Shelf", ["wall shelf"]),
        ("Remote Control", ["remote control"]),
        ("Lab Coat", ["lab coat"]),
        ("Safety Shoes", ["safety shoe", "steel toe shoe", "safety footwear"]),
        ("Gloves", ["gloves"]),
        ("TDS Meter", ["tds meter"]),
        ("Enema Kit", ["enema kit"]),
        ("Kajal", ["kajal"]),
        ("Fitness Accessories", ["wrist support", "abdomen support"]),
        ("Velcro Tape", ["velcro tape"]),
        ("Protective Goggles", ["safety goggle", "motorcycle goggles", "riding goggles"]),
    ]

    for category, keywords in category_rules:
        for keyword in keywords:
            if keyword in name:
                return category

    return "Unknown"


df["category"] = df["clean_product_name"].apply(extract_category)

 
 # Extract Product Capacity

def extract_capacity(product_name):

    name = str(product_name)

    pattern = r'\b\d+(?:\s*-\s*\d+)?(?:\.\d+)?\s?(?:LITRE|LITER|ML|KG|G|TB|GB|MB|TON|L)\b'

    match = re.search(pattern, name, re.IGNORECASE)

    if match:
        return match.group().strip()

    return "Not Specified"

# Extract Product Wattage

def extract_wattage(product_name):
    name = str(product_name)

    pattern = r'\b\d+(?:\.\d+)?\s?W\b'

    match = re.search(pattern, name, re.IGNORECASE)

    if match:
        return match.group().strip()

    return "Not Specified"

df["capacity"] = df["clean_product_name"].apply(extract_capacity)
df["wattage"] = df["clean_product_name"].apply(extract_wattage)

print("\nWattage Extraction Results:")
print(
    df[["clean_product_name", "wattage"]]
    .drop_duplicates()
    .head(30)
    .to_string(index=False)
)

print("\nCapacity Extraction Results:")

print(
    df[["clean_product_name", "capacity"]]
    .drop_duplicates()
    .head(30)
    .to_string(index=False)
)

print("\nCategory Extraction Results:")

print(
    df[["clean_product_name", "category"]]
    .drop_duplicates()
    .head(30)
    .to_string(index=False)
)


print("\nCategory-wise Product Count:")

print(
    df[["clean_product_name", "category"]]
    .drop_duplicates()["category"]
    .value_counts()
)


print("\nProducts with Unknown Category:")

unknown_categories = df[
    df["category"] == "Unknown"
]["clean_product_name"].drop_duplicates()

print(unknown_categories.to_string(index=False))



# Create Product Catalog

product_catalog = (
    df[["clean_product_name", "brand", "category", "capacity", "wattage"]]
    .drop_duplicates()
    .sort_values("clean_product_name")
)

product_catalog.to_csv(
    "reports/product_catalog.csv",
    index=False
)

print("\nProduct Catalog Created Successfully!")
print("Total Products:", len(product_catalog))