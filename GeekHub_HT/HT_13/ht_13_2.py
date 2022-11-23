'''
2. Створити клас Matrix, який буде мати наступний функціонал:
1. __init__ - вводиться кількість стовпців і кількість рядків
2. fill() - заповнить створений масив числами - по порядку. Наприклад:
+────+────+
| 1  | 2  |
+────+────+
| 3  | 4  |
+────+────+
| 5  | 6  |
+────+────+
3. print_out() - виведе створений масив (якщо він ще не заповнений даними - вивести нулі
4. transpose() - перевертає створений масив. Тобто, якщо взяти попередню таблицю, результат буде
+────+────+────+
| 1  | 3  | 5  |
+────+────+────+
| 2  | 4  | 6  |
+────+────+────+
P.S. Всякі там Пандас/Нампай не використовувати - тільки хардкор ;)
P.P.S. Вивід не обов’язково оформлювати у вигляді таблиці - головне, щоб було видно, що це окремі стовпці / рядки
'''


class Matrix:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.__fill = None
        self.matrix = None

    def count_of_element_in_matrix(self):
        return self.rows * self.columns

    def fill(self):
        self.__fill = [i for i in range(1, self.columns * self.rows + 1)]
        return self.__fill

    def create_matrix(self):
        matrix = []
        for i in range(self.rows):
            row_list = []
            for j in range(self.columns):
                row_list.append(self.__fill[self.columns * i + j])
            matrix.append(row_list)
        self.matrix = matrix
        return self.matrix

    def print_out(self):
        matrix_list = self.create_matrix()
        for lists in matrix_list:
            print(*lists, sep='|')

    def transpose(self):
        transpose_matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        for row in transpose_matrix:
            print(row)


my_matrix = Matrix(2, 3)
print(my_matrix.fill())
my_matrix.print_out()
print(my_matrix.create_matrix())
print('Transpose matrix')
my_matrix.transpose()
