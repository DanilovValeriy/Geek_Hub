'''2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параметрів не відповідає вимогам - породити виключення із відповідним текстом.'''
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

# print(validation('rt'))
# print(validation('gfhdj3333'))
# print(validation('@kfkhkfjdkjfc17'))
