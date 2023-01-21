print('What is the mass of the planet?')
planet_mass = float(input())
print('What is the radius of the planet?')
planet_radius = float(input())
GRAVITATIONAL_CONSTANT = 6.674E-11
acceleration = GRAVITATIONAL_CONSTANT * planet_mass / (planet_radius ** 2)
print('The acceleration is ' + str(acceleration))