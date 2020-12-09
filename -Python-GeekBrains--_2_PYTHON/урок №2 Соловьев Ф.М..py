# Задание №1
list = [1, 2.04, 'строка', complex(7, 8), [1, 2, 3], (1, 2, 3), set('abrakadabra'), frozenset('abrakadabra'), {'key_1': 'val_1', 'key_2': 'val_2'}, True, bytes('text', encoding = 'utf-8'), bytearray(b"some text"), None]
for el in list:
   print("Задание №1.", type(el))


# Задание 2
list = (input("Задание №2. Введите через запятую элементы, чтобы сформировать список: ")).split(',')
print(list)
i=0
x = 0
if len(list) % 2 != 0:
    x = list.pop(len(list) - 1)
    for el in range(0, len(list) - 1, 2):
        list[i], list[i+1] = list[i+1], list[i]
        i += 2
    list.append(x)
else:
    for x in range(0, len(list), 2):
        list[i], list[i + 1] = list[i + 1], list[i]
        i +=2
print(list)

# Задание 3
month = int(input("Задание №3. Введите месяц в виде целого числа от 1 до 12:"))
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
seasons = {
    1: "Зима",
    2: "Зима",
    12: "Зима",
    3: "Весна",
    4: "Весна",
    5: "Весна",
    6: "Лето",
    7: "Лето",
    8: "Лето",
    9: "Осень",
    10: "Осень",
    11: "Осень",
}
print(seasons[list[month]])

# Задание №4
list = (input("Задание №4. Введите через пробелы несколько слов: ")).split(' ')

for ind, el in enumerate(list, 1):
    if len(el) > 10:
        print(ind, el[:10])
    else:
        print(ind, el)

#Задание №5
list = [7, 5, 3, 3, 2]
new_list = []
number = 0
while number != 111:
    number = int(input("Задание №5. Вводите натуральное число для формирования рейтинга (выход из рейтинга - число 111):"))
    list.append(number)
    print(sorted(list, reverse=True))



# Задание №6
i = 0
list_article = []
list_name = []
list_price = []
list_number = []
print("Введите структуру данных 4 товаров")
for x in range(0, 3):
    i += 1
    name = input("Введите название товара:")
    price = int(input("Введите цену товара:"))
    number = int(input("Введите количество товара:"))
    list_name.append(name)
    list_price.append(price)
    list_number.append(number)
    dict_article = {
        "Название": name,
        "Цена": price,
        "Количество": number,
        "Ед.": "шт."
    }
    tuple_article = (i, dict_article)
    list_article.append(tuple_article)
print("Структура данных: ", list_article)
dict_analitics = {
    "Название": list_name,
    "Цена": list_price,
    "Количество": list_number,
    "Ед": ["шт."],
}
print("Аналитика о товарах: ", dict_analitics)
