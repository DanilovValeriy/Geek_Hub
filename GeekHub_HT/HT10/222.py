DEN = [(1000, 0), (500, 1), (200, 4), (100, 0), (50, 5), (20, 5), (10, 0)]
D = [1000, 500, 200, 100, 50, 20, 10]
D1 = [1000, 500, 200, 100, 50, 20, 10]


def not_simple_decomposition(number, my_nominal):
    index = 0
    my_list = []
    for el in my_nominal:
        if number // el[0] > my_nominal[index][1]:
            my_list.append(my_nominal[index][1])
            number -= my_nominal[index][1] * el[0]
        else:
            my_list.append(number // el[0])
            number %= el[0]
        index += 1
    return my_list


def composition(my_list, nominal_list):
    my_sum = 0
    for el in zip(nominal_list, my_list):
        # print(el)
        my_sum += el[0] * el[1]
    return my_sum


def decomposition(number, D, DEN):
    arr_inside = D
    finnaly_list = []
    flag = True
    nom_list = DEN
    while flag:
        copy_simple_dec = not_simple_decomposition(number, nom_list)
        if composition(copy_simple_dec, arr_inside) == number:
            if not (finnaly_list):
                return copy_simple_dec
            else:
                return finnaly_list + copy_simple_dec
        if len(copy_simple_dec) == 0:
            return finnaly_list
        elif copy_simple_dec[0] > 0:
            finnaly_list.append(copy_simple_dec[0] - 1)
            el = copy_simple_dec.pop(0)
            number -= (el - 1) * arr_inside.pop(0)
            nom_list.pop(0)
        else:
            finnaly_list.append(copy_simple_dec.pop(0))
            nom_list.pop(0)
            try:
                arr_inside.pop(0)
            except IndexError as err:
                print('The entered amount cannot be issued')
                return None


s = decomposition(1170, D1, DEN)
# v = decomposition(110, D1, DEN)
# print('1170 =', s)
# print('110 =', v)

# print(composition(s, D1))
