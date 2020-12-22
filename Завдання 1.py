#
# конструктор без параметрів, конструктор з параметрами, конструктор копіювання;
# введення/виведення елементів вектора;
# визначення довжини вектора;
# нормування вектора;
# порівняння з іншим вектором;
# перевантаження операторів + (додавання векторів), – (віднімання векторів), * (знаходження скалярного добутку).
#

import math
class TVektor2D:
    def __init__(self, *args):
        arguments_count = len(args)
        if arguments_count == 0:
            self.x1 = 0
            self.x2 = 0
            self.y1 = 1
            self.y2 = 1

        elif arguments_count == 1:
            self.x1 = args[0]
            self.x2 = 0
            self.y1 = 0
            self.y2 = 0

        elif arguments_count == 2:
            self.x1 = args[0]
            self.x2 = args[1]
            self.y1 = 0
            self.y2 = 0

        elif arguments_count == 3:
            self.x1 = args[0]
            self.x2 = args[1]
            self.y1 = args[2]
            self.y2 = 0

        else:
            self.x1 = args[0]
            self.x2 = args[1]
            self.y1 = args[2]
            self.y2 = args[3]



    @property
    def function(self):
        print('firs vektor = [{0}, {1}]'.format(self.x1, self.x2))
        print('second vektor = [{0}, {1}]'.format(self.y1, self.y2))

    @property
    def lehghtVekror(self):
        return print(math.fabs(math.sqrt(((self.x1 - self.y1) ** 2 ) + ((self.x2 - self.y2) ** 2))))

    @property
    def normalizationvektor(self):
        z = (math.pow(self.x1, 2) + math.pow(self.x2, 2) + (self.y1 ** 2) + (self.x2 ** 2))
        print('x1 = ', self.x1/z)
        print('x2 = ', self.x2/z)
        print('y1 = ', self.y1/z)
        print('y2 = ', self.y2/z)

    @property
    def comparison(self):
        A = math.sqrt(math.pow(self.x1, 2) + math.pow(self.x2, 2))
        B = math.sqrt(math.pow(self.y1, 2) + math.pow(self.y2, 2))
        A = math.fabs(A)
        B = math.fabs(B)
        return (A, B)
    def __add__(self, other):
        return TVektor2D(self.x1 + other,
                         self.x2 + other,
                         self.y1 + other,
                         self.y2 + other)

    def __sub__(self, other):
        return TVektor2D(self.x1 - other,
                         self.x2 - other,
                         self.y1 - other,
                         self.y2 - other)

    def __mul__(self, other):
        return TVektor2D(self.x1 * other,
                         self.x2 * other,
                         self.y1 * other,
                         self.y2 * other)



g = TVektor2D(5, 8, 3, 2)
# ------2
g.function
# ------3
g.lehghtVekror
# ------4
g.normalizationvektor
# ------5
print(g.comparison)
p = g+10
# ------6
print(p.function)
p = g - 10
# ------7
print(p.function)
# ------8
p = g * 2
print(p.function)
