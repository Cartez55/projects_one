from datetime import *

name = []
date = []
name_date = {}

button_off = True


def write_name():
    while button_off:
        controll = input('Запишем ещё?:')
        if controll == "нет":
            print(name_date)
            break
        elif controll == "да":
            name.append(input('Name: '))
            date.append(input('Date: '))


for i in range(0, len(name)):
    name_date[name[i]] = date[i]


print(name_date)




# Проверка
write_name()
# print(name[0])
# print(type(date[0]))
