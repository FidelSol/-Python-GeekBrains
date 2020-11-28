a = 10

print(bin(a)) # 2
print(oct(a)) # 8
print(hex(a)) # 16

a = 'Привет'
b = 'Мир'
print(a + str(10) + b)

a = "Привет как дела?"
print(a[0:3])
print(a[0:3:2]) # шаг 2
print(a[::-1]) # быстро перевернуть строку, реверс строк

a = 'Привет как дела?'
print(len(a))
b = a.lower()
print(b)
print(a.find('дел')) # начинается с 11 номера 'дел'

b = []
a = [1, 10.5, 'Привет', True]
a.append('Я новенький') # дополняет в конец
a.pop() # если пустой - удаляет последний
a.pop(2) # удаляет второй элемент
a.insert(2, 'Я новенький') # вставляет на вторую позицию строку

a = 'Привет как дела давай прогуляемся'
b = a.split()
print(b[0][1]) # р

a = 'Привет,как,дела,давай,прогуляемся'
b = a.split(',')
print(b)

b = a.split(',')
c = ' '.join(b) # разделитель
print(c)

a = (1, 'Hello', True)
print(a)

a = set('abrkaa') # изменяемое множество
b = frozenset('abrkaa') # неизменяемое множество
print(a)
print(b)
a.add('!') # добавляется рандомным местом
a.remove('k') # удаляет k
a.add('a') # ничего не произойдет
print(a)

person = {
    'Name': 'Tom',
    'Work': 'Google',
    'Car': 'Ferrari',
    'Phone': 1223455,
}
print(person['Name'])

# метод get
print(person.get('Car', 'Не существует'))

# преобразовать в список список ключей
print(list(person.keys()))

# преобразовать в список список значений
print(list(person.values()))

# то же по итемам - список кортежей
print(list(person.items()))

# работает для всех метод len

a = -1
b = []
c = 0
d = 'ffff'
e = ''

print(bool(a), bool(b), bool(c))


# тернарный оператор
a = 1
b = 2
c = 3 if a > 2 else 'Ошибка'
print(c)


# ЦИКЛЫ

a = ['ddd', '333', '444', '781']
count = 0
while count < len(a):
    print(a)

for element in a:
    print(element)

for i in range(0, len(a), 2): # 2 - шаг
    print(i, a[i])





