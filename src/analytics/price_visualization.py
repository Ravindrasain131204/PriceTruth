import pandas as pd
import matplotlib.pyplot as plt

# Load Price Intelligence Report
df = pd.read_csv("reports/price_intelligence.csv")

# Count Price Positions
price_counts = df["price_position"].value_counts()

# Create Bar Chart
plt.figure(figsize=(10, 6))

price_counts.plot(
    kind="bar",
    edgecolor="black"
)

plt.title("Product Price Position Analysis")
plt.xlabel("Price Position")
plt.ylabel("Number of Products")

plt.xticks(rotation=15)
plt.tight_layout()

# Save Chart
plt.savefig("reports/price_position_analysis.png", dpi=300)

plt.show()

print("Price Visualization Created Successfully!")