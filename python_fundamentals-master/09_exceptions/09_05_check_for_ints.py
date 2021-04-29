'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

while True:

    try:
        integer_prompt = int(input("Enter any integer: "))
        if type(integer_prompt) == int:
            break

    except ValueError:
        print("""
        What you entered doesn't seem to be an integer. Try again.
        """)