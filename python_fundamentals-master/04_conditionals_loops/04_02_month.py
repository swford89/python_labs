'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7:"July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
    }

user_num = int(input("Enter a number: "))

if user_num in range(1,13):
    if user_num in month_dict:
        print(month_dict[user_num])
else:
    print("Other")