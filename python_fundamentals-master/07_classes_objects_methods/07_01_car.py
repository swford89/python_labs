'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car():
    
    def __init__(self, model, year, max_speed) -> None:
        """ initializing the attributes for our Car instances """
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self) -> str:
        return f"{self.year} {self.model}"

    def speed_upgrade(self):
        """ to increase the car's max speed """
        self.max_speed += 5
        return self.max_speed

mitsubishi_lancer = Car("Mitsubishi Lancer", 2019, 220)
kia_sorento = Car("Kia Sorento", 2019, 250)

print(mitsubishi_lancer)
print(mitsubishi_lancer.max_speed)
print(mitsubishi_lancer.speed_upgrade())
print(f"{mitsubishi_lancer.model} with a max speed of {mitsubishi_lancer.max_speed}")