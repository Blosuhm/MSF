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
t, g, v_terminal = sp.symbols("t g v_terminal")

position = (sp.Pow(v_terminal, 2) / g) * sp.log(sp.cosh(g * t / v_terminal))
velocity = sp.diff(position, t)
acceleration = sp.diff(velocity, t)


def graph_position(ax):
    position_array = sp.lambdify(
        t,
        position.subs([(g, GRAVITY_MS2), (v_terminal, TERMINAL_VELOCITY_MS)]),
        "numpy",
    )(TIME)

    ax.plot(
        TIME,
        position_array,
    )
    ax.set_xlim(0, X_LIM)
    ax.set_ylim(0, Y_LIM)
    ax.set_ylabel("Distance (m)")
    ax.set_xlabel("Time (s)")


def graph_velocity(ax):
    velocity_array = sp.lambdify(
        t,
        velocity.subs([(g, GRAVITY_MS2), (v_terminal, TERMINAL_VELOCITY_MS)]),
        "numpy",
    )(TIME)

    ax.plot(
        TIME,
        velocity_array,
    )
    ax.set_xlim(0, X_LIM)
    ax.set_ylim(0, Y_LIM)
    ax.set_ylabel("Velocity (m/s)")
    ax.set_xlabel("Time (s)")


def graph_acceleration(ax):
    acceleration_array = sp.lambdify(
        t,
        acceleration.subs([(g, GRAVITY_MS2), (v_terminal, TERMINAL_VELOCITY_MS)]),
        "numpy",
    )(TIME)

    ax.plot(
        TIME,
        acceleration_array,
    )
    ax.set_xlim(0, X_LIM)
    ax.set_ylim(0, Y_LIM)
    ax.set_ylabel("Acceleration (m/s^2)")
    ax.set_xlabel("Time (s)")


def main():
    fig, ax = plt.subplots(nrows=1, ncols=1)
    sp.pprint(acceleration)
    sp.pprint(velocity)
    graph_position(ax)
    graph_velocity(ax)
    graph_acceleration(ax)

    plt.show()


if __name__ == "__main__":
    main()
