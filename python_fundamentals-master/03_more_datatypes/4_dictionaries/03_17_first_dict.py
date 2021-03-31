'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''
new_dict = {}

for num in range(1,11):
    new_dict[num] = num * num

print(f"Dictionary with a key of 'n' and a value of 'n * n': \n{new_dict}")