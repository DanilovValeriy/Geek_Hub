'''
HT 14 TASK  #2.  Створіть програму для отримання курсу валют за певний період.
- отримати від користувача дату (це може бути як один день так і інтервал - початкова
   і кінцева дати, продумайте механізм реалізації) і назву валюти
- вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних
'''
import json
from datetime import datetime

import requests


class MyError(BaseException):
    pass


class Currency:
    base_url = 'https://api.privatbank.ua/p24api/exchange_rates?json&date='

    def __init__(self, date, currency):
        self.date = date
        self.currency = currency

    def get_currency(self):
        self.base_url = self.base_url + self.date
        page = requests.get(self.base_url).text
        all_information = json.loads(page)
        for kay, value in all_information.items():
            if kay == 'exchangeRate':
                base = value
                return base

    def return_base(self, base):
        for element in base:
            for kay, value in element.items():
                if kay == 'currency' and value == self.currency:
                    return element

    def return_result(self, element):

        result = f'\n Exchange rate {self.date} for {self.currency}.\n'
        for kay, value in element.items():
            if kay == 'saleRateNB':
                result += f' NBU rate (sell) - {value} uah.'
            if kay == 'purchaseRateNB':
                result += f' NBU rate (buy) - {value} uah.:'
            if kay == 'saleRate':
                result += f'Commercial rate (sale) - {value} uah.'
            if kay == 'purchaseRate':
                result += f'Commercial rate (buy)  - {value} uah.'
        return result


def choices_currency():
    currency_dict = {
        'USD': 'US dollar', 'EUR': 'Euro',
        'CHF': 'swiss franc', 'GBP': 'british pound',
        'PLZ': 'polish zloty', 'SEK': 'swedish krona',
        'XAU': 'gold', 'CAD': 'canadian dollar'
    }
    print('\n Choice current from:\n')
    for key, value in currency_dict.items():
        print(f'  {key} - {value}')
    while True:
        currency = input('\nInput abbreviate fo current\n')
        if currency in currency_dict:
            return currency
        print('Something went wrong. Try again')


def check_data(my_data):
    try:
        result_dt = datetime.strptime(my_data, '%d.%m.%Y')
    except ValueError:
        raise MyError('Please enter a valid date format(dd.mm.yyyy)')

    if result_dt > datetime.now():
        raise MyError(
            f'The date:{my_data} in the future - information not present')

    if result_dt < datetime.strptime('01.01.2015', '%d.%m.%Y'):
        raise MyError(
            f'The date:{my_data} is too late - must be after 01.01.2015')

    return result_dt.strftime('%d.%m.%Y')


def choise_data():
    flag = True
    while flag:
        first_data = check_data(input('Input data in format dd.mm.yyyy after 01.01.2015\n'))
        second_data = check_data(input('Input data in format dd.mm.yyyy after 01.01.2015\n'))

        first_data_data = datetime.strptime(first_data, '%d.%m.%Y')
        second_data_data = datetime.strptime(second_data, '%d.%m.%Y')
        if first_data_data < second_data_data:
            dates = [first_data, second_data]
        else:
            dates = [second_data, first_data]
        return dates


currency = choices_currency()
dates = choise_data()
for date in dates:
    course_start = Currency(date, currency)
    base = course_start.get_currency()
    element = course_start.return_base(base)
    print(course_start.return_result(element))
