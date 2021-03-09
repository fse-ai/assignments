import assignment_005
import torch
import pytest
from numpy.testing import assert_array_equal

@pytest.fixture
def tensor_input():
    torch.random.manual_seed(9)
    tensor_input = (10 - (-10)) * torch.rand((2, 5)) + (-10)
    return tensor_input


@pytest.fixture
def sigmoid_out():
    sigmoid_out = torch.load('sigmoid_test.pt')
    return sigmoid_out


@pytest.fixture
def relu_out():
    relu_out = torch.load('relu_test.pt')
    return relu_out


@pytest.fixture
def tanh_out():
    tanh_out = torch.load('tanh_test.pt')
    return tanh_out


@pytest.fixture
def softmax_out():
    softmax_out = torch.load('softmax_test.pt')
    return softmax_out


def test_sigmoid(tensor_input, sigmoid_out):
    out = assignment_005.sigmoid(tensor_input)
    assert_array_equal(out.numpy(), sigmoid_out.numpy())


def test_relu(tensor_input, relu_out):
    out = assignment_005.relu(tensor_input)
    assert_array_equal(out.numpy(), relu_out.numpy())
    #assert torch.all(torch.eq(out, relu_out))


def test_tanh(tensor_input, tanh_out):
    out = assignment_005.tanh(tensor_input)
    assert_array_equal(out.numpy(), tanh_out.numpy())


def test_softmax(tensor_input, softmax_out):
    out = assignment_005.softmax(tensor_input)
    assert_array_equal(out.numpy(), softmax_out.numpy())

