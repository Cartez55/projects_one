import re

# ПОИСК СЛОВ ПРИ ПОМОЩИ REGEXP

ls = []

# Регулярка проверяется на сайте https://regex101.com/

for i in ls:
    gr = re.search("(уз....)|(полу....)|(най..)|(соз....)|(подключи..)|(уточ....)|(увид...)|(посм......)|(взя..)", i)
    if gr:
          print(gr.group())