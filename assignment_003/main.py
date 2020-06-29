# assignment_003: Design a multilayer perceptron for solving XOR from scratch with
# hard coded parameters with both numpy(task1) and pytorch(task2).

# Task 1: Define function network_numpy() for computing XOR as multilayer perceptron with numpy
import numpy as np

# Your codes here..
# Define the data set XOR
# X = array of shape 4 x 3
# Y = array of shape 4 x 1

# Define weights for each layer OR, NAND and AND
# Each weights are array of shape 1 x 3


# Your function here..
def network_numpy(x):
    '''
    Computing XOR as multilayer perceptron with numpy
    :param x: Inputs are numpy arrays [0, 0], [0, 1], [1, 0],and [1, 1]
    :return: y result of XOR on x
    '''
    # your code here...
    # Your output as type int
    return y

# Task 2: Define function network_torch() for computing XOR as multilayer perceptron with Pytorch
import torch

# Your codes here..

import torch

# Your function here..
def network_torch(x):
    '''
    Computing XOR as multilayer perceptron with Pytorch
    :param x: Inputs are torch Tensors [0, 0], [0, 1], [1, 0],and [1, 1]
    :return: y result of XOR on x
    '''
    # your code here...
    # Your output as type int
    return y
