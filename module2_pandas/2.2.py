import pandas as pd

# Customer data
customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'city': ['NYC', 'LA', 'NYC', 'Chicago', 'LA']
})

# Transaction data
transactions = pd.DataFrame({
    'transaction_id': [101, 102, 103, 104, 105, 106, 107],
    'customer_id': [1, 2, 1, 3, 2, 5, 1],
    'amount': [50, 100, 75, 200, 150, 300, 125]
})

print("Customers:")
print(customers)
print("\nTransactions:")
print(transactions)
print("\n" + "="*50 + "\n")

# TODO: Merge the two DataFrames on customer_id
# Hint: pd.merge(df1, df2, on='column_name')
merged = pd.merge(customers, transactions, on = 'customer_id')

print("Merged data:")
print(merged)
print("\n" + "="*50 + "\n")

# TODO: Calculate total spending per customer
# Hint: Group by customer_id and sum the amounts
total_per_customer = merged.groupby('customer_id')['amount'].sum()

print("Total spending per customer:")
print(total_per_customer)
print("\n" + "="*50 + "\n")

# TODO: Join this back to customers to show name with total spending
# Hint: Merge customers with your total_per_customer result
final_result = pd.merge(customers, total_per_customer, on = 'customer_id')

print("Customer names with total spending:")
print(final_result)