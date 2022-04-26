
while True:
    number_one = int(input('Введите первое число'))
    calculation = input('Введите знак')
    number_two = int(input('Введите второе число'))
    if calculation == '0':
        break
    elif calculation == '-':
        print(number_one - number_two)
    elif calculation == '*':
        print(number_one * number_two)
    elif calculation == '/' and number_two == 0:
        print('Деление на 0 невозможно')
    elif calculation == '/':
        print(number_one / number_two)
    elif calculation == '+':
        print(number_one + number_two)
    else:
        print('Ошибка! Попробуй еще раз!')
