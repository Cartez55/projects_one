import re
from random import choice
import json
import glob

# ПОИСК СЛОВ ПРИ ПОМОЩИ REGEXP - LIST

# ls = []

# # Регулярка проверяется на сайте https://regex101.com/

# for i in ls:
#     gr = re.search("[a-z]", i)
#     if gr:
#         print(gr.group())

# ПОИСК СЛОВ ПРИ ПОМОЩИ REGEXP - TXT

# for file in glob.glob("word\\*.txt"):
#     txt_file = file
#
# with open(txt_file, "r", encoding="utf-8") as items:
#     lst = items.readlines()
#     for i in lst:
#         gr_ls = re.search("(сбер.{6}|Сбер.{6})|(с.{3} + прайм)|(прайм|ПРАЙМ)", i)
#         if gr_ls:
#             print(gr_ls.group())

# ПОИСК СЛОВ ИЗ СПИСКА

# МЕТОД 1 ИЗ ФАЙЛА JSON

# Находим любой файл json

# for file in glob.glob("*.json"):
#     directory = file
#
word_find = ["категор", "Категор"
             ]
#
# #  РАБОТ С JSON ФАЙЛОМ
#
# # with open(directory, "r", encoding="utf-8") as item:
# #     list_word = json.load(item)
# #     # Итерация по файлу json
# #     for word in list_word.items():
# #         # Итерация по списку слов для поиска
# #         for list_w in word_find:
# #             # Итерация по списку из json
# #             with open("find_word.txt", "w") as file:
# #                 for line in word[1]:
# #                     if list_w in line:
# #                         file.write('"' + line + '"' + "\n")
# #                         print('"' + line + '"' + "\n")
#
# #  РАБОТ С TXT ФАЙЛОМ
#


for file in glob.glob("word\\*.txt"):
    txt = file


def remove_word():
    # #
    with open(txt, "r+", encoding="utf-8") as element:
        list_item = element.readlines()
        list_remove = []
        list_item = list(set(list_item))
        for w_f in word_find:
            for i in list_item:
                list_r = re.search(f"^.*{w_f}.*", i, re.I)
                if list_r:
                    list_remove.append(i)
        for line in list_remove:
            if line in list_item:
                list_item.remove(line)
        with open("remove\\word_remove.txt", "w", encoding="utf-8") as items:
            items.writelines(list_item)


#
# with open(txt, "r", encoding="utf-8") as item:
#     lst = item.readlines()
#     with open("find.txt", "w", encoding="utf-8") as fs:
#         # Итерация по файлу txt
#         for word in lst:
#             for list_w in word_find:
#                 if list_w in word:
#                     fs.write(word)
#                     # Чтобы не удалять слова из списка закоменть
#                     remove_word()
#                     print(word + "\n")

#

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

# Комбинация текста
phrase1 = ['категория']
phrase2 = ["бонус"]
phrase3 = ['спасибо', 'spasibo']
for i in phrase1:
    for b in phrase2:
        for e in phrase3:
            print('"'+ i, b, e + '"' + ",")
