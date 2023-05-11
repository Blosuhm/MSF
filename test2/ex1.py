import numpy as np
import matplotlib.pyplot as plt
import formulas as f
import utils as u

# as formulas estão em formulas.py
# as funções de utilidade estão em utils.py (euler_method, graph, graph_all, get_axis, find_index)


def main():
    position_array, velocity_array, acceleration_array = u.euler_method(
        TIME,
        TIME_STEP,
        initial_acceleration=initial_acceleration,
        initial_velocity=initial_velocity,
        initial_position=initial_position,
        acceleration_formula=acceleration_formula,
    )

    (
        position_array_magnus,
        velocity_array_magnus,
        acceleration_array_magnus,
    ) = u.euler_method(
        TIME,
        TIME_STEP,
        initial_acceleration=initial_acceleration,
        initial_velocity=initial_velocity,
        initial_position=initial_position,
        acceleration_formula=acceleration_formula_magnus,
    )

    # Processing data

    position_array_x, position_array_y = position_array[:, 0], position_array[:, 1]
    position_array_x_magnus, position_array_y_magnus = (
        position_array_magnus[:, 0],
        position_array_magnus[:, 1],
    )

    idx, closest = u.find_index(position_array_y, 0)
    idx_magnus, closest_magnus = u.find_index(position_array_y_magnus, 0)

    print(f"y: {closest}")
    print(f"x: {position_array_x[idx]}")
    print(
        "Serviço inválido sem força de magnus"
    )  # y: -7.220443190434028e-05 x: 19.687807326095484

    print(f"y: {closest_magnus}")
    print(f"x: {position_array_x_magnus[idx_magnus]}")
    print("Serviço válido com a força de magnus")

    # Graphs
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(16, 8))
    fig, ax2 = plt.subplots(nrows=1, ncols=3, figsize=(16, 8))
    fig, bx = plt.subplots(nrows=1, ncols=1, figsize=(10, 10))
    fig, bx2 = plt.subplots(nrows=1, ncols=1, figsize=(10, 10))

    u.graph_all(
        ax,
        TIME,
        [position_array, velocity_array, acceleration_array],
        ["position", "velocity", "acceleration"],
        x_label_array=["t (s)"] * 3,
        y_label_array=["x (m)", "v (m/s)", "a (m/s²)"],
    )

    u.graph_all(
        ax2,
        TIME,
        [position_array_magnus, velocity_array_magnus, acceleration_array_magnus],
        ["position magnus", "velocity magnus", "acceleration magnus"],
        x_label_array=["t (s)"] * 3,
        y_label_array=["x (m)", "v (m/s)", "a (m/s²)"],
    )

    u.graph(
        bx, position_array_x, position_array_y, "Position", x_label="x", y_label="y"
    )

    u.graph(
        bx2,
        position_array_x_magnus,
        position_array_y_magnus,
        "Position magnus",
        x_label="x",
        y_label="y",
    )

    plt.show()


def acceleration_formula(a, v, p):
    gravity_force = np.array([0, -f.GRAVITY * mass, 0])
    air_resistance_force = f.air_resistance_force_with_vt(terminal_velocity, v, mass)
    force = gravity_force + air_resistance_force

    acceleration = f.force2acceleration(force, mass)

    return acceleration


def acceleration_formula_magnus(a, v, p):
    gravity_force = np.array([0, -f.GRAVITY * mass, 0])
    air_resistance_force = f.air_resistance_force_with_vt(terminal_velocity, v, mass)
    magnus_force = f.magnus_force(area, radius, omega, v)
    force = gravity_force + air_resistance_force + magnus_force

    acceleration = f.force2acceleration(force, mass)

    return acceleration


# Time

TIME_STEP = 0.0001
START_TIME, END_TIME = 0, 2
TIME = np.arange(START_TIME, END_TIME, TIME_STEP)
N = TIME.size

# Variables

mass = 0.057  # kg
radius = 0.034  # m
area = np.pi * radius**2  # m²
terminal_velocity = 20  # m/s
omega = np.array([0, 0, -60])  # rad/s

# Initial conditions

initial_position = np.array([0, 3, 0])
initial_velocity = np.array([30, 0, 0])
initial_acceleration = acceleration_formula(0, initial_velocity, 0)


if __name__ == "__main__":
    main()
