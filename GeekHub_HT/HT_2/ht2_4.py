'''Write a script which accepts a <number> from user and then <number> times asks user for string input. 
At the end script must print out result of concatenating all <number> strings.'''


number_of_str = int(input('Input number of string\n'))
finally_str = ''
for _ in range(number_of_str):
    finally_str += input('Input your string\n')

print(f'Your finally string = {finally_str}')