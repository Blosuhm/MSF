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
RAMP_ANGLE = 5

# Variables
power = horse2watt(0.4)
mass = 75

# Initial conditions
initial_position_x = np.array([0, 0, 0])
initial_velocity_x = np.array([1, 0, 0])
initial_acceleration_x = np.array([power / (mass * initial_velocity_x[0]), 0, 0])

# Time
TIME_STEP = 0.0025
TIME_START, TIME_END = 0, 500
TIME = np.arange(TIME_START, TIME_END, TIME_STEP)
N = len(TIME)


def acceleration_formula(a, velocity, p):
    vx, vy, vz = velocity
    abs_velocity = abs(vx)
    abs_velocity_sqrd = abs_velocity * vx

    cyclist_acceleration = power / (mass * vx)
    gravity_drag = -np.sin(np.deg2rad(RAMP_ANGLE)) * GRAVITY
    normal = np.cos(np.deg2rad(RAMP_ANGLE)) * GRAVITY
    rolling_friction = -normal * FRICTION_COEFFICIENT
    air_drag = -(
        RESISTANCE_COEFFICIENT * FRONTAL_AREA * AIR_DENSITY * abs_velocity_sqrd
    ) / (2 * mass)

    acceleration_x = cyclist_acceleration + gravity_drag + rolling_friction + air_drag
    acceleration = np.array([acceleration_x, 0, 0])

    return acceleration


def acceleration_formula2(a, velocity, p):
    gravity_x, gravity_y = get_gravity_projections(RAMP_ANGLE, mass, degrees=True)

    gravity_drag = -np.array([gravity_x, 0, 0]) / mass
    normal = np.array([0, gravity_y, 0])

    force = (
        power2force(power, velocity)
        + gravity_drag
        + friction_force(FRICTION_COEFFICIENT, normal, velocity)
        + air_resistance_force(RESISTANCE_COEFFICIENT, FRONTAL_AREA, velocity)
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
        acceleration_formula=acceleration_formula,
        cromer=True,
    )

    p_x = get_axis(p, 0)
    v_x = get_axis(v, 0)
    a_x = get_axis(a, 0)

    print("Terminal velocity: ", v_x[-1])

    array = np.array([p_x, v_x, a_x])

    fig, ax = plt.subplots(1, 3, figsize=(16, 8))

    graph_all(ax, TIME, array, ["Position", "Velocity", "Acceleration"])

    plt.show()


if __name__ == "__main__":
    main()
