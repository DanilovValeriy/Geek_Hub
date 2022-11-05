'''Банкомат 2.0
    - усі дані зберігаються тільки в sqlite3 базі даних у відповідних таблицях. Більше ніяких файлів.
    Якщо в попередньому завданні ви добре продумали структуру програми
    то у вас не виникне проблем швидко адаптувати її до нових вимог.
    - на старті додати можливість залогінитися або створити нового користувача
    (при створенні нового користувача, перевіряється відповідність логіну і паролю мінімальним вимогам.
    Для перевірки створіть окремі функції)
    - в таблиці з користувачами також має бути створений унікальний користувач-інкасатор,
    який матиме розширені можливості (домовимось, що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
    - банкомат має власний баланс
    - кількість купюр в банкоматі обмежена (тобто має зберігатися номінал та кількість).
    Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
    - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор
    - користувач через банкомат може покласти на рахунок лише суму кратну мінімальному номіналу що підтримує банкомат.
     В іншому випадку - повернути "здачу" (наприклад при поклажі 1005 --> повернути 5).
     Але це не має впливати на баланс/кількість купюр банкомату, лише збільшується баланс користувача
     (моделюємо наявність двох незалежних касет в банкоматі - одна на прийом, інша на видачу)
    - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
    - при неможливості виконання якоїсь операції - вивести повідомлення з причиною
    (невірний логін/пароль, недостатньо коштів на рахунку, неможливо видати суму наявними купюрами тощо.)
    - файл бази даних з усіма створеними таблицями і даними також додайте в репозиторій,
    що б ми могли його використати
    '''
import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()


# sql.execute("""CREATE TABLE IF NOT EXISTS users (
#             login TEXT,
#             password TEXT,
#             balance BIGINT,
#             is_collector BOOLEAN
#             )""")
# db.commit()

# USERS = [
#     ('Den', 'FRt%^%56', 1000, False),
#     ('Valerii', '1234%%55', 1000, False),
#     ('admin', 'admin', 10000, True)
# ]
# sql.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", USERS)
# db.commit()


def add_users(my_login1, my_password1):
    sql.execute(f"INSERT INTO users (login, password, balance, is_collector) VALUES (?, ?, ?, ?)",
                (my_login1, my_password1, 0, False))
    db.commit()


def is_login_allowed(my_login):
    sql.execute("SELECT login FROM users")
    if (my_login,) in sql.fetchall():
        print("You can't use this login")
        return False
    else:
        print('You can use this login')
        return True


def check_password(my_password):
    return bool(len(my_password) > 5 and set('!@#$%^&*').intersection(set(my_password)))


def check_user_in_system(my_login, my_password):
    sql.execute("SELECT login, password FROM users")
    if (my_login, my_password) in sql.fetchall():
        print("Welcome to the system")
        return True
    else:
        print("You don't have access to system")
        print("Invalid login or password")
        return False


def look_balance(my_login):
    sql.execute(f"SELECT login, balance FROM users")
    for el in sql.fetchall():
        if el[0] == my_login:
            return el[1]


def check_number(number):
    try:
        number = float(number)
        if number < 0:
            print('The sum can not be less zero')
            return False
        else:
            return number
    except ValueError as err:
        print(err)
        return False


def change_balance(my_login, number, oper='+'):
    if not (check_number(number)):
        return None
    else:
        balance = look_balance(my_login)
        if oper == '+':
            sql.execute(f"UPDATE users set balance =? where login =?", (balance + number, my_login))
            db.commit()
            print(f'Your account has been topped up. The amount on the account is {look_balance(my_login)}')
        else:
            if number > balance:
                print('There are not enough funds in your account to complete the transaction')
                return None
            else:
                sql.execute(f"UPDATE users set balance =? where login =?", (balance - number, my_login))
                db.commit()
                print(f'You have withdrawn {number}. The amount in the account is {look_balance(my_login)}')


def login_or_create():
    flag = True
    while flag:
        choice = input('Do you have an account?. y/n. Press x to exit\n')
        if choice in {'x', 'X'}:
            flag = False
            print('Have a nice day')
            continue

        elif choice in {'y', 'Y'}:
            login = input('Input your login: ')
            password = input('Input your password: ')
            check_user_in_system(login, password)

        elif choice in {'n', 'N'}:
            sec_choice = input('Do you want to create an account? y/n\n')
            if sec_choice in {'y', 'Y'}:
                fl = True
                while fl:
                    my_login = input('Input your login: ')
                    if not is_login_allowed(my_login):
                        continue
                    else:
                        iter = 1
                        while iter < 4:
                            my_password = input("Input password more than 5 letters, consider one of '!@#$%^&' "
                                                "simbols: ")
                            if check_password(my_password):
                                add_users(my_login, my_password)
                                print('Your account successfully create')
                                print(f'Your login {my_login}, your password {my_password}')
                                iter = 4
                                fl = False


def start():




login_or_create()

# 1. Look at the balance
# 2. Top up the balance
# 3. Take the money
# 4. Exit
