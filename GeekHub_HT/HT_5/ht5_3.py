'''3. Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000, 
и яка вертатиме True, якщо це число просте і False - якщо ні.'''


def is_prime(num):
    sqrt_num = int(num ** 0.5 + 1)
    for i in range(2, sqrt_num):
        if not num % i:
            return False
    return True

for i in range(2, 1000):
    if is_prime(i):
        print(i)
