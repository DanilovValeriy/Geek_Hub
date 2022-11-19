'''1. Напишіть програму, де клас «геометричні фігури» (Figure) містить властивість color
з початковим значенням white і метод для зміни кольору фігури, а його підкласи «овал» (Oval)
і «квадрат» (Square) містять методи _init_ для завдання початкових розмірів об'єктів при їх створенні.'''


class GeometricShapes:
    color = 'white'

    def change_color(self, new_color):
        self.color = new_color


class Ellipse(GeometricShapes):

    def __init__(self, semi_major_axis, semi_minor_axis, centre):
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis
        self.centre = centre


class Square(GeometricShapes):

    def __init__(self, side):
        self.side = side


my_ellips = Ellipse(10, 2, 0)
my_square = Square(30)
print(my_square.side)
print(my_square.color)
my_square.change_color('Black')
print(my_square.color)
