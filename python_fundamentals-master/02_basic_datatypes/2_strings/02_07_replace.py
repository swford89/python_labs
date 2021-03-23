'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

user_string = input("Enter a fun sentence: ")
user_symbol = input("Enter a symbol that you like: ")
fun_string = user_string.replace(user_string[0], user_symbol)
print(f"Before: {user_string}\nAfter: {fun_string}")