'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
import re

search_text = ""
russian_count = 0

with open("/mnt/c/Users/Scott/Desktop/dostoevsky.txt", "rt") as dosto_text: # using WSL, so had to switch to a non-Windows path
    reading_text = dosto_text.read()
    #print(reading_text)
    search_word = ' evil'
    search_text = re.findall(search_word, reading_text)
    russian_count = len(search_text)
    print(f"The word '{search_word.strip()}' appears in Notes from the Underground: {russian_count} times")

sample_paragraph = """
    The author of the diary and the diary itself
     are, of course, imaginary.  Nevertheless it is clear
     that such persons as the writer of these notes
     not only may, but positively must, exist in our
     society, when we consider the circumstances in
     the midst of which our society is formed.  I have
     tried to expose to the view of the public more
     distinctly than is commonly done, one of the
     characters of the recent past.  He is one of the
     representatives of a generation still living.  In this
     fragment, entitled "Underground," this person
     introduces himself and his views, and, as it were,
     tries to explain the causes owing to which he has
     made his appearance and was bound to make his
     appearance in our midst.  In the second fragment
     there are added the actual notes of this person
     concerning certain events in his life.--AUTHOR'S NOTE.
"""
top_occurence = ""
top_value = 0

split_paragraph = sample_paragraph.split()

for word in split_paragraph:
    counting_occurrence = split_paragraph.count(word)
    if counting_occurrence > top_value:
        top_value = counting_occurrence

print(f"The word with the most occurrences: '{top_occurence}', with {top_value} occurrences")