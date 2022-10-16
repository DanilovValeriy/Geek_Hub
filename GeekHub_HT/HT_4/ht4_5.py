'''Ну і традиційно - калькулятор :slightly_smiling_face: 
Повинна бути 1 функцiя, яка приймає 3 аргументи - один з яких операцiя, 
яку зробити! Аргументи брати від юзера (можна по одному - окремо 2, окремо +, 
окремо 2; можна всі разом - типу 2 + 2). 
Операції що мають бути присутні: +, -, *, /, %, //, **. 
Не забудьте протестувати з різними значеннями на предмет помилок!'''


# Реалізував для будь-якої кількості чисел і арифметичних операцій. 
# Реалізовано виключно для цілих чисел на вході.
# Ділення - ":"
# Ціла частина при діленні - "/"

# Вводити строкою без пробілів. Наприклад:
# 100+200-500*3/6 == -100


def data_validate(x):
    if set(x).difference('+', '-', '*', ':', '%', '/', '1', '2', '3',
     '4', '5', '6', '7', '8', '9', '0'):
       print('Invalid value!')
       return False
    else:
        return x
        


def my_split(my_str, my_arr):
    '''Function separated numbers and arifmetical operations from string'''
    s = ''
    ind = 0
    set_operation = {'+', '-', '*', ':', '%', '/'}
    for val in my_str:
        if val not in set_operation:
            s += val
        else:
            my_arr.append(s)
            my_arr.append(val)
            # якщо в частині строки, яка залишилася є оператори, то повторно розкладаємо
            if set(list(my_str[ind+1:])).intersection(set_operation):
                my_split(my_str[ind+1:], my_arr)
                break
            my_arr.append(my_str[ind+1:])
        ind += 1
    return my_arr


def calc(a, b, c):
    match b:
        case '+':
            return float(a) + float(c)
        case '-':
            return float(a) - float(c)
        case ':':
            if c != 0:
                return float(a) / float(c)
            else:
                print('Divizion by zero')
                return False
        case '*':
            return float(a) * float(c)
        case '%':
            if c != 0:
                return float(a) % float(c)
            else:
                print('Divizion by zero')
                return False
        case '/':
            if c != 0:
                return float(a) // float(c)
            else:
                print('Divizion by zero')
                return False


def my_calc(my_list):
    res = float(my_list[0])
    for ind in range(0,len(my_list)-2, 2):
        res = calc(res, my_list[ind + 1], my_list[ind + 2])
    return res


def calc_input():
    value = input('Input numbers with arifmatical operations\n')
    if not data_validate(value):
        print('You input incorrect values')
        return None
    else:
        print(my_calc(my_split(value, [])))

calc_input()
