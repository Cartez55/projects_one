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
# ------------------------------
# Kwargs:
# def name_function (**kwargs): - передаем несколько именновых аргументов
# name_function(a = 1, b = 2) - например словарь
# Возможность передать готовый словарь в качестве аргумента:
# payload = {
#     'pass' : 1
# }
# name_function(**payload)




# Замыкание в python
def get_multiplier(number):
    def inner(a):
        return a * number
    return inner

get_multiplier2 = get_multiplier(2)
# print(get_multiplier2(10))