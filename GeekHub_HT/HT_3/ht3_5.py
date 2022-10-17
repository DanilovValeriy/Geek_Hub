'''Write a script to remove values duplicates from dictionary. 
Feel free to hardcode your dictionary.'''


dict_1 = {'1': 1, '2': [2, 5], 'f': 1, 'g': 2, 'r': [2, 5], 77: {'e': 4}, 66: {'e': 4}}
my_dict = {}
my_arr = []
for key, val in dict_1.items():
    if val not in my_arr:
        my_arr.append(val)
        my_dict.update({key: val})
print(my_dict)
