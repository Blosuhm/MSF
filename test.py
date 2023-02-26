from modules.linear_regression import linear_regression, plot_regression_line
import numpy as np
import matplotlib.pyplot as plt


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

    print(slope)
    # slope, intercept = linear_regression(array)
    # plot_regression_line(array, slope, intercept)
    m, b = np.polyfit(array[:, 0], array[:, 1], 1)
    plot_regression_line(array, m, b)


if __name__ == "__main__":
    main()
