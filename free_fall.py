# Euler's method for free fall
from modules.plot import plot
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Constants
g = 9.8  # m/s^2
dt = 0.0001  # s
# dt = 0.1  # s

# Initial conditions
t0 = 0  # s
tf = 3  # s
v0 = 0  # m/s
y0 = 0  # m

# Arrays
n = int((tf - t0) / dt + 0.1)
t = np.zeros(n + 1)
y = np.zeros(n + 1)
vy = np.zeros(n + 1)
ay = np.zeros(n + 1)

# Initial conditions
t[0] = t0
y[0] = y0
vy[0] = v0


def get_value(x, dx, array):
    """Get speed at time t."""
    i = x / dx
    return array[round(i)]


# Euler's method
def euler(ay, y, vy, t, dt, n):
    for i in range(n):
        ay[i] = g  # queda livre
        # (em geral pode ser qualquer função de x[i] e vx[i])
        y[i + 1] = y[i] + vy[i] * dt
        vy[i + 1] = vy[i] + ay[i] * dt  # atualizar velocidade sabendo aceleração
        t[i + 1] = t[i] + dt  # atualizar tempo


def error_function(n=6):
    """Error function."""
    array_x = np.zeros(n)
    array_y = np.zeros(n)
    for i in range(1, n):
        bananas = 10**-i
        euler(ay, y, vy, t, bananas, n)
        value = get_value(2, bananas, y)
        array_y[i] = abs(value - 19.6)
        array_x[i] = i
    return array_x, array_y


def main():
    """Main function."""
    euler(ay, y, vy, t, dt, n)
    print(get_value(2, dt, y), "m")
    plot(
        t,
        y,
        title="Trajectory of Shuttlecock",
        x_label="Time (s)",
        y_label="Height (m)",
        cols=2,
        rows=2,
    )
    plot(
        t,
        vy,
        title="Derivative of Trajectory of Shuttlecock",
        x_label="Time (s)",
        y_label="Velocity (m/s)",
        cols=2,
        rows=2,
    )
    plot(
        t,
        ay,
        title="Derivative of Trajectory of Shuttlecock",
        x_label="Time (s)",
        y_label="Acceleration (m/s^2)",
        cols=2,
        rows=2,
    )
    array_x, array_y = error_function()
    plot(
        array_x,
        array_y,
        title="Error function",
        x_label="Time (s)",
        y_label="Error (m)",
        cols=2,
        rows=2,
    )

    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    plt.show()


if __name__ == "__main__":
    main()
