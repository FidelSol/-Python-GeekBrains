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








