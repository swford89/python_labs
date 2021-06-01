'''
Using a list comprehension, create a *cartesian product* (google this!)
of the given lists.

Then open up your online shop ;)

'''

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

new_list = []

for color in colors:
    for size in sizes:
        color_size = f'{color}: {size}'
        new_list.append(color_size)
print(new_list)

colour_size = [f'{color}: {size}' for color in colors for size in sizes]
print(colour_size)
