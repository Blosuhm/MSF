import numpy as np
import matplotlib.pyplot as plt


def linear_regression(array: list[tuple]):
    """Returns the slope and intercept of a linear regression line."""
    x = np.array([i[0] for i in array])
    y = np.array([i[1] for i in array])
    slope = (np.mean(x) * np.mean(y) - np.mean(x * y)) / (
        np.mean(x) ** 2 - np.mean(x**2)
    )
    intercept = np.mean(y) - slope * np.mean(x)
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
