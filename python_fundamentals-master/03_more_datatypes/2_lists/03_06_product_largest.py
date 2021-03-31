'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
num_list = []
num_sum = 0
biggest_num = 0

for num in range(10):
    num = int(input("Enter a whole number: "))
    num_list.append(num)
    if num > biggest_num:
        biggest_num = num

print(f"Here's a list of all the entered numbers: {num_list}")
print(f"The biggest number you entered: {max(num_list)}")
print(f"This is the biggest number (without using max()): {biggest_num}")

for num in num_list:
    num_sum += num

print(f"The sum of all the numbers you entered: {num_sum}")

