import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users (
            login TEXT,
            password TEXT,
            balance BIGINT,
            is_collector BOOLEAN            
            )""")
db.commit()


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
        print('There is no user with this login in the system')
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


print(look_balance('Den'))
change_balance('Den', 100, '-')

print(look_balance('Den'))

sql.close()

# 1. Look at the balance
# 2. Top up the balance
# 3. Take the money
# 4. Exit
