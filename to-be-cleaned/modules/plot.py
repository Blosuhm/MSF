import matplotlib.pyplot as plt

id_gen = iter(range(1, 10))


def plot(x_array, y_array, *, title="", x_label="", y_label="", rows=None, cols=None):
    """Plots a graph."""
    if rows and cols:
        plt.subplot(rows * 100 + cols * 10 + next(id_gen))
    plt.plot(x_array, y_array)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
