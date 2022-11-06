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
#
# sql.execute("""CREATE TABLE IF NOT EXISTS transactions (
#             login TEXT,
#             action TEXT
#             )""")
# db.commit()
#
# USERS = [
#     ('Den', 'FRt%^%56', 1000, False),
#     ('Valerii', '1234%%55', 1000, False),
#     ('admin', 'admin', 10000, True),
#     ('bankomat', 'bJ%f$$^vBJD55^&$%6', 1000, False)
# ]
# sql.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", USERS)
# db.commit()
#
# sql.execute("""CREATE TABLE IF NOT EXISTS bankomat (
#             denomination INT,
#             number INT
#             )""")
# db.commit()
#
# BANKOMAT = [(10, 10), (20, 10), (50, 10), (100, 10), (200, 10), (500, 10), (1000, 10)]
#
# sql.executemany("INSERT INTO bankomat VALUES (?, ?)", BANKOMAT)
# db.commit()


def logging(my_login, my_action):
    sql.execute(f"INSERT INTO transactions (login, action) VALUES (?, ?)",
                (my_login, my_action))
    db.commit()


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


def cash_in_the_bankomat():
    sql.execute("SELECT denomination, number FROM bankomat")
    my_sum = 0
    for el in sql.fetchall():
        my_sum += el[0] * el[1]
    return my_sum


print(cash_in_the_bankomat())


def check_number(number):
    try:
        number = float(number)
        if number < 0:
            print('The sum can not be less zero')
            return False
        else:
            return float(number)
    except ValueError as err:
        print(err)
        return False


def change_balance(my_login, number, oper='+'):
    if not (check_number(number)):
        return None
    else:
        balance = look_balance(my_login)
        if oper == '+':
            sql.execute(f"UPDATE users set balance =? where login =?", (float(balance) + float(number), my_login))
            db.commit()
            print(f'Your account has been topped up. The amount on the account is {look_balance(my_login)}')
            logging(my_login, f'Your account has been topped up. The amount on the account is {look_balance(my_login)}')

        else:
            if float(number) > float(balance):
                print('There are not enough funds in your account to complete the transaction')
                logging(my_login, 'There are not enough funds in your account to complete the transaction')
                return None
            else:
                sql.execute(f"UPDATE users set balance =? where login =?", (float(balance) - float(number), my_login))
                db.commit()
                if my_login != 'bankomat':
                    print(f'You have withdrawn {number}. The amount in the account is {look_balance(my_login)}')
                    logging(my_login,
                            f'You have withdrawn {number}. The amount in the account is {look_balance(my_login)}')


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
            if check_user_in_system(login, password):
                flag = False
            else:
                continue
            start(login)

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
                                start(my_login)


def start(login):
    print(f'Hi, {login}')
    choice = 0
    while choice != 4:
        try:
            choice = int(input('Choice operation\n1. Look at the balance\n2. Top up the balance\n'
                               '3. Take the money\n4. Exit\n5. Top up the balance ATM (admin only)\n'))
            match choice:
                case 1:
                    print(look_balance(login))
                    logging(login, 'Look at the balance')

                case 2:
                    number = input('How much you want to top up the account?\n')
                    if not check_number(number):
                        continue
                    else:
                        change_balance(login, number, '+')

                case 3:
                    number = input('how much money you want to withdraw from the account?\n')
                    if not check_number(number):
                        continue
                    elif cash_in_the_bankomat() > float(number):
                        change_balance(login, number, '-')
                        change_balance('bankomat', float(number), '-')
                    else:
                        print('There are not enough funds in the ATM')
                        logging(login, 'There are not enough funds in the ATM')

                case 4:
                    print('Have a nice day. Good bye')
                    logging(login, 'the end of working with an ATM')

                case 5:
                    if login == 'admin':
                        number = input('How much you want to top up the ATM?\n')
                        if not check_number(number):
                            print('Ha-ha-ha/ Very funny. I suppose you are seriously man')
                        else:
                            change_balance('bankomat', float(number), '+')

        except ValueError as err:
            print(err)
            return None

# login_or_create()
