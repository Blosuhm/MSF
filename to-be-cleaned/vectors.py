import math
import matplotlib.pyplot as plt
import numpy as np

plt.axes().set_aspect("equal", adjustable="box")
plt.xlim(0, 12)
plt.ylim(0, 25)

print(np.cross([0, 0, 10], [0, 1, 0]))


def get_position(t):
    """Get position at time t."""
    return 2 * t, math.pow(t, 2)


def get_velocity(t):
    """Get velocity at time t."""
    return 2, 2 * t


for i in range(1, 5):
    x, y = get_position(i)
    xv, yv = get_velocity(i)
    plt.arrow(
        0,
        0,
        x,
        y,
        color="r",
        antialiased=True,
    )
    plt.arrow(
        x,
        y,
        xv,
        yv,
        antialiased=True,
    )


plt.show()
