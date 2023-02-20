from modules.linear_regression import linear_regression, plot_regression_line
import numpy as np


def main():
    """Main function."""
    array = np.array(
        [
            (222, 2.3),
            (207.5, 2.2),
            (194, 2),
            (171.5, 1.8),
            (153, 1.6),
            (133, 1.4),
            (113, 1.2),
            (93, 1),
        ]
    )

    N = array.size
    sum_xy = np.sum(array[:, 0] * array[:, 1])
    sum_x = np.sum(array[:, 0])
    sum_y = np.sum(array[:, 1])
    sum_x2 = np.sum(array[:, 0] ** 2)
    sum_y2 = np.sum(array[:, 1] ** 2)
    slope = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - sum_x**2)

    print(slope)
    slope, intercept = linear_regression(array)
    plot_regression_line(array, slope, intercept)


if __name__ == "__main__":
    main()
