#8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
#Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

number_one = (input('Введите число'))
number_two = (input('Ввидите какую цифру нужно посчитать'))
q = 0
for i in number_one:
    if i in number_two:
        q +=1
print(q)