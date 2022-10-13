'''Write a script to get the maximum and minimum VALUE in a dictionary.'''

def python_rishaka(val):
     if isinstance(val, (float, int)):
          return val
     else:
          return len(val)


dict_1 = {'foo': 92, 'bar': 23, 'dou': 333, 'USD': 36, 'dofu': 877, 'USD': 36, 'eee': 'ggg', '11': {1}}


print(f'Max element of dict = {max(dict_1.keys(), key=(lambda k: python_rishaka(dict_1[k])))},\
     min element of dict = {min(dict_1.keys(), key=(lambda k: python_rishaka(dict_1[k])))}')
