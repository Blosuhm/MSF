import numpy as np


def euler_method(
    initial_value,
    time_step,
    time_array,
    derivative_array,
):
    """Calculate the value of a function at each time step using Euler's method.

    Args:
        initial_value (float): The value of the function at the first time step.
        time_step (float): The time step.
        time_array (numpy.ndarray): The array of times.
        derivative_function (function): The derivative of the function.

    Returns:
        numpy.ndarray: The value of the function at each time step.
    """
    value_array = np.zeros(len(time_array))
    value_array[0] = initial_value
    for i in range(1, len(time_array)):
        value_array[i] = value_array[i - 1] + time_step * derivative_array[i - 1]
    return value_array
