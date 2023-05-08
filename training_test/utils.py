import numpy as np
import matplotlib.pyplot as plt


def euler_method(
    time_array,
    time_step,
    *,
    initial_acceleration=np.zeros(3),
    initial_velocity=np.zeros(3),
    initial_position=np.zeros(3),
    acceleration_formula=lambda a, v, p: a,
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

    acceleration_array = np.zeros((n, 3))
    velocity_array = np.zeros((n, 3))
    position_array = np.zeros((n, 3))

    acceleration_array[0] = initial_acceleration
    velocity_array[0] = initial_velocity
    position_array[0] = initial_position

    for i in range(n - 1):
        acceleration_array[i + 1] = acceleration_formula(
            acceleration_array[i], velocity_array[i], position_array[i]
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
    # Ignore this cuz its just stupid
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


def find_instant(array, time_array, value):
    """
    Find the instant of a value in an array.

    Parameters
    ----------
    array : array_like

    value : float

    Returns
    -------
    instant : float
    """
    idx = -1
    for i, v in enumerate(array):
        if v == 0 or (v - value) * (array[i + 1] - value) < 0:
            idx = i
            break

    if idx == -1:
        return None

    closest = min(array[idx], array[idx + 1], key=lambda x: abs(x - value))
    time = time_array[idx]

    return time, closest


def time2index(array, time_step, time):
    """
    Convert time to index.

    Parameters
    ----------
    array : array_like

    time_step : float

    time : float

    Returns
    -------
    value : float

    time_idx : int
    """

    time_idx = int(np.ceil(time / time_step))
    value = array[time_idx]

    return value, time_idx


def find_max(array, time_array):
    """
    Find the maximum value in an array.

    Parameters
    ----------
    array : array_like

    time_array : array_like

    Returns
    -------
    time : float

    value : float
    """
    idx = np.argmax(array)
    time = time_array[idx]
    value = array[idx]

    return time, value


def kmh2ms(kmh):
    """
    Convert km/h to m/s.

    Parameters
    ----------
    kmh : float

    Returns
    -------
    ms : float
    """
    return kmh / 3.6


def get_x_y_components(value, angle, *, degrees=False):
    """
    Get the x and y components of a value.

    Parameters
    ----------
    value : float

    angle : float

    Returns
    -------
    x_component : float

    y_component : float
    """
    if degrees:
        angle = np.deg2rad(angle)
    x_component = value * np.cos(angle)
    y_component = value * np.sin(angle)

    return x_component, y_component


def find_index(array, value):
    """
    Find the index of a value in an array.

    Parameters
    ----------
    array : array_like

    value : float

    Returns
    -------
    index : int
    """
    idx = -1
    for i, v in enumerate(array):
        if v == value or (v - value) * (array[i + 1] - value) < 0:
            idx = i
            break

    closest = min(array, key=lambda x: abs(x - value))
    if idx == -1:
        idx = np.where(array == closest)[0][0]
    return idx, closest
