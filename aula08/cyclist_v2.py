import numpy as np
import matplotlib.pyplot as plt
from utils import euler_method, graph_all, get_axis
from formulas import (
    power2force,
    force2acceleration,
    air_resistance_force,
    get_gravity_projections,
    friction_force,
)


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
initial_position_x = np.array([0, 0, 0])
initial_velocity_x = np.array([1, 0, 0])
initial_acceleration_x = np.array([power / (mass * initial_velocity_x[0]), 0, 0])

# Time
TIME_STEP = 0.001
TIME_START, TIME_END = 0, 200
TIME = np.arange(TIME_START, TIME_END, TIME_STEP)
N = len(TIME)


def acceleration_formula(a, velocity, p):
    vx, vy, vz = velocity
    abs_velocity = abs(vx)
    abs_velocity_sqrd = abs_velocity * vx

    acceleration_x = (
        power / (mass * vx)
        - (RESISTANCE_COEFFICIENT * FRONTAL_AREA * AIR_DENSITY * abs_velocity_sqrd)
        / (2 * mass)
        - (FRICTION_COEFFICIENT * GRAVITY)
    )

    acceleration = np.array([acceleration_x, 0, 0])

    return acceleration


def acceleration_formula2(a, velocity, p):
    force = (
        power2force(power, velocity)
        + air_resistance_force(RESISTANCE_COEFFICIENT, FRONTAL_AREA, velocity)
        + friction_force(velocity, FRICTION_COEFFICIENT, GRAVITY)
    )

    acceleration = force2acceleration(force, mass)

    return acceleration


def main():
    p, v, a = euler_method(
        TIME,
        TIME_STEP,
        initial_acceleration=initial_acceleration_x,
        initial_velocity=initial_velocity_x,
        initial_position=initial_position_x,
        acceleration_formula=acceleration_formula2,
        cromer=True,
    )

    px = get_axis(p, 0)
    vx = get_axis(v, 0)
    ax = get_axis(a, 0)
    arrays = [px, vx, ax]

    print("Terminal velocity: ", np.max(vx))

    fig, ax = plt.subplots(1, 3, figsize=(16, 8))

    graph_all(ax, TIME, arrays, ["Position", "Velocity", "Acceleration"], grid=False)

    plt.show()


if __name__ == "__main__":
    main()
