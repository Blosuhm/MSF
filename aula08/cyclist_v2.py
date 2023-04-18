import numpy as np
import matplotlib.pyplot as plt
from utils import euler_method, graph_all


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


def acceleration_formula(a, velocity):
    abs_velocity = abs(velocity)
    abs_velocity_sqrd = abs_velocity * velocity

    acceleration = (
        power / (mass * velocity)
        - (RESISTANCE_COEFFICIENT * FRONTAL_AREA * AIR_DENSITY * abs_velocity_sqrd)
        / (2 * mass)
        - (FRICTION_COEFFICIENT * GRAVITY)
    )

    return acceleration


def main():
    arrays = euler_method(
        TIME,
        TIME_STEP,
        initial_acceleration=initial_acceleration_x,
        initial_velocity=initial_velocity_x,
        initial_position=initial_position_x,
        acceleration_formula=acceleration_formula,
        cromer=True,
    )[::-1]

    fig, ax = plt.subplots(1, 3, figsize=(15, 5))

    graph_all(
        ax, TIME, arrays, ["Acceleration", "Velocity", "Position"][::-1], grid=True
    )

    plt.show()


if __name__ == "__main__":
    main()
