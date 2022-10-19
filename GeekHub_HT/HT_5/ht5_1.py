'''1. Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата,
 і вертатиме 3 значення у вигляді кортежа: периметр квадрата, 
площа квадрата та його діагональ.'''


def square(a):
    try:
        a = float(a)
    except ValueError as err:
        return err
    return (4 * a, a * a, (2 * a ** 2) ** 0.5 )


print(square(input('Input side of a square\n')))
