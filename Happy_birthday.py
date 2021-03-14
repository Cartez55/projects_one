from datetime import *

name = []
date = []

i
while True:
    name.append(input('Name: '))
    date.append(input('Date: '))


    name_date = {}

    for i in range(0, len(name)):
        name_date[name[i]] = date[i]

# Проверка
# print(name_date['Вагнер'])
# print(name[0])
print(type(date[0]))
