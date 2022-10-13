'''Write a script which accepts a <number>(int) from user 
and generates dictionary in range <number> where key is <number> and value is <number>*<number>
    e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}'''

print({x: x**2 for x in range(int(input('Input integer number\n')))})
