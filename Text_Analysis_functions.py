import re
from random import choice
import json
import glob

# ПОИСК СЛОВ ПРИ ПОМОЩИ REGEXP

# ls = []

# Регулярка проверяется на сайте https://regex101.com/

# for i in ls:
#     gr = re.search("[a-z]", i)
#     if gr:
#         print(gr.group())


# ПОИСК СЛОВ ИЗ СПИСКА

# МЕТОД 1 ИЗ ФАЙЛА JSON

# Находим любой файл json

# for file in glob.glob("*.json"):
#     directory = file
#
word_find = ['не р', 'Не р']

# ЭКСПЕРИМЕНТ

list_test = ["Не работает сберпрайм",
             "Не работает подписка сберпрайм при переходе в приложения партнёров скидка не предоставляется",
             "По данному номеру X XXX XXX XX XX сказали подписка СберПрайм не подтянулась поэтому скидку не применили.\nПочему сервис не работает должным образом и как мне получать скидки в рамках пакета услуг?",
             "Почему не работает сберпрайм?",
             "Не работает скидка по сберпрайм в citimobil и delivery-club",
             "Сберпрайм не работает! Я расстроена!",
             "У меня подписка сберпрайм. Но приложения по ней с учётом скидок не работают. Просьба помочь",
             "Почему не работает сберпрайм ?",
             "Сберпрайм подключен но не работает",
             "Почему не работает подписка сберпрайм в приложении Окко?",
             "Здравствуйте пол года не работает купленая услуга сберпрайм вы перестали даже информировать меня о состоянии разбирательствапрошу вернуть мне деньги.",
             "Не работает подписка сберпрайм",
             "Не работает Подписка Сбер прайм",
             "Не работает прайм",
             "Сберпрайм не работает",
             "Не работает СберПрайм!!!"
             "Как оплатить сберпрайм бонусами спасибо",
             "Здравствуйте а подскажите пожалуйста как отключить автопродление сберпрайма?",
             "В январе открыт вклад Дополнительный процент. В опциях бесплатная подписка на Сбер Прайм. Как подключить?",
             "Просьба отключить подписку сберпрайм и вернуть деньги",
             "Отменить подключение к подписке на год Сберпрайм",
             "Здравствуйте! У меня подписка СберПрайм где найти сбер ld и как авторизоваться у партнеров",
             "Где посмотреть подписки например сберпрайм?",
             "Что такое сбер прайм",
             ]

print(list_test)

#  РАБОТ С JSON ФАЙЛОМ

# with open(directory, "r", encoding="utf-8") as item:
#     list_word = json.load(item)
#     # Итерация по файлу json
#     for word in list_word.items():
#         # Итерация по списку слов для поиска
#         for list_w in word_find:
#             # Итерация по списку из json
#             with open("find_word.txt", "w") as file:
#                 for line in word[1]:
#                     if list_w in line:
#                         file.write('"' + line + '"' + "\n")
#                         print('"' + line + '"' + "\n")

for file in glob.glob("word\\*.txt"):
    txt = file

list_remove = []


def remove_string():
    for w_f in word_find:
        list_remove = []
        for i in list_test:
            list_r = re.search(f"^.*{w_f}.*", i)
            if list_r:
                list_r.group()
                list_remove.append(list_r.group())
                for e_r in list_remove:
                    if e_r in i:
                        list_test = i.replace(e_r, "")
    print(list_test)

#
# def str_remove():
#     for w_f in word_find:
#         list_remove = []
#         list_r = re.search(f"^.*{w_f}.*", word)
#         if list_r:
#             list_remove.append(list_r.group())
#             print(type(list_remove))
#     for e_r in list_remove:
#         print(word.replace(e_r, "блоха"))
#
#
# with open(txt, "r+", encoding="utf-8") as item:
#     lst = item.readlines()
#     with open("find.txt", "w", encoding="utf-8") as fs:
#         # Итерация по файлу txt
#         for word in lst:
#             for list_w in word_find:
#                 if list_w in word:
#                     fs.write(word + "\n")
#                 # str_remove()
#                     print(word + "\n")

# МЕТОД 2 ИЗ СПИСКА

# # Слова для поиска
# word_find = []
# # Список в котором ищем
# word_lst = []
#
# # Поиск слов или части слова из списка
# for ls in word_find:
#     for line in word_lst:
#         if ls in line:
#             print(''.join(line), end="")

# Рандомная комбинация текста
# phrase1 = []
# phrase2 = []
#
# for i in phrase1:
#     for b in phrase2:
#         print("Как", i, b)
