# Terminal velocity of the parachutist with open and closed parachute
# Euler Method: f(Ndx + dx) = f(Ndx) + f'(Ndx)dx


import numpy as np
import matplotlib.pyplot as plt

# Constants
GRAVITY_MS2 = 9.8
HEIGHT_M = 800
TERMINAL_VELOCITY_OPEN_PARACHUTE_MS = 5
TERMINAL_VELOCITY_CLOSED_PARACHUTE_MS = 60
AIR_DENSITY_KG_PER_M3 = 1.225

# Time
TIME_STEP = 0.001
TIME_START, TIME_END = (0, 100)
TIME = np.arange(TIME_START, TIME_END, TIME_STEP)
N = TIME.size


def time2index(time):
    return int(time / TIME_STEP)


def index2time(index):
    return index * TIME_STEP


def get_closest_index(array, value):
    return np.where(np.abs(array - value) == np.abs(array - value).min())[0]


def get_position_velocity_acceleration_arrays():
    # Arrays
    array_position = np.zeros(N)
    array_velocity = np.zeros(N)
    array_acceleration = np.zeros(N)

    # Initial conditions
    array_position[0] = HEIGHT_M
    array_velocity[0] = 0
    array_acceleration[0] = -GRAVITY_MS2

    # Euler method
    for i in range(1, N):
        abs_velocity = abs(array_velocity[i - 1])
        d = GRAVITY_MS2 / np.power(TERMINAL_VELOCITY_CLOSED_PARACHUTE_MS, 2)
        array_velocity[i] = (
            array_velocity[i - 1] + array_acceleration[i - 1] * TIME_STEP
        )
        array_position[i] = array_position[i - 1] + array_velocity[i - 1] * TIME_STEP
        array_acceleration[i] = -GRAVITY_MS2 - (
            d * array_velocity[i - 1] * abs_velocity
        )
    return array_position, array_velocity, array_acceleration


def get_position_velocity_acceleration_arrays_open_parachute():
    # Arrays
    array_position = np.zeros(N)
    array_velocity = np.zeros(N)
    array_acceleration = np.zeros(N)

    # Initial conditions
    array_position[0] = HEIGHT_M
    array_velocity[0] = 0
    array_acceleration[0] = -GRAVITY_MS2

    # Euler method
    for i in range(1, N):
        abs_velocity = abs(array_velocity[i - 1])
        terminal_velocity = (
            TERMINAL_VELOCITY_OPEN_PARACHUTE_MS
            if TIME[i] > 10
            else TERMINAL_VELOCITY_CLOSED_PARACHUTE_MS
        )
        d = GRAVITY_MS2 / np.power(terminal_velocity, 2)
        array_velocity[i] = (
            array_velocity[i - 1] + array_acceleration[i - 1] * TIME_STEP
        )
        array_position[i] = array_position[i - 1] + array_velocity[i] * TIME_STEP
        array_acceleration[i] = -GRAVITY_MS2 - (
            d * array_velocity[i - 1] * abs_velocity
        )
    return array_position, array_velocity, array_acceleration


def main():
    (
        position_closed,
        velocity_closed,
        acceleration,
    ) = get_position_velocity_acceleration_arrays()

    # Find the moment the parachutist got to the ground
    time_closed = index2time(get_closest_index(position_closed, 0)[0])
    print("Time:", time_closed)
    print("Velocity:", velocity_closed[time2index(time_closed)])

    (
        position_open,
        velocity_open,
        acceleration,
    ) = get_position_velocity_acceleration_arrays_open_parachute()

    time_open = index2time(get_closest_index(position_open, 0)[0])
    print("Time:", time_open)
    print("Velocity:", velocity_open[time2index(time_open)])

    # plt.plot(TIME, position_closed)
    plt.plot(TIME, position_open)
    plt.show()


if __name__ == "__main__":
    main()
