import math
import numpy as np
import matplotlib.pyplot as plt


def horse2watt(horsepower):
    return horsepower * 745.7


# Constants

GRAVITY = 9.81
RESISTANCE_COEFFICIENT = 0.9
FRONTAL_AREA = 0.3
AIR_DENSITY = 1.225
FRICTION_COEFFICIENT = 0.004

# Variables
power = horse2watt(0.4)
mass = 75

# Initial conditions
initial_position_x = 0
initial_velocity_x = 1
initial_acceleration_x = power / (mass * initial_velocity_x)

# Time
TIME_STEP = 0.001
TIME_START, TIME_END = 0, 200
TIME = np.arange(TIME_START, TIME_END, TIME_STEP)
N = len(TIME)


def euler_cromer_method():
    position_x_array = np.zeros(N)
    velocity_x_array = np.zeros(N)
    acceleration_x_array = np.zeros(N)

    position_x_array[0] = initial_position_x
    velocity_x_array[0] = initial_velocity_x
    acceleration_x_array[0] = initial_acceleration_x

    for i in range(1, N):
        abs_velocity = abs(velocity_x_array[i - 1])
        abs_velocity_sqrd = abs_velocity * velocity_x_array[i - 1]

        acceleration_x = (
            power / (mass * velocity_x_array[i - 1])
            - (RESISTANCE_COEFFICIENT * FRONTAL_AREA * AIR_DENSITY * abs_velocity_sqrd)
            / (2 * mass)
            - (FRICTION_COEFFICIENT * GRAVITY)
        )

        acceleration_x_array[i] = acceleration_x

        velocity_x_array[i] = (
            velocity_x_array[i - 1] + acceleration_x_array[i - 1] * TIME_STEP
        )
        position_x_array[i] = position_x_array[i - 1] + velocity_x_array[i] * TIME_STEP

    return position_x_array, velocity_x_array, acceleration_x_array


def main():
    position_x_array, velocity_x_array, acceleration_x_array = euler_cromer_method()

    for i, a in enumerate(acceleration_x_array):
        if a < 10**-3:
            print("Terminal velocity: ", velocity_x_array[i], "m/s")
            break

    print(acceleration_x_array[-1])
    _, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(10, 10))

    ax0.plot(TIME, position_x_array)
    ax0.set_xlabel("Time (s)")
    ax0.set_ylabel("Position (m)")

    ax1.plot(TIME, velocity_x_array)
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Velocity (m/s)")

    ax2.plot(TIME, acceleration_x_array)
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Acceleration (m/s²)")

    plt.show()


if __name__ == "__main__":
    main()
