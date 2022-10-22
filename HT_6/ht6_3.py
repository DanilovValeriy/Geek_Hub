'''3. На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів 
   (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, 
   перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)'''


class MyException(BaseException):
   pass


def validation(password):
   if not 3 < len(password) < 51:
      raise MyException('The password must be more than three and less than 51 characters')
   elif not(set('1234567890').intersection(set(password)) and len(password) > 8):
      raise MyException('the password must be at least 8 characters long and must contain at least one number')
   elif not set('@#$%^&*!?').intersection(set(password)):
      raise MyException('the password must contain one of "@#$%^&*!?" characters')
   return 'Your password is OK'


users_list = [('Alex', 'ff'), ('Valerii', 'qwerty12#ff'), ('Oleg', 'q1w2e3r4'),\
         ('Ivan', 'Moskva5&&&&'), ('buryat', 'gruz200')]

for user in users_list:
    try:
        print(f'Name: {user[0]}', f'Password: {user[1]}', f'Status: {validation(user[1])}', sep='\n')
    except MyException as my_err:
        print(f'Name: {user[0]}', f'Password: {user[1]}', f'Status: {my_err}', sep='\n')
        # print(my_err)
    print()
