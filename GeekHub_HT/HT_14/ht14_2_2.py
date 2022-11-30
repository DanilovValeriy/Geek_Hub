'''
2. Створіть програму для отримання курсу валют за певний період.
- отримати від користувача дату (це може бути як один день так і інтервал
- початкова і кінцева дати, продумайте механізм реалізації) і назву валюти
- вивести курс по відношенню до гривні на момент вказаної дати
(або за кожен день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних
'''

import json
from datetime import datetime, timedelta

import requests


def get_currency_rate_in_range():
    first_date = input('Input first date in format (dd.mm.yyyy) after 01.01.2015\n')
    second_date = input('Input second date in format (dd.mm.yyyy) after 01.01.2015\n')

    try:
        first_date = datetime.strptime(first_date, '%d.%m.%Y')
    except ValueError:
        print('Invalid date')
        return

    if second_date:
        try:
            date_end = datetime.strptime(second_date, '%d.%m.%Y')
            if (date_end - first_date).days < 0:
                print('Incorrect date')
                return
        except ValueError:
            print('Incorrect date')
            return
        date_range = [(first_date + timedelta(days=x)).strftime('%d.%m.%Y') for x in
                      range(0, (date_end - first_date).days + 1)]
        for day in date_range:
            get_currency_rate(day)
    else:
        get_currency_rate(datetime.strftime(first_date, '%d.%m.%Y'))


def get_currency_rate(date):
    url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
    response = requests.get(url)
    if response.status_code != 200:
        print(f'No information for this date - {date}')
        return
    print(date)
    response_content = response.content
    currency_info = json.loads(response_content)
    for currency in currency_info['exchangeRate']:
        if currency['currency'] in ('USD', 'EUR', 'GBP', 'PLN'):
            print(f'{currency["currency"]} sell: {currency["saleRate"]} buy: {currency["purchaseRate"]}')


get_currency_rate_in_range()
