'''Користувач вводить змінні "x" та "y" з довільними цифровими значеннями. 
Створіть просту умовну конструкцію (звiсно вона повинна бути в тiлi ф-цiї), 
під час виконання якої буде перевірятися рівність змінних "x" та "y" 
та у випадку нерівності - виводити ще і різницю.
    Повинні працювати такі умови (x, y, z заміність на відповідні числа):
    x > y;       вiдповiдь - "х бiльше нiж у на z"
    x < y;       вiдповiдь - "у бiльше нiж х на z"
    x == y.      відповідь - "х дорівнює y"'''


def validate_date(date):
    try:
        date = float(date)
        return date
    except ValueError as arr:
        print('Expected float or integer date!', arr)


def compare_numbers(x, y):
    if not(validate_date(x)) or not(validate_date(y)):
        return 'Not numerical values'
    x, y = list(map(float,(x, y)))
    if x > y:
        return f'{x} бiльше нiж {y} на {x - y}'
    elif y > x:
        return f'{y} бiльше нiж {x} на {y - x}'
    else:
        return f'{x} дорівнює {y}'
         
a, b = (input('Input numbers comma separated\n').split(','))

print(compare_numbers(a, b))
