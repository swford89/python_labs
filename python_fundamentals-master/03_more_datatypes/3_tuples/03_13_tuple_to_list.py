'''
Write a script that takes a tuple and turns it into a list.

'''
some_tup = ('singleton',)
print(f"{some_tup} is: {type(some_tup)}")
singleton_list = list(some_tup)
print(f"{singleton_list} is: {type(singleton_list)}")