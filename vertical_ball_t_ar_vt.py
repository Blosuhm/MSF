# Vertical throw of a ball with air resistance and terminal velocity
import numpy as np
import matplotlib.pyplot as plt
import math

# Constants
GRAVITY = 9.8
TIME_STEP = 0.01
TIME = np.arange(0, 2, TIME_STEP)
TERMINAL_VELOCITY_KMH = 100
TERMINAL_VELOCITY_MS = TERMINAL_VELOCITY_KMH / 3.6
D = GRAVITY / math.pow(TERMINAL_VELOCITY_MS, 2)
N = TIME.size
INITIAL_VELOCITY_MS = 10

# Air resistance formula -g-(m*v^2)/2


def euler_method():
    acceleration_array = np.zeros(N)

    velocity_array = np.zeros(N)
    velocity_array[0] = INITIAL_VELOCITY_MS

    position_array = np.zeros(N)
    position_array[0] = 0

    for i in range(1, N):
        abs_velocity = abs(velocity_array[i - 1])
        acceleration_array[i - 1] = -GRAVITY - D * abs_velocity * velocity_array[i - 1]
        velocity_array[i] = (
            velocity_array[i - 1] + acceleration_array[i - 1] * TIME_STEP
        )
        position_array[i] = position_array[i - 1] + velocity_array[i - 1] * TIME_STEP

    return acceleration_array, velocity_array, position_array


def graph_position(ax):
    *_, position_array = euler_method()

    ax.plot(TIME, position_array)


def graph_position_no_resistance(ax):
    ax.plot(TIME, INITIAL_VELOCITY_MS * TIME - GRAVITY / 2 * np.power(TIME, 2))


def main():
    fig, ax = plt.subplots(nrows=1, ncols=1)
    graph_position(ax)
    graph_position_no_resistance(ax)
    plt.show()


if __name__ == "__main__":
    main()
