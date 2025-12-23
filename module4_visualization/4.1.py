import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set style
sns.set_style("whitegrid")

# Sample data (larger dataset for better visualization)
np.random.seed(42)
customers = pd.DataFrame({
    'customer_id': range(1, 101),
    'age': np.random.randint(20, 70, 100),
    'total_spent': np.random.gamma(2, 50, 100),
    'num_purchases': np.random.poisson(10, 100),
    'segment': np.random.choice(['Budget', 'Standard', 'Premium'], 100, p=[0.5, 0.3, 0.2])
})

print(customers.head())

# TODO: Create a figure with 4 subplots (2 rows, 2 columns)
fig, axes = # Your code here: plt.subplots(2, 2, figsize=(12, 10))

# TODO: Plot 1 (Top-left) - Histogram of ages
# Hint: axes[0, 0].hist(data, bins=20, color='steelblue', edgecolor='black')
# Your code here

axes[0, 0].set_xlabel('Age')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].set_title('Distribution of Customer Ages')

# TODO: Plot 2 (Top-right) - Scatter plot: age vs total_spent
# Hint: axes[0, 1].scatter(x, y, alpha=0.6)
# Your code here

axes[0, 1].set_xlabel('Age')
axes[0, 1].set_ylabel('Total Spent ($)')
axes[0, 1].set_title('Age vs Total Spending')

# TODO: Plot 3 (Bottom-left) - Bar chart: average spending by segment
# First calculate the average
avg_by_segment = # Your code here: customers.groupby('segment')['total_spent'].mean()
# Then plot
# Your code here: axes[1, 0].bar(...)

axes[1, 0].set_xlabel('Customer Segment')
axes[1, 0].set_ylabel('Average Spending ($)')
axes[1, 0].set_title('Average Spending by Segment')

# TODO: Plot 4 (Bottom-right) - Box plot: purchases by segment
# Hint: customers.boxplot(column='num_purchases', by='segment', ax=axes[1, 1])
# Your code here

axes[1, 1].set_xlabel('Customer Segment')
axes[1, 1].set_ylabel('Number of Purchases')
axes[1, 1].set_title('Purchase Distribution by Segment')

plt.tight_layout()
plt.savefig('customer_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nDashboard saved as 'customer_dashboard.png'")