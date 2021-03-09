
import assignment_006
import pytest
import numpy as np


@pytest.fixture
def prediction_input():
    prediction_input = np.array([[0.25, 0.25, 0.25, 0.25], [0.01, 0.01, 0.01, 0.96]])
    return prediction_input


@pytest.fixture
def target_input():
    target_input = np.array([[0, 0, 0, 1], [0, 0, 0, 1]])
    return target_input


def test_categorical_cross_entropy(prediction_input, target_input):
    assert assignment_006.categorical_cross_entropy(prediction_input,
                                                    target_input) == 0.7135581778200729
