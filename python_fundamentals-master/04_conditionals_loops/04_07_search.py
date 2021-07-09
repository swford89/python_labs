'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
while True:
    try:
        user_num = int(input('Enter a number between 0 and 1,000,000,000: '))
        break
    except ValueError:
        print("""
        You're only allowed to enter an integer.
        """)

counter = 0
while counter < 1000000000:
    if counter == user_num:
        print(f"Found the number you entered: {counter}")
        break
    else:
        print(counter)
        counter += 1