'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
word_list = []

for user_string in range(3):
    user_string = input("Enter a fun word: ")
    word_list.append(user_string)

for word in word_list:
    print(f"{len(word)}, {word}")

max_word = max(word_list)
print(f"Printing ONLY the word with the most characters: {len(max_word)}, {max_word}")
