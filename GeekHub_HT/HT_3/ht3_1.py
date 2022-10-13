'''Write a script that will run through a list of tuples and replace the last value for each tuple. 
The list of tuples can be hardcoded. The "replacement" value is entered by user.
The number of elements in the tuples must be different.'''


my_list = [(), (1,2), (1,2,3), (1,2,3,4), (1,2,3,4,5)]
try:
    user_number = int(input('Input integer number\n'))
except ValueError as err:
    print(f'Got error: {err}', 'Please input integer number', sep='\n')

def change_value(my_arr, num):
    if not my_arr:
        return my_arr
    my_arr[-1] = num
    return my_arr
# tried to use lambda function to change last element, but nothing worked
my_arr = map(lambda x: change_value(x, user_number), list(map(list, my_list)))
my_arr = list(map(tuple, my_arr))

print(my_arr)
