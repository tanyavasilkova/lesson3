class Point:
    def __init__(self, x, y):
        self.coord = (x, y)

    def __repr__(self):
        return "Point(%s, %s)" % self.coord

p1 = Point(1, 2)
p2 = Point(4, 5)
print(p1)
print(p2)

class Line:
    delta_x = 3  # сдвиг всего отрезка по оси ОХ: если значение положительное - вправо, отрицательное - влево
    delta_y = 1  # сдвиг всего отрезка по оси ОУ: если значение положительное - вверх отрицательное - влево

    def __init__(self, p1, p2):
        self.line = (p1, p2)

    def __repr__(self):
        return "Line(%s, %s)" % self.line

    def sdvig_x(self, a, b, d):
        a = self.p1.((x + delta_x),y)
        a = self.p2.((x + delta_x), y)

        self.d = ()
        return


l = Line(p1, p2)
print(l)

