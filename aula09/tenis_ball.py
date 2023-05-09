import numpy as np
import matplotlib.pyplot as plt
from utils import kmh2ms, euler_method, graph, get_x_y_components, get_axis, time2index
from formulas import (
    GRAVITY,
    kinetic_energy,
    air_resistance_force_with_vt,
    force2acceleration,
    gravitational_potential_energy,
    trapezoidal_integral,
)

# Variables

angle = np.deg2rad(10)
mass = 57e-3  # kg

array_air_resistance_work = [0]


def acceleration_formula(a, v, p):
    air_resistance = air_resistance_force_with_vt(kmh2ms(100), v, mass)
    gravity = np.array([0, -GRAVITY, 0]) * mass
    force = air_resistance + gravity
    acceleration = force2acceleration(force, mass)

    array_air_resistance_work.append(air_resistance * v)
    return acceleration


# Initial conditions

initial_velocity_norm = kmh2ms(100)
initial_velocity_x, initial_velocity_y = get_x_y_components(
    initial_velocity_norm, angle
)

initial_position = np.array([0, 0, 0])
initial_velocity = np.array([initial_velocity_x, initial_velocity_y, 0])
initial_acceleration = np.array([0, -GRAVITY, 0])

# Time

TIME_STEP = 0.00001
START_TIME, END_TIME = 0, 0.8
TIME = np.arange(START_TIME, END_TIME, TIME_STEP)
N = TIME.size


def main():
    _kinetic_energy = kinetic_energy(mass, initial_velocity)
    print(f"a) kinetic energy: {_kinetic_energy}")

    position_array, velocity_array, acceleration_array = euler_method(
        TIME,
        TIME_STEP,
        initial_acceleration=initial_acceleration,
        initial_velocity=initial_velocity,
        initial_position=initial_position,
        acceleration_formula=acceleration_formula,
        cromer=True,
    )

    position_x_array, position_y_array = get_axis(position_array, 0), get_axis(
        position_array, 1
    )

    # Formula -> Em = Ec + Ep
    mechanical_energy = np.zeros(N)
    for i in range(N):
        mechanical_energy[i] = kinetic_energy(
            mass, velocity_array[i]
        ) + gravitational_potential_energy(mass, position_y_array[i])

    fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=4, figsize=(18, 8))
    fig, (bx) = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))

    _, idx04 = time2index(array_air_resistance_work, TIME_STEP, 0.4)

    t1 = -trapezoidal_integral(array_air_resistance_work, 1, TIME_STEP)
    t2 = -trapezoidal_integral(array_air_resistance_work, idx04, TIME_STEP)
    t3 = -trapezoidal_integral(array_air_resistance_work, N, TIME_STEP)

    print(f"c)\nt1 -> {t1}\nt2 -> {t2}\nt3 -> {t3}")

    graph(
        ax0,
        TIME,
        position_array,
        "Position",
        x_label="x (m)",
        y_label="t (s)",
    )

    graph(
        ax1,
        TIME,
        velocity_array,
        "Velocity",
        x_label="v (m/s)",
        y_label="t (s)",
    )

    graph(
        ax2,
        TIME,
        acceleration_array,
        "Acceleration",
        x_label="a (m/s²)",
        y_label="t (s)",
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
        mechanical_energy,
        "Mechanical energy",
        x_label="t (s)",
        y_label="E (J)",
    )

    plt.show()


if __name__ == "__main__":
    main()
