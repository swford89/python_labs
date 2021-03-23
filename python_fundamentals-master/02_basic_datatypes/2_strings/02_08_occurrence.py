'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
user_string = input("Enter in another fun sentence: ")
user_char = input("Enter in a single letter from your sentence: ")
count_char = user_string.count(user_char)
print(f"Your Sentence: {user_string}\nYour Letter: {user_char}\nTotal count of of the letter '{user_char}' in your sentence: {count_char}")