'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
vowel_string = "aeiouAEIOU"
user_string = input("Enter a sentence: ")


for char in vowel_string:
    print(f"{char} count: {user_string.count(char)}")