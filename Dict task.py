import  calendar
'''
print(1 - 3.2)
print(int(10 / 2))
print(True > False)
x = False
print(1 < 0 < x)
print(bool(0))
'''
# Проверка на високосный год
year = 2020
is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(is_leap)

print(calendar.isleap(2020))