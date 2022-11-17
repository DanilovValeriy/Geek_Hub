"""Банкомат 4.0: переробіть программу з функціонального підходу програмування на використання класів.
Додайте шанс 10% отримати бонус на баланс при створенні нового користувача.
"""

import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

denomination_of_banknotes = [1000, 500, 200, 100, 50, 20, 10]


# add the admin account to the database
# sql.execute("INSERT INTO users VALUES (?, ?, ?, ?)", ('admin', 'admin', 10000, 1))
# db.commit()


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

# USERS = [
#     ('Den', 'FRt%^%56', 1000, False),
#     ('Valerii', '1234%%55', 1000, False),
#     ('admin', 'admin', 10000, True),
#     ('bankomat', 'bJ%f$$^vBJD55^&$%6', 1000, False)
# ]
# sql.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", USERS)
# db.commit()

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


class MyError(BaseException):
    pass


class Account:

    @staticmethod
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

    @staticmethod
    def check_password(password):
        if len(password) > 5 and set('!@#$%^&*').intersection(set(password)):
            return True
        else:
            return False

    @staticmethod
    def create_account(login, password, cash_on_balance=0, is_admin=0):
        try:
            if Account.check_password(password):
                sql.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (login, password, cash_on_balance, is_admin))
                db.commit()
            else:
                print('Password must contain at least one character !@#$%^&*. Len of password can not be less '
                      'than 5')
        except TypeError('password must be string'):
            return f'User {login} with password {password} has not been created'

    @staticmethod
    def check_user_in_system(my_login, my_password):
        sql.execute("SELECT login, password FROM users")
        if (my_login, my_password) in sql.fetchall():
            print("Welcome to the system")
            return True
        else:
            print("You don't have access to system")
            print("Invalid login or password")
            return False

    def money_on_user_balance(self):
        sql.execute(f"SELECT login, balance FROM users")
        for el in sql.fetchall():
            if el[0] == self.name:
                return el[1]

    @staticmethod
    def __check_number(amount):
        try:
            amount = int(amount)
            if amount < 0:
                print('The sum can not be less zero')
                return False
            else:
                return int(amount)
        except ValueError as err:
            print(err)
            return False


class ATM:
    DENOMINATION = [1000, 500, 200, 100, 50, 20, 10]

    @staticmethod
    def cash_in_atm():
        sql.execute("SELECT denomination, number FROM bankomat")
        cash_in_atm = 0
        for money_field in sql.fetchall():
            cash_in_atm += money_field[0] * money_field[1]
        return cash_in_atm

    def top_up_the_balance_atm(self):
        pass

    def withdraw_the_balance_atm(self):
        pass

# Account.create_account('Misha', 'gfg$$ghg', 1000)

# print(ATM.cash_in_atm())
# Account.create_account('Nikita', '12;:%№;3', 100)
# Account.create_account('admin')
