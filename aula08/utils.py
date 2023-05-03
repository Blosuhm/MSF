import numpy as np
import matplotlib.pyplot as plt


fig, default_ax = plt.subplots(1, 3, figsize=(16, 8))


def euler_method(
    time_array,
    time_step,
    *,
    initial_acceleration=np.array([0, 0, 0]),
    initial_velocity=np.array([0, 0, 0]),
    initial_position=np.array([0, 0, 0]),
    acceleration_formula=lambda a, v: a,
    cromer=False
):
    """
    Euler method for solving differential equations.

    Parameters
    ----------
    time_array : array_like

    time_step : float

    initial_acceleration : float, optional
        Default is 0.

    initial_velocity : float, optional
        Default is 0.

    initial_position : float, optional
        Default is 0.

    acceleration_formula : callable, optional
        Default is lambda a, v: a.
        Note the function should take three arguments (acceleration, velocity).

    cromer : bool, optional
        Default is False.

    Returns
    -------
    acceleration_array : ndarray
        Array of accelerations.

    velocity_array : ndarray
        Array of velocities.

    position_array : ndarray
        Array of positions.
    """
    n = len(time_array)

    acceleration_array = np.array([np.zeros(3)] * n)
    velocity_array = np.array([np.zeros(3)] * n)
    position_array = np.array([np.zeros(3)] * n)

    acceleration_array[0] = initial_acceleration
    velocity_array[0] = initial_velocity
    position_array[0] = initial_position

    for i in range(n - 1):
        acceleration_array[i + 1] = acceleration_formula(
            acceleration_array[i], velocity_array[i]
        )

        velocity_array[i + 1] = velocity_array[i] + acceleration_array[i] * time_step

        cromer_index = i + 1 if cromer else i
        position_array[i + 1] = (
            position_array[i] + velocity_array[cromer_index] * time_step
        )

    return position_array, velocity_array, acceleration_array


def graph(ax, time_array, array, title, *, x_label=None, y_label=None, grid=False):
    """
    Graph an array.

    Parameters
    ----------
    array : array_like

    time_array : array_like

    title : str
    """

    ax.plot(time_array, array)
    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.grid(grid)


def graph_all(
    ax_array,
    time_array,
    array_array,
    title_array,
    *,
    x_label_array=None,
    y_label_array=None,
    grid=False
):
    """
    Graph multiple arrays.

    Parameters
    ----------
    ax_array : array_like

    time_array : array_like

    array_array : array_like

    title_array : array_like

    x_label_array : array_like, optional
        Default is None.

    y_label_array : array_like, optional
        Default is None.

    grid : bool, optional
    """
    if x_label_array is None:
        x_label_array = [None] * len(array_array)

    if y_label_array is None:
        y_label_array = [None] * len(array_array)

    to_zip = (ax_array, array_array, title_array, x_label_array, y_label_array)

    for ax, array, title, x_label, y_label in zip(*to_zip):
        graph(ax, time_array, array, title, x_label=x_label, y_label=y_label, grid=grid)


def get_axis(array, axis):
    """
    Get an axis from an array.

    Parameters
    ----------
    array : array_like

    axis : int

    Returns
    -------
    axis_array : list
    """
    return list(zip(*array))[axis]
