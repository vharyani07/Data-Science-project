import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

transactions = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=200, freq='D'),
    'revenue': np.random.gamma(3, 1000, 200),
    'category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Books'], 200),
    'region': np.random.choice(['North', 'South', 'East', 'West'], 200)
})

transactions['month'] = transactions['date'].dt.month

print(transactions.head())

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# TODO: Plot 1 - Line plot: revenue over time
# Use seaborn lineplot
sns.lineplot(data=transactions, x='date', y='revenue', ax=axes[0, 0])

axes[0, 0].set_title('Revenue Over Time')
axes[0, 0].set_xlabel('Date')
axes[0, 0].set_ylabel('Revenue ($)')
axes[0, 0].tick_params(axis='x', rotation=45)

# TODO: Plot 2 - Violin plot: revenue by category
# Use seaborn violinplot
sns.violinplot(data=transactions, x='category', y='revenue', ax=axes[0, 1])

axes[0, 1].set_title('Revenue Distribution by Category')
axes[0, 1].set_xlabel('Category')
axes[0, 1].set_ylabel('Revenue ($}')

# TODO: Plot 3 - Heatmap: average revenue by category and region
pivot_table = transactions.pivot_table(values='revenue', index='category', columns='region', aggfunc='mean')
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='.0f', ax=axes[1, 0])

axes[1, 0].set_title('Average Revenue by Category and Region')

# TODO: Plot 4 - Count plot: transactions by region
# Use seaborn countplot
sns.countplot(data=transactions, x='region', ax=axes[1, 1])

axes[1, 1].set_title('Transaction Count by Region')
axes[1, 1].set_xlabel('Region')
axes[1, 1].set_ylabel('Count')

plt.tight_layout()
plt.savefig('statistical_viz.png', dpi=300, bbox_inches='tight')
plt.show()