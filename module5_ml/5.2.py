from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
X = np.random.randn(100, 5)

# TODO: Standardize the data
scaler = StandardScaler()
X_scaled = # Your code here

# TODO: Apply PCA to reduce to 2 dimensions
pca = # Your code here
X_pca = # Your code here

# TODO: Print explained variance ratio
print(f"Variance explained by each component: {pca.explained_variance_ratio_}")
print(f"Total variance explained: {sum(pca.explained_variance_ratio_):.2%}")

# TODO: Plot the 2D representation
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.6)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('PCA Visualization')
plt.grid(True, alpha=0.3)
plt.show()