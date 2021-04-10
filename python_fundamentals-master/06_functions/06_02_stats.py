'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list_):
  # define the function here
  list_sum = 0
  stats_dict = {}
  for num in list_:
    list_sum += num
  stats_dict['max_value'] = max(list_)
  stats_dict['min_value'] = min(list_)
  stats_dict['sum'] = list_sum

  print(f"Biggest value in the list: {max(list_)}")
  print(f"Smallest value in the list: {min(list_)}")
  print(f"The average of the values in the list: {list_sum / len(list_)}")
  print(f"The sum of all the values in the list: {list_sum}")
  return stats_dict

# call the function below here
stats(example_list)