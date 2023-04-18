import numpy as np


def euler_method(
    time_array,
    time_step,
    *,
    initial_acceleration=0,
    initial_velocity=0,
    initial_position=0,
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
    acceleration_array = np.zeros(n)
    velocity_array = np.zeros(n)
    position_array = np.zeros(n)

    acceleration_array[0] = initial_acceleration
    velocity_array[0] = initial_velocity
    position_array[0] = initial_position

    for i in range(n - 1):
        acceleration_array[i + 1] = acceleration_formula(
            acceleration_array[i], velocity_array[i], position_array[i]
        )
        velocity_array[i + 1] = (
            velocity_array[i] + acceleration_array[i + 1] * time_step
        )
        cromer_index = i + 1 if cromer else i
        position_array[i] = velocity_array[cromer_index] + velocity_array[i + 1]

    return acceleration_array, velocity_array, position_array
