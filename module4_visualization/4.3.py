import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)

sales_data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'sales_2023': np.random.randint(50000, 150000, 12),
    'sales_2024': np.random.randint(60000, 180000, 12),
    'target': [100000] * 12
})

fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# TODO: Plot 1 - Multi-line plot with legend
# Plot sales_2023, sales_2024, and target on the same axis
x = np.arange(len(sales_data['month']))

axes[0].plot(x, sales_data['sales_2023'], label='2023')
axes[0].plot(x, sales_data['sales_2024'], label='2024')
axes[0].plot(x, sales_data['target'], label='Target')

axes[0].set_xlabel('Month', fontsize=12)
axes[0].set_ylabel('Sales ($)', fontsize=12)
axes[0].set_title('Sales Comparison: 2023 vs 2024', fontsize=14, fontweight='bold')
axes[0].set_xticks(x)
axes[0].set_xticklabels(sales_data['month'])
axes[0].legend(loc='upper left')
axes[0].grid(True, alpha=0.3, linestyle='--')

# TODO: Plot 2 - Grouped bar chart
width = 0.35
axes[1].bar(x - width/2, sales_data['sales_2023'], width, label='2023')
axes[1].bar(x + width/2, sales_data['sales_2024'], width, label='2024')

axes[1].set_xlabel('Month', fontsize=12)
axes[1].set_ylabel('Sales ($)', fontsize=12)
axes[1].set_title('Monthly Sales Breakdown', fontsize=14, fontweight='bold')
axes[1].set_xticks(x)
axes[1].set_xticklabels(sales_data['month'])
axes[1].legend()
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('advanced_plots.png', dpi=300, bbox_inches='tight')
plt.show()

# TODO: Calculate and print year-over-year growth
growth = sales_data['sales_2024'].mean() / sales_data['sales_2023'].mean() - 1
print("\nYear-over-Year Growth:")
print(growth)