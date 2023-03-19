import matplotlib.pyplot as plt
import numpy as np

# constants
CAR_KMH = 70
CAR_MS = 70 / 3.6
POLICE_MS2 = 2

X_LIM = 15
Y_LIM = 250

# Range
TIME = np.linspace(0, 30)


def graph_police(ax):
    ax.plot(
        TIME,
        POLICE_MS2 * np.power(TIME, 2),
    )
    ax.set_xlim(0, X_LIM)
    ax.set_ylim(0, Y_LIM)
    ax.set_ylabel("Distance (m)")
    ax.set_xlabel("Time (s)")


def graph_car(ax):
    ax.plot(
        TIME,
        CAR_MS * TIME,
    )
    ax.set_xlim(0, X_LIM)
    ax.set_ylim(0, Y_LIM)
    ax.set_ylabel("Distance (m)")
    ax.set_xlabel("Time (s)")


def graph_car_police(ax):
    ax.plot(
        TIME,
        CAR_MS * TIME,
    )
    ax.plot(
        TIME,
        POLICE_MS2 * np.power(TIME, 2),
    )
    ax.set_xlim(0, X_LIM)
    ax.set_ylim(0, Y_LIM)
    ax.set_ylabel("Distance (m)")
    ax.set_xlabel("Time (s)")


def main():
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)

    graph_car(ax1)
    graph_police(ax2)
    graph_car_police(ax3)

    plt.show()


if __name__ == "__main__":
    main()
