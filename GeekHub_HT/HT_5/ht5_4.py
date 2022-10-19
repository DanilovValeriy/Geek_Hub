'''4. Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона,
 і вертатиме список простих чисел всередині цього діапазона. 
 Не забудьте про перевірку на валідність введених даних та 
 у випадку невідповідності - виведіть повідомлення.'''

def validator(data):
    try:
        data = int(data)
    except ValueError as err:
        print(err)
        return False
    return True


def is_prime(num):
    sqrt_num = int(num ** 0.5 + 1)
    for i in range(2, sqrt_num):
        if not num % i:
            return False
    return True


def prime_list(start, finish):
    if not (validator(start) and validator(finish)):
        return 'Invalid data'
    start = int(start)
    finish = int(finish)
    my_list = []
    for i in range(start, finish + 1):
        if is_prime(i):
            my_list.append(i)
    return my_list

print(prime_list(3, 200))
print(prime_list(3, '200'))
print(prime_list('4e', 200))