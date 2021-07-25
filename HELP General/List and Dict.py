import random

# СПИСКИ[LIST]

# empty_list = []
# Создание списка из None
# none_list = [None] * 10

# Получаем длину объекта len(none_list)
# Обращаемся к элементу списка: none_list[0]
# Изменение элемента списка через обращение к нему через индекс none_list[0] = 'new element'
# Проверка существования элемента в списке "element" in none_list
# Поддержка среза как в строках none_list[1:3] none_list[::2] - шаг
# Добавление элемента через none_list.append('2element') или none_list += ['2element']
# Добавление другого списка в конец через none_list.extend('list')
# Удаление элемента списка через индекс del none_list[1]
# Форматирование в строку none_list  -> ', '.join(none_list) -> None, None ...
# Сортировка элементов списка sorted(none_list), обратный порядок sorted(none_list, reverse=True) | БЕЗ ИЗМЕНЕНИЯ СПИСКА
# Сортировка элементов списка none_list.sort(), обратный порядок none_list.sort(reverse=True) | C ИЗМЕНЕНИЕМ СПИСКА

# Итерация по элементам списка
# # Вывод индекса при помощи метода enumerate
# for idx, item in enumerate(none_list):
#     print('Список содержит {} с индексом {}'.format(item, idx))

# numbers = [4, 15, 16]
# Минимальный, максимальный элемент и их сумма
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# numbers = []
# for _ in range(10):
#     # Добавление элемента в список numbers
#     numbers.append(random.randint(1, 20))
# print(numbers)

# КОРТЕЖ(TUPLE) - НЕИЗМЕНЯЕМЫЕ СПИСКИ
# number = ()
# immutables = (int, str, tuple)

# _____________________

# СЛОВАРЬ[DICT]
# Определение словаря

# empty_dict = {}
# empty_dict = dict()

# Проверка наличия ключа в словаре через оператор in -> 'imutable' in example_dict
# Добавление элемента в словарь example_dict['New_key'] = 'New_value' (var1)
# Добавление элемента в словарь example_dict.update({'New_key' : 'New_value'}) (var2)
# Удаление элемента из словаря del example_dict['Name_key'] (var1)
# Удаление элемента из словаря del example_dict.pop('Name_key') (var2)
# Проверка ключа 'Key' и добавление если нет в словаре - ключ, значение exaple_dict = {} -> exaple_dict.setdefault('Key', 'New_value')
# Итерация по словарю по ключу или по значению:
example_dict = {
    1: 'dsdsd',
    2: 'rgfgd'
}

for key in example_dict:
    print(example_dict[key])
# Итерация по элементам(key, value) с помощью метода items(), key - keys(), value - values()

# for value in example_dict.values():
# print('{}'.format(value))

# _____________________

zen_python_text = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''


# my_word = '''dfdf sdsd lol'''
# zen_map = dict()
# # Разбиваем строки на слова по пробелу split()
# for word in zen_python_text.split():
#     # Удаляем символы в строке (strip)
#     clean_word = word.strip('!,.').lower()
#     # Если
#     if word not in zen_map:
#         zen_map[clean_word] = 0
#     else:
#         zen_map[clean_word] += 1
#
# print(zen_map)
#
# zen_items = zen_map.items()

