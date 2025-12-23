import sqlite3
import pandas as pd

# Create sample data (you're already good at this!)
customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'age': [25, 35, 45, 30, 50],
    'city': ['NYC', 'LA', 'NYC', 'Chicago', 'LA']
})

orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105, 106],
    'customer_id': [1, 2, 1, 3, 2, 5],
    'amount': [100, 200, 150, 300, 250, 400],
    'date': ['2024-01-01', '2024-01-02', '2024-01-03', 
             '2024-01-04', '2024-01-05', '2024-01-06']
})

# TODO: Create an in-memory database
conn = sqlite3.connect(':memory:')

# TODO: Write both DataFrames to SQL tables
# Hint: customers.to_sql('table_name', conn, if_exists='replace', index=False)
# Your code here
customers.to_sql('customers', conn, if_exists='replace', index=False)
orders.to_sql('orders', conn, if_exists='replace', index=False)


# TODO: Write a SQL query to find total order amount per customer
query = """
SELECT customer_id, SUM(amount) as total_amount
FROM orders
GROUP BY customer_id
ORDER BY total_amount DESC
"""

result = pd.read_sql_query(query, conn)

print("Total orders per customer:")
print(result)
print("\n" + "="*50 + "\n")

# TODO: Write a JOIN query to get customer names with their total orders
join_query = """
SELECT c.name, c.city, o.total_amount as total_spent
FROM customers as c
JOIN (
    SELECT customer_id, SUM(amount) as total_amount
    FROM orders
    GROUP BY customer_id 
) AS o ON c.customer_id = o.customer_id
ORDER BY total_spent DESC    
"""

final = pd.read_sql_query(join_query, conn)

print("Customer names with total spending:")
print(final)

conn.close()