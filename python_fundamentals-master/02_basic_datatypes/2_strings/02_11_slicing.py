'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''
user_name = input("Enter your name: ")
pig_latin = user_name[1:] + user_name[0] + "ay"
print(pig_latin)