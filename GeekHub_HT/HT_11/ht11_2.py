"""2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати якісь аргументи,
які зберігатиме в відповідні змінні. - Методи, які повинні бути в класі Person - show_age, print_name,
show_all_information. - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атрибут
profession (його не має інсувати під час ініціалізації в самому класі) та виведіть його на екран (прінтоніть)
"""


class Person:

    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name

    def show_age(self):
        print(self.age)

    def print_name(self):
        print(self.name)

    def show_all_information(self):
        print(f'My name is {self.name}. I am {self.age} years old')


david = Person('David', 39)
sashko = Person('Sashko', 22)

david.profession = 'Associate Professor of Mathematical Sciences'
sashko.profession = 'Loader'

print(david.profession)
print(sashko.profession)
