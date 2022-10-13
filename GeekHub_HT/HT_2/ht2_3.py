'''Write a script which accepts a <number> from user 
and print out a sum of the first <number> positive integers.'''

my_number = int(input('Input number of numbers\n'))
print(f'Sum of the first {my_number} positive integers = ', sum(range(1, my_number+1)))
