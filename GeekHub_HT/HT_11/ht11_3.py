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


#
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
    # Construct an Account object

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

    def working_with_atm(self):
        if not Account.login_in_account(self, self.login, self.pin_code):
            raise MyError('Access denied. Wrong login or password')
        else:
            print('HALLO')

    def __init__(self, login, pin_code, user_balance=0):
        self.login = login
        self.pin_code = pin_code
        self.__user_balance = user_balance

    # def user_connecting_to_db(self):
    #     pass

    def login_in_account(self, login, pin_code):
        return self.login == login and self.pin_code == pin_code

    @property
    def user_balance(self):
        return self.__user_balance

    @user_balance.setter
    def user_balance(self, amount):
        if not Account.__check_number(amount):
            raise MyError('Amount must be float or integer and more than 0.')
        self.__user_balance += amount

    def money_on_user_balance(self):
        sql.execute(f"SELECT login, balance FROM users")
        for el in sql.fetchall():
            if el[0] == self.login:
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
