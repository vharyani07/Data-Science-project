import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
torch.manual_seed(42)

n_samples = 500
age = np.random.randint(20, 70, n_samples)
purchases = np.random.randint(1, 50, n_samples)
total_spent = age * 5 + purchases * 20 + np.random.randn(n_samples) * 50

X = np.column_stack([age, purchases])
y = total_spent.reshape(-1, 1)

X_train = torch.FloatTensor(X[:400])
y_train = torch.FloatTensor(y[:400])
X_test = torch.FloatTensor(X[400:])
y_test = torch.FloatTensor(y[400:])

# TODO: Define a neural network class
class SpendingPredictor(nn.Module):
    def __init__(self):
        super(SpendingPredictor, self).__init__()
        # TODO: Define layers (input=2, hidden=16, output=1)
        
    def forward(self, x):
        # TODO: Define forward pass with ReLU activation
        pass

# TODO: Create model, loss function, and optimizer
model = # Your code here
criterion = # Your code here (MSELoss)
optimizer = # Your code here (Adam, lr=0.01)

# TODO: Training loop (50 epochs)
losses = []
for epoch in range(50):
    # Your training code here
    pass
    
    if (epoch + 1) % 10 == 0:
        print(f'Epoch {epoch+1}, Loss: {loss.item():.4f}')

# TODO: Make predictions on test set
model.eval()
with torch.no_grad():
    predictions = # Your code here

# TODO: Calculate test MSE
test_loss = # Your code here

print(f"\nTest Loss: {test_loss:.4f}")

plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.show()