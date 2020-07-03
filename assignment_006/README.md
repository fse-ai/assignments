# assignment_006:Categorical Cross EntropynLoss

The task is to build a function for computing the Cross Entroy for a multi class classification problem from Scratch using numpy. 


The Categorical CRoss Entropy is a special case of the Cross Entropy Loss used for Multiclass classification. It is also called as the Softmax Loss as it is a Softmax activation plus a Cross-Entropy loss. If we use this loss, we will train a CNN to output a probability over the C classes for each image.
Note that here the the labels are one-hot encoded vectors. It can be expressed as:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;CE=\sum_{i=1}^{C}{t_{i}y_{i}}" title="equation" />
<img src="https://latex.codecogs.com/svg.latex?\Large&space;y_{i}=f(x_{i})=\frac{e^{x_{i}}}{\sum_{k=1}^{K}{e^{x_{k}}}" title="y equation" />. 


This loss is a very good measure of how distinguishable two discrete probability distributions are from each other. Note that ti is the one hot encoded target and yi is the output which is a sigmoid function. The minus sign in CE 
ensures that the loss gets smaller when the distributions get closer to each other.

## Prerequisites:
1. Python, NumPy
2. Training Neural Network Models
3. Loss Function
