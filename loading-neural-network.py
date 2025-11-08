import numpy as np
import matplotlib as plt


data = np.load("mnist_model.npz")
W1 = data["W1"]
b1 = data["b1"]
W2 = data["W2"]
b2 = data["b2"]

