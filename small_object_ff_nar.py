# Euler's method for free fall without air resistance
from modules.euler_method import euler_method
import numpy as np
import matplotlib.pyplot as plt

# Constants
GRAVITY = 9.8
TIME_STEP = 0.00001
TIME = np.arange(0, 4, TIME_STEP)

ARRAY_TIME_STEPS = np.array([0.01, 0.005, 0.001, 0.0005, 0.0001, 0.00005, 0.00001])
# copilot im sry but i need u to calculate the position at 2 seconds of the falling object for this values, subtract from the real value(19.6) and plot the error vs time step


def get_error_array():
    error_array = np.zeros(ARRAY_TIME_STEPS.size)
    for i in range(ARRAY_TIME_STEPS.size):
        time_step = ARRAY_TIME_STEPS[i]
        time = np.arange(0, 4, time_step)
        array_velocity = euler_method(0, time_step, time, GRAVITY * np.ones(time.size))
        array_position = euler_method(0, time_step, time, array_velocity)
        error_array[i] = abs(array_position[get_time_index(2, time_step)] - 19.6)
    return error_array


# Functions
def get_velocity():
    array_velocity = euler_method(0, TIME_STEP, TIME, GRAVITY * np.ones(TIME.size))
    return array_velocity


def get_position():
    new_time = np.arange(0, 3, TIME_STEP)
    array_velocity = get_velocity()
    array_position = euler_method(0, TIME_STEP, new_time, array_velocity)
    return array_position


def get_time_index(time, time_step=TIME_STEP):
    return int((time) / time_step) + 1


def main():
    array_velocity = get_velocity()
    print(array_velocity[get_time_index(3)])
    array_position = get_position()
    print(array_position[get_time_index(2)])
    print(get_error_array())
    print(ARRAY_TIME_STEPS)
    plt.plot(ARRAY_TIME_STEPS, get_error_array(), "o")
    plt.show()


if __name__ == "__main__":
    main()
