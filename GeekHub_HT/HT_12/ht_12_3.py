'''3. Створіть клас в якому буде атрибут який буде рахувати кількість створених екземплярів класів.'''


class MyClass:
    counter = 0

    def __init__(self):
        MyClass.counter += 1


first = MyClass()
second = MyClass()
third = MyClass()

print(first.counter)
print(second.counter)
print(third.counter)
