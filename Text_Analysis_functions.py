import re


# ПОИСК СЛОВ ПРИ ПОМОЩИ REGEXP

ls = []

# Регулярка проверяется на сайте https://regex101.com/

for i in ls:
    gr = re.search("(сб+.+ id)|(Сб+.+ id)|(сб+.+|id)|(ID)|(айд.)|(Сб+.+ а...)|(Id)|(Сб+.+|ID)", i)
    print(gr.group(0))