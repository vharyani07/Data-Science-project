import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
torch.manual_seed(42)

n_samples = 800
X = np.random.randn(n_samples, 6)
y = (X[:, 0] * 2 + X[:, 1] ** 2 + np.sin(X[:, 2]) * 3 + 
     X[:, 3] * X[:, 4] + np.random.randn(n_samples) * 0.5).reshape(-1, 1)

X_train = torch.FloatTensor(X[:600])
y_train = torch.FloatTensor(y[:600])
X_test = torch.FloatTensor(X[600:])
y_test = torch.FloatTensor(y[600:])

y_mean = y_train.mean()
y_std = y_train.std()
y_train = (y_train - y_mean) / y_std
y_test = (y_test - y_mean) / y_std

# TODO: Define a deeper neural network
class DeepPredictor(nn.Module):
    def __init__(self):
        super(DeepPredictor, self).__init__()
        # TODO: Define layers (input=6, hidden1=32, hidden2=16, hidden3=8, output=1)
        # TODO: Add dropout layers (0.2 dropout rate)
        
    def forward(self, x):
        # TODO: Define forward pass with ReLU and dropout
        pass

# TODO: Create model, loss, optimizer
model = # Your code here
criterion = # Your code here
optimizer = # Your code here (Adam, lr=0.001)

# TODO: Training loop (100 epochs)
train_losses = []
test_losses = []

for epoch in range(100):
    # TODO: Training step
    
    # TODO: Evaluation step (no gradient calculation)
    model.eval()
    with torch.no_grad():
        # Your code here
        pass
    model.train()
    
    if (epoch + 1) % 20 == 0:
        print(f'Epoch {epoch+1}, Train Loss: {train_loss:.4f}, Test Loss: {test_loss:.4f}')

# TODO: Calculate R² score on test set
model.eval()
with torch.no_grad():
    predictions = model(X_test)
    ss_res = torch.sum((y_test - predictions) ** 2)
    ss_tot = torch.sum((y_test - y_test.mean()) ** 2)
    r2_score = # Your code here

print(f"\nR² Score: {r2_score:.4f}")

plt.plot(train_losses, label='Train Loss')
plt.plot(test_losses, label='Test Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training vs Test Loss')
plt.legend()
plt.show()