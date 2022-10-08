'''Write a script which accepts a sequence of comma-separated numbers
 from user and generates a list and a tuple with those numbers.'''
user_num = input("Input a sequence of comma-separated numbers\n")
list_num = list(map(int, user_num.split(',')))
tuple_user = tuple(list_num)

print(f'list_num = {list_num}, tuple_user = {tuple_user}')