import numpy as np

GRAVITY = 9.81
AIR_DENSITY = 1.225
G = 6.67408e-11
K = 8.9875517923e9


def air_resistance_force_with_vt(terminal_velocity, velocity, mass, *, gravity=GRAVITY):
    """Calculates the air resistance force.

    Args:
    -----
        terminal_velocity (float): Terminal velocity.

        velocity (np.array): Velocity vector.

        mass (float): Mass of the object.

        gravity (float, optional): Gravity. Defaults to 9.81m/s².


    Formula:
    --------
        F = -m * D * |v|² * û

        m = mass

        D = g / v_t²

        g = gravitational acceleration

        v_t = terminal velocity

        v = velocity vector

        û = unit vector of velocity

    """

    D = gravity / np.power(terminal_velocity, 2)
    velocity_norm = np.linalg.norm(velocity)
    unit_velocity = velocity / velocity_norm

    return -mass * D * np.power(velocity_norm, 2) * unit_velocity


def air_resistance_force(resistance_coefficient, area, velocity):
    """Calculates the air resistance force.

    Args:
    -----
        resistance_coefficient (float): Resistance coefficient.

        area (float): Area of the object.

        velocity (np.array): Velocity vector.


    Formula:
    --------
        F = -C_res/2 * A * p * |v|² * û

        C_res = resistance coefficient

        A = area

        p = air density

        v = velocity vector

        û = unit vector of velocity

    """
    velocity_norm = np.linalg.norm(velocity)

    return -resistance_coefficient / 2 * area * AIR_DENSITY * velocity_norm * velocity


def newton_gravity_force(mass1, mass2, distance):
    """Calculates the gravitational force between two objects.

    Args:
    -----
        mass1 (float): Mass of the first object.

        mass2 (float): Mass of the second object.

        distance (np.array): Distance vector between the two objects.


    Formula:
    --------
        F = G * m1 * m2 / |r|² * û

        G = gravitational constant

        m1 = mass of the first object

        m2 = mass of the second object

        r = distance vector between the two objects

        û = unit vector of the distance vector

    """
    distance_norm = np.linalg.norm(distance)
    unit_distance = distance / distance_norm

    return G * mass1 * mass2 / np.power(distance_norm, 2) * unit_distance


def weight(mass, *, gravity=GRAVITY):
    """Calculates the weight of an object.

    Args:
    -----
        mass (float): Mass of the object.

        gravity (float, optional): Gravity. Defaults to 9.81m/s².


    Formula:
    --------
        P = m * g

        m = mass

        g = gravitational acceleration

    """
    return mass * gravity


def electrostatic_force(charge1, charge2, distance):
    """Calculates the electrostatic force between two objects.

    Args:
    -----
        charge1 (float): Charge of the first object.

        charge2 (float): Charge of the second object.

        distance (np.array): Distance vector between the two objects.


    Formula:
    --------
        F = K * q1 * q2 / |r|² * û

        K = Coulomb's constant

        q1 = charge of the first object

        q2 = charge of the second object

        r = distance vector between the two objects

        û = unit vector of the distance vector

    """

    distance_norm = np.linalg.norm(distance)
    unit_distance = distance / distance_norm

    return K * charge1 * charge2 / np.power(distance_norm, 2) * unit_distance


def magnetic_force(charge, velocity, magnetic_field):
    """Calculates the magnetic force on a moving charge.

    Args:
    -----
        charge (float): Charge of the object.

        velocity (np.array): Velocity vector of the object.

        magnetic_field (np.array): Magnetic field vector.


    Formula:
    --------
        F = q * v x B

        q = charge

        v = velocity vector

        B = magnetic field vector

        (Note: "x" is the cross product)

    """
    return charge * np.cross(velocity, magnetic_field)


def magnus_force(
    section_area, radius, rotation_vector, velocity, *, air_density=AIR_DENSITY
):
    """Calculates the Magnus force on a rotating object.

    Args:
    -----
        section_area (float): Section area of the object.

        air_density (float): Air density.

        radius (float): Radius of the object.

        rotation_vector (np.array): Rotation vector of the object.

        velocity (np.array): Velocity vector of the object.


    Formula:
    --------
        F = 1/2 * A * p * r * w x v

        A = section area

        p = air density

        r = radius

        w = rotation vector

        v = velocity vector

    """
    return section_area / 2 * air_density * radius * np.cross(rotation_vector, velocity)


def friction_force(friction_coefficient, normal_force, velocity):
    """Calculates the friction force.

    Args:
    -----
        friction_coefficient (float): Friction coefficient.

        normal_force (np.array): Normal force vector.

        velocity (np.array): Velocity vector.


    Formula:
    --------
        F = -mu * |N| * û

        mu = friction coefficient

        N = normal force vector

        û = unit vector of the velocity vector

    """
    velocity_norm = np.linalg.norm(velocity)
    unit_velocity = velocity / velocity_norm
    normal_force_norm = np.linalg.norm(normal_force)

    return -friction_coefficient * normal_force_norm * unit_velocity


def get_gravity_projections(inclination, mass, *, gravity=GRAVITY, degrees=False):
    """Calculates the projections of the gravity vector.

    Args:
    -----
        inclination (float): Inclination of the gravity vector.

        mass (float): Mass of the object.

        gravity (float, optional): Gravity. Defaults to 9.81m/s².

        degrees (bool, optional): If the inclination is in degrees. Defaults to False.


    Formula:
    --------
        Px = m * g * cos(θ)

        Py = m * g * sin(θ)

        m = mass

        g = gravitational acceleration

        θ = inclination

    """
    if degrees:
        inclination = np.deg2rad(inclination)

    gravity_x = mass * gravity * np.sin(inclination)
    gravity_y = mass * gravity * np.cos(inclination)
    return gravity_x, gravity_y


def power2force(power, velocity):
    """Calculates the force of an object.

    Args:
    -----
        power (float): Power of the object.

        velocity (np.array): Velocity vector.


    Formula:
    --------
        F = P / |v|

        P = power

        v = velocity vector

    """
    velocity_norm = np.linalg.norm(velocity)
    unit_velocity = velocity / velocity_norm
    return power / velocity_norm * unit_velocity


def force2acceleration(force, mass):
    """Calculates the acceleration of an object.

    Args:
    -----
        force (np.array): Force vector.

        mass (float): Mass of the object.


    Formula:
    --------
        a = F / m

        F = force vector

        m = mass

    """
    return force / mass


def trapezoidal_integral(function_array, n, dt):
    """Calculates the integral of a function using the trapezoidal rule.

    Args:
    -----
        function_array (np.array): Array of the function values.

        n (int): Number of points.

        dt (float): Time step.


    Formula:
    --------
        I = dt * (f0 + fn-1) / 2 + sum(fi)

        dt = time step

        f0 = first value of the function

        fn-1 = last value of the function

        fi = value of the function at the i-th point

    """

    for i, _ in enumerate(function_array):
        function_array[i] = np.linalg.norm(function_array[i])

    return dt * (
        (function_array[0] + function_array[n - 1]) / 2
        + np.sum(function_array[1 : n - 1])
    )


def kinetic_energy(mass, velocity):
    """Calculates the kinetic energy of an object.

    Args:
    -----
        mass (float): Mass of the object.

        velocity (np.array): Velocity vector.


    Formula:
    --------
        E_k = 1/2 * m * |v|²

        m = mass

        v = velocity vector

    """
    velocity_norm = np.linalg.norm(velocity)
    return 1 / 2 * mass * np.power(velocity_norm, 2)


def gravitational_potential_energy(mass, height, *, gravity=GRAVITY):
    """Calculates the gravitational potential energy of an object.

    Args:
    -----
        mass (float): Mass of the object.

        height (float): Height of the object.

        gravity (float, optional): Gravity. Defaults to 9.81m/s².


    Formula:
    --------
        E_p = m * h * g

        m = mass

        h = height

        g = gravitational acceleration

    """

    return mass * height * gravity


def horse2watt(horse):
    """Converts horse power to watt.

    Args:
    -----
        horse (float): Horse power.


    Formula:
    --------
        W = 745.7 * HP

        W = watt

        HP = horse power

    """
    return 735.5 * horse
