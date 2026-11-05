
import streamlit as st
import pandas as pd

# 
# PAGE CONFIGURATION


st.set_page_config(
    page_title="Price Truth | Price Intelligence",
    page_icon="🛒",
    layout="wide"
)


# MAIN TITLE


st.title("🛒 Price Truth")

st.subheader("Shopping Price Intelligence Platform")

st.markdown(
    """
    Discover product prices, compare category benchmarks,
    and explore product ratings using data analytics.
    """
)

st.divider()


# LOAD PROJECT DATA


price_df = pd.read_csv(
    "reports/price_intelligence.csv"
)

review_df = pd.read_parquet(
    "data/processed/cleaned_flipkart_reviews.parquet"
)


# SIDEBAR

st.sidebar.title("Price Truth")

st.sidebar.markdown("### Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Dashboard",
        "Product Explorer",
        "Price Intelligence"
    ]
)


# DASHBOARD PAGE


if page == "Dashboard":

    st.header("Price Truth Overview")

    st.write(
        "Real-time analytics from our product review dataset."
    )

    # Calculate KPIs
    total_products = price_df["clean_product_name"].nunique()

    total_reviews = len(review_df)

    average_price = price_df["product_price"].mean()

    average_rating = review_df["Rate"].mean()

    # Display KPI Cards
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Products",
        f"{total_products:,}"
    )

    col2.metric(
        "Total Reviews",
        f"{total_reviews:,}"
    )

    col3.metric(
        "Average Price",
        f"₹{average_price:,.2f}"
    )

    col4.metric(
        "Average Rating",
        f"{average_rating:.2f} / 5"
    )

    st.divider()

    st.success("Dataset connected successfully!")

    st.header("Welcome to Price Truth")

    st.info(
        "Your shopping price intelligence dashboard "
        "is successfully running!"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Platform", "Price Truth")
    col2.metric("Analytics", "Enabled")
    col3.metric("Dashboard", "Active")


# =====================================
# PRODUCT EXPLORER PAGE
# =====================================

elif page == "Product Explorer":

    st.header("🔍 Product Explorer")

    st.write(
        "Search and explore products from our dataset."
    )

    # Search
    search = st.text_input(
        "Search Product",
        placeholder="Enter product name..."
    )

    # Filters
    col1, col2 = st.columns(2)

    categories = sorted(
        price_df["category"].dropna().unique()
    )

    brands = sorted(
        price_df["brand"].dropna().unique()
    )

    with col1:
        selected_category = st.selectbox(
            "Select Category",
            ["All Categories"] + categories
        )

    with col2:
        selected_brand = st.selectbox(
            "Select Brand",
            ["All Brands"] + brands
        )

    # Apply Filters
    filtered_df = price_df.copy()

    if search:
        filtered_df = filtered_df[
            filtered_df["clean_product_name"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    if selected_category != "All Categories":
        filtered_df = filtered_df[
            filtered_df["category"] == selected_category
        ]

    if selected_brand != "All Brands":
        filtered_df = filtered_df[
            filtered_df["brand"] == selected_brand
        ]

    # Display Columns
    display_columns = [
        "clean_product_name",
        "brand",
        "category",
        "product_price",
        "average_rating",
        "total_reviews"
    ]

    # Product Results
    st.subheader("Product Results")

    st.info(
        f"Showing {len(filtered_df)} products "
        f"out of {len(price_df)} total products."
    )

    if filtered_df.empty:

        st.warning(
            "No products found. Try changing your search or filters."
        )

    else:

        st.dataframe(
            filtered_df[display_columns],
            use_container_width=True,
            hide_index=True
        )

    # Download CSV
    csv_data = filtered_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Product Results",
        data=csv_data,
        file_name="price_truth_products.csv",
        mime="text/csv"
    )


# PRICE INTELLIGENCE PAGE

elif page == "Price Intelligence":

    st.header("💰 Price Intelligence")

    st.write(
        "Analyze product prices using category-level benchmarks."
    )

    # Price Position Summary
    price_counts = price_df["price_position"].value_counts()

    below = price_counts.get("Below Category Benchmark", 0)
    near = price_counts.get("Near Category Benchmark", 0)
    above = price_counts.get("Above Category Benchmark", 0)

    # KPI Cards
    col1, col2, col3 = st.columns(3)

    col1.metric("Below Benchmark", below)
    col2.metric("Near Benchmark", near)
    col3.metric("Above Benchmark", above)

    st.divider()

    # Price Position Chart
    st.subheader("Product Price Position Analysis")

    st.bar_chart(price_counts)

    st.divider()

    # Category Analysis
    st.subheader("Category-wise Price Analysis")

    categories = sorted(price_df["category"].dropna().unique())

    selected_category = st.selectbox(
        "Select Product Category",
        categories
    )

    category_data = price_df[
        price_df["category"] == selected_category
    ]

    st.dataframe(
        category_data[
            [
                "clean_product_name",
                "product_price",
                "category_median_price",
                "price_difference_percent",
                "price_position"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    # Download Report
    st.download_button(
        label="Download Price Intelligence Report",
        data=price_df.to_csv(index=False).encode("utf-8"),
        file_name="price_intelligence.csv",
        mime="text/csv"
    )
