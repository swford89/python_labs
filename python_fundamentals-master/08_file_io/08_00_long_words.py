'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''
long_words = []

with open("words.txt", "r") as reading_file:
    for line in reading_file.readlines():
        line = line.rstrip()
        if len(line) > 20:
            long_words.append(line)

print(f"List of words with more than 20 characters:\n{long_words}")