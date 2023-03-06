import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Constants
TIME_RANGE_S = np.linspace(0, 4, 100)

# Functions
def shuttlecock_trajectory(time_range_s):
    t, g, vt = sp.symbols("t g vt")
    expr = sp.Pow(vt, 2) / g * sp.log(sp.cosh(g * t / vt), 10)
    expr = expr.subs([(g, 9.8), (vt, 6.8)])
    y_vals = sp.lambdify(t, expr, "numpy")(time_range_s)
    print(sp.latex(expr))
    return y_vals


def shuttlecock_derivative(time_range_s):
    t, g, vt = sp.symbols("t g vt")
    expr = sp.Pow(vt, 2) / g * sp.log(sp.cosh(g * t / vt), 10)
    expr = expr.subs([(g, 9.8), (vt, 6.8)])
    expr = sp.diff(expr, t)
    y_vals = sp.lambdify(t, expr, "numpy")(time_range_s)
    print(sp.latex(expr))
    return y_vals


trajectory = shuttlecock_trajectory(TIME_RANGE_S)
derivative = shuttlecock_derivative(TIME_RANGE_S)


plt.plot(TIME_RANGE_S, trajectory)
plt.plot(TIME_RANGE_S, derivative)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Trajectory of Shuttlecock")
plt.show()
