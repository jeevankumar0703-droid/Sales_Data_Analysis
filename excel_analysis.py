import pandas as pd

# Load the Excel file
df = pd.read_excel(r"C:\Users\chris\OneDrive\Documents\Sales_Data_Analysis.xlsx")

# Display first few rows
print(df.head())

# Clean column names
df.columns = ['Salesperson', 'Revenue']

# Remove any total or NaN rows
df = df.dropna()
df = df[df['Salesperson'] != 'Grand Total']

# Convert revenue column to numeric (in case it's stored as text)
df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')

# Sort by revenue
df = df.sort_values(by='Revenue', ascending=False)

print("\n✅ Cleaned Sales Data:")
print(df)

# Display total revenue
print("\n💰 Total Revenue:", df['Revenue'].sum())


import matplotlib.pyplot as plt

# Create a bar chart of Salesperson vs Revenue
plt.figure(figsize=(8, 5))
plt.bar(df['Salesperson'], df['Revenue'], color='skyblue', edgecolor='black')

plt.title('Sales Revenue by Salesperson', fontsize=14)
plt.xlabel('Salesperson', fontsize=12)
plt.ylabel('Revenue', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()