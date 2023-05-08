import numpy as np
import matplotlib.pyplot as plt
import formulas as f
import utils as u


def main():
    position_array, velocity_array, acceleration_array = u.euler_method(
        TIME,
        TIME_STEP,
        initial_acceleration=initial_acceleration,
        initial_velocity=initial_velocity,
        initial_position=initial_position,
        acceleration_formula=acceleration_formula_inclination,
    )

    # Processing data

    x = u.get_axis(position_array, 0)

    idx_x, closest = u.find_index(x, 2000)
    time_at_2km = TIME[idx_x]
    print(idx_x, closest)
    print(f"b) time at 2km: {time_at_2km}")

    # Graphs
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(16, 8))

    u.graph_all(
        ax,
        TIME,
        [position_array, velocity_array, acceleration_array],
        ["position", "velocity", "acceleration"],
        x_label_array=["t (s)"] * 3,
        y_label_array=["x (m)", "v (m/s)", "a (m/s²)"],
    )

    plt.show()


def acceleration_formula(a, v, p):
    air_resistance = f.air_resistance_force(air_resistance_coefficient, frontal_area, v)
    friction = f.friction_force(friction_coefficient, f.GRAVITY * mass, v)
    vehicle_force = f.power2force(power, v)
    force = air_resistance + friction + vehicle_force

    acceleration = f.force2acceleration(force, mass)

    return acceleration


def acceleration_formula_inclination(a, v, p):
    # setup
    normal, gravity = u.get_x_y_components(f.GRAVITY * mass, 4, degrees=True)

    gravity_force = np.array([-gravity, 0, 0])

    if p[0] > 1500:
        normal, gravity = u.get_x_y_components(f.GRAVITY * mass, 1, degrees=True)
        gravity_force = np.array([gravity, 0, 0])

    # forces
    air_resistance = f.air_resistance_force(air_resistance_coefficient, frontal_area, v)
    friction = f.friction_force(friction_coefficient, normal, v)
    vehicle_force = f.power2force(power, v)
    force = air_resistance + friction + vehicle_force + gravity_force
    acceleration = f.force2acceleration(force, mass)

    return acceleration


# Variables

mass = 60 + 12  # kg
power = f.horse2watt(0.48)  # W
friction_coefficient = 0.01
air_resistance_coefficient = 0.9
frontal_area = 0.5  # m²

# Initial conditions

initial_position = np.array([0, 0, 0])
initial_velocity = np.array([0.5, 0, 0])
initial_acceleration = acceleration_formula(0, initial_velocity, 0)


# Time

TIME_STEP = 0.001
START_TIME, END_TIME = 0, 350
TIME = np.arange(START_TIME, END_TIME, TIME_STEP)
N = TIME.size

if __name__ == "__main__":
    main()
