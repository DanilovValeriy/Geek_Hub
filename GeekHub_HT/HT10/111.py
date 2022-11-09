import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("SELECT denomination, number FROM bankomat")
ATM_LIST = sql.fetchall()
ATM_LIST_DESC = sorted(ATM_LIST)

print(ATM_LIST)
print(ATM_LIST_DESC)


def money_in_atm():
    sql.execute("SELECT denomination, number FROM bankomat")
    all_sum = 0
    for el in sql.fetchall():
        # print(el)
        # print(f'There are {el[1]} bills of denomination {el[0]}')
        all_sum += el[1] * el[0]
    return all_sum


print(money_in_atm())


def comparison_list(my_list):
    sql.execute("SELECT denomination, number FROM bankomat")
    atm_list = sql.fetchall()
    for i in range(7):
        if my_list[i] > atm_list[i][1]:
            return False
    return True


def simple_decomposition(number):
    sql.execute("SELECT denomination, number FROM bankomat")
    atm_list = sql.fetchall()
    # print(atm_list)
    index = 0
    my_list = []
    for el in atm_list:
        if number // el[0] > atm_list[index][1]:
            my_list.append(atm_list[index][1])
            number -= atm_list[index][1] * el[0]
        else:
            my_list.append(number // el[0])
            number %= el[0]
    return my_list


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
            # logging('admin', f'Looking ATM denomination - {nominal}, number - {old_number}')
            continue
        operation = choose_operation()
        if operation == '+':
            my_number = my_input()
            print(f'ATM has {old_number} of {nominal}')
            sql.execute(f"UPDATE bankomat SET number =? where denomination =?",
                        (old_number + int(my_number), nominal))
            db.commit()
            print(f'ATM have {old_number + int(my_number)} of {nominal}')
            # logging('admin', f'Put on the ATM denomination - {nominal}, number - {my_number}')
        else:
            my_number = my_input()
            print(f'ATM has {old_number} of {nominal}')
            while my_number > old_number:
                print(f'There are not enough bills of this denomination. ATM contains {old_number} numbers')
                # logging('admin', 'There are not enough bills of this denomination')
                my_number = my_input()
            sql.execute(f"UPDATE bankomat SET number =? where denomination =?",
                        (old_number - int(my_number), nominal))
            db.commit()
            print(f'ATM have {old_number - int(my_number)} of {nominal}')
            # logging('admin', f'Admin took the money from ATM denomination - {nominal}, number - {my_number}')


c = simple_decomposition(4080)
print(c)
# print(comparison_list(c))
# change_bankomat_cash()
# simple_decomposition(4570)
