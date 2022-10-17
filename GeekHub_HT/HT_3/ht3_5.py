'''Write a script to remove values duplicates from dictionary. 
Feel free to hardcode your dictionary.'''


dict_1 = {'1': 1, '2': 2, 'f': 1, 'g': 2, 'r': 3}
my_dict = {}
my_set = set()
for key, val in dict_1.items():
    if val not in my_set:
        my_set.add(val)
        my_dict.update({key: val})
print(my_dict)
