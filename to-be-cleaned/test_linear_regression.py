import modules.linear_regression as lr
import numpy as np
import matplotlib.pyplot as plt

ARRAY = np.array(
    [
        (222.0, 2.3),
        (207.5, 2.2),
        (194.0, 2.0),
        (171.5, 1.8),
        (153.0, 1.6),
        (133.0, 1.4),
        (113.0, 1.2),
        (92.0, 1.0),
    ]
)
X_RANGE = np.linspace(0, 250)


def main():
    slope, intercept, r2 = lr.linear_regression(ARRAY)

    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")
    print(f"R²: {r2}")

    plt.plot(ARRAY[:, 0], ARRAY[:, 1], "o")
    plt.plot(X_RANGE, slope * X_RANGE + intercept)

    plt.xlabel("Distance (m)")
    plt.ylabel("Distance (m)")
    plt.title("Linear Regression")
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    main()
