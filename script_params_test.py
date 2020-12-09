# задание №1
# scrypt_params_test.py
from sys import argv

script_name, p_1, p_2, p_3 = argv

p_1 = float(p_1)
p_2 = float(p_2)
p_3 = float(p_3)


print(f"Money - {p_1 * p_2 + p_3}")

