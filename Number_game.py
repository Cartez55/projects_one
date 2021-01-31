from random import randint

number = randint(0, 101)

while True:
    answer = input('Введите число: ')

    if not answer or answer == 'exit':
        break

    if not answer.isdigit():
        print('Введите число, а не строку')
        continue

    user_answer = int(answer)

    if user_answer == number:
        print('Вы угадали')
        break
    elif user_answer > number:
        print('Число меньше')
    elif user_answer < number:
        print('Число больше')
