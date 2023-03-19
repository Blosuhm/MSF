import numpy as np
import matplotlib.pyplot as plt

# Constants
TEMPERATURE_ARRAY = np.array(
    [200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0]
)
ENERGY_ARRAY = np.array(
    [0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7]
)


def graph_points(ax):
    ax.plot(TEMPERATURE_ARRAY, ENERGY_ARRAY, "o")


def graph_log_points(ax):
    ax.plot(np.log(TEMPERATURE_ARRAY), np.log(ENERGY_ARRAY), "o")


def main():
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

    graph_points(ax1)
    ax1.set_ylabel("Energy")
    ax1.set_xlabel("Temperature")

    graph_log_points(ax2)
    ax2.set_ylabel("Log Energy")
    ax2.set_xlabel("Log Temperature")

    plt.show()


if __name__ == "__main__":
    main()
