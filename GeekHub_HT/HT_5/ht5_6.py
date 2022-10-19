'''6. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. 
Тобто функція приймає два аргументи: список і величину зсуву 
(якщо ця величина додатна - пересуваємо з кінця на початок, якщо від'ємна - 
навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
   fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
   fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]'''


def validator(data):
    try:
        data = int(data)
    except ValueError as err:
        print(err)
        return False
    return True


def fnc(my_list, shift):
    if not(validator(shift)):
        return None
    my_list_2 = []
    for i in range(len(my_list)):
        my_list_2.append(my_list[(i + shift) % len(my_list)])
    return my_list_2


print(fnc([1, 2, 3, 4, 5, 6, 7, 8], 17))
print(fnc([1, 2, 3, 4, 5, 6, 7, 8], 'f'))
