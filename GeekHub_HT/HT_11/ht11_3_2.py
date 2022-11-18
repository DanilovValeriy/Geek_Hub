"""Банкомат 4.0: переробіть программу з функціонального підходу програмування на використання класів.
Додайте шанс 10% отримати бонус на баланс при створенні нового користувача.
"""

import random
import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()
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
#
# USERS = [
#     ('Den', 'FRt%^%56', 1000, False),
#     ('Valerii', '1234%%55', 1000, False),
#     ('admin', 'admin', 10000, True),
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

denomination_of_banknotes = [1000, 500, 200, 100, 50, 20, 10]


def logging(my_login, my_action):
    sql.execute(f"INSERT INTO transactions (login, action) VALUES (?, ?)",
                (my_login, my_action))
    db.commit()


def choose_operation():
    oper = input("Choose operation '+' or '-': ")
    while oper not in {'+', '-'}:
        oper = input("Choose operation '+' or '-': ")
    return oper


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


class ATM:
    def __init__(self, name, account_password, balance=0, exist=0):
        self.name = name
        if self.is_admin(account_password):
            self.account_password = account_password
        else:
            raise Exception('Your password must contain more 5 characters and contain !@#$%^&')
        self.balance = balance
        if exist == 0:
            self.create_new_user()

    def create_new_user(self):
        sql.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (self.name, self.account_password, self.balance, 0))
        db.commit()
        logging(self.name, 'Has been created')

    def cash_in_the_bankomat(self):
        sql.execute("SELECT denomination, number FROM bankomat")
        my_sum = 0
        for el in sql.fetchall():
            my_sum += el[0] * el[1]
        return my_sum

    def check_password(self, password):
        if len(password) > 5 and set('!@#$%^&*').intersection(set(password)) or password == 'admin':
            return True
        else:
            return False

    @staticmethod
    def check_number(amount):
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

    @staticmethod
    def user_balance(login):
        sql.execute(f"SELECT login, balance FROM users")
        for el in sql.fetchall():
            if el[0] == login:
                return el[1]

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

    def change_atm_cash(self):
        if self.name != 'admin':
            print('Access denied')
            return None
        else:
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

    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Password: {self.account_password}")
        print(f"Available balance: {self.balance}\n")

    @staticmethod
    def denomination_in_atm(f_print=True):
        sql.execute("SELECT denomination, number FROM bankomat")
        val = sql.fetchall()
        for el in val:
            if f_print:
                print(f'Denomination {el[0]} has {el[1]}')
        return val

    def deposit(self, amount):
        if ATM.check_number(amount):
            # lottery chance
            lottery = random.randint(1, 1000)
            if lottery % 10 == 0:
                print('YOU WIN!!!\n CONGRATULATIONS!!!\n You got +10% to your amount\n')
                self.balance = self.balance + amount * 1.1
            else:
                self.balance = self.balance + amount
            sql.execute(f"UPDATE users set balance =? where login =?", (self.balance, self.name))
            db.commit()
            print(f'Your account has been topped up. The amount on the account is {self.balance}')
            logging(self.name, f'Your account has been topped up. The amount on the account is {self.balance}')

            print("Current account balance: ", self.balance)
        else:
            print(f'You can not put {amount}')

    def history_of_logging(self):
        sql.execute(f"SELECT login, action FROM transactions")
        for el in sql.fetchall():
            if self.name == 'admin':
                print(f'{el[0]} has operation {el[1]}')
            elif el[0] == login:
                print(el[1])

    def withdraw(self, amount):
        if not ATM.check_number(amount):
            print(f'You can not withdraw {amount}')
            return None
        elif amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is {self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - amount
            sql.execute(f"UPDATE users set balance =? where login =?", (self.balance, self.name))
            db.commit()
            print(f'You have withdrawn {self.balance}. The amount in the account is {self.balance}')
            logging(self.name, f'You have withdrawn {amount}. The amount in the account is {self.balance}')
            print(f"{amount} withdrawal successful!")
            print("Current account balance: ", self.balance)
            print()

    def check_balance(self):
        sql.execute(f"SELECT login, balance FROM users")
        for el in sql.fetchall():
            if el[0] == self.name:
                return el[1]

    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Information
            6. Exit
            11. If you admin input 11
        *********************
        """)
        option = 0
        while option != 6:
            try:
                option = int(input("Enter 1, 2, 3, 4, 5 or 6 for exit: "))
            except:
                print("Error: Enter 1, 2, 3, 4, 5 or 6 only!\n")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    print(f'You got {atm.check_balance()}')
                elif option == 3:
                    amount = int(input("How much you want to deposit():"))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw():"))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
                printing receipt..............
          ******************************************
              Transaction is now complete.                         
              Transaction number: {random.randint(10000, 1000000)} 
              Account holder: {self.name.upper()}                  
              Account password: {self.account_password}                
              Available balance: {self.balance}                    

              Thanks for choosing us as your bank                  
          ******************************************
          """)
                elif option == 11:
                    if self.name != 'admin' or self.account_password != 'admin':
                        print('Access denied')
                        continue
                    else:
                        print('Hello, Big Boss! Make your choice')
                        choice = 0
                        while choice != 4:
                            try:
                                choice = int(input(
                                    'Choice operation\n1. Denomination and balance ATM\n2. Change the balance ATM\n'
                                    '3. History of using ATM\n4. Exit\n'))

                                match choice:
                                    case 1:
                                        print(f'Balance of the ATM {atm.cash_in_the_bankomat()}')
                                        ATM.denomination_in_atm()
                                        logging('admin', 'Big boss looking the balance an ATM')
                                    case 2:
                                        self.change_atm_cash()

                                    case 3:
                                        self.history_of_logging()

                            except ValueError as err:
                                print(err)


print("*******WELCOME TO BANK*******")

choice = 0
while choice not in {'x', 'X'}:
    choice = input("Do you have an account? y/n. Press x or X to exit\n")
    if choice == "y":
        login = input('Input your login: ')
        password = input('Input your password: ')
        if ATM.check_user_in_system(login, password):
            atm = ATM(login, password, ATM.user_balance(login), 1)
            atm.transaction()
    elif choice == 'n':
        choice = input("Do you want to create an account? y/n. Press x or X to exit\n")
        if choice == 'y':
            print("___________________________________________________________\n")
            print("----------ACCOUNT CREATION----------")
            login = input("Enter your name: ")
            password = input("Enter your password MORE than 5 characters and contain !@#$%^: ")
            atm = ATM(login, password)
            atm.transaction()
            print("Congratulations! Account created successfully......\n")

print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
