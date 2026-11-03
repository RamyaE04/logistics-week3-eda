"""
Week 3: Advanced Data Analysis and Visualization in Logistics
Run: python week3_exploratory_data_analysis.py
Input: logistics_dataset.csv (same folder)
Output: visualizations/*.png and printed EDA summary
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = os.path.dirname(os.path.abspath("C://Users//Administrator//Downloads//logistics_dataset.csv"))
DATA_PATH = os.path.join(BASE_DIR, "logistics_dataset.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "visualizations")
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv("C://Users//Administrator//Downloads//logistics_dataset.csv")

print("\\n--- DATA OVERVIEW ---")
print(df.head())
print("\\nShape:", df.shape)
print("\\nData types:")
print(df.dtypes)
print("\\nMissing values:")
print(df.isnull().sum())
print("\\nDuplicate rows:", df.duplicated().sum())

numeric_df = df.select_dtypes(include="number")
print("\\n--- DESCRIPTIVE STATISTICS ---")
print(numeric_df.describe().round(2))
print("\\nMeans:")
print(numeric_df.mean().round(2))
print("\\nMedians:")
print(numeric_df.median().round(2))
print("\\nModes:")
print(numeric_df.mode().iloc[0])
print("\\nCorrelation matrix:")
print(numeric_df.corr().round(2))

# 1. Delivery-time histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Delivery_Time_days"], bins=24, edgecolor="black")
plt.title("Distribution of Delivery Time")
plt.xlabel("Delivery time (days)")
plt.ylabel("Number of shipments")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "delivery_time_analysis.png"), dpi=160)
plt.show()

# 2. Transportation-cost box plot
plt.figure(figsize=(8, 5))
plt.boxplot(df["Transportation_Cost_INR"])
plt.title("Transportation Cost Distribution")
plt.ylabel("Transportation cost (INR)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "transportation_cost.png"), dpi=160)
plt.show()

# 3. Shipment volume by warehouse
volume_by_wh = df.groupby("Warehouse")["Shipment_Volume"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
volume_by_wh.plot(kind="bar")
plt.title("Total Shipment Volume by Warehouse")
plt.xlabel("Warehouse")
plt.ylabel("Total packages")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "shipment_volume.png"), dpi=160)
plt.show()

# 4. Correlation heatmap
plt.figure(figsize=(9, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", center=0)
plt.title("Correlation Heatmap of Numerical Variables")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "correlation_heatmap.png"), dpi=160)
plt.show()

# 5. Delivery status pie chart
status_counts = df["Delivery_Status"].value_counts()
plt.figure(figsize=(7, 5))
plt.pie(status_counts.values, labels=status_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Delivery Status Share")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "delivery_status.png"), dpi=160)
plt.show()

# 6. Distance vs transportation cost scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df["Distance_km"], df["Transportation_Cost_INR"], alpha=0.55)
plt.title("Distance vs Transportation Cost")
plt.xlabel("Distance (km)")
plt.ylabel("Transportation cost (INR)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "distance_vs_cost.png"), dpi=160)
plt.show()

print("\\nCharts saved in:", OUTPUT_DIR)
print("Delayed shipment percentage: {:.1f}%".format(
    (df["Delivery_Status"].eq("Delayed").mean()) * 100))
print("Average delivery time: {:.2f} days".format(df["Delivery_Time_days"].mean()))
print("Distance-cost correlation: {:.2f}".format(
    df["Distance_km"].corr(df["Transportation_Cost_INR"])))
print("\\nEDA completed successfully.")
