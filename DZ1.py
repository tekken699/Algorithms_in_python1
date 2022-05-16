import sys

n = int(input('Введите трехзначное число '))
c = n % 10
n = n // 10
b = n % 10
a = n // 10
print('Сумма чисел ', a + b + c)
print('Произведение чисел ', a * b * c)

get_size = sys.getsizeof(n) + sys.getsizeof(c) + sys.getsizeof(b) + sys.getsizeof(a)
print(f'В программе задействованно {get_size} байтов')

# Урок 2, задача № 3. Сформировать из введенного числа обратное по порядку
# входящих в него цифр и вывести на экран. Например, если введено число 3486,
# то надо вывести число 6843.
print('***************************************')

number = input('ВВедите число')[::-1]
print(number)

print(f'{sys.getsizeof(number)} байтa')


print('***************************************')

#4. Определить, какое число в массиве встречается чаще всего.

a = [2,5,2,65,21,342,2,12,52,24,52]

a_set = set(a)

numbers = None
qty_com = 0

for i in a_set:
    qty = a.count(i)
    if qty > qty_com:
        qty_com = qty
        numbers = i

print(numbers)
 
get_size_2 = sys.getsizeof(a) + sys.getsizeof(a_set) + sys.getsizeof(number) + sys.getsizeof(qty_com)

print(f'В программе зайдествованно {get_size_2} байтов')
