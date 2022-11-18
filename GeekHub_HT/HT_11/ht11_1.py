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
    """The class was created to calculate elementary arithmetic operations

        Raises:
            ZeroDivisionError: if in __truediv__ second argument == 0

        Returns:
            _type_: integer or float
        """
    last_result = None

    @staticmethod
    def check_number(number):
        try:
            number = float(number)
        except ValueError as err:
            print(err, '\nNeed float or integer number')
            return False
        return float(number)

    def add(self, first_number, second_number):
        if not Calc.check_number(first_number) and Calc.check_number(second_number):
            return 'Numbers must be float or integer'
        last_result = first_number + second_number
        Calc.last_result = last_result
        return last_result

    def mul(self, first_number, second_number):
        if not Calc.check_number(first_number) and Calc.check_number(second_number):
            return 'Numbers must be float or integer'
        last_result = first_number * second_number
        Calc.last_result = last_result
        return last_result

    def my_mod(self, first_number, second_number):
        if not Calc.check_number(first_number) and Calc.check_number(second_number):
            return 'Numbers must be float or integer'
        if second_number == 0:
            raise ZeroDivisionError
        last_result = first_number / second_number
        Calc.last_result = last_result
        return last_result

    def sub(self, first_number, second_number):
        if not Calc.check_number(first_number) and Calc.check_number(second_number):
            return 'Numbers must be float or integer'
        last_result = first_number * second_number
        Calc.last_result = last_result
        return last_result


a = Calc()
print(a.last_result)
print(a.add(1, 4))
print(a.last_result)
print(a.sub(10, 20))
print(a.last_result)
print(a.mul(11, 33))
print(a.last_result)
print(a.my_mod(11, 33))
print(a.last_result)
