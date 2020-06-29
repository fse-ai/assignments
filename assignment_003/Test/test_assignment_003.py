
import assignment_003
import pytest
import numpy as np
import torch


@pytest.mark.parametrize("x, y", [([0, 0], 0), ([1, 1], 0), ([0, 1], 1), ([1, 0], 1)])
def test_network(x, y):
    assert assignment_003.network_numpy(x) == y


@pytest.mark.parametrize("x, y", [(torch.Tensor([0, 0]), 0), (torch.Tensor([1, 1]), 0),
                                  (torch.Tensor([0, 1]), 1), (torch.Tensor([1, 0]), 1)])
def test_network(x, y):
    assert assignment_003.network_torch(x) == y
