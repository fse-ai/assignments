# assignment_007: Build a model and train the model for MNIST Dataset with three different activations,
# sigmoid, ReLu, and tanh using the activation functions defined in assignment_005
# Compare the training by plotting a graph for 'loss' vs 'epochs' for 3 different activations

from torchvision import transforms, datasets
from torch.utils.data import DataLoader
import torch.nn as nn
import numpy as np
from assignment_005 import sigmoid, relu, tanh


# Loading MNIST Dataset from torchvision
trainset = datasets.MNIST('', download=True, train=True, transform=transforms.ToTensor())
testset = datasets.MNIST('', download=True, train=False, transform=transforms.ToTensor())
train_loader = DataLoader(dataset=trainset, batch_size=64, shuffle=True)
test_loader = DataLoader(dataset=testset, batch_size=64, shuffle=False)

# Defining network layers
input_size = 784
hidden_size = [128, 64]
output_size = 10


# Defining the nn model
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NeuralNet, self).__init__()

        # Inputs to hidden layer linear transformation
        self.layer1 = nn.Linear(input_size, hidden_size[0])
        # Hidden layer 1 to HL2 linear transformation
        self.layer2 = nn.Linear(hidden_size[0], hidden_size[1])
        # HL2 to output linear transformation
        self.layer3 = nn.Linear(hidden_size[1], output_size)

        self.LogSoftmax = nn.LogSoftmax(dim=1)

    def forward(self, x, activation):
        # HL1 with relu activation
        out = activation(self.layer1(x))
        # HL2 with relu activation
        out = activation(self.layer2(out))
        # Output layer with LogSoftmax activation
        out = self.LogSoftmax(self.layer3(out))
        return out


model = NeuralNet(input_size, hidden_size, output_size)

# Your codes here...
# Hint:
# Loop your training over the different activations
# Store loss for epoch in arrays and plot them together
