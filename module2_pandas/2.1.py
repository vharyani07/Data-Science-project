#Pandas
import pandas as pd
import numpy as np

# TODO: Create a DataFrame with 10 customers
# Columns: customer_id, name, age, city, total_purchases

np.random.seed(42)  # For reproducibility

customers = pd.DataFrame({
    'customer_id': range(1, 11),
    'name': ["Liam", "Sophia", "Ethan", "Olivia", "Noah", "Ava", "Mason", "Isabella", "Lucas", "Mia"],
    'age': np.random.randint(20, 60, 10),
    'city': np.random.choice(['NYC', 'LA', 'Chicago', 'SF', 'Dallas'], 10),
    'total_purchases': np.random.randint(0, 1000, 10)
})

print(customers)

# TODO: Find customers with more than $500 in purchases
high_value = customers[customers['total_purchases'] > 500]

# TODO: Calculate average age by city
avg_age_by_city = customers.groupby('city')['age'].mean()

# TODO: Add a new column 'age_group' that categorizes:
# 'Young' if age < 30, 'Middle' if 30-50, 'Senior' if > 50
# Hint: You can use a function with .apply() or np.where()

def categorize_age(age):
    if age < 30:
        return 'Young'
    elif age < 50:
        return 'Middle'
    else:
        return 'Senior'
    pass

customers['age_group'] = customers['age'].apply(categorize_age)

print("\n" + "="*50)
print("High value customers (>$500):")
print(high_value)
print("\n" + "="*50)
print("Average age by city:")
print(avg_age_by_city)
print("\n" + "="*50)
print("Customers with age groups:")
print(customers)
