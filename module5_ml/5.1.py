import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

np.random.seed(42)
n_customers = 200

group1 = np.random.normal(loc=[25, 100], scale=[5, 20], size=(60, 2))
group2 = np.random.normal(loc=[45, 500], scale=[7, 100], size=(80, 2))
group3 = np.random.normal(loc=[60, 1000], scale=[8, 150], size=(60, 2))

X = np.vstack([group1, group2, group3])
customers = pd.DataFrame(X, columns=['age', 'total_spent'])

# TODO: Standardize the data
scaler = StandardScaler()
X_scaled = # Your code here

# TODO: Apply K-Means with k=3
kmeans = # Your code here
labels = # Your code here

# TODO: Add cluster labels to DataFrame
customers['cluster'] = labels

# TODO: Calculate mean values per cluster
cluster_summary = # Your code here

print(cluster_summary)

# TODO: Create a scatter plot colored by cluster
plt.scatter(customers['age'], customers['total_spent'], c=customers['cluster'], cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Total Spent')
plt.title('Customer Segments')
plt.colorbar(label='Cluster')
plt.show()