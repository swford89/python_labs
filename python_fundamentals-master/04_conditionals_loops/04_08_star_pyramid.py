'''
Write a script that takes in a number from the user as input and prints the following structure.

Suppose the input is 5, you will output
*
* *
* * * 
* * * *
* * * * * 
i.e. number of rows will be 5, 1st row will have 1 star, 2nd row will have 2 stars, 3rd row 3 stars, 4th row will have 4 stars and 5th row will have 5 stars.

Another example: if input is 3, you will output
*
* *
* * *

Hint: Think of nested for loops

'''
star_char = "*"

while True:
    try:
        user_num = int(input("Enter a realatively small number: "))
        break
    except ValueError:
        print("""
        Enter an integer.
        """)

print_count = 1
while print_count < user_num:
    if print_count > 1:
        multi_star_char = star_char * print_count
        print(" ".join(multi_star_char))
        print_count += 1
    else:
        print(star_char)
        print_count += 1