from space.planet import Planet
from space.calc import planet_mass,planet_vol

planet=Planet("Earth",490000,6,"Earth system")

earth_mass=planet_mass(planet.gravity, planet.radius)
earth_volume=planet_vol(planet.radius)

print(f"The mass is==={earth_mass}")
print(f"The volume is==={earth_volume}")