'''7. Написати функцію, яка приймає на вхід список (через кому), 
підраховує кількість однакових елементів у ньому і виводить результат. 
Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"'''


my_list = [1, 1, 0, 0, 'foo',{3, 6, 9, 12}, [1, 2], True, False, 'foo', 1, [1, 2], [1, 2], [1, 2], {6: 6, 7: 7, 8: 8}, {3, 6, 9, 12}, {6: 6, 7: 7, 8: 8}]


def counter(my_list, element):
    if isinstance(element, (dict, list, set)):
        return len(list(filter(lambda x: x == element, my_list)))
    else:
        return len(list(filter(lambda x: x is element, my_list)))


def my_func(m_list):
    list_of_values = []
    finish_list = []
    for el in m_list:
        if not counter(list_of_values, el):
            finish_list.append(f'{el} --> {counter(m_list, el)}')
            list_of_values.append(el)
    return ', '.join(finish_list)


print(my_func(my_list))