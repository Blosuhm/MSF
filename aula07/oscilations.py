import numpy as np
import matplotlib.pyplot as plt
import utils as u
import formulas as f


def main():
    position, velocity, acceleration = u.euler_method(
        TIME,
        TIME_STEP,
        initial_position=initial_position,
        initial_velocity=initial_velocity,
        initial_acceleration=initial_acceleration,
        acceleration_formula=acceleration_formula,
    )

    position_x = position[:, 0]
    position_x_true = np.zeros(N)
    for i, t in enumerate(TIME):
        position_x_true[i] = position_formula(t)[0]

    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 10))

    u.graph(ax, TIME, position_x, "Position", x_label="t (s)", y_label="x (m)")
    u.graph(ax, TIME, position_x_true, "Position", x_label="t (s)", y_label="x (m)")
    ax.
    plt.show()


def position_formula(t):
    return np.array([amplitude * np.cos(t * omega + phi), 0, 0])


def acceleration_formula(a, v, r):
    return -k * r / m


# Time
TIME_STEP = 0.01
TIME_START, TIME_END = 0, 10
TIME = np.arange(TIME_START, TIME_END, TIME_STEP)
N = len(TIME)


# Variables
amplitude = 4
k = 1
m = 1
omega = np.sqrt(k / m)
phi = 0


initial_position = np.array([4, 0, 0])
initial_velocity = np.array([0, 0, 0])
initial_acceleration = acceleration_formula(0, 0, position_formula(TIME_START))


if __name__ == "__main__":
    main()
