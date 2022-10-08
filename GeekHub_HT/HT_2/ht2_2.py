'''Write a script which accepts two sequences of comma-separated colors from user. 
Then print out a set containing all the colors from color_list_1 which are not present in color_list_2.'''

first_seq = input('Input first sequences\n').split(',')
second_seq = input('Input second sequences\n').split(',')

finally_set = set(first_seq).difference(set(second_seq))
print('Finally set = ', finally_set)