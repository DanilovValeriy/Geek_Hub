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

db = sqlite3.connect('my.db')
sql = db.cursor()


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

# 1. Look at the balance
# 2. Top up the balance
# 3. Take the money
# 4. Exit
