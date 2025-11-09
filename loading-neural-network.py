import numpy as np
from PIL import Image

# Load your trained model
data = np.load("mnist_model.npz")
W1 = data["W1"]
b1 = data["b1"]
W2 = data["W2"]
b2 = data["b2"]

# Load and preprocess image
img = Image.open("C:/Users/quick/OneDrive/Documents/Creating-A-Neural-Network-From-Scratch/testing-number-9.jpg").convert("L")
img = img.resize((28, 28))
arr = np.array(img).flatten().astype(np.float32)

# Normalize and reshape for network
X = (arr / 255.0).reshape(784, 1)

# Neural network functions
def ReLU(Z):
    return np.maximum(0, Z)

def softmax(Z):
    Z -= np.max(Z, axis=0, keepdims=True)
    expZ = np.exp(Z)
    return expZ / np.sum(expZ, axis=0, keepdims=True)

def forward_prop(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return A2

def get_predictions(A2):
    return np.argmax(A2, axis=0)

# Run prediction
A2 = forward_prop(W1, b1, W2, b2, X)
print("Predicted digit:", get_predictions(A2)[0])