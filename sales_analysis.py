# Step 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np  # For generating random data

# Step 2: Create imaginary sales data
np.random.seed(42)  # For consistent random results

# Create date range for 1 year (2023)
dates = pd.date_range(start='2023-01-01', end='2023-12-31')

# Generate imaginary data
data = {
    'Date': np.random.choice(dates, 500),
    'Product': np.random.choice(['T-Shirt', 'Jeans', 'Shoes', 'Jacket', 'Hat'], 500),
    'Units Sold': np.random.randint(1, 20, 500),
    'Unit Price': np.random.choice([15.99, 49.99, 89.99, 129.99, 24.99], 500),
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Total Sales
df['Total Sales'] = df['Units Sold'] * df['Unit Price']

# Step 3: Explore the data
print("First 5 rows:")
print(df.head())

print("\nBasic information:")
print(df.info())

print("\nDescriptive statistics:")
print(df.describe())

# Step 4: Analyze the data
# Monthly sales analysis
df['Month'] = df['Date'].dt.month_name()
monthly_sales = df.groupby('Month')['Total Sales'].sum().reset_index()

# Product performance
product_performance = df.groupby('Product').agg({
    'Units Sold': 'sum',
    'Total Sales': 'sum'
}).reset_index()

# Step 5: Visualize the results
plt.figure(figsize=(12, 6))

# Monthly sales plot
plt.subplot(1, 2, 1)
sns.lineplot(x='Month', y='Total Sales', data=monthly_sales, marker='o')
plt.title('Monthly Sales Trend')
plt.xticks(rotation=45)

# Product performance plot
plt.subplot(1, 2, 2)
sns.barplot(x='Total Sales', y='Product', data=product_performance)
plt.title('Product Sales Performance')

plt.tight_layout()
plt.savefig('sales_analysis.png')
plt.show()

# Step 6: Save cleaned data
df.to_csv('sales_data.csv', index=False)
print("\nAnalysis complete! Check sales_analysis.png and sales_data.csv")
