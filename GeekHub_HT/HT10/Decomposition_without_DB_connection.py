cash_in_terminal = [(1000, 5), (500, 1), (200, 4), (100, 0), (50, 1), (20, 3), (10, 0)]

denomination_of_banknotes = [1000, 500, 200, 100, 50, 20, 10]


def my_print(my_list_of_decomposition):
    if isinstance(my_list_of_decomposition, str):
        print(str)
        return None
    denomination = [1000, 500, 200, 100, 50, 20, 10]
    for index, number in enumerate(my_list_of_decomposition):
        if number:
            print(f'{denomination[index]} count {number}')
    return None


def simple_decomposition(number, cash_in_terminal_list):
    resulting_list = []
    for index, el in enumerate(cash_in_terminal_list):
        if number // el[0] > cash_in_terminal_list[index][1]:
            resulting_list.append(cash_in_terminal_list[index][1])
            number -= cash_in_terminal_list[index][1] * el[0]
        else:
            resulting_list.append(number // el[0])
            number %= el[0]
    return resulting_list


def composition(my_decomposition_list, nominal_list):
    my_sum = 0
    for el in zip(nominal_list, my_decomposition_list):
        my_sum += el[0] * el[1]
    return my_sum


def decomposition(number, denomination_of_banknotes, cash_in_terminal):
    number = (number // 10) * 10
    list_of_denomination = denomination_of_banknotes[:]
    resulting_list = []
    flag = True
    cash_in_terminal_list = cash_in_terminal[:]
    while flag:
        list_from_simple_decomposition = simple_decomposition(number, cash_in_terminal_list)
        if composition(list_from_simple_decomposition, list_of_denomination) == number:
            if not resulting_list:
                return list_from_simple_decomposition
            else:
                return resulting_list + list_from_simple_decomposition
        if len(list_from_simple_decomposition) == 0:
            return resulting_list
        elif list_from_simple_decomposition[0] > 0:
            resulting_list.append(list_from_simple_decomposition[0] - 1)
            coefficient = list_from_simple_decomposition.pop(0)
            number -= (coefficient - 1) * list_of_denomination.pop(0)
            cash_in_terminal_list.pop(0)
        else:
            resulting_list.append(list_from_simple_decomposition.pop(0))
            cash_in_terminal_list.pop(0)
            try:
                list_of_denomination.pop(0)
            except IndexError:
                print('The entered amount cannot be issued')
                return None


def checking_correctness_amount(number, decomposite_list):
    return number == composition(decomposite_list, denomination_of_banknotes)


def result_of_decomposition(number):
    decomposite_list = decomposition(1170, denomination_of_banknotes, cash_in_terminal)
    if checking_correctness_amount(number, decomposite_list):
        return decomposite_list
    else:
        return "Can't withdraw this sum"



my_print(result_of_decomposition(1170))
