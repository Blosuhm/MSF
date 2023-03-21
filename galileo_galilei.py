import numpy as np
import matplotlib.pyplot as plt
from modules.linear_regression import (
    get_r_squared,
    get_delta_slope,
    get_delta_intercept,
)

TIME_SEC = np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5])
DISTANCE_CM = np.array([0.1, 1.4, 1.7, 6.5, 7.7, 10.4, 19.5, 26.1, 26.5, 45.9, 52.5])

# Plot the data
def graph_data(ax):
    """Plots the data."""
    ax.plot(TIME_SEC, DISTANCE_CM, "o")


def graph_linear_regression(ax):
    """Plots the data and the linear regression line."""
    slope, intercept = np.polyfit(TIME_SEC, DISTANCE_CM, 1)
    delta_slope = get_delta_slope(TIME_SEC, DISTANCE_CM, slope, intercept)
    delta_intercept = get_delta_intercept(TIME_SEC, delta_slope)
    r_squared = get_r_squared(TIME_SEC, DISTANCE_CM, slope, intercept)

    print(f"Slope: {slope:.3f} +/- {delta_slope:.3f}")
    print(f"Intercept: {intercept:.3f} +/- {delta_intercept:.3f}")
    print(f"R-squared: {r_squared:.3f}")

    # use the formula for a line to plot

    ax.plot(TIME_SEC, slope * TIME_SEC + intercept)


def graph_data_log(ax):
    """Plots the logorithm of the data."""
    ax.plot(np.log(TIME_SEC), np.log(DISTANCE_CM), "o")


def graph_linear_regression_log(ax):
    """Plots the logorithm of the data and the linear regression line."""
    slope, intercept = np.polyfit(np.log(TIME_SEC), np.log(DISTANCE_CM), 1)
    delta_slope = get_delta_slope(
        np.log(TIME_SEC), np.log(DISTANCE_CM), slope, intercept
    )
    delta_intercept = get_delta_intercept(np.log(TIME_SEC), delta_slope)
    r_squared = get_r_squared(np.log(TIME_SEC), np.log(DISTANCE_CM), slope, intercept)

    print(f"Slope: {slope:.3f} +/- {delta_slope:.3f}")
    print(f"Intercept: {intercept:.3f} +/- {delta_intercept:.3f}")
    print(f"R-squared: {r_squared:.3f}")

    # use the formula for a line to plot

    ax.plot(np.log(TIME_SEC), slope * np.log(TIME_SEC) + intercept)


def main():
    """Main function."""
    fig, (ax1, ax2) = plt.subplots(ncols=2, nrows=1)
    graph_data(ax1)
    graph_linear_regression(ax1)
    graph_data_log(ax2)
    graph_linear_regression_log(ax2)
    plt.show()


if __name__ == "__main__":
    main()
