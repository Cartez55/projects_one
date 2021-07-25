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
# phrase1 = ['категория']
# phrase2 = ["бонус"]
# phrase3 = ['спасибо', 'spasibo']
# for i in phrase1:
#     for b in phrase2:
#         for e in phrase3:
#             print('"'+ i, b, e + '"' + ",")

# Подсчет количества слов в тексте
from collections import Counter

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

# cleaned_list = []
# for word in zen_python_text.split():
#     # Очищаем список от лишних символов и приводим к lower_case
#     cleaned_list.append(word.strip('!,.-').lower())
# # Выводим количество слов из списка
# print(Counter(cleaned_list).most_common())

# Рандомный GUID

string = 'ODHrUBHVNKYjSGIrRaThrergJbzOOsQZAAkmilgiOIZtTYnaHUNfWfMjShxzOVpQjhrryrvxAslNvqqFldFuSzoisphGLQcBzWRMcxPXyxJE'
letter = 'abcdefghijklmnopqrstuvwxyz'
letter_upper = letter.upper()
random_GUID = []
for i in range(0, 36):
    random_GUID.append(choice(letter+letter_upper))

print(''.join(random_GUID))
