#Data Standardization
import numpy as np

# Sample data: customer spending amounts (in dollars)
spending = np.array([50, 150, 200, 80, 500, 120, 90, 300])


# TODO: Calculate mean
mean_spending = np.mean(spending[:]) #axis=0 for each column, axis=1 for each row

# TODO: Calculate standard deviation
std_spending = np.std(spending[:])

# TODO: Standardize the data using formula: (value - mean) / std
# This transforms data to have mean=0 and std=1
standardized_spending = (spending - mean_spending) / std_spending

print(f"Original: {spending}")
print(f"Mean: {mean_spending:.2f}")
print(f"Std: {std_spending:.2f}")
print(f"Standardized: {standardized_spending}")
print(f"\nVerification:")
print(f"Mean of standardized (should be ~0): {np.mean(standardized_spending):.6f}")
print(f"Std of standardized (should be 1): {np.std(standardized_spending):.6f}")