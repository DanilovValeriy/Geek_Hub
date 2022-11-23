'''
1. Створіть клас Car, який буде мати властивість year (рік випуску).
Додайте всі необхідні методи до класу, щоб можна було виконувати порівняння car1 > car2 , яке буде показувати,
що car1 старша за car2. Також, операція car1 - car2 повинна повернути різницю між роками випуску.
'''


class Car:
    def __init__(self, year):
        self.year = year

    def __lt__(self, other):
        return self.year > other.year

    def __sub__(self, other):
        return self.year - other.year


bmw = Car(2010)
toyota = Car(2000)

# must return True
print(toyota > bmw)
# must return 10
print(bmw - toyota)
