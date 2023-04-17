import math
import numpy as np
import matplotlib.pyplot as plt


# DATA
INITIAL_X = -10
INITIAL_Y = 1
INITIAL_Z = 0
INITIAL_POSITION_VECTOR = (INITIAL_X, INITIAL_Y, INITIAL_Z)

INITIAL_VELOCITY_KMH = 130
INITIAL_VELOCITY = INITIAL_VELOCITY_KMH / 3.6

ANGLE_DEGREES = 10
ANGLE = np.deg2rad(ANGLE_DEGREES)

INITIAL_X_VELOCITY = INITIAL_VELOCITY * math.cos(ANGLE)
INITIAL_Y_VELOCITY = INITIAL_VELOCITY * math.sin(ANGLE)
INITIAL_Z_VELOCITY = 0
INITIAL_VELOCITY_VECTOR = (INITIAL_X_VELOCITY, INITIAL_Y_VELOCITY, INITIAL_Z_VELOCITY)

MASS_G = 57
MASS = MASS_G * math.pow(10, -3)

DIAMETER_MM = 67
DIAMETER = DIAMETER_MM * math.pow(10, -3)
RADIUS = DIAMETER / 2
SECTION_AREA = math.pi * math.pow(RADIUS, 2)

TERMINAL_VELOCITY_KMH = 100
TERMINAL_VELOCITY = 100 / 3.6

ROTATION_VECTOR = (0, 0, 0)

# Constants
AIR_DENSITY = 1.225
GRAVITY = 9.8


# TIME
START_TIME, END_TIME = (0, 2)
TIME_STEP = 0.00001
TIME = np.arange(START_TIME, END_TIME, TIME_STEP)
N = TIME.size


# GRAPH OPTIONS
X_START, X_END = (None, None)
Y_START, Y_END = (None, None)


def calculate_x_y_position():
    # Arrays
    array_x_position = np.zeros(N)
    array_y_position = np.zeros(N)

    array_x_velocity = np.zeros(N)
    array_y_velocity = np.zeros(N)

    array_x_acceleration = np.zeros(N)
    array_y_acceleration = np.zeros(N)

    # Initial conditions
    array_x_position[0] = INITIAL_X
    array_y_position[0] = INITIAL_Y

    array_x_velocity[0] = INITIAL_X_VELOCITY
    array_y_velocity[0] = INITIAL_Y_VELOCITY

    array_x_acceleration[0] = 0
    array_y_acceleration[0] = -GRAVITY

    d = GRAVITY / np.power(TERMINAL_VELOCITY, 2)

    # Euler method
    for i in range(1, N):
        abs_x_velocity = abs(array_x_velocity[i - 1])
        abs_y_velocity = abs(array_y_velocity[i - 1])

        air_x_resistance = d * array_x_velocity[i - 1] * abs_x_velocity
        air_y_resistance = d * array_y_velocity[i - 1] * abs_y_velocity

        prev_velocity_vector = (array_x_velocity[i - 1], array_y_velocity[i - 1], 0)

        magnus_force = (
            1
            / 2
            * SECTION_AREA
            * AIR_DENSITY
            * RADIUS
            * np.cross(ROTATION_VECTOR, prev_velocity_vector)
        )
        magnus_x, magnus_y = magnus_force[0] / MASS, magnus_force[1] / MASS

        array_x_acceleration[i] = -air_x_resistance + magnus_x
        array_y_acceleration[i] = -GRAVITY - air_y_resistance + magnus_y

        array_x_velocity[i] = (
            array_x_velocity[i - 1] + array_x_acceleration[i - 1] * TIME_STEP
        )
        array_y_velocity[i] = (
            array_y_velocity[i - 1] + array_y_acceleration[i - 1] * TIME_STEP
        )

        array_x_position[i] = (
            array_x_position[i - 1] + array_x_velocity[i - 1] * TIME_STEP
        )
        array_y_position[i] = (
            array_y_position[i - 1] + array_y_velocity[i - 1] * TIME_STEP
        )
    return array_x_position, array_y_position


def is_negative_index(array):
    for i, y in enumerate(array):
        if y < 0:
            return i


def graph_position(ax):
    array_x_position, array_y_position = calculate_x_y_position()
    i = is_negative_index(array_y_position)
    print(i)
    ax.plot(array_x_position[:i], array_y_position[:i])


def main():
    fig, (ax) = plt.subplots(nrows=1, ncols=1)
    array_x_position, array_y_position = calculate_x_y_position()
    i = is_negative_index(array_y_position)

    print(f"Reach: {array_x_position[i-1]}")
    print(f"Max height: {max(array_y_position)}")
    graph_position(ax)
    plt.show()


if __name__ == "__main__":
    main()
