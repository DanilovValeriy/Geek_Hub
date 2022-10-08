'''Write a script to concatenate all elements in a list into a string and print it.
 List must include both strings and integers and must be hardcoded.'''


my_list = [1, 5.5, True, 'Nema', (1, 2), {'1': 'a', '2': 'b'}]
print(''.join(map(str, my_list)))
