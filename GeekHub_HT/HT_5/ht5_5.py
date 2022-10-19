'''5. Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі, 
що не перевищують його.'''


def validator(data):
    try:
        data = int(data)
    except ValueError as err:
        print(err)
        return False
    return True


def fibonacci(n):
    if not(validator(n)):
        return None
    n = int(n)
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        while (a + b) < n:
            print(a + b)
            a, b = b, a + b
            

fibonacci('n19')
fibonacci('19')
