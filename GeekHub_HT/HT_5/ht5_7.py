'''7. Написати функцію, яка приймає на вхід список (через кому), 
підраховує кількість однакових елементів у ньому і виводить результат. 
Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"'''


my_list = [1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2], {6: 6, 7: 7, 8: 8}, {3, 6, 9, 12}, {6: 6, 7: 7, 8: 8}]


def my_func(m_list):
    m_list = list(map(str, m_list))
    list_of_values = []
    finish_list = []
    for el in m_list:
        if el not in list_of_values:
            finish_list.append(f'{el} --> {m_list.count(el)}')
            list_of_values.append(el)
    return ', '.join(finish_list)


print(my_func(my_list))
