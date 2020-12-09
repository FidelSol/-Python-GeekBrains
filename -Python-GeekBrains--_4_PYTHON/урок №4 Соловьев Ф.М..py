
# задание №1
# scrypt_params_test.py
from sys import argv

script_name, p_1, p_2, p_3 = argv

p_1 = float(p_1)
p_2 = float(p_2)
p_3 = float(p_3)
print(f"Money - {p_1 * p_2 + p_3}")

# Задание №2

my_list = [15, 16, 2 , 3, 1, 7, 5, 4, 10]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(my_list)
print(more_then)

# Задание №3

list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(list)

# Задание №4
from random import randint

my_list = [randint(-10, 10) for _ in range(20)]
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Начальный список\n{my_list}\nСписок без повторений\n{uniq_list}')

# Задание №5
from functools import reduce

def my_func(el_1, el_2):
    return el_1 * el_2

list = [el for el in range(100, 1001) if el % 2 == 0]

print("Первый вариант: ", reduce(my_func, list))

def my_list(el_1, el_2):
    return el_1 * el_2

uniq_list = [el for el in range(100, 1001, 2)]
print(f"Второй вариант: List\n{uniq_list}\nMultiplication of numbers\n{reduce(my_list, uniq_list)}")

print("Третий вариант: ", reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))

# задание №6 Генератор целых чисел
# iterator_1.py

from itertools import count
from sys import argv

script_name, p_1, p_2 = argv

p_1 = int(p_1)
p_2 = int(p_2)

for el in count(p_1):
    if el > p_2:
        break
    else:
        print(el)


# задание №6 Генератор цикла
# iterator_2.py

from itertools import cycle
from sys import argv

script_name, p_2, seq = argv

p_2 = int(p_2)
seq = list(seq)
iter = cycle(seq)

for el in range(0, p_2):
    print(next(iter))

# Задание №7
from functools import reduce
from math import factorial


def fact_gen(number):
    f_num = 1
    if number == 0:
        yield f'{number}!= 1'
    else:
        for i in range(1, number + 1):
            f_num *= i
            yield f'{i}!= {f_num}'

for el in fact_gen(int(input('Factorial number: '))):
    print(el)



