import numpy as np
import math


def linear_regression(array):
    """Returns the slope and intercept of a linear regression line."""
    N = array.size
    sum_xy = np.sum(array[:, 0] * array[:, 1])
    sum_x = np.sum(array[:, 0])
    sum_y = np.sum(array[:, 1])
    sum_x2 = np.sum(np.power(array[:, 0], 2))
    sum_y2 = np.sum(np.power(array[:, 1], 2))

    slope = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - math.pow(sum_x, 2))
    intercept = (sum_x2 * sum_y - sum_x * sum_xy) / (N * sum_x2 - math.pow(sum_x, 2))

    r2 = math.pow((N * sum_xy - sum_x * sum_y), 2) / (
        (N * sum_x2 - math.pow(sum_x, 2)) * (N * sum_y2 - math.pow(sum_y, 2))
    )

    return slope, intercept, r2


def get_r_squared(x, y, slope, intercept):
    """Returns the r-squared value of a linear regression line."""
    y_pred = slope * x + intercept
    r_squared = 1 - (np.sum(np.power(y - y_pred, 2)) / ((len(y) - 1) * np.var(y)))
    return r_squared


def get_delta_slope(x, y, slope, intercept):
    """Returns the delta slope of a linear regression line."""
    y_pred = slope * x + intercept
    delta_m = np.sqrt(np.sum(np.power(y_pred - y, 2)) / (len(x) - 2)) / np.sqrt(
        np.sum(np.power(x - np.mean(x), 2))
    )
    return delta_m


def get_delta_intercept(x, delta_m):
    """Returns the delta intercept of a linear regression line."""
    delta_b = delta_m * np.sqrt(np.sum(np.power(x, 2)) / len(x))
    return delta_b
