from random import randint

rand_com = randint(1, 101)

i = 10
while True:
    human = int(input('Введите число'))
    i -= 1
    print(f'Осталось', i, 'попыток!')
    if human == rand_com:
        print('Вы победили !')
        break
    elif i == 0:
        print()
        print(f'Вы проиграли ! Загаданное число', rand_com)
    elif human > rand_com:
        print('Введенное число больше загаданного')
    elif human < rand_com:
        print('Введенное число меньше загаданного')

