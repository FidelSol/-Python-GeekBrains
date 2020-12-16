# Задание №1
class Matrix:


    def __init__(self, *args):
        self.list_of_lists = []
        for n in args:
            self.list_of_lists.append(n)

    def __str__(self):
        for n in range(0, len(self.list_of_lists)):
            print(self.list_of_lists[n])
            if len(self.list_of_lists[n]) != len(self.list_of_lists[0]):
                return f"Неверно введены данные для матрицы!"
                break
        return f'Матрица {len(self.list_of_lists)} на {len(self.list_of_lists[0])}'

    def __add__(self, other):
        self.new_list_of_lists = []
        for x in range(0, len(self.list_of_lists)):
            self.sum_matrix = [self.list_of_lists[x][n] + other.list_of_lists[x][n] for n in range(0, len(self.list_of_lists[0]))]
            self.new_list_of_lists.append(self.sum_matrix)
        for n in range(0, len(self.new_list_of_lists)):
            print(self.new_list_of_lists[n])
        return f'Матрица {len(self.new_list_of_lists)} на {len(self.new_list_of_lists[0])}'

m1 = Matrix([1, 1, 1], [2, 2, 2], [3, 3, 3])
print(m1)
m2 = Matrix([1, 1, 1], [2, 2, 2], [3, 3, 3])
print(m2)
print(m1 + m2)


# Задание №2

class Coat:
    def __init__(self, v):
        self.consumption = round(v / 6.5 + 0.5)

    def __str__(self):
        return f'Пальто - расход {self.consumption}'

class Suit:
    def __init__(self, h):
        self.consumption = round(2 * h + 0.3)

    def __str__(self):
        return f'Костюм - расход {self.consumption}'

class Clothes:
    def __init__(self):
        self.consumption = 0
        self.main_list = []

    def __str__(self):
        return f'Одежда'

    def add_main(self, v, h):
        self.main_list.append(Coat(v))
        self.main_list.append(Suit(h))

    @property
    def main_consuption(self):
        for el in self.main_list:
            self.consumption += el.consumption
        print('Полный расход')
        return self.consumption

c = Coat(40)
s = Suit(30)
print(c)
print(s)
cl = Clothes()
print(cl)
cl.add_main(30, 40)
print(cl.main_consuption)


# Задание №3

class Cell:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'Количество ячеек в клетке - {self.number}'

    def __add__(self, other):
        print(f'Сложение клеток. {Cell(self.number + other.number)}')
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number > other.number:
            print(f'Разница клеток. {Cell(self.number - other.number)}')
            return Cell(self.number - other.number)
        elif self.number < other.number:
            print(f'Разница клеток. {Cell(other.number - self.number)}')
            return Cell(other.number - self.number)
        else:
            print(f'Деление невозможно!')

    def __mul__(self, other):
        print(f'Умножение клеток. {Cell(other.number * self.number)}')
        return Cell(other.number * self.number)

    def __truediv__(self, other):
        print(f'Деление клеток. {Cell(other.number / self.number)}')
        return Cell(other.number / self.number)

    def make_order(self):
        x = '*****/n'
        y = '*'
        line_cell = (self.number // 5) * x + (self.number - (5 * (self.number // 5))) * y
        print(f'Ячейки: ')
        print(line_cell)
        return line_cell

c1 = Cell(10)
print(c1)
c2 = Cell(7)
print(c2)
print(c1 + c2)
print(c2 - c1)
print(c1 * c2)
print(c1 / c2)
c1.make_order()
c2.make_order()


















