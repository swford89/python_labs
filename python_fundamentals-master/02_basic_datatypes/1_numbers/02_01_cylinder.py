'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
from math import pi

cylinder_radius = 3.14
cylinder_height = 5
cylinder_volume = pi * cylinder_radius**2 * cylinder_height
print(f"Volume of the cylinder: {cylinder_volume}")

cylinder_surface_area = (2 * pi * cylinder_radius * cylinder_height) + (2 * pi * cylinder_radius**2)
print(f"Surface area of this cylinder: {cylinder_surface_area}")