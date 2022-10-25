'''1. Створіть функцію, всередині якої будуть записано СПИСОК із п'яти користувачів (ім'я та пароль). 
Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) 
і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
Логіка наступна:
    якщо введено правильну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція повертає False
        якщо silent == False - породжується виключення LoginException (його також треба створити =))'''



class MyException(BaseException):
    pass 


def my_users(username, password, silent=False):
    users_list = [('Alex', '12345'), ('Valerii', 'qwerty'), ('Oleg', 'q1w2e3r4'),\
         ('Ivan', 'Moskva5'), ('buryat', 'gruz200')]
    if (username, password) in users_list:
        return True
    else:
        if silent is True:
            return False
        else:
            raise MyException('You got a problem, man')


print(my_users('Alex', '12345e', True))
print(my_users('Alex', '12345', True))
print(my_users('Alex', '12345e'))
