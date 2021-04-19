'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():
    
    def __init__(self, name, sun_distance) -> None:
        self.name = name
        self.sun_distance = sun_distance

    def __str__(self) -> str:
        return f"Planet {self.name}"

mercury = Planet("Mercury", 0.4)
venus = Planet("Venus", 0.7)
earth = Planet("Earth", 1.0)
mars = Planet("Mars", 1.5)
jupiter = Planet("Jupiter", 5.2)
saturn = Planet("Saturn", 9.5)
uranus = Planet("Uranus", 19.0)
neptune = Planet("Neptune", 30.0)
pluto = Planet("Pluto", 39.5)

solar_system_list = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]

for planet in solar_system_list:
    print(f"{planet.name} is {planet.sun_distance} AU from the sun.")
