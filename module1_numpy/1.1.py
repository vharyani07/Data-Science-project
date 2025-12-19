import numpy as np

# Create data for 5 customers: [age, num_purchases, total_spent]
customer_data = np.array([
    [25, 10, 500],
    [35, 15, 750],
    [45, 5, 200],
    [30, 20, 1000],
    [50, 8, 400]
])

# Your tasks:
# 1. Calculate mean age
# 2. Find total spending across all customers
# 3. Find which customer (row index) spent the most

print("Customer data shape:", customer_data.shape)
# Now you try the calculations!
mean_age = np.mean(customer_data[:, 0])
total_spending = np.sum(customer_data[:, 2])
max_spender_index = np.argmax(customer_data[:, 2])


print("Mean age:", mean_age)
print("Total spending:", total_spending)
print("Customer who spent the most:", max_spender_index)
