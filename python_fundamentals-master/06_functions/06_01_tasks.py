'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

def four_or_seven_divisible(num):
    if num % 4 == 0 or num % 7 == 0:
        result_or = f"{num % 4 == 0 or num % 7 == 0}"
        print(f"{result_or}. {num} is divisible by 4 or 7.")
    else:
        result_or = num % 4 == 0 or num % 7 == 0
    
    return result_or

four_or_seven_divisible(36)
four_or_seven_divisible(49)

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

def four_and_seven_divisible(num):
    if num % 4 == 0 and num % 7 == 0:
        result_and = f"{num % 4 == 0 and num % 7 == 0}"
        print(f"{result_and}. {num} is divisible by BOTH 4 and 7.")
    else:
        result_and = num % 4 == 0 and num % 7 == 0
    
    return result_and

four_and_seven_divisible(56)

# take in a number from the user between 1 and 1,000,000,000

user_num = int(input("Enter a whole number between 1 and 1,000,000,000: "))

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

result_or = four_or_seven_divisible(user_num)
result_and = four_and_seven_divisible(user_num)

# print your new variables to display the results
print(f"Is {user_num} divisible by 4 or 7: {result_or}")
print(f"Is {user_num} divisible by BOTH 4 and 7: {result_and}")