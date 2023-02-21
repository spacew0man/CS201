def compute_acceleration():  # Computes acceleration of an object based on its force and mass
    print('Enter force: ')
    force = float(input())
    print('Enter mass: ')
    mass = float(input())
    acceleration = force / mass
    print(acceleration)
    return force / mass


def compute_wavelength():  # Computes the color of light based on its frequency
    print('Enter frequency: ')
    frequency = float(input())
    wavelength = 3E8 / frequency
    print(wavelength)
    return 3E8 / frequency


def compute_distance():  # Computes the distance of celestial bodies based on its speed
    print('Enter speed: ')
    speed = float(input())
    distance = speed / 73
    print(distance)
    return speed / 73


compute_acceleration()
compute_wavelength()
compute_distance()
