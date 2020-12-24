#Задание №1
import time


class Trafficlight:
    def __init__(self):
        print('Внимание светофор!')
        self.__color = ['КРАСНЫЙ', 'ЖЕЛТЫЙ', 'ЗЕЛЕНЫЙ']

    def running(self):
        while True:
            for el in self.__color:
                time.sleep(7) if el == 'КРАСНЫЙ' else time.sleep(2)
                print(el)

trafficlight = Trafficlight()
trafficlight.running()

# Задание №2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        mass = self._length * self._width * 25 * 0.5
        print(mass, "т.")
        return mass

a = Road(20, 50)
a.mass()

# Задание №3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        total = self._income["wage"] + self._income["bonus"]
        print(total)

p = Position('Brad', 'Pit', 'Chief', 40, 50)
p.get_full_name()
p.get_total_income()

# Задание №4
class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        print(f'машина повернула {direction}')

    def show_speed(self):
        print(f'скорость - {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ')
        else:
            print(f'скорость - {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ')
        else:
            print(f'скорость - {self.speed}')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


w = WorkCar(50, 'green', 'picap')
print(w.speed)
print(w.is_police)
w.go()
w.turn('направо')
w.show_speed()

t = TownCar(120, 'red', '99')
t.show_speed()

p = PoliceCar(60, 'blue', 'nissan')
print(p.is_police)

# Задание №5
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationary):

    def draw(self):
        print('рисуем ручкой')


class Pencil(Stationary):

    def draw(self):
        print('рисуем карандашом')


class Handle(Stationary):

    def draw(self):
        print('рисуем маркером')

s = Stationary('title')
s.draw()
pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')

pen.draw()
pencil.draw()
handle.draw()


print(pen.title, pencil.title, handle.title)















