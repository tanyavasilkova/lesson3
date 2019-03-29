import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

p1 = Point(2, 2)
p2 = Point(5, 5)

class Line(Point):

    def __repr__(self):
        return 'Координаты прямой: ({}, {})'.format(p1, p2)

    def sdvig_xy(self, delta_x, delta_y): # сдвиг отрезка по оси ОХ на delta_x, по си ОУ - delta_y
       self.x1 = p1.x + delta_x
       self.y1 = p1.y + delta_y
       self.x2 = p2.x + delta_x
       self.y2 = p2.y + delta_y
       return  'Координаты линии после сдвига линии на {} по ОХ, на {} по ОУ: ({}, {}),({}, {})'.format(delta_x, delta_y, self.x1, self.y1, self.x2, self.y2)

    def dlina(self):
        self.dl = '{:.2f}'.format(((p2.x-p1.x)*2 + (p2.y-p1.y)*2 )**.5)
        return 'Длина отрезка равна {}'.format(self.dl)

    def ygol(self):
        self.yg = math.degrees(math.atan((p2.y-p1.y)/(p2.x-p1.x)))
        return 'Угол наклона прямой к оси ОХ: {}'.format(self.yg)


l = Line(p1, p2)
print(p1) #  вывод коорд точки р1
print(p2) #  вывод коорд точки р2
print(l) #  вывод коорд прямой l
print(l.sdvig_xy(4,2))
print(l.dlina())
print(l.ygol())
