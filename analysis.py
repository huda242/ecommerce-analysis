import pandas as pd
import matplotlib.pyplot as plt
import os

print("Starting analysis...")

# Load CSV
df = pd.read_csv("data.csv")
print("CSV Loaded!\n")
print(df.head(), "\n")

# Create Revenue column
df['Revenue'] = df['Quantity'] * df['Amount']

# Total Revenue
print("Total Revenue:", df['Revenue'].sum(), "\n")

# Revenue by City
city_revenue = df.groupby('City')['Revenue'].sum()
print("Revenue by City:")
print(city_revenue, "\n")

# Revenue by Category
category_revenue = df.groupby('Category')['Revenue'].sum()
print("Revenue by Category:")
print(category_revenue, "\n")

# Top Customers
top_customers = df.groupby('Customer')['Revenue'].sum().sort_values(ascending=False)
print("Top Customers:")
print(top_customers, "\n")

# Monthly Revenue Trend
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
monthly_revenue = df.groupby('Month')['Revenue'].sum()
print("Monthly Revenue:")
print(monthly_revenue, "\n")

# -------------------------
# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# -------------------------
# Save charts automatically

# 1. Revenue by City
plt.figure(figsize=(6,4))
city_revenue.plot(kind='bar', color='skyblue', title='Revenue by City')
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("outputs/revenue_by_city.png")
plt.close()

# 2. Revenue by Category
plt.figure(figsize=(6,4))
category_revenue.plot(kind='bar', color='orange', title='Revenue by Category')
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("outputs/revenue_by_category.png")
plt.close()

# 3. Top Customers
plt.figure(figsize=(6,4))
top_customers.plot(kind='bar', color='green', title='Top Customers')
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("outputs/top_customers.png")
plt.close()

# 4. Monthly Revenue Trend
plt.figure(figsize=(8,4))
monthly_revenue.plot(kind='line', marker='o', color='purple', title='Monthly Revenue Trend')
plt.ylabel("Revenue")
plt.xlabel("Month")
plt.tight_layout()
plt.savefig("outputs/monthly_revenue_trend.png")
plt.close()

print("Analysis complete! All charts saved in 'outputs/' folder.")