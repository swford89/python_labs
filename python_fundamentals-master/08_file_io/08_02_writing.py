'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''
words_list = []

with open("words.txt", "r") as reading_file:
    words = reading_file.readlines()
    for word in words:
        stripped_word = word.rstrip()
        words_list.append(stripped_word)

with open("reversed_words.txt", "w") as writing_file:
        for word in reversed(words_list):
            writing_file.write(word + "\n")