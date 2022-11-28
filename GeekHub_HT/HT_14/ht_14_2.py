'''
2. Створіть програму для отримання курсу валют за певний період.
- отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева дати,
продумайте механізм реалізації) і назву валюти
- вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних
'''
from datetime import datetime as data


class MyError(BaseException):
    pass


def check_data(my_data):
    try:
        result_dt = data.strptime(my_data, '%d.%m.%Y')
    except ValueError:
        raise MyError(
            'Please enter a valid date format(dd.mm.yyyy)')

    if result_dt > data.now():
        raise MyError(
            f'The date:{my_data} in the future - information not present')

    # before 02.09.1996 was karbovanets
    if result_dt < data.strptime('02.09.1996', '%d.%m.%Y'):
        raise MyError(
            f'The date:{my_data} is too late - information presents '
            f'from 02.09.1996')

    return result_dt.strftime('%d.%m.%Y')


print(check_data('81.10.1998'))
