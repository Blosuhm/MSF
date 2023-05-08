import numpy as np
import matplotlib.pyplot as plt


# Constants
GRAVITY_MS2 = 9.8
TERMINAL_VELOCITY_MS = 20

# Initial conditions
x0 = 0
y0 = 2

initial_velocity_ms = 15
angle_degrees = 30
initial_velocity_x_ms = initial_velocity_ms * np.cos(np.deg2rad(angle_degrees))
initial_velocity_y_ms = initial_velocity_ms * np.sin(np.deg2rad(angle_degrees))

acceleration_x_ms2 = 0
acceleration_y_ms2 = -GRAVITY_MS2


# Time
TIME_STEP = 0.01
START_TIME = 0
END_TIME = 3
TIME = np.arange(START_TIME, END_TIME, TIME_STEP)
N = TIME.size

# Graph

X_MIN = 0
Y_MIN = 0


def time2index(time):
    return int(time / TIME_STEP)


def index2time(index):
    return index * TIME_STEP


def get_closest_indices(array, value):
    return np.where(np.abs(array - value) == np.abs(array - value).min())


def get_x_position():
    # Arrays
    array_position = np.zeros(N)
    array_velocity = np.zeros(N)
    array_acceleration = np.zeros(N)

    # Initial conditions
    array_position[0] = x0
    array_velocity[0] = initial_velocity_x_ms
    array_acceleration[0] = -GRAVITY_MS2

    # Euler method
    for i in range(1, N):
        abs_velocity = abs(array_velocity[i - 1])
        d = GRAVITY_MS2 / np.power(TERMINAL_VELOCITY_MS, 2)
        array_velocity[i] = (
            array_velocity[i - 1] + array_acceleration[i - 1] * TIME_STEP
        )
        array_position[i] = array_position[i - 1] + array_velocity[i - 1] * TIME_STEP
        array_acceleration[i] = -(d * array_velocity[i - 1] * abs_velocity)
    return array_position


def get_y_position():
    # Arrays
    array_position = np.zeros(N)
    array_velocity = np.zeros(N)
    array_acceleration = np.zeros(N)

    # Initial conditions
    array_position[0] = y0
    array_velocity[0] = initial_velocity_y_ms
    array_acceleration[0] = -GRAVITY_MS2

    # Euler method
    for i in range(1, N):
        abs_velocity = abs(array_velocity[i - 1])
        d = GRAVITY_MS2 / np.power(TERMINAL_VELOCITY_MS, 2)
        array_velocity[i] = (
            array_velocity[i - 1] + array_acceleration[i - 1] * TIME_STEP
        )
        array_position[i] = array_position[i - 1] + array_velocity[i - 1] * TIME_STEP
        array_acceleration[i] = -GRAVITY_MS2 - (
            d * array_velocity[i - 1] * abs_velocity
        )
    return array_position


def graph():
    plt.plot(get_x_position(), get_y_position())
    plt.xlabel("x position (m)")
    plt.ylabel("y position (m)")
    plt.title("Ball trajectory")
    plt.xlim(X_MIN)
    plt.ylim(Y_MIN)

    index_final = get_closest_indices(get_y_position()[20::], 3)[0]
    time_final = index2time(index_final)
    print(f"Time to reach 3m: {time_final} s")
    x_final = get_x_position()[index_final]
    print(f"Distance from initial point to reach 3m: {x_final} m")

    plt.show()


def main():
    graph()


if __name__ == "__main__":
    main()
