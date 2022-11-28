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


def print_currency():
    print('''Виберіть валюту, курс якої бажаєте подивитися\n
            AUD	1	Австралійський долар
            AZN	1	Азербайджанський манат
            BYN	1	Білоруський рубль13
            BGN	1	Болгарський лев
            KRW	100	Вона
            HKD	1	Гонконгівський долар
            DKK	1	Данська крона
            USD	1	Долар США
            EUR	1	Євро
            EGP	1	Єгипетський фунт
            JPY	10	Єна
            PLN	1	Злотий
            INR	10	Індійська рупія
            CAD	1	Канадський долар
            HRK	1	Куна
            MXN	1	Мексиканське песо
            MDL	1	Молдовський лей
            ILS	1	Новий ізраїльський шекель
            NZD	1	Новозеландський долар
            NOK	1	Норвезька крона
            ZAR	1	Ренд
            RUB	10	Російський рубль
            RON	1	Румунський лей
            IDR	1000	Рупія
            SGD	1	Сінгапурський долар
            XDR	1	СПЗ (спеціальні права запозичення)
            KZT	100	Теньге
            TRY	1	Турецька ліра
            HUF	100	Форинт
            GBP	1	Фунт стерлінгів
            CZK	1	Чеська крона
            SEK	1	Шведська крона
            CHF	1	Швейцарський франк
            CNY	1	Юань Женьміньбі
            ''')


def my_url_join(url):
    URL = 'https://bank.gov.ua/ua/markets/exchangerates'
    ADDITIONAL_URL = '-chart?cn%5B%5D='
    return str(URL)[:-1] + ADDITIONAL_URL + url


# print(requests.get(my_url_join('AZN')).text)
print_currency()


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

# print(check_data('81.10.1998'))
