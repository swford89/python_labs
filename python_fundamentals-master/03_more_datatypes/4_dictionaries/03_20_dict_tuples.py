'''
CHALLENGE: Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

NOTE: Check out the Python docs and see whether you can come up with a solution, even if you don't yet
      completely understand _why_ it works the way it does:
      https://docs.python.org/3/howto/sorting.html#key-functions
      Feel free to discuss any questions you have with your mentor and on the forum!

'''
input_dict = {"item1": 5, "item2": 6, "item3": 1}
sorted_items = sorted(input_dict.items())
sorted_values = sorted(sorted_items, key=lambda x: x[1])

print(f"List of the sorted items in the dictionary:\n{sorted_items}")
print(f"Same list but sorted by values, with a lambda function that sorted the tuple items by their 1st index:\n{sorted_values}")
