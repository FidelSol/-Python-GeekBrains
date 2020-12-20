# Задание №1
class Data:
    def __init__(self):
        try:
            self.start_date = input("Введите дату в формате 'день-месяц-год': ")

        except ValueError:
            print("Неверный формат!")

    def __str__(self):
        return f'{self.start_date}'

    @classmethod
    def retrieve(cls, start_date):
        list = [int(el) for el in start_date.split('-')]
        print(list)
        return list

    @staticmethod
    def validation(list):
        if 1 <= list[0] < 32 and 1 <= list[1] <= 12:
            if list[2] > 0:
                print(f"Данные валидны: день - {list[0]}, месяц - {list[1]}, год - {list[2]}.")
            else:
                print('Данные невалидны!')

d1 = Data()
print(d1)
Data.retrieve('20-12-2020')
d1.retrieve('20-12-2020')
Data.validation([20, 12, 2020])
d1.validation([20, 12, 2020])

# Задание №2
class NotNumber(ValueError):
    pass

my_list = []
while True:
    try:
        value = input('Введите положительное число в список: ')
        if value == 'stop':
            break
        if not value.isdigit():
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as ex:
        print('Не валидно!', ex)
print(my_list)

# Задание №3
class MyZeroDivision(ZeroDivisionError):
    def __init__(self, txt):
        print(f'Мой обработчик - {txt}')

inp = (input('Введите частное и делитель через запятую: ')).split(',')
data = [int(el) for el in inp if len(inp) == 2]
try:
    if data[1] == 0:
        raise MyZeroDivision('Делить на ноль нельзя!!!')
    else:
        div = data[0] / data[1]
except MyZeroDivision as err:
    print(err)
except ValueError:
    print("Невалидные данные!!!")
else:
    print(f'Деление равно {div}')
finally:
    print(f'Программа завершена')

# Задание №4, 5, 6
class Storage:
    data = {}
    def __init__(self, grade, square):
        self.grade = grade
        self.square = square


    def __str__(self):
        return f'Склад оргтехники класса {self.grade}, площадь склада - {self.square} кв.м.'

    @classmethod
    def to_retrieve(cls, name, number):
        number_int = isinstance(number, int)
        if number_int == False:
            print("Количество товара вводится числом!")
        else:
            cls.data.update({name: number})
            print(f'На склад оргтехники поступил товар: {name} в количестве {number}')
            print(cls.data)
            return cls.data

    @classmethod
    def to_refer(cls, name, number, firm):
        number_int = isinstance(number, int)
        if number_int == False:
            print("Количество товара вводится числом!")
        else:
            rest = cls.data.get(name) - number
            if rest >= 0:
                cls.data.update({name: rest})
                print(f'В фирму {firm} передан товар {name} в количестве {number}')
                return cls.data
            else:
                print(f"На складе товара {name} всего в количестве {cls.data.get(name)}. Вы не можете передать в фирму {firm} товар в количестве {number}")

class OfficeTech:
    def __init__(self, name, size, method, color, functional):
        self.name = name
        self.size = size
        self.method = method
        self.color = color
        self.functional = functional

    def __str__(self):
        return f'Оргтехника: название - {self.name}, размер - {self.size}, принцип сканирования - {self.method}, цветность - {self.color}, функциональность - {self.functional}'


class Printer(OfficeTech):
    def __init__(self, name, method_type, format_p, speed, size, method, color, functional):
        super().__init__(name, size, method, color, functional)
        self.method_type = method_type
        self.format_p = format_p
        self.speed = speed


    def add_storage(self, name, number):
        self.name = name
        Storage.to_retrieve(name=self.name, number=number)

    def refer_to_firm(self, name, number, firm):
        Storage.to_refer(name, number, firm)

class Scaner(OfficeTech):
    def __init__(self, name, type_class, sensor, pyxel, size, method, color, functional):
        super().__init__(name, size, method, color, functional)
        self.type_class = type_class
        self.sensor = sensor
        self.pyxel = pyxel

    def add_storage(self, name, number):
        self.name = name
        Storage.to_retrieve(name=self.name, number=number)

    def refer_to_firm(self, name, number, firm):
        Storage.to_refer(name, number, firm)


class Copier(OfficeTech):
    def __init__(self, name, dpi, number_copies, speed, size, method, color, functional):
        super().__init__(name, size, method, color, functional)
        self.dpi = dpi
        self.number_copies = number_copies
        self.speed = speed

    def add_storage(self, name, number):
        self.name = name
        Storage.to_retrieve(name=self.name, number=number)

    def refer_to_firm(self, name, number, firm):
        Storage.to_refer(name, number, firm)


st = Storage("A", 500)
print(st)
p1 = Printer("Принтер №1", "лазерный метод", "формат A4", 30, "малогабаритный", "цифровой", "цветной", "печать")
print(p1)
print(p1.name)
p1.add_storage("Принтер №1", 100)
p1.refer_to_firm("Принтер №1", 50, "ОАО 'Собаки и копыта'")
print(st.data)
s1 = Scaner("Сканер №1", "планшетный тип", "CIS", "600x1200", "малогабаритный", "цифровой", "цветной", "сканирование")
print(s1)
s1.add_storage("Сканер №1", 56)
s1.refer_to_firm("Сканер №1", 30, "ООО 'Малиновый чизкейк'")
print(st.data)

# Задание №7
class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Комплексное число: {complex(self.x, self.y)}'

    def __add__(self, other):
        print(f'Сумма: {complex(self.x, self.y) + complex(other.x, other.y)}')
        return complex(self.x, self.y) + complex(other.x, other.y)

    def __mul__(self, other):
        print(f'Умножение: {complex(self.x, self.y) * complex(other.x, other.y)}')
        return complex(self.x, self.y) * complex(other.x, other.y)

c1 = Complex(2, 4)
print(c1)
c2 = Complex(3, 5)
print(c2)
print(c1 + c2)
print(c1 * c2)
print(complex(2, 4) + complex(3, 5))
print(complex(2, 4) * complex(3, 5))
