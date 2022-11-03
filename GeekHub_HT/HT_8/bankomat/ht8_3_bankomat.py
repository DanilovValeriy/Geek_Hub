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
import json


def users_validate(my_user, my_pass, file='users.csv'):
    with open(file, 'r', encoding='utf-8') as my_file:
        for el in csv.DictReader(my_file):
            if el.get('user') == my_user and el.get('password') == my_pass:
                return True
    return False


def my_logger(file, my_log):
    with open(file, 'a+') as my_file:
        json.dump(my_log, my_file, indent=4)


def validate_number(number):
    try:
        number = float(number)
    except ValueError as err:
        print(err)
        return False
    return number


def add_user_files(name):
    file_transaction = name + '_transaction.json'
    file_balance = name + '_balance.txt'
    with open(file_transaction, 'w', encoding='utf-8') as ft:
        pass
    with open(file_balance, 'w', encoding='utf-8') as fb:
        pass


def add_in_users(name, password):
    with open('users.csv', 'a', encoding='utf-8') as users_f:
        fieldnames = ["user", "password"]
        writer = csv.DictWriter(users_f, fieldnames, dialect='unix')
        writer.writerow({"user": f"{name}", "password": f"{password}"})


def check_score(file, my_sum=0):
    with open(file) as my_file:
        return float(my_file.readline()) >= my_sum


def change_balance(name, number, operation='-'):
    file = name + '_balance.txt'
    with open(file, 'r', encoding='utf-8') as f:
        my_sum = float(f.read())

    with open(file, 'w', encoding='utf-8') as f:
        if operation == '-':
            sum_after = my_sum - number
            f.write(str(sum_after))
        else:
            sum_after = my_sum + number
            f.write(str(sum_after))
    return f'Sum after operation: {sum_after}'


def show_balance(name):
    file_name = name + '_balance.txt'
    with open(file_name) as fn:
        return float(fn.read())


def start():
    u_name, u_password = input('Hi! Input your name and password, space separated\n').split(' ')
    if not users_validate(u_name, u_password):
        print('You are not registered in our system')
        answer = input('Would you like to register? Y/N\n')
        if answer not in {'y', 'Y'}:
            print('Have a nice day. Good by')
            return None
        else:
            add_in_users(u_name, u_password)
            add_user_files(u_name)
            print(f'You successful added in our system\nUser: {u_name} with password: {u_password}')

    else:
        print(f'Hi, {u_name}')
        try:
            choice = int(input('Choice operation\n1. Look at the balance\n2. Top up the balance\n'
                         '3. Take the money\n4. Exit\n'))
            match choice:
                case 1:
                    return show_balance(u_name)

                case 2:
                    try:
                        my_sum = float(input('How much money do you want to put into the account?\n'))
                        message = f"Your balance successful updated. {change_balance(u_name, my_sum, '+')}"
                        print(message)
                    except ValueError as err:
                        print(err)

        except ValueError as err:
            print(err)
            return None


# start()
# 1. Подивитись баланс
# 2. Поповнити баланс
# 3. Take the money
# 4. Вихід