'''
Print out every prime number between 1 and 100.

'''
even_list = []
odd_list = []
prime_list = []

for possible_num in range(2,101):
    prime_num = True
    for num in range(2, possible_num):
        print(f"num = {num}\npossible_num = {possible_num}")
        if possible_num % num == 0:
            prime_num = False  
            break  
    if prime_num:
        prime_list.append(possible_num)

print(prime_list)