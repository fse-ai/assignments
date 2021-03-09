# assignment_005: Activation Functions
Activation functions are mathematical equations that determine the output of a neural network. The function is attached to each neuron in the network, and determines whether it 
should be activated, 'fired' or not, based on whether each neuron’s input is relevant for the model’s prediction. The task is to build the following activation function from 
scratch using pytorch tensors.

## 1. Sigmoid
The Sigmoid Function curve looks like a S-shape takes a real value as input and outputs another value between 0 and 1.. Models where we have to predict the probability as an output use this activation function 
since probability of anything exists only between the range of 0 and 1. It’s easy to work with and has all the nice properties of activation functions: it’s non-linear, continuously differentiable, monotonic, and has a fixed output range.

<img src="https://latex.codecogs.com/svg.latex?\Large&space;f(x)=\frac{1}{1+e^{-x}}" title="sigmoid equation" />

![](https://github.com/hanoonaR/fseai_image_collection/blob/master/sigmoid.JPG)

## 2. Tanh
Tanh squashes a real-valued number to the range [-1, 1]. It’s non-linear. But unlike Sigmoid, its output is zero-centered. The advantage is that the negative inputs will be mapped strongly negative and the zero inputs will be mapped near zero in the tanh 
graph.

<img src="https://latex.codecogs.com/svg.latex?\Large&space;f(x)=\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}" title="tanh equation" />

![](https://github.com/hanoonaR/fseai_image_collection/blob/master/tanh.JPG)

The image below shows a comparison between the sigmoid and the Tanh function.

![](https://github.com/hanoonaR/fseai_image_collection/blob/master/sigmod_vs_tanh.JPG)

## 3. ReLu
The Rectified Linear Unit activation function is simple and can be expressed as 
<img src="https://latex.codecogs.com/svg.latex?\Large&space;f(x)=max(o,x)" title="relu equation" />. 

Despite its name and appearance, it’s not linear. A ReLU has output 0 if the input is less than 0, and raw output otherwise. That is, if the input is greater than 0, the output is equal to the input.

![](https://github.com/hanoonaR/fseai_image_collection/blob/master/relu.JPG)

## 4. Softmax
Softmax function calculates the probabilities distribution of the event over ‘n’ different events. In general way of saying, this function will calculate the probabilities of 
each target class over all possible target classes. Later the calculated probabilities will be helpful for determining the target class for the given inputs.

<img src="https://latex.codecogs.com/svg.latex?\Large&space;f(x_{j})=\frac{e^{x_{j}}}{\sum_{k=1}^{K}{e^{x_{k}}}" title="relu equation" />. 

## Prerequisites:
1. Python, Pytorch
2. Neural Network Architecture
3. Forward Pass and Activation functions
