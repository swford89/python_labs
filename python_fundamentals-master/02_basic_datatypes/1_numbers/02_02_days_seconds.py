'''

Write a script that takes in a number in days from the user between 1 and 1,000,000,000 and convert it to seconds.

NOTE: We will use the input() funtion to collect users input. An example is demonstrated below.

'''

# the input of the user will be saved in the variable days.
# because the input() function collects the input as a string, we have to convert it to an int
# The string passed to the input() function is what the user is prompted with
days = int(input("Please enter a number in days between 1 and 1,000,000,000: "))

# 60 seconds in 1 minute
# 60 minutes in 1 hour
# 24 hours in 1 day
days_in_seconds = 60 * 60 * 24 * days
print(f"There are {days_in_seconds:,} seconds in {days} days")
