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
number = ()
immutables = (int, str, tuple)
