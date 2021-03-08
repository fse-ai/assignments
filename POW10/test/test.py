import network
import pytest
import numpy as np


@pytest.fixture
def network_initialization():
	num_of_inputs = 2
	CONFIG = (8, 6, 5, 3)
	return [num_of_inputs, CONFIG]

def test_output(network_initialization):
	num_of_inputs = network_initialization[0]
	CONFIG = network_initialization[1]
	model = network.Network(CONFIG)
	network_output = model.forward(np.random.rand(num_of_inputs, CONFIG[0]))
	assert np.array(network_output).shape == (num_of_inputs, 1, CONFIG[-1])

def test_weights(network_initialization):
	CONFIG = network_initialization[1]
	model = network.Network(CONFIG)
	k = 0
	for i in model.weights:
		assert (np.array(i, dtype=np.float32).shape) == tuple((CONFIG[k+1], CONFIG[k]))
		k += 1

def test_biases(network_initialization):
	CONFIG = network_initialization[1]
	model = network.Network(CONFIG)
	k = 0
	for i in model.biases:
		assert (np.array(i, dtype=np.float32).shape) == tuple((1, CONFIG[k+1]))
		k += 1
