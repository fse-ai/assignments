#assignment_005:Build activation function from scratch using pytorch tensors.

#Define function for the following activations:
# 1. Sigmoid
# 2. ReLu
# 3. Tanh
# 4. Softmax

import torch


def sigmoid(x):
    return 1/(1 + torch.exp(-x))

def relu(X):
    X[X < 0] = 0
    return X

def softmax(X):
    expo = torch.exp(X)
    expo_sum = torch.sum(torch.exp(X))
    return expo/expo_sum

def tanh(X):
    return (1 - torch.square(X))