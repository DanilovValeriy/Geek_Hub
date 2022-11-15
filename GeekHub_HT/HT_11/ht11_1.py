'''HT #11
1. Створити клас Calc, який буде мати атребут last_result та 4 методи.
Методи повинні виконувати математичні операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
- Якщо під час створення екземпляру класу звернутися до атрибута last_result він повинен повернути пусте значення.
- Якщо використати один з методів - last_result повинен повернути результат виконання ПОПЕРЕДНЬОГО методу.
    Example:
    last_result --> None
    1 + 1
    last_result --> None
    2 * 3
    last_result --> 2
    3 * 4
    last_result --> 6
    ...
- Додати документування в клас (можете почитати цю статтю:
https://realpython.com/documenting-python-code/ )'''


class Calc:
    last_result = None

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        last_result = self.number + other.number
        return self.number + other.number

    def __mul__(self, other):
        last_result = self.number * other.number
        return self.number * other.number

    def __truediv__(self, other):
        if other.number == 0:
            raise ZeroDivisionError(f'Division by zero!')
        last_result = self.number / other.number
        return self.number / other.number

    def __sub__(self, other):
        last_result = self.number - other.number
        return self.number - other.number


first = Calc(10)
second = Calc(100)
print(first.last_result)
print(first / second)
print(first.last_result)
# print(dir(first))
# print(first // second)
print(second - first)
print(first.last_result)
