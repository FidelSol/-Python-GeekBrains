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


