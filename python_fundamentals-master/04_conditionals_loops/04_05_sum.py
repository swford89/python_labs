'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''
first_num = int(input("Enter a number:"))
second_num = int(input("Enter a second number, which is larger than the your first: "))

num_sum = 0

for num in range(first_num, second_num + 1):
    num_sum += num

print(f"The sum of {first_num}, {second_num}, and all the whole numbers in between: {num_sum}")