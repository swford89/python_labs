'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'
first_num = 0

try:

    with open(file_name, "r") as int_text:
        reading_int = int_text.read()
        first_num =+ reading_int        # not converting this into a int, so as to raise the error

except IOError:
    print("""
    Your file name may be incorrect. Check it.
    """)

except TypeError as te:
    print(f"""
    {te}
    {first_num}: {type(first_num)}
    Make sure you're working with the same datatypes!
    """)
    