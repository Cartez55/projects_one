import sys

count = int(sys.argv[1])
# Чтобы избежать пробела в начале вывода начинаем с 1
# Чтобы уровеней было = count добавляем count + 1
for i in range(1, count + 1):
    # Обратная лестница создается благодаря конструкции ' ' * (count - i)
    print(' ' * (count - i) + i * '#')
