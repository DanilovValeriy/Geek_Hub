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

denomination_of_banknotes = [1000, 500, 200, 100, 50, 20, 10]


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
# BANKOMAT = [(1000, 10), (500, 10), (200, 10), (100, 10), (50, 10), (20, 10), (10, 10)]
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
    logging(my_login1, f'{my_login1} create the account')


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


def check_number(number):
    try:
        number = int(number)
        if number < 0:
            print('The sum can not be less zero')
            return False
        else:
            return int(number)
    except ValueError as err:
        print(err)
        return False


def change_balance(my_login, number, oper='+'):
    if not (check_number(number)):
        return None
    else:
        balance = look_balance(my_login)
        if oper == '+':
            sql.execute(f"UPDATE users set balance =? where login =?", (int(balance) + int(number), my_login))
            db.commit()
            print(f'Your account has been topped up. The amount on the account is {look_balance(my_login)}')
            logging(my_login, f'Your account has been topped up. The amount on the account is {look_balance(my_login)}')

        else:
            if int(number) > int(balance):
                print('There are not enough funds in your account to complete the transaction')
                logging(my_login, 'There are not enough funds in your account to complete the transaction')
                return None
            else:
                sql.execute(f"UPDATE users set balance =? where login =?", (int(balance) - int(number), my_login))
                db.commit()
                if my_login != 'bankomat':
                    print(f'You have withdrawn {number}. The amount in the account is {look_balance(my_login)}')
                    logging(my_login,
                            f'You have withdrawn {number}. The amount in the account is {look_balance(my_login)}')


def my_input():
    flag = True
    while flag:
        number = input('Input number bigger than zero\n')
        try:
            number = int(number)
            if number > 0:
                return number
            else:
                continue
        except ValueError as err:
            print(err)


def choose_operation():
    oper = input("Choose operation '+' or '-': ")
    while oper not in {'+', '-'}:
        oper = input("Choose operation '+' or '-': ")
    return oper


def change_bankomat_cash():
    DENOMINATION = [10, 20, 50, 100, 200, 500, 1000]
    for nominal in DENOMINATION:
        sql.execute(f"SELECT number FROM bankomat WHERE denomination = {nominal}")
        old_number = sql.fetchone()[0]
        g = input(f'Do you want working with {nominal}? y - changing balance, n - showing old balance: ')
        if g in {'n', 'N'}:
            print(f'ATM has {old_number} of {nominal}')
            logging('admin', f'Looking ATM denomination - {nominal}, number - {old_number}')
            continue
        operation = choose_operation()
        if operation == '+':
            my_number = my_input()
            print(f'ATM has {old_number} of {nominal}')
            sql.execute(f"UPDATE bankomat SET number =? where denomination =?",
                        (old_number + int(my_number), nominal))
            db.commit()
            print(f'ATM have {old_number + int(my_number)} of {nominal}')
            logging('admin', f'Put on the ATM denomination - {nominal}, number - {my_number}')
        else:
            my_number = my_input()
            print(f'ATM has {old_number} of {nominal}')
            while my_number > old_number:
                print(f'There are not enough bills of this denomination. ATM contains {old_number} numbers')
                logging('admin', 'There are not enough bills of this denomination')
                my_number = my_input()
            sql.execute(f"UPDATE bankomat SET number =? where denomination =?",
                        (old_number - int(my_number), nominal))
            db.commit()
            print(f'ATM have {old_number - int(my_number)} of {nominal}')
            logging('admin', f'Admin took the money from ATM denomination - {nominal}, number - {my_number}')


def history_of_logging(login):
    sql.execute(f"SELECT login, action FROM transactions")
    for el in sql.fetchall():
        if login == 'admin':
            print(f'{el[0]} has operation {el[1]}')
        elif el[0] == login:
            print(el[1])


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
                            my_password = input("Input password more than 5 letters, contains one of '!@#$%^&' "
                                                "simbols: ")
                            if check_password(my_password):
                                add_users(my_login, my_password)
                                print('Your account successfully create')
                                print(f'Your login {my_login}, your password {my_password}')
                                iter = 4
                                fl = False
                                start(my_login)


def denomination_in_atm(f_print=True):
    sql.execute("SELECT denomination, number FROM bankomat")
    val = sql.fetchall()
    for el in val:
        if f_print:
            print(f'Denomination {el[0]} has {el[1]}')
    return val


def withdraw_from_atm(login, my_list):
    DENOMINATION = [1000, 500, 200, 100, 50, 20, 10]
    index = 0
    for nominal in DENOMINATION:
        sql.execute(f"SELECT number FROM bankomat WHERE denomination = {nominal}")
        old_nominal = sql.fetchone()[0]
        new_nominal = my_list[index] - old_nominal
        if my_list[index]:
            print(f'You take {my_list[index]} of {nominal}')
            logging(login, f'You take {my_list[index]} of {nominal}')
        index += 1
        sql.execute(f"UPDATE bankomat SET number =? where denomination =?", (new_nominal, nominal))
        # logging()
        db.commit()


def start(login):
    if login != 'admin':
        print(f'Hi, {login}')
        choice = 0
        while choice != 6:
            try:
                choice = int(input('Choice operation\n1. Look at the balance\n2. Top up the balance\n'
                                   '3. Take the money\n4. View transaction history.\n5. Return to start menu\n6. '
                                   'Exit\n'))
                match choice:
                    case 1:
                        print(look_balance(login))
                        logging(login, 'Look at the balance')

                    case 2:
                        number = input('How much you want to top up the account?\n')
                        if not check_number(number):
                            continue
                        else:
                            change_balance(login, (int(number) // 10) * 10, '+')
                            print(f'your chang = {int(number) % 10}')

                    case 3:
                        number = input('how much money you want to withdraw from the account?\n')
                        if not check_number(number):
                            continue
                        elif cash_in_the_bankomat() > int(number):
                            chang = int(number) % 10
                            number = (int(number) // 10) * 10
                            withdraw_from_atm(login, decomposition(number, [1000, 500, 200, 100, 50, 20, 10],
                                                                   denomination_in_atm(False)))

                            print(f'your chang = {chang}')
                            change_balance(login, int(number), '-')

                        else:
                            print('There are not enough funds in the ATM')
                            logging(login, 'There are not enough funds in the ATM')

                    case 4:
                        history_of_logging(login)
                        logging(login, "View transaction history")

                    case 6:
                        print('Have a nice day. Good bye')
                        logging(login, 'the end of working with an ATM')

                    case 5:
                        login_or_create()
                        logging(login, 'Return to start menu')

            except ValueError as err:
                print(err)
                return None
    else:
        print('Hello, Big Boss! Make your choice')
        choice = 0
        while choice != 5:
            try:
                choice = int(input('Choice operation\n1. Denomination and balance ATM\n2. Change the balance ATM\n'
                                   '3. History of using ATM\n4. Return to start menu.\n5. Exit\n'))

                match choice:
                    case 1:
                        print(f'Balance of the ATM {cash_in_the_bankomat()}')
                        denomination_in_atm()
                        logging('admin', 'Big boss looking the balance an ATM')
                    case 2:
                        change_bankomat_cash()

                    case 3:
                        history_of_logging('admin')

                    case 4:
                        login_or_create()

            except ValueError as err:
                print(err)


def simple_decomposition(number, cash_in_terminal_list):
    resulting_list = []
    for index, el in enumerate(cash_in_terminal_list):
        if number // el[0] > cash_in_terminal_list[index][1]:
            resulting_list.append(cash_in_terminal_list[index][1])
            number -= cash_in_terminal_list[index][1] * el[0]
        else:
            resulting_list.append(number // el[0])
            number %= el[0]
    return resulting_list


def composition(my_decomposition_list, nominal_list):
    my_sum = 0
    for el in zip(nominal_list, my_decomposition_list):
        my_sum += el[0] * el[1]
    return my_sum


def decomposition(number, denomination_of_banknotes, cash_in_terminal):
    number = (number // 10) * 10
    list_of_denomination = denomination_of_banknotes[:]
    resulting_list = []
    flag = True
    cash_in_terminal_list = cash_in_terminal[:]
    while flag:
        list_from_simple_decomposition = simple_decomposition(number, cash_in_terminal_list)
        if composition(list_from_simple_decomposition, list_of_denomination) == number:
            if not resulting_list:
                return list_from_simple_decomposition
            else:
                return resulting_list + list_from_simple_decomposition
        if len(list_from_simple_decomposition) == 0:
            return resulting_list
        elif list_from_simple_decomposition[0] > 0:
            resulting_list.append(list_from_simple_decomposition[0] - 1)
            coefficient = list_from_simple_decomposition.pop(0)
            number -= (coefficient - 1) * list_of_denomination.pop(0)
            cash_in_terminal_list.pop(0)
        else:
            resulting_list.append(list_from_simple_decomposition.pop(0))
            cash_in_terminal_list.pop(0)
            try:
                list_of_denomination.pop(0)
            except IndexError:
                print('The entered amount cannot be issued')
                return None


def checking_correctness_amount(number, decomposite_list):
    denomination_of_banknotes = [1000, 500, 200, 100, 50, 20, 10]
    return number == composition(decomposite_list, denomination_of_banknotes)


def result_of_decomposition(number):
    denomination_of_banknotes = [1000, 500, 200, 100, 50, 20, 10]
    cash_in_terminal = denomination_in_atm()
    decomposite_list = decomposition(number, denomination_of_banknotes, cash_in_terminal)
    if checking_correctness_amount(number, decomposite_list):
        return decomposite_list
    else:
        return "Can't withdraw this sum"


# print(decomposition())
login_or_create()
