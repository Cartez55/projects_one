# Старый метод
# templ = "%s придет %s (%s)"
# s = templ % ("Игорь", "рано", "поздно")
# print(s)

# Новый метод
# print("{} не лгут, но {} пользуются формулами.".format("Цифры", "лжецы"))
# Варант с наименованием переменных
# print("{num} КБ должно хватить для любых задач".format(num=640))
# F строка
subject = 'Рыжый'
autor = 'Rutgert'
mas = {1:1, 2:2, 3:3}
for i in mas:
    print(f'{subject} человек {i} корень зла. ({autor})')
