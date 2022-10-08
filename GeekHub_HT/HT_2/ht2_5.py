'''Write a script which accepts a decimal number from user and converts it to hexadecimal.'''


dec_number = int(input('Input decimal number\n'))
print('Number in hex style = ', hex(dec_number))
print('Number whitout 0x = ', str(hex(dec_number))[2:])
