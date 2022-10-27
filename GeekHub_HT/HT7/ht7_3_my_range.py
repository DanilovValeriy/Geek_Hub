'''3. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції. 
Тобто щоб її можна було використати у вигляді:
    for i in my_range(1, 10, 2):
        print(i)
    1
    3
    5
    7
    9
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати 
   документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
   P.P.P.S Не забудьте обробляти невалідні ситуації (типу range(1, -10, 5) тощо). 
   Подивіться як веде себе стандартний range в таких випадках.'''


class MyError(BaseException):
    pass


def my_range(*args):

    if not args:
        raise MyError('range expected at least 1 argument, got 0')
    if not all(list(map(lambda x: isinstance(x, int), args))):
        raise MyError('argument of my_range must be int')
    if len(args) > 3:
        raise MemoryError(f'my_range expected at most 3 arguments, got {len(args)}')

    elif len(args) == 1:
        if args[0] < 1:
            yield []
        else:
            el = 0
            while el < args[0]:
                yield el
                el += 1

    elif len(args) == 2:
        if args[0] >= args[1]:
            yield []
        else:
            start = args[0]
            stop = args[1]
            while start < stop:
                yield start
                start += 1
    
    else:
        if args[2] == 0:
            raise MyError('my_range() arg 3 must not be zero')
        if args[0] > args[1] and args[2] > 0 or args[0] < args[1] and args[2] < 0:
            yield []
        elif args[0] < args[1]:
            start = args[0]
            stop = args[1]
            step = args[2]
            while start < stop:
                yield start
                start += step
        else:
            start = args[0]
            stop = args[1]
            step = args[2]
            while start > stop:
                yield start
                start += step      


print(*range(-9))
print(*my_range(-9))

print(*range(9))
print(*my_range(9))

print(*range(9, 1))
print(*my_range(9, 1))

print(*range(1, 9))
print(*my_range(1, 9))

print(*range(1, 9, 3))
print(*my_range(1, 9, 3))

print(*range(9, 1, -3))
print(*range(9, 1, -3))
