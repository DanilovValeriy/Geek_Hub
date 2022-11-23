'''
4. Створіть клас, який буде повністю копіювати поведінку list, за виключенням того,
що індекси в ньому мають починатися з 1, а індекс 0 має викидати помилку
(такого ж типу, яку кидає list якщо звернутися до неіснуючого індексу)
'''


class MyList(list):
    def __getitem__(self, index):
        if index == 0:
            raise IndexError("list index out of range")
        index -= 1
        return super().__getitem__(index)


my_list = MyList((1, 2, 3, 4, 5, 6))
print(my_list)

print(f'Index 1 = {my_list[1]}')
print(f'Index 2 = {my_list[2]}')
print(f'Index 3 = {my_list[3]}')
print(f'Index 4 = {my_list[4]}')
print(f'Index 5 = {my_list[5]}')
print(f'Index 6 = {my_list[6]}')

# raise Exception IndexError
# my_list[0]
