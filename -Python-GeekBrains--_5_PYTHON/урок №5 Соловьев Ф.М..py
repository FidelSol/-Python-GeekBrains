# Задание №1
with open("text1.txt", "w",  encoding='utf-8') as f:
    while True:
        line = input("Введите строки в файл f: ")
        f.write(line + '\n')
        if line == "":
            break

# Задание №2
from itertools import count

with open("text2.txt", "r+", encoding='utf-8') as f:
    line = input("Вводим пару предложений одной строкой, разделим их двумя пробелами:").split('  ')
    print(f'Количество строк: {len(line)}')
    f.write(f'Количество строк: {len(line)}\n')
    for el in count(0):
        if el >= len(line):
            break
        else:
            f.write(f'В строке {el+1}: {len(line[el].split())} слова(слов)\n')
            print(f'В строке {el+1}: {len(line[el].split())} слова(слов)')

# Задание №3
with open('text3.txt', 'r+') as f:
    new_list = []
    avg_list = []
    while True:
        try:
            line = input("Информация уже имеется в файле, дополните ее. Введите фамилию и величину месячного оклада, разделив слова пробелом, по завершении введите пустую строку:").split()
            f.write(f'Сотрудник {line[0]} - оклад {line[1]}\n')
            new_list += [line[0] + '\n' for el in line if float(line[1]) < 20000]
            avg_list += [int(line[1]) for el in line]
        except IndexError:
            print("Конец ввода.")
        if not line:
            break
    new_list = list(set(new_list))
    avg_list = list(set(avg_list))
    f.write("Список сотрудников, чей оклад меньше 20000 рублей:\n")
    f.writelines(new_list)
    f.write(f'Среднее величина дохода сотрудников: {round(sum(avg_list)/len(avg_list), 2)} рублей')
    print(f.read())

# Задание №4
from googletrans import Translator

translator = Translator(service_urls=['translate.googleapis.com'])
with open('text5.txt', 'w', encoding='utf-8') as fw:
    with open('text4.txt', 'r', encoding='utf-8') as fr:
        list = (fr.read()).split()
        new_list = [el for el in list if len(el) > 1]
        result = translator.translate(new_list, src='en', dest='ru')
        x = 1
        for trans in result:
            print(f'{trans.text} - {x}\n')
            fw.write(f'{trans.text} - {x}\n')
            x += 1

# Задание №5
with open("text6.txt", "w", encoding='utf-8') as f:
    line = input("Вводим числа одной строкой, разделяя их пробелом:").split()
    s = sum([int(el) for el in line])
    f.write(f'Список чисел: {line}. Сумма: {s}')
    print(f'Список чисел: {line}. Сумма: {s}')

# Задание №6
name = ''
result = {}
with open("text7.txt", "w", encoding='utf-8') as f:
    while True:
        name = input("Введите предмет. Конец ввода - q: ")
        if name == 'q':
            break
        list_input = input("Введите количество лекций, практических работ, лабораторных работ соответсвенно числами через пробел: ")
        super = sum([int(el) for el in list_input.split()])
        x = list_input.replace(' 0', ' -')
        list_w = x.split()
        if list_w[0] == '0':
            list_w[0] = '-'
        result.update({name: super})
        print(f'{name}: {list_w[0]}(л), {list_w[1]}(пр), {list_w[2]}(лаб). Сумма: {super}')
        print(result)
        f.write(f'{name}: {list_w[0]}(л), {list_w[1]}(пр), {list_w[2]}(лаб). Сумма: {super}')
    f.write(f'{result}')

# Задание №7
import json

with open('7.json', 'w', encoding='utf-8') as fw:
    with open('text8.txt', encoding='utf-8') as f:
        sr_list = []
        result = {}
        for line in f:
            list = line.split('  ')
            prib = float(list[2]) - float(list[3])
            if prib > 0:
               sr_list.append(prib)
            result.update({list[0]: prib})
        result_list = [result, {'AVERAGE VALUE': round(sum(sr_list)/len(sr_list))}]
        json.dump(result_list, fw)
        print(result_list)





















