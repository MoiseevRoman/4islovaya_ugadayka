from random import *


def is_valid(s, diap):
    if s.isdigit() and 1 <= int(s) <= diap:
        return True
    else:
        return False

def ugadayka(num, diap):
    count = 0
    while True:
        n = input(f'Введите число от 1 до {diap}:')
        count += 1
        if is_valid(n, diap):
            n = int(n)
            if n < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif n > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                print(f'Вы угадали, поздравляем! Вы справились за {count} попыток')
                break
        else:
            print(f'А может быть все-таки введем целое число от 1 до {diap}?')
            continue


print('Добро пожаловать в числовую угадайку')
n = int(input('Укажите правую границу для случайного выбора числа:'))
digit = randint(1, n)

while True:
    ugadayka(digit, n)
    if input('Хотите ли сыграть еще раз(да/нет):') == 'да':
        n = int(input('Укажите правую границу для случайного выбора числа:'))
        digit = randint(1, n)
    else:
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
