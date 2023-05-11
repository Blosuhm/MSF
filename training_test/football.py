import numpy as np
import matplotlib.pyplot as plt
import formulas as f
import utils as u


def main():
    position_array, velocity_array, acceleration_array = u.euler_method(
        TIME,
        TIME_STEP,
        initial_acceleration=initial_acceleration,
        initial_velocity=initial_velocity,
        initial_position=initial_position,
        acceleration_formula=acceleration_formula,
    )

    # Processing data

    x, y = u.get_axis(position_array, 0), u.get_axis(position_array, 1)

    idx_x, closest = u.find_index(x, 20)
    y_value = y[idx_x]
    print(idx_x, closest)
    print(f"a) y value at x = 20m: {y_value}")

    # Graphs
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(16, 8))
    fig, bx = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))

    u.graph_all(
        ax,
        TIME,
        [position_array, velocity_array, acceleration_array],
        ["position", "velocity", "acceleration"],
        x_label_array=["t (s)"] * 3,
        y_label_array=["x (m)", "v (m/s)", "a (m/s²)"],
    )

    u.graph(
        bx,
        x,
        y,
        "position",
        x_label="x (m)",
        y_label="y (m)",
    )

    plt.show()


def acceleration_formula(a, v, p):
    gravity_force = np.array([0, -f.GRAVITY * mass, 0])
    air_resistance_force = f.air_resistance_force_with_vt(u.kmh2ms(100), v, mass)
    magnus_force = f.magnus_force(area, radius, magnus_rotation, v)
    print(magnus_force)
    force = gravity_force + air_resistance_force + magnus_force

    acceleration = f.force2acceleration(force, mass)

    return acceleration


# Variables

ball_speed = u.kmh2ms(100)
ball_angle = np.deg2rad(16)
ball_speed_x, ball_speed_y = u.get_x_y_components(ball_speed, ball_angle)
mass = 0.45  # kg
magnus_rotation = np.array([0, 0, -10])

radius = 11e-2  # m
area = np.pi * radius**2


# Initial conditions

initial_position = np.array([0, 0, 0])
initial_velocity = np.array([ball_speed_x, ball_speed_y, 0])
initial_acceleration = acceleration_formula(0, initial_velocity, 0)


# Time

TIME_STEP = 0.001
START_TIME, END_TIME = 0, 1.5
TIME = np.arange(START_TIME, END_TIME, TIME_STEP)
N = TIME.size

if __name__ == "__main__":
    main()
