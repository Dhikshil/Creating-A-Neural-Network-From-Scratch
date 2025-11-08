import numpy as np
import matplotlib as plt


data = np.load("mnist_model.npz")
W1 = data["W1"]
b1 = data["b1"]
W2 = data["W2"]
b2 = data["b2"]

images = np.loadtxt("image.csv", delimiter=",")
images = images.T
images = images / 255.0

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
    return Z1, A1, Z2, A2

def get_predictions(A2):
    return np.argmax(A2, axis=0)

Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, images)
print("Predicted digits:", get_predictions(A2))

def show_image(img_vec):
    img = img_vec.reshape(28, 28) * 255
    plt.imshow(img, cmap="gray")
    plt.axis("off")
    plt.show()

