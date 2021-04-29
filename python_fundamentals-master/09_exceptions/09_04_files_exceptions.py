'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''
import webbrowser
class PrinceError(Exception):

    def __init__(self, prince_string) -> None:
        self.prince_string = prince_string
        self.url = webbrowser.open_new_tab(error_url)

tolstoy_list = []
war_peace = ""
crime_punishment = ""
pride_prejudice = ""
error_url = "https://www.reddit.com/r/PRINCE/comments/d1j0hs/my_attempt_at_a_prince_meme/"

war_path = "/mnt/c/Users/Scott/Desktop/python_fundamentals_git/labs/python_fundamentals-master/09_exceptions/books/war_and_peace.txt"
crime_path = "/mnt/c/Users/Scott/Desktop/python_fundamentals_git/labs/python_fundamentals-master/09_exceptions/books/crime_and_punishment.txt"
pride_path = "/mnt/c/Users/Scott/Desktop/python_fundamentals_git/labs/python_fundamentals-master/09_exceptions/books/pride_and_prejudice.txt"

# reading war and peace
try:
    with open(war_path, "r") as reading_war:
        war_peace_read = reading_war.read()
        war_peace = "".join(war_peace_read)
        tolstoy_list.append(war_peace)

except IOError:
    print("""
    There could be an error with your file or the path to it. Check it out.
    """)

# overwriting crime and punishment
try:
    with open(crime_path, "w") as writing_crime:
        crime_punish = writing_crime.write(" ")

    with open(crime_path, "r") as reading_crime:
        overwritten_crime_read = reading_crime.read()
        crime_punishment = "".join(overwritten_crime_read)
        tolstoy_list.append(crime_punishment)

except IOError:
    print("""
    There could be an error with your file or the path to it. Check it out.
    """)

# reading pride and prejudice
try:
    with open(pride_path, "r") as reading_pride:
        pride_prejudice_read = reading_pride.read()
        pride_prejudice = "".join(pride_prejudice_read)
        tolstoy_list.append(pride_prejudice)

except IOError:
    print("""
    There could be an error with your file or the path to it. Check it out.
    """)

# looping through stories to get first character
for story in tolstoy_list:
    print(f"First character in the story: {story[0]}")

# looping through stories and raising custom error
for story in tolstoy_list:
    try:
        if "Prince" in story[0:101]:
            raise PrinceError("Found a Prince!")
    
    except PrinceError as pe:
        pe.url