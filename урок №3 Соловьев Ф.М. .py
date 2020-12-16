# Задание №1
a = float(input('Введите чсило a: '))
b = float(input('Введите чсило b: '))

def divide(a, b):
    if b == 0:
        print("На ноль делить нельзя!")
        return
    else:
        c = a / b
        print(c)
        return c

divide(a, b)


# Задание №2
def person_info(**kwargs):
    return kwargs

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год: ')
town = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите номер телефона: ')

print(person_info(имя=name, фамилия=surname, год=year, город=town, почта=email, телефон=phone))

# Задание №3
print('Задание №3')
def my_func(a, b, c):
    list = [a, b, c]
    list.sort()
    s = list[1] + list[2]
    print(s)
    return s

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

my_func(a, b, c)

# Задание №4
print('Задание №4 - 1 способ')
def my_func(x, y):
    c = 1 / (x**y)
    return c

x = int(input('Введите положительное число x: '))
y = -int(input('Введите отрицательное число y: '))

print(my_func(x, y))

print('Задание №4 - 2 способ')
def my_func(x, y):
    c = 1 / x
    for i in range(0, y):
        c /= x
    return c

x = int(input('Введите положительное число x: '))
y = -int(input('Введите отрицательное число y: '))

print(my_func(x, y))

# Задание №5
list = []
new_list = []
i = 0
x = 0
spec = 's'

while True:
    try:
        list = (input("Введите через пробелы несколько чисел. Специальный символ для завершения 's': ")).split(' ')
        for i, item in enumerate(list):
            if list[i] != "s":
                list[i] = int(item)
            else:
                break
        sum(list)
        x += sum(list)
        print(x)
    except TypeError:
        list.remove('s')
        x += sum(list)
        print(x)
        break

# Задание №6
def int_func():
    word = input("Введите слово из маленьких латинских букв: ").capitalize()
    print(word)
int_func()

def int_func():
    sentence = list(input("Введите строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре: ").split())
    for i, item in enumerate(sentence):
        sentence[i] = item.capitalize()
    print(' '.join(sentence))
int_func()













