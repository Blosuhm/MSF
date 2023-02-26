import numpy as np
import matplotlib.pyplot as plt


def linear_regression(array: list[tuple]):
    """Returns the slope and intercept of a linear regression line."""
    N = array.size
    sum_xy = np.sum(array[:, 0] * array[:, 1])
    sum_x = np.sum(array[:, 0])
    sum_y = np.sum(array[:, 1])
    sum_x2 = np.sum(array[:, 0] ** 2)
    sum_y2 = np.sum(array[:, 1] ** 2)
    slope = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - sum_x**2)

    # TODO: Fix intercept
    # intercept = np.mean(y) - slope * np.mean(x)
    intercept = 0
    return slope, intercept


def plot_regression_line(array: list[tuple], slope: float, intercept: float):
    """Plots a linear regression line."""
    x = np.array([i[0] for i in array])
    y = np.array([i[1] for i in array])
    plt.scatter(x, y)
    plt.plot(x, slope * x + intercept, color="red")
    plt.show()


if __name__ == "__main__":
    main()
