import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
torch.manual_seed(42)

n_samples = 1000
X = np.random.randn(n_samples, 10)
y = (X[:, 0] + X[:, 1] * 2 - X[:, 2] + np.random.randn(n_samples) * 0.1).reshape(-1, 1)

X_train = torch.FloatTensor(X[:800])
y_train = torch.FloatTensor(y[:800])
X_test = torch.FloatTensor(X[800:])
y_test = torch.FloatTensor(y[800:])

class OptimizedNet(nn.Module):
    def __init__(self, input_dim, hidden_dims, output_dim, dropout_rate=0.3):
        super(OptimizedNet, self).__init__()
        # TODO: Create a flexible architecture using nn.ModuleList
        # hidden_dims is a list like [64, 32, 16]
        pass
        
    def forward(self, x):
        # TODO: Forward pass through all layers
        pass

# TODO: Create model with architecture [10, 64, 32, 16, 1]
model = # Your code here

# TODO: Try different optimizers and learning rates
criterion = nn.MSELoss()
optimizer = # Your code here (try SGD, Adam, or RMSprop)

# TODO: Implement early stopping
best_loss = float('inf')
patience = 10
patience_counter = 0

losses = []
for epoch in range(200):
    # TODO: Training step
    
    # TODO: Validation step
    
    # TODO: Early stopping logic
    
    if (epoch + 1) % 20 == 0:
        print(f'Epoch {epoch+1}, Loss: {loss.item():.4f}')

plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training with Early Stopping')
plt.show()