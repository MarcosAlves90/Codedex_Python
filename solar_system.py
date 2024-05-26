# Write code below 💖

from math import pi; from random import choice as ch

planets = {
    'Mercúrio': 2440,
    'Vênus': 6052,
    'Terra': 6371,
    'Marte': 3390,
    'Saturno': 58232
}

random_planet = ch(list(planets.keys()))

r = 4 * pi * planets[random_planet] ** 2

if r:
    print(f"O raio do planeta \"{random_planet}\" é {round(r)} km².")
else:
    print("Oops! Um erro ocorreu.")