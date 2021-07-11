# ФУНКЦИИ[FUNCTION]

# Для опеределения тела фукнции используется отступ
# Вывод значения из функции - return
# Вызов фукнции - name_function(оставляем либо пустыми, либо добавляем аргумент)
# def function (*args, **kwargs):
#     """Описание что делает функция"""
# Вывод документации по функции - name_function.__doc__
#     return pass
# Вывод имени функции - name_function.__name__

# Аннотация типов:
# def name_function(x: type, y: type) -> int: - т.е указываем типы данных к конкретному аругументу
# !!!Но в даже если будет другой тип код всеравно исполнится!!!

# Использование ссылки на объект или его значения:
# def extender(source_list, extend_list):
#     source_list.extend(extend_list)
# values = [1,2,3]
# extender(values - используется ссылка на объект в памяти, [4,5,6] - используется значение)

# Именновые аргумены:
# def name_function(name, greeting):
# При передаче аргументов указываем значение к конкретному:
# name_function(name='Kitty', greeting='One')

# Область видимости:
# result = 0
#
# def increment():
#     return result + 1
# !!!Нельзя внутри функции изменять глобальные переменные!!!
# increment() - будет ошибка

# Аргументы по умолчанию:
# def greeting(name='it\'s me'):
# print('Hello, {}'.format(name))
# greeting()
# -> Hello it's me
# Узнать значение по умолчанию - name_function.__defaults__

# Args, kwargs:
# Args:
# def name_function(*args):
# name_function(1,2,3,4,5)- передаем tuple(неизменяемый список)
# Возможно передать готовый список в качестве аргумента:
# name_list = ["VzInisL", "NdWdT6SK", "97a", "gT2", "QtM41eB"]
# name_function(*name_list)
# -----------------------------
# Kwargs:
# def name_function (**kwargs): - передаем несколько именновых аргументов
# name_function(a = 1, b = 2) - например словарь
# Возможность передать готовый словарь в качестве аргумента:
# payload = {
#     'pass' : 1
# }
# name_function(**payload)


# Вызов фукнции в парметрах другой функции:
# def caller(func, params):
#     return func(*params)
#
# def printer(name, origin):
#     print('I\'m {} {}'.format(name, origin))
#
# caller(printer,['Igor', 'Prokopenko'])
# -> I'm Igor Prokopenko
# -----------------------------
# Замыкание в python:
# def get_multiplier(number):
#     def inner(a):
#         return a * number
#     return inner
#
# get_multiplier2 = get_multiplier(2)
# # print(get_multiplier2(10))
# -> 20

# Полезные фукнции (встроенные):

# MAP
# По дефолту map возвращает map.object
# def squarify(a):
#     return a ** 2
# Map - итерируется по всему range и применяет(здесь умножает) squarify к каждому объекту и выводит список этих элементов
# list(map(squarify,range(5)))
# -> [0,1,4,9,16]

# FILTER
# def is_positive(a):
#     return a > 0
# Функция filter оставляет в выводе только те числа, которые соответсвуют условию is_positive
# print(list(filter(is_positive, range(-2, 3))))
# -> [1, 2]

# LAMBDA (анонимная функция)
# list(map(lambda x: x ** 2, range(5)))
# Анонимная функция принимает один аргумент и возводит его в квадрат
# list(map(lambda param: param ** 2, range(5)))
# Filter оставил только тот, ответ, который отвечает условию в lambda
# list(filter(lambda x: x > 0, range(-2, 3)))

# Список чисел превращаем в список строк:
# Вариант 1
# def int_to_string(a):
#     return str(a)
# При указании аргументов в функции map, параметры в скобках функции(int_to_string) заменяются вторым аргументом map
# print(list(map(int_to_string, range(0, 5))))
# -----------------------------
# Вариант 2
# def int_to_string(num_list):
# В качестве аргумента map указываем фукнцю str, а данных num_list
#     return list(map(str, num_list))
#
# print(int_to_string(range(10)))

# FUNCTOOLS - модуль содержит полезные функции
#
# REDUCE
# from functools import reduce
#
# def multiply(a, b):
#     return a * b
# # Функция reduce применяет multiply к каждому из списка -> 1*2 -> 2*3 -> 6*4 -> 24*5 и возвращает единичное значение.
# print(reduce(multiply, [1, 2, 3, 4, 5]))
# -----------------------------
# PARTIAL
#
# from functools import partial
#
# def greeter(person, greeting):
#     return '{}, {}!'.format(greeting, person)
# Функция partial заменяет значение аргумента в функции greeter, на другой именованый аргумент
# hier = partial(greeter, greeting='Hi')
# hello = partial(greeter, greeting = 'Hello')
#
# print(hier("Bill"))
# -> Hi, Bill!
# print(hello("Bill"))
# -> Hello, Bill!

# СПИСОЧНЫЕ ВЫРАЖЕНИЯ
# FOR
# square_list = [number ** 2 for number in range(10)]
# print(square_list)
# -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Цикл по range, number ** 2
# square_list = [выражение с использованием переменной for переменная in последовательность
# (список, строка или объект, полученный при помощи функции range)]
# -----------------------------
# FOR С УСЛОВИЕМ
# even_list = [num for num in range(10) if num % 2 == 0]
# print(even_list)
# -> [0, 2, 4, 6, 8]
# even_list = [переменная for переменная in последовательность if условие]
# -----------------------------
# Определение словаря с помощью списочного выражения
# square_map = {number : number ** 2 for number in range(5)}
# print(square_map)
# -> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# -----------------------------
# ZIP
# num_list = range(7)
# squared_list = [x ** 2 for x in num_list]
# Функция zip склеивает по одному элементу из каждого объекта в отдельные tuple
# print(list(zip(num_list, squared_list)))
# -> [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]
# Пример использования zip and map в одной строке
# list(zip(filter(bool, range(3)), [x for x in range(3) if x]))
# -> [(1,1), (2,2)]