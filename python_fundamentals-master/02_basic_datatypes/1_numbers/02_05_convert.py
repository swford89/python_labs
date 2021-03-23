'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
integer_to_float = float(2)
float_to_integer = int(3.14)
floor_div = 3.4//2
remainder_div = 3.4 % 2
print(f"Result of floot dividing 3.4//2: {floor_div}")
print(f"The remainder from 3.4 % 2: {remainder_div}")

user_input_one = float(input("Enter a number: "))
user_input_two = float(input("Enter a number: "))
multi_input = user_input_one * user_input_two
print(f"Multiplying {user_input_one} and {user_input_two} = {multi_input}")
