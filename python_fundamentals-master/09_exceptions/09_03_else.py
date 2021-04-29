'''
Write a script that demonstrates a try/except/else.

'''
while True:

    try:
        numerator = int(input("Enter a whole number: "))
        denominator = int(input("Enter a whole number to divide by: "))
        print(f"The quotient of {numerator} divided by {denominator} is: {numerator/denominator}")

    except ValueError:
        print("""
        Be sure to enter a number and not a letter.
        """)

    except ZeroDivisionError:
        print("""
        You're not allowed to divide by zero.
        """)
        
    else:
        print("""
        No errors encountered.
        """)