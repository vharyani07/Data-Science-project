from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
n_customers = 300

X = np.random.randn(n_customers, 4)
X[:100] += [2, 2, 0, 0]
X[100:200] += [-2, -2, 0, 0]
X[200:] += [0, 0, 2, -2]

# TODO: Standardize the data
scaler = StandardScaler()
X_scaled = # Your code here

# TODO: Calculate inertia for different k values (2 to 10)
inertias = []
K_range = range(2, 11)

for k in K_range:
    # Your code here: create kmeans, fit, append inertia
    pass

# TODO: Plot the elbow curve
plt.plot(K_range, inertias, 'bo-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal k')
plt.grid(True, alpha=0.3)
plt.show()

# TODO: Based on the elbow, choose optimal k and cluster the data
optimal_k = # Your choice based on the plot
kmeans_final = # Your code here
labels = # Your code here

print(f"Optimal k: {optimal_k}")
print(f"Cluster sizes: {np.bincount(labels)}")