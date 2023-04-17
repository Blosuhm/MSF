# 0 48 96 144 192 240 288 336 384
# 10.03 7.06 4.88 3.38 2.26 1.66 1.14 0.79 0.58
import numpy as np
import matplotlib.pyplot as plt
from linear_regression import get_delta_slope, get_delta_intercept, get_r_squared


# Constants
TIME_HRS = np.array([0, 48, 96, 144, 192, 240, 288, 336, 384])
ACTIVITY_MBQ = np.array([10.03, 7.06, 4.88, 3.38, 2.26, 1.66, 1.14, 0.79, 0.58])


# Regression
slope, intercept = np.polyfit(TIME_HRS, ACTIVITY_MBQ, 1)
delta_m = get_delta_slope(TIME_HRS, ACTIVITY_MBQ, slope, intercept)
delta_b = get_delta_intercept(TIME_HRS, delta_m)
r_squared = get_r_squared(TIME_HRS, ACTIVITY_MBQ, slope, intercept)


slope_log, intercept_log = np.polyfit(TIME_HRS, np.log(ACTIVITY_MBQ), 1)
delta_m_log = get_delta_slope(TIME_HRS, np.log(ACTIVITY_MBQ), slope_log, intercept_log)
delta_b_log = get_delta_intercept(TIME_HRS, delta_m_log)
r_squared_log = get_r_squared(TIME_HRS, np.log(ACTIVITY_MBQ), slope_log, intercept_log)


def graph_data(ax):
    """Graphs the data."""
    ax.plot(TIME_HRS, ACTIVITY_MBQ, "o")
    ax.set_xlabel("Time (hrs)")
    ax.set_ylabel("Activity (mBq)")


def graph_regression(ax, slope, intercept):
    """Graphs the linear regression line."""
    x = np.linspace(0, 400, 100)
    y = slope * x + intercept

    ax.plot(x, y, label="Linear Regression")


def graph_log_data(ax):
    ax.plot(TIME_HRS, np.log(ACTIVITY_MBQ), "o")
    ax.set_xlabel("Time (hrs)")
    ax.set_ylabel("Log Activity (mBq)")


def graph_log_regression(ax, slope, intercept):
    x = np.linspace(0, 400, 100)
    y = slope * x + intercept

    ax.plot(x, y, label="Linear Regression")


def main():
    fig, (ax1, ax2) = plt.subplots(ncols=2, nrows=1)
    graph_data(ax1)
    graph_regression(ax1, slope, intercept)
    print(f"y = {slope}x + {intercept}")
    print(f"Delta m: {delta_m}")
    print(f"Delta b: {delta_b}")
    print(f"R-squared: {r_squared}")

    graph_log_data(ax2)
    graph_log_regression(ax2, slope_log, intercept_log)
    print(f"y = {slope_log}x + {intercept_log}")
    print(f"Delta m: {delta_m_log}")
    print(f"Delta b: {delta_b_log}")
    print(f"R-squared: {r_squared_log}")
    plt.show()


if __name__ == "__main__":
    main()
