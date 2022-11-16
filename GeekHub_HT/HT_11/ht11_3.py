"""Банкомат 4.0: переробіть программу з функціонального підходу програмування на використання класів.
Додайте шанс 10% отримати бонус на баланс при створенні нового користувача.
"""
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
class MyError(BaseException):
    pass


class Account:
    # Construct an Account object

    def working_with_atm(self):
        if not login_in_account(self, self.login, self.pin_code):
            raise MyError('Access denied. Wrong login or password')

    def __init__(self, login, pin_code, user_balance=0):
        self.login = login
        self.pin_code = pin_code
        self.user_balance = user_balance

    def login_in_account(self, login, pin_code):
        return self.login == login and self.pin_code == pin_code

    def checking_balance_of_user(self):
        return self.user_balance

    def withdraw_the_balance_of_user(self, amount):
        if not isinstance(amount, (int, float)) and amount < 0:
            return None
        # elif
        self.user_balance -= amount

    def top_up_the_balance_of_user(self, amount):
        if not isinstance(amount, (int, float)) and amount < 0:
            return None
        self.user_balance += amount


class ATM:
    DENOMINATION = [1000, 500, 200, 100, 50, 20, 10]

    def cash_in_atm(self):
        pass

    def top_up_the_balance_atm(self):
        pass

    def withdraw_the_balance_atm(self):
        pass
