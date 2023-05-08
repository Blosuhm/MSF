"""Logarithmic Graph of Radioactive Isotope Activity"""

import numpy as np
import matplotlib.pyplot as plt

# Constants

# Activity of a radioactive isotope in mCi
ACTIVITY_ARRAY = np.array(
    [9.676, 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119]
)
TIME_ARRAY_DAYS = np.arange(0, 5 * ACTIVITY_ARRAY.size, 5)


def graph_points(ax):
    ax.plot(TIME_ARRAY_DAYS, ACTIVITY_ARRAY, "o")


def graph_semilog_points(ax):
    ax.plot(TIME_ARRAY_DAYS, np.log(ACTIVITY_ARRAY), "o")


def main():
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

    graph_points(ax1)
    ax1.set_ylabel("Activity")
    ax1.set_xlabel("Time (days)")

    graph_semilog_points(ax2)
    ax2.set_ylabel("Log Activity")
    ax2.set_xlabel("Time (days)")

    plt.show()


if __name__ == "__main__":
    main()
