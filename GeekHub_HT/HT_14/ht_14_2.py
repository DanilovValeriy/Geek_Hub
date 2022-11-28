'''
2. Створіть програму для отримання курсу валют за певний період.
- отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева дати,
продумайте механізм реалізації) і назву валюти
- вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних
'''
from datetime import datetime


class MyError(BaseException):
    pass


def print_currency():
    print('''Виберіть валюту, курс якої бажаєте подивитися\n
            AUD	    1	Австралійський долар
            AZN	    1	Азербайджанський манат
            BYN	    1	Білоруський рубль13
            BGN	    1	Болгарський лев
            KRW	    100	Вона
            HKD	    1	Гонконгівський долар
            DKK	    1	Данська крона
            USD	    1	Долар США
            EUR	    1	Євро
            EGP	    1	Єгипетський фунт
            JPY	    10	Єна
            PLN	    1	Злотий
            INR	    10	Індійська рупія
            CAD	    1	Канадський долар
            HRK	    1	Куна
            MXN	    1	Мексиканське песо
            MDL	    1	Молдовський лей
            ILS	    1	Новий ізраїльський шекель
            NZD	    1	Новозеландський долар
            NOK	    1	Норвезька крона
            ZAR	    1	Ренд
            RUB	    10	Російський рубль
            RON	    1	Румунський лей
            IDR	    1000	Рупія
            SGD	    1	Сінгапурський долар
            XDR	    1	СПЗ (спеціальні права запозичення)
            KZT	    100	Теньге
            TRY	    1	Турецька ліра
            HUF	    100	Форинт
            GBP	    1	Фунт стерлінгів
            CZK	    1	Чеська крона
            SEK	    1	Шведська крона
            CHF	    1	Швейцарський франк
            CNY	    1	Юань Женьміньбі
            ''')


def choose_currency() -> str:
    CURRENCY_LIST = ['AUD', 'AZN', 'BYN', 'BGN', 'KRW', 'HKD', 'DKK', 'USD', 'EUR', 'EGP', 'JPY', 'PLN', 'INR', 'CAD',
                     'HRK', 'MXN',
                     'MDL', 'ILS', 'NZD', 'NOK', 'ZAR', 'RUB', 'RON', 'IDR', 'SGD', 'XDR', 'KZT', 'TRY', 'HUF', 'GBP',
                     'CZK', 'SEK',
                     'CHF', 'CNY']

    flag = True
    while flag:
        print_currency()
        currency = input('Input abbreviation of currency')
        if currency not in CURRENCY_LIST:
            continue
        else:
            flag = False
            return my_url_join(currency)


def my_url_join(url):
    URL = 'https://bank.gov.ua/ua/markets/exchangerates'
    ADDITIONAL_URL = '-chart?cn%5B%5D='
    return str(URL)[:-1] + ADDITIONAL_URL + url


def url_date_join(first_date: str, second_date: str) -> str:
    BASE_URL = choose_currency()
    START = '&startDate='
    END = '&endDate='
    return BASE_URL + START + first_date + END + second_date


def check_data(my_data):
    try:
        result_dt = datetime.strptime(my_data, '%d.%m.%Y')
    except ValueError:
        raise MyError(
            'Please enter a valid date format(dd.mm.yyyy)')

    if result_dt > datetime.now():
        raise MyError(
            f'The date:{my_data} in the future - information not present')

    # before 02.09.1996 was karbovanets
    if result_dt < datetime.strptime('02.09.1996', '%d.%m.%Y'):
        raise MyError(
            f'The date:{my_data} is too late - must be after 02.09.1996')

    return result_dt.strftime('%d.%m.%Y')


first_data = check_data(input('Input data in format dd.mm.yyyy after 02.09.1996\n'))
second_data = check_data(input('Input data in format dd.mm.yyyy after 02.09.1996\n'))

first_data_data = datetime.strptime(first_data, '%d.%m.%Y')
second_data_data = datetime.strptime(second_data, '%d.%m.%Y')

if second_data_data < first_data_data:
    second_data, first_data = first_data, second_data

print(url_date_join(first_data, second_data))

# 12.12.2000
# 12.12.2001
