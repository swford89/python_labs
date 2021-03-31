'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]

print(f"The list prior to removing duplicates: {list_}")

for num in list_:
    if list_.count(num) > 1:
        list_.remove(num) # removes first occurence of number; numbers still in order because of the 3, 4 after

print(f"The list after removing duplicates: {list_}")