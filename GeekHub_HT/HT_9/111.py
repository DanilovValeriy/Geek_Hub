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


# sql.execute(
#     "INSERT INTO users (login, password, balance, is_collector) VALUES ('my_login', 'my_password', "
#     "0, False)")
# db.commit()


# def login_user(my_login, my_password):
#     sql.execute(
#         "INSERT INTO users (login, password, balance, is_collector) VALUES ('my_login', 'my_password', "
#         "0, False)")
#
#     db.commit()


def add_users(my_login1, my_password1):
    sql.execute(f"INSERT INTO users (login, password, balance, is_collector) VALUES (?, ?, ?, ?)",
                (my_login1, my_password1, 0, False))
    db.commit()


# add_users('Ashot', '12345')
# add_users('Den', 'frgdhGG^')


def is_login_allowed(my_login):
    sql.execute("SELECT login FROM users")
    if (my_login,) in sql.fetchall():
        print("You can't use this login")
        return False
    else:
        print('There is no user with this login in the system')
        return True


is_login_allowed('Dens')

# d = sql.execute("SELECT login FROM users")
# for el in sql.fetchall():
#     print(el)
# print(sql.fetchall())
# d = sql.fetchone("SELECT login FROM users")
# print(d[0])
# print(is_login_allowed('Valerii'))
# is_login_exist('Valerkii')
# login_user('Valerii', '123456')

sql.close()
