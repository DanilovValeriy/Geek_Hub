'''1. Напишіть програму, де клас «геометричні фігури» (Figure) містить властивість color
з початковим значенням white і метод для зміни кольору фігури, а його підкласи «овал» (Oval)
і «квадрат» (Square) містять методи _init_ для завдання початкових розмірів об'єктів при їх створенні.'''


class GeometricShapes:
    color = 'white'

    def change_color(self, new_color):
        self.color = new_color

