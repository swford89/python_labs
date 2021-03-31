'''
Write a script that takes a string from the user and creates a dictionary of letters that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
user_string = input("Enter in a fun sentence: ")

occur_dict = {}

for char in user_string:
    char_counting = user_string.count(char)
    occur_dict[char] = char_counting

print(f'''Dictionary with the key being the character in the string, and the value being the number of it occurrences:
        {occur_dict}''')
