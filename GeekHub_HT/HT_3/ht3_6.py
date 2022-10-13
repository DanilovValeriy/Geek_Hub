'''Write a script to get the maximum and minimum VALUE in a dictionary.'''


dict_1 = {'foo': -2, 'bar': 23, 'dou': 333, 'USD': 36, 'dofu': 877, 'USD': 36, 'eee': 2}


print(f'Max element of dict = {max(dict_1.keys(), key=(lambda k: dict_1[k]))},\
     min element of dict = {min(dict_1.keys(), key=(lambda k: dict_1[k]))}')
