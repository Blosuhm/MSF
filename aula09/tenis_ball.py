import numpy as np
import matplotlib.pyplot as plt
from utils import kmh2ms, euler_method, graph, get_x_y_components, get_axis
from formulas import (
    GRAVITY,
    kinetic_energy,
    air_resistance_force_with_vt,
    force2acceleration,
)

# Variables

angle = np.deg2rad(10)
mass = 57e-3  # kg


def acceleration_formula(a, v, p):
    air_resistance = air_resistance_force_with_vt(kmh2ms(100), v, mass)
    # print(f"air_resistance: {air_resistance}")
    gravity = np.array([0, -GRAVITY, 0]) * mass
    force = air_resistance + gravity
    print(f"force: {force}")
    acceleration = force2acceleration(force, mass)
    print(f"acceleration: {acceleration}")
    return acceleration


# Initial conditions

initial_velocity_norm = kmh2ms(100)
initial_velocity_x, initial_velocity_y = get_x_y_components(
    initial_velocity_norm, angle
)

print(f"initial_velocity_x: {initial_velocity_x}")
print(f"initial_velocity_y: {initial_velocity_y}")

initial_position = np.array([0, 0, 0])
initial_velocity = np.array([initial_velocity_x, initial_velocity_y, 0])
initial_acceleration = acceleration_formula(0, initial_velocity, 0)

# Time

TIME_STEP = 0.01
START_TIME, END_TIME = 0, 0.8
TIME = np.arange(START_TIME, END_TIME, TIME_STEP)
N = TIME.size


def main():
    _kinetic_energy = kinetic_energy(mass, initial_velocity)
    print(f"a)kinetic energy: {_kinetic_energy}")

    position_array, velocity_array, acceleration_array = euler_method(
        TIME,
        TIME_STEP,
        initial_acceleration=initial_acceleration,
        initial_velocity=initial_velocity,
        initial_position=initial_position,
        acceleration_formula=acceleration_formula,
        cromer=True,
    )

    print(velocity_array)

    position_x_array, position_y_array = get_axis(position_array, 0), get_axis(
        position_array, 1
    )

    fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=4, figsize=(18, 8))
    fig, (bx) = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))

    graph(
        ax0,
        TIME,
        position_array,
        "Position",
        x_label="x (m)",
        y_label="y (m)",
    )

    graph(
        ax1,
        TIME,
        velocity_array,
        "Velocity",
        x_label="x (m)",
        y_label="y (m)",
    )

    graph(
        ax2,
        TIME,
        acceleration_array,
        "Acceleration",
        x_label="x (m)",
        y_label="y (m)",
    )

    graph(
        ax3,
        position_x_array,
        position_y_array,
        "Position x",
        x_label="x (m)",
        y_label="y (m)",
    )

    graph(
        bx,
        TIME,
        position_x_array,
        "Position x",
        x_label="x (m)",
        y_label="y (m)",
    )

    plt.show()


if __name__ == "__main__":
    main()
