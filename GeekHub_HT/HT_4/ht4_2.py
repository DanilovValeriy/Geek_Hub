''' Створіть 3 рiзних функцiї (на ваш вибiр). 
Кожна з цих функцiй повинна повертати якийсь результат 
(напр. інпут від юзера, результат математичної операції тощо). 
Також створiть четверту ф-цiю, яка всередині викликає 3 попередні,
обробляє їх результат та також повертає результат своєї роботи. 
Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.'''

def say_hello(name):
    return f'Hello, {name}'


def validate_date(date):
    try:
        date = float(date)
        return date
    except:
        return False


def validate_age(age):
    return float(age) > 18


def lets_go_beer():
    flag = True
    iteration = 1
    while flag:
        if iteration == 1:
            my_name = input('Input your name\n')
            say_hello(my_name)
            my_age = input(f'Hi, {my_name}. How old are you?\n')

        if iteration > 1:
            my_age = input(f'Hey, {my_name}. Are you kidding me? Input your age. It must be number\n')

        if validate_date(my_age):
            flag = False
            print("Let's go have a beer") if validate_age(my_age) else print('Go to bed, kid')
    
        else:
            iteration += 1
    
lets_go_beer()
