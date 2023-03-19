import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Constants
TIME = np.linspace(0, 4, 100)
X_LIM = None
Y_LIM = None
TERMINAL_VELOCITY_MS = 6.8
GRAVITY_MS2 = 9.8


# Sympy
t = sp.Symbol("t")

position = (math.pow(TERMINAL_VELOCITY_MS, 2) / GRAVITY_MS2) * sp.log(
    sp.cosh(GRAVITY_MS2 * t / TERMINAL_VELOCITY_MS)
)


def graph_position(ax):
    position_array = sp.lambdify(t, position, "numpy")(TIME)

    ax.plot(
        TIME,
        position_array,
    )
    ax.set_xlim(0, X_LIM)
    ax.set_ylim(0, Y_LIM)
    ax.set_ylabel("Distance (m)")
    ax.set_xlabel("Time (s)")


def graph_velocity(ax):
    velocity = sp.diff(position, t)
    velocity_array = sp.lambdify(t, velocity, "numpy")(TIME)

    ax.plot(
        TIME,
        velocity_array,
    )
    ax.set_xlim(0, X_LIM)
    ax.set_ylim(0, Y_LIM)
    ax.set_ylabel("Velocity (m/s)")
    ax.set_xlabel("Time (s)")


def main():
    fig, ax = plt.subplots(nrows=1, ncols=1)
    graph_position(ax)
    graph_velocity(ax)

    plt.show()


if __name__ == "__main__":
    main()
