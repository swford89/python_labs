'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
while True:
    
    try:
        numerator = int(input("Enter a number for your numerator: "))
        denominator = int(input("Enter a second number for your denominator: "))
        quotient = numerator / denominator
        print(f"{numerator} divided by {denominator} give you the quotient: {quotient}")
        break
    
    except ValueError:
        print("""
        Make sure to enter a number value and not a letter.
        """)

    except ZeroDivisionError:
        print("""
        Make sure your denominator isn't zero. You can't divide by it.
        """)
   