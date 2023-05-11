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
        acceleration_formula=acceleration_formula,
    )

    new_pos_ar, new_vel_ar, new_acc_ar = u.euler_method(
        TIME,
        TIME_STEP,
        initial_acceleration=new_init_acc,
        initial_velocity=new_init_vel,
        initial_position=new_init_pos,
        acceleration_formula=new_acc_formula,
    )

    # Processing data

    x = u.get_axis(position_array, 0)

    idx_x, closest = u.find_index(x, 2000)
    time_at_2km = TIME[idx_x]
    print(f"x: {closest}")
    print(f"b) time at 2km: {time_at_2km} s")

    position_x = position_array[:, 0]
    velocity_x = velocity_array[:, 0]

    work = f.trapezoidal_integral(force_list, idx_x, TIME_STEP)

    print(f"c) work until 332.67: {work} J")

    print()

    new_x = u.get_axis(new_pos_ar, 0)
    new_idx_x, new_closest = u.find_index(new_x, 2000)
    new_time_at_2km = TIME[new_idx_x]
    print(f"x: {new_closest}")
    print("d) nao acabado")

    # Graphs
    fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

    u.graph(
        ax0,
        TIME,
        position_x,
        "position",
        x_label="t (s)",
        y_label="x (m)",
    )

    u.graph(
        ax1,
        TIME,
        velocity_x,
        "velocity",
        x_label="t (s)",
        y_label="v (m/s)",
    )

    plt.show()


force_list = []

new_force_list = []


def acceleration_formula(a, v, p):
    gravity_force = np.array([-mass * f.GRAVITY * np.sin(np.deg2rad(5)), 0, 0])
    normal_force = np.array([0, mass * f.GRAVITY * np.cos(np.deg2rad(5)), 0])
    air_resistance = f.air_resistance_force(air_resistance_coefficient, frontal_area, v)
    friction = f.friction_force(friction_coefficient, normal_force, v)
    vehicle_force = f.power2force(power, v)
    force = air_resistance + friction + vehicle_force + gravity_force
    force_list.append(force)

    acceleration = f.force2acceleration(force, mass)

    return acceleration


def new_acc_formula(a, v, p):
    gravity_force = np.array([mass * f.GRAVITY * np.sin(np.deg2rad(5)), 0, 0])
    normal_force = np.array([0, mass * f.GRAVITY * np.cos(np.deg2rad(5)), 0])
    air_resistance = f.air_resistance_force(air_resistance_coefficient, frontal_area, v)
    friction = f.friction_force(friction_coefficient, normal_force, v)
    vehicle_force = f.power2force(new_power, v)
    force = air_resistance + friction + vehicle_force + gravity_force
    new_force_list.append(force)

    acceleration = f.force2acceleration(force, mass)

    return acceleration


# Time

TIME_STEP = 0.01
START_TIME, END_TIME = 0, 500
TIME = np.arange(START_TIME, END_TIME, TIME_STEP)
N = TIME.size

# Variables

mass = 2000  # kg
power = 40000  # W
new_power = 10000  # W
friction_coefficient = 0.25
air_resistance_coefficient = 0.9
frontal_area = 2  # m²

# Initial conditions

initial_position = np.array([0, 0, 0])
initial_velocity = np.array([1, 0, 0])
initial_acceleration = acceleration_formula(0, initial_velocity, 0)

new_init_pos = np.array([0, 0, 0])
new_init_vel = np.array([20, 0, 0])
new_init_acc = new_acc_formula(0, new_init_vel, 0)


if __name__ == "__main__":
    main()
