from datetime import *

name, date = []
name.append(input('Name:'))
date.append(input('Date:'))

name_date = {}

for i in range(0, len(name)):
    name_date[name[i]] = date[i]

# Проверка
print(name_date['Вагнер'])

# name = ('John', 'Nicholas', 'Mercy')
# age = 25
#
# dict_sample = dict.fromkeys(name, age)
#
# print(dict_sample)
