# POW - 10

## Create a neural network class from scratch

Create a python script to implement a basic nerual network architecture from scratch.

The `Network()` class must have:

- `__init__()` method that takes in parameters for layer configuration as an iterable (list or tuple). Randomly initialize the weights and biases using the NumPy module.

- `forward()` module that takes an input, find the weighted sum and produces the output array.

Activation functions are not required.

---

### Example output code

```python
config = (5, 6, 6, 2)
model = Network(config)
model.forward(np.array([0.1, 0.5, 0.6, -0.5, 0.8]))
```

In the above code, `config` is set as a tuple with 4 values. Let's break it down.

The first value `5` means this network should have 5 inputs. So the input layer has 5 nodes.

The last value in the `config` tuple is `2`. This means that the output layer has two classes (nodes). 

All the values in between the input layer and the output layer is our hidden layers. So here we have 2 hidden layers with 6 nodes each.

This configuration can have any  number of layers.

![network in this example](images\SimpleNetwork.gif)

**Output**

The output for the above code is a NumPy array with two values like we said in the configuration.

```python
array([[-17.03379203,   9.73953923]])
```

You can find the skeleton program in `main.py`.

---

#### Prerequisites

- NumPy
