import numpy as np
import matplotlib.pyplot as plt
import modules.linear_regression as lr

DISTANCE_ARRAY = np.array(
    [0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.666, 6.329]
)
TIME_RANGE_MIN = np.arange(0, DISTANCE_ARRAY.size)
TIME_RANGE_MIN_CONTINUOUS = np.linspace(0, DISTANCE_ARRAY.size - 1, 1000)


def graph_points():
    plt.plot(TIME_RANGE_MIN, DISTANCE_ARRAY, "o")


def graph_line(slope, intercept):
    plt.plot(TIME_RANGE_MIN, slope * TIME_RANGE_MIN + intercept)


def graph_polyfit():
    coefficients = np.polyfit(TIME_RANGE_MIN, DISTANCE_ARRAY, 1)
    print(coefficients)
    line_function = np.poly1d(coefficients)
    plt.plot(TIME_RANGE_MIN_CONTINUOUS, line_function(TIME_RANGE_MIN_CONTINUOUS))


def main():
    graph_points()

    slope, intercept, r2 = lr.linear_regression(
        np.column_stack((TIME_RANGE_MIN, DISTANCE_ARRAY))
    )

    graph_polyfit()

    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")
    print(f"R²: {r2}")

    graph_line(slope, intercept)

    plt.show()


if __name__ == "__main__":
    main()
