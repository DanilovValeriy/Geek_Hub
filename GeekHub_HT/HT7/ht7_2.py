'''2. Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100 не включно), 
сума цифр кожного елемент якого буде дорівнювати 10.
   Результат: [19, 28, 37, 46, 55, 64, 73, 82, 91]'''


# костиль =) для фана
list_generator = [i for i in range(19,100,9)]
print(list_generator)


list_generator_2 = [num for num in range(100) if num // 10 + num % 10 == 10]
print(list_generator_2)
