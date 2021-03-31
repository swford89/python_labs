'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
# convert the string into a list of words
user_input = input("Enter a sentence: ").split()

result_list = []

for word in user_input:
    for char in word:
        new_tup = tuple(word)
    result_list.append(new_tup)

print(result_list)