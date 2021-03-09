# assignment_003: MultiLayer Percepton for XOR Gate

The task is to design a multilayer perceptron for solving XOR from scratch with hard coded parameters(weights and biases) with both numpy(task1) and pytorch(task2).

![](https://github.com/hanoonaR/fseai_image_collection/blob/master/Mod%202up-10q.jpg)

We can represent XOR as a combination of other logical gates which are linearly solvable. Therefore, XOR can be represented by a multilayer perceptron.

<img src="https://latex.codecogs.com/svg.latex?\Large&space;XOR(x1,x2)=AND(NOT(AND(x1,x2))),OR(x1,x2))" title="XOR equation" />

![](https://github.com/hanoonaR/fseai_image_collection/blob/master/Mod%202-11.jpg)

The architecture of the model will have 1 hidden layer, with 2 units for representing the OR gate and the NAND gate. The output layer is represents an AND gate combining the outputs
of the OR and the NAND from the previous layer.

![](https://github.com/hanoonaR/fseai_image_collection/blob/master/Mod%202-122.jpg)

## Prerequisites:
1. Python, NumPy
2. Pytorch Basics
3. Perceptrons and Multilayer Perceptron
