import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Constants
id_gen = iter(range(1, 10))
TIME_RANGE_SEC = np.linspace(0, 4, 100)
TERMINAL_VELOCITY_MS = 6.8
g = 9.8


def position(domain=np.linspace(0, 10, 100)):
    vt, t = sp.symbols("vt t")
    y = sp.Pow(vt, 2) / (g) * sp.log(sp.cosh(g * t / vt))
    expr = y.subs([(vt, TERMINAL_VELOCITY_MS)])
    y_values = sp.lambdify(t, expr, "numpy")(domain)
    return y_values, expr, vt, t


def velocity(domain=np.linspace(0, 10, 100)):
    array, expr, vt, t = position(domain)
    expr = sp.diff(expr, t)
    y_values = sp.lambdify(t, expr, "numpy")(domain)
    return y_values, expr, vt, t


def acceleration(domain=np.linspace(0, 10, 100)):
    array, expr, vt, t = position(domain)
    expr = sp.diff(expr, t, 2)
    y_values = sp.lambdify(t, expr, "numpy")(domain)
    return y_values


def main():
    """Main function."""
    # print(position()[1])
    sp.pprint(position()[1], use_unicode=True)
    # print(velocity()[1])
    sp.pprint(velocity()[1], use_unicode=True)
    position_y = position(TIME_RANGE_SEC)[0]
    plt.figure()
    plot(
        TIME_RANGE_SEC,
        position_y,
        title="Trajectory of Shuttlecock",
        x_label="Time (s)",
        y_label="Height (m)",
    )
    velocity_y = velocity(TIME_RANGE_SEC)[0]
    plot(
        TIME_RANGE_SEC,
        velocity_y,
        title="Derivative of Trajectory of Shuttlecock",
        x_label="Time (s)",
        y_label="Velocity (m/s)",
    )

    plt.subplots_adjust(hspace=0.5)
    plt.show()


if __name__ == "__main__":
    main()
