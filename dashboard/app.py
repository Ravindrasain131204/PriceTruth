
import streamlit as st
import pandas as pd

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Price Truth | Price Intelligence",
    page_icon="🛒",
    layout="wide"
)

# =====================================
# PREMIUM CUSTOM CSS
# =====================================

st.markdown("""
<style>

/* Main Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0b1120, #111827, #172033);
    color: #f1f5f9;
}

/* Header */
[data-testid="stHeader"] {
    background: rgba(11, 17, 32, 0.95);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827, #0f172a);
    border-right: 1px solid #263449;
}

[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}

/* Main Content */
.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* Headings */
h1 {
    color: #f8fafc !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #5eead4 !important;
    font-weight: 700 !important;
}

/* Paragraphs */
p, label {
    color: #cbd5e1;
}

/* Metric Cards */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, #1e293b, #172554);
    border: 1px solid #334155;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25);
}

/* Metric Labels */
[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
}

/* Metric Values */
[data-testid="stMetricValue"] {
    color: #5eead4 !important;
    font-size: 30px !important;
    font-weight: 800 !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #0d9488, #2563eb);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 8px 20px;
    font-weight: 600;
}

/* Download Button */
.stDownloadButton > button {
    background: linear-gradient(90deg, #0d9488, #2563eb);
    color: white;
    border: none;
    border-radius: 10px;
}

/* DataFrames */
[data-testid="stDataFrame"] {
    border: 1px solid #334155;
    border-radius: 12px;
}

/* Dividers */
hr {
    border-color: #334155;
}

/* Alert Box */
div[data-testid="stAlert"] {
    background: linear-gradient(90deg, #172554, #1e293b) !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
}

div[data-testid="stAlert"] p {
    color: #5eead4 !important;
    font-weight: 600 !important;
}

div[data-testid="stAlert"] svg {
    fill: #5eead4 !important;
}

/* Search Input */
input {
    background-color: #1e293b !important;
    color: #ffffff !important;
    border: 1px solid #475569 !important;
    -webkit-text-fill-color: #ffffff !important;
}

/* Input Container */
div[data-baseweb="input"] {
    background-color: #1e293b !important;
}

/* Selectbox */
div[data-baseweb="select"] {
    background-color: #1e293b !important;
}

div[data-baseweb="select"] > div {
    background-color: #1e293b !important;
    border: 1px solid #475569 !important;
    border-radius: 10px !important;
}

div[data-baseweb="select"] div,
div[data-baseweb="select"] span {
    color: #ffffff !important;
}

/* Dropdown Menu */
ul[role="listbox"] {
    background-color: #1e293b !important;
}

li[role="option"] {
    background-color: #1e293b !important;
    color: white !important;
}

/* Placeholder */
input::placeholder {
    color: #94a3b8 !important;
    -webkit-text-fill-color: #94a3b8 !important;
}

/* Dropdown Popup */
[data-baseweb="popover"] {
    background-color: #111827 !important;
    border: 1px solid #334155 !important;
    border-radius: 10px !important;
}

/* Dropdown Options */
[data-baseweb="popover"] ul,
[role="listbox"] {
    background-color: #111827 !important;
}

[role="option"] {
    background-color: #111827 !important;
    color: #e2e8f0 !important;
}

/* Hover Effect */
[role="option"]:hover {
    background-color: #1e3a5f !important;
    color: #5eead4 !important;
}

/* Selected Option */
[aria-selected="true"] {
    background-color: #164e63 !important;
    color: #5eead4 !important;
}

/* Dropdown Text */
[data-baseweb="popover"] * {
    color: #e2e8f0;
}

</style>
""", unsafe_allow_html=True)


# # =====================================
# # MAIN TITLE
# # =====================================

# st.title("🛒 Price Truth")

# st.subheader("Shopping Price Intelligence Platform")

# st.markdown(
#     """
#     Discover product prices, compare category benchmarks,
#     and explore product ratings using data analytics.
#     """
# )

# st.divider()


# =====================================
# LOAD PROJECT DATA
# =====================================

price_df = pd.read_csv(
    "reports/price_intelligence.csv"
)

review_df = pd.read_parquet(
    "data/processed/cleaned_flipkart_reviews.parquet"
)


# =====================================
# SIDEBAR
# =====================================

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


# =====================================
# DASHBOARD PAGE
# =====================================

if page == "Dashboard":

    # PREMIUM HERO SECTION

   # PREMIUM HERO SECTION

    st.markdown("""
<div style="background: linear-gradient(120deg, #172554, #164e63, #0f766e);
padding: 40px; border-radius: 20px; border: 1px solid #2dd4bf;
margin-bottom: 30px; box-shadow: 0 10px 35px rgba(0,0,0,0.3);">

<div style="color: #5eead4; font-size: 13px; font-weight: bold; letter-spacing: 3px;">
SHOPPING PRICE INTELLIGENCE PLATFORM
</div>

<h1 style="color: white; font-size: 42px; margin-top: 15px; margin-bottom: 10px;">
PRICE TRUTH
</h1>

<p style="color: #e2e8f0; font-size: 18px;">
Shop Smarter. Compare Better. Know the Real Value.
</p>

<p style="color: #cbd5e1; font-size: 14px;">
Explore product pricing, category benchmarks,
customer ratings and shopping insights through data analytics.
</p>

</div>
""", unsafe_allow_html=True)

    st.header("Price Truth Overview")
    st.write(
    "Explore data-driven insights from our product review dataset."
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

    # =================================
    # TOP 10 PRODUCT CATEGORIES
    # =================================

    st.divider()

    st.subheader("📊 Top 10 Product Categories")

    category_summary = (
        price_df.groupby("category")
        .agg(
            total_products=("clean_product_name", "nunique"),
            average_price=("product_price", "mean"),
            average_rating=("average_rating", "mean")
        )
        .sort_values(
            "total_products",
            ascending=False
        )
        .head(10)
    )

    # Dark Theme Category Chart

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(12, 5))

    fig.patch.set_facecolor("#0b1120")
    ax.set_facecolor("#0b1120")

    category_summary["total_products"].plot(
        kind="bar",
        ax=ax,
        color="#14b8a6",
        width=0.65
    )

    ax.set_xlabel("Product Categories", color="#cbd5e1")
    ax.set_ylabel("Total Products", color="#cbd5e1")
    ax.set_title(
        "Product Distribution by Category",
        color="#5eead4",
        fontsize=15,
        fontweight="bold"
    )

    ax.tick_params(axis="x", colors="#cbd5e1", rotation=45)
    ax.tick_params(axis="y", colors="#cbd5e1")

    ax.grid(axis="y", linestyle="--", alpha=0.2)
    ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.tight_layout()

    st.pyplot(fig)
    plt.close(fig)

    
    st.subheader("Category Performance Details")

    display_category = category_summary.rename(
        columns={
            "total_products": "Total Products",
            "average_price": "Average Price (₹)",
            "average_rating": "Average Rating"
        }
    )
    
    display_category.index.name = "Category"
    display_category = display_category.reset_index()

    styled_category = display_category.round(2).style.set_properties(
        **{
            "background-color": "#111827",
            "color": "#e2e8f0",
            "border-color": "#334155"
        }
    ).set_table_styles([
        {
            "selector": "th",
            "props": [
                ("background-color", "#1e293b"),
                ("color", "#5eead4"),
                ("border", "1px solid #334155")
            ]
        },
        {
            "selector": "td",
            "props": [
                ("border", "1px solid #334155")
            ]
        }
    ])

    display_category.index.name = "Category"

    st.dataframe(
    styled_category,
    use_container_width=True,
    hide_index=True
)
    st.success("Dataset connected successfully!")

    st.markdown(
    """
    ### Your Shopping Intelligence Starts Here

    Explore products, analyze category benchmarks
    and discover useful insights from customer reviews.
    """
)


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

        display_df = filtered_df[display_columns]

        # Styled DataFrame
        styled_df = display_df.style.set_properties(
            **{
                "background-color": "#111827",
                "color": "#e2e8f0",
                "border-color": "#334155"
            }
        ).set_table_styles([
            {
                "selector": "th",
                "props": [
                    ("background-color", "#1e293b"),
                    ("color", "#5eead4"),
                    ("border", "1px solid #334155")
                ]
            },
            {
                "selector": "td",
                "props": [
                    ("border", "1px solid #334155")
                ]
            }
        ])

        st.dataframe(
            styled_df,
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


# =====================================
# PRICE INTELLIGENCE PAGE
# =====================================

elif page == "Price Intelligence":

    st.header("💰 Price Intelligence")

    st.write(
        "Analyze product prices using category-level benchmarks."
    )

    # =================================
    # PRICE POSITION SUMMARY
    # =================================

    price_counts = price_df["price_position"].value_counts()

    below = price_counts.get(
        "Below Category Benchmark", 0
    )

    near = price_counts.get(
        "Near Category Benchmark", 0
    )

    above = price_counts.get(
        "Above Category Benchmark", 0
    )

    # KPI Cards
    col1, col2, col3 = st.columns(3)

    col1.metric("Below Benchmark", below)

    col2.metric("Near Benchmark", near)

    col3.metric("Above Benchmark", above)

    st.divider()

    # =================================
    # PRICE POSITION CHART
    # =================================

    st.subheader("Product Price Position Analysis")

    st.bar_chart(price_counts)

    st.divider()

    # =================================
    # CATEGORY ANALYSIS
    # =================================

    st.subheader("Category-wise Price Analysis")

    categories = sorted(
        price_df["category"].dropna().unique()
    )

    selected_category = st.selectbox(
        "Select Product Category",
        categories
    )

    category_data = price_df[
        price_df["category"] == selected_category
    ]

    # Display Columns
    display_df = category_data[
        [
            "clean_product_name",
            "product_price",
            "category_median_price",
            "price_difference_percent",
            "price_position"
        ]
    ]

    # Styled DataFrame
    styled_df = display_df.style.set_properties(
        **{
            "background-color": "#111827",
            "color": "#e2e8f0",
            "border-color": "#334155"
        }
    ).set_table_styles([
        {
            "selector": "th",
            "props": [
                ("background-color", "#1e293b"),
                ("color", "#5eead4"),
                ("border", "1px solid #334155")
            ]
        },
        {
            "selector": "td",
            "props": [
                ("border", "1px solid #334155")
            ]
        }
    ])

    st.dataframe(
        styled_df,
        use_container_width=True,
        hide_index=True
    )

    # =================================
    # DOWNLOAD REPORT
    # =================================

    st.download_button(
        label="Download Price Intelligence Report",
        data=price_df.to_csv(
            index=False
        ).encode("utf-8"),
        file_name="price_intelligence.csv",
        mime="text/csv"
    )
