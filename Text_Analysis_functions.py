import re
from random import choice
import json

# ПОИСК СЛОВ ПРИ ПОМОЩИ REGEXP

# ls = []

# Регулярка проверяется на сайте https://regex101.com/

# for i in ls:
#     gr = re.search("[a-z]", i)
#     if gr:
#         print(gr.group())

# ПОИСК СЛОВ ИЗ СПИСКА

for file in glob.glob("*.json"):
    scenarios_dir = file

with open(scenarios_dir, "r", encoding="utf-8") as scenario:
    data = json.load(scenario)
    guid = list(data["scenario"].keys())[0]
    numb = guid[5:10]


word_find = ['wor', 'goo']

welcome = ["Hello world! Goodbye world!", "Ted Nelson, the inventor of hypertext",
           "This book was more a stream-of-consciousness collage than anything else"]
f = []




# Рандомная комбинация текста
# phrase1 = []
# phrase2 = []
#
# for i in phrase1:
#     for b in phrase2:
#         print("Как", i, b)
