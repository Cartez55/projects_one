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

for file in glob.glob("*.json"):
    directory = file

word_find = ['не р']

with open(directory, "r", encoding="utf-8") as item:
    list_word = json.load(item)
    # Итерация по файлу json
    for word in list_word.items():
        # Итерация по списку слов для поиска
        for list_w in word_find:
            # Итерация по списку из json
            with open("find_word.txt", "w") as file:
                for line in word[1]:
                    if list_w in line:
                        file.write('"' + line + '"' + "\n")
                        print(''.join(line))

# МЕТОД 2 ИЗ СПИСКА

# Слова для поиска
# word_find = []
# Список в котором ищем
# welcome = []
#
# # Поиск слов или части слова из списка
# for ls in word_find:
#     for line in welcome:
#         if ls in line:
#             print(''.join(line))

# Рандомная комбинация текста
# phrase1 = []
# phrase2 = []
#
# for i in phrase1:
#     for b in phrase2:
#         print("Как", i, b)
