'''Write a script to check whether a value from user input is contained in a group of values.
    e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
         [1, 2, 'u', 'a', 4, True] --> 5 --> False'''


our_list = [1, 2, 8.8, 'u', 'a', 4, True]
my_list = list(map(str, our_list))
value = input('Input your value\n')

print(value in my_list)
# print('Your value in list') if value in my_list else print('Nema')
