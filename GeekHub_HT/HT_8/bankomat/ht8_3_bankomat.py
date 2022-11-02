'''3. Програма-банкомат.
   Використовуючи функції створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>) 
      та історію транзакцій (файл <{username_transactions.JSON>);
      - є можливість як вносити гроші, так і знімати їх. 
      Обов'язкова перевірка введених даних (введено цифри; знімається не більше, ніж є на рахунку і т.д.).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. 
      Але якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - на початку роботи - логін користувача (програма запитує ім'я/пароль). 
      Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (
        хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :))
      - потім - елементарне меню типн:
        Введіть дію:
           1. Подивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив, можете розширювати функціонал, 
      але основне завдання має бути повністю реалізоване :)
    P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно)
    P.S.S. Добре продумайте структуру програми та функцій'''

import csv


def users_validate(file, my_user, my_pass):
    with open(file, 'r', encoding='utf-8') as my_file:
        for el in csv.DictReader(my_file):
            print(el)
            if el.get('user') == my_user and el.get('password') == my_pass:
                return True
    return False


def validate_number(number):
    try:
        number = float(number)
    except ValueError as err:
        print(err)
        return False
    return number


def check_score(file, my_sum=0):
    with open(file) as my_file:
        return float(my_file.readline()) >= my_sum


print(check_score('Valerii_balance.txt', 4444))
# with open('users.csv', 'r', encoding='utf-8') as file:
#     print(csv.DictReader(file))
# print(csv.DictReader(file))
# for el in csv.DictReader(file):
# for el in csv.reader(file):
#     print(el["user"] == "Valerii")


# print((users_validate('users.csv', 'Valerii', 'cherkasy85')))
