'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
shortest_word = 100
longest_word = 0
word_count = 0

shortest_word_list = []
longest_word_list = []

with open("words.txt", "r") as reading_file:
    words = reading_file.readlines()
    for word in words:
        stripped_word = word.rstrip()
        word_count += 1
        if len(stripped_word) < shortest_word:
            shortest_word = len(stripped_word)
        elif len(stripped_word) > longest_word:
            longest_word = len(stripped_word)
    
with open("words.txt", "r") as reading_file:
    words = reading_file.readlines()
    for word in words:
        stripped_word = word.rstrip()    
        if len(stripped_word) == shortest_word:
            shortest_word_list.append(stripped_word)
        elif len(stripped_word) == longest_word:
            longest_word_list.append(stripped_word)
        
    print(f"Length of shortest word: {shortest_word}\nList of the shortest word(s): {shortest_word_list}")
    print(f"Length of longest word: {longest_word}\nList of the longest word(s): {longest_word_list}")
    print(f"Total word count: {word_count}")
