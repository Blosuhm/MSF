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


# def plot_regression_line(array: list[tuple], slope: float, intercept: float):
#     """Plots a linear regression line."""
#     x = np.array([i[0] for i in array])
#     y = np.array([i[1] for i in array])
#     plt.scatter(x, y)
#     plt.plot(x, slope * x + intercept, color="red")
#     plt.show()


def main():
    """Main function."""
    array = [
        (222, 2.3),
        (207.5, 2.2),
        (194, 2),
        (171.5, 1.8),
        (153, 1.6),
        (133, 1.4),
        (113, 1.2),
        (93, 1),
    ]
    slope, intercept = linear_regression(array)
    print(slope, intercept)
    # plot_regression_line(array, slope, intercept)


if __name__ == "__main__":
    main()
