import numpy as np
import matplotlib.pyplot as plt


# Constants
GRAVITY_MS2 = 9.8
TERMINAL_VELOCITY_KMH = 100
TERMINAL_VELOCITY_MS = TERMINAL_VELOCITY_KMH * 1000 / 3600

# Initial conditions
x0 = 0
y0 = 0

initial_velocity_kmh = 100
initial_velocity_ms = initial_velocity_kmh * 1000 / 3600
angle_degrees = 10
initial_velocity_x_ms = initial_velocity_ms * np.cos(np.deg2rad(angle_degrees))
initial_velocity_y_ms = initial_velocity_ms * np.sin(np.deg2rad(angle_degrees))

acceleration_x_ms2 = 0
acceleration_y_ms2 = -GRAVITY_MS2


# Time
TIME_STEP = 0.01
START_TIME = 0
END_TIME = 1
TIME = np.arange(START_TIME, END_TIME, TIME_STEP)
N = TIME.size


def time2index(time):
    return int(time / TIME_STEP)


def index2time(index):
    return index * TIME_STEP


def get_x_position():
    array_position = np.zeros(N)
    array_position[0] = x0
    previous_velocity = initial_velocity_x_ms
    # Euler method no resistance
    for i in range(1, N):
        current_velocity = previous_velocity + acceleration_x_ms2 * TIME_STEP
        array_position[i] = array_position[i - 1] + current_velocity * TIME_STEP
        previous_velocity = current_velocity
    return array_position


def get_y_position():
    array_position = np.zeros(N)
    array_position[0] = y0
    previous_velocity = initial_velocity_y_ms
    # Euler method no resistance
    for i in range(1, N):
        current_velocity = previous_velocity + acceleration_y_ms2 * TIME_STEP
        array_position[i] = array_position[i - 1] + current_velocity * TIME_STEP
        previous_velocity = current_velocity
    return array_position


def graph():
    plt.plot(get_x_position(), get_y_position())
    plt.xlabel("x position (m)")
    plt.ylabel("y position (m)")
    plt.title("Ball trajectory")
    plt.show()


def main():
    print(get_x_position())
    graph()


if __name__ == "__main__":
    main()
