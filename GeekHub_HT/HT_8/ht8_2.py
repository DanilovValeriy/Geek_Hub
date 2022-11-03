'''2. Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів.
Файл також додайте в репозиторій.
На екран має бути виведений список із трьома блоками - символи з початку,
із середини та з кінця файлу. Кількість символів в блоках - та, яка введена в другому параметрі.
Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі або,
наприклад, файл із двох символів і треба вивести по одному символу,
то що виводити на місці середнього блоку символів?).
Не забудьте додати перевірку чи файл існує.'''


class MyError(BaseException):
    pass


def middle_of_two_symbols(my_str):
    return [my_str[0], 'None', my_str[1]]


def blocks_of_data(my_file, number=1):
    try:
        with open(my_file, 'r', encoding='utf-8') as my_file:
            my_str = ''.join(my_file.readlines())
            if len(my_str) < number:
                raise MyError(f'functon must get less than {len(my_str)}, get {number}')
            elif len(my_str) == 2 and number == 1:
                return middle_of_two_symbols(my_str)
            middle = len(my_str) // 2
        return [my_str[:number], my_str[middle - number // 2:middle + number // 2 + number % 2], my_str[-number:]]
    except FileNotFoundError as err:
        print(err)


# print(blocks_of_data('two_symbol.txt', 1))

# print(blocks_of_data('one_symbol.txt', 1))
print(blocks_of_data('my_txt.txt', 5))
# a = middle_of_two_simbols('two_symbol.txt')
