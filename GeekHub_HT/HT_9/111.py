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


# print(check_user_in_system('Ashot', '12345g'))

sql.close()

# 1. Look at the balance
# 2. Top up the balance
# 3. Take the money
# 4. Exit
