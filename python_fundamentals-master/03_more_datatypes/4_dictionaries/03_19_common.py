'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}
result_dict = {}

for key in dict_1.keys():
    if key in dict_2.keys():
        result_dict[key] = dict_1[key] + dict_2[key]
    elif key not in dict_2.keys():
        result_dict[key] = dict_1[key]

for key in dict_2.keys():
    if key not in dict_1.keys():
        result_dict[key] = dict_2[key]

print(result_dict)
