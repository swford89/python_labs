'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
# WHILE LOOP SOLUTION ############################################################################
# A) hard coded list example with even numbers
practice_list = [55,22,99,11,33,15]
sorted_list = sorted(practice_list)
copy_list = sorted_list.copy()
new_list = []

while copy_list:
    slice = tuple(copy_list[0:2])
    new_list.append(slice)
    del copy_list[0:2]
    print(f"Items remaining in copy_list: {copy_list}")
print(new_list)

# WHILE LOOP SOLUTION ############################################################################
# B) turn the user input into a list
user_nums = input("Enter a list of numbers (ex. 1 2 3 ...): ").split()

# adjust for odd number entry
if len(user_nums) % 2 == 1:
    user_nums.append(str(0))

# sort the list
user_nums_sorted = sorted(user_nums)

# convert list strings into integers
# make a copy of the list to delete the tuples from
list_of_ints = [int(strng) for strng in user_nums_sorted]
copy_ints = list_of_ints.copy()
print(f"List of user-entered sorted numbers: {list_of_ints}\nLength of list: {len(list_of_ints)}")

# initialize list holding tuples
list_of_tups = []
while copy_ints:
    int_tup = tuple(copy_ints[0:2])
    list_of_tups.append(int_tup)
    del copy_ints[0:2]

print(f"Sorted tuples from the user-entered number list: {list_of_tups}")

# COUNTER SOLUTION ############################################################################
# A) hardcoded even number list example
practice_list = [33,88,11,66,99,44]
sorted_ = sorted(practice_list) # [11,33,44,66,88,99]
list_tups = []

counter = 0
for num in sorted_[::2]:
    counter += 1
    sliced = num, sorted_[counter]
    counter += 1
    list_tups.append(sliced)

print(f"Sorted tuples from the hardcoded number list: {list_tups}\n")

# COUNTER SOLUTION ############################################################################
# B) modifying user-input to get a ordered list of tuples
user_nums = input("Enter a set of numbers (ex. 1 2 3 ...): ").split()

# if odd number of numbers, add 0
if len(user_nums) % 2 == 1:
    user_nums.append(str(0))

# convert string numbers into integers
# sort the list
list_of_ints = [int(num) for num in user_nums]
sorted_ints = sorted(list_of_ints)
print(f"Sorted list of integers: {sorted_ints}")

# initialize empty list for tuples
# set a counter to index the next number in the sequence
user_tups = []
stop_value = 0
for num in sorted_ints[::2]:
    stop_value += 1
    make_tup = num, sorted_ints[stop_value]
    stop_value += 1
    user_tups.append(make_tup)  

print(f"Sorted tuples from the user-entered numbers: {user_tups}")