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

    if len(args) == 1:
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

    

    


        
        
    
# print(f'range = {range(0)}')
# print(*range(10, 1, 7,7))

# print('my_range = ', my_range(-90))
print(*my_range(7, 17,6,6,6,6))

# for i in my_range(1):
#     print(i)

