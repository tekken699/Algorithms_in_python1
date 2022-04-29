from random import random

#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
#кратны каждому из чисел в диапазоне от 2 до 9.

# numbers = range(2,100)
# a = [0]*8
# for i in range(2,100):
#     for j in range(2,10):
#         if i % j == 0:
#             a[j-2] += 1
# i = 0
#
# while i < len(a):
#     print(i + 2, ' - ', a[i])
#     i += 1

#4. Определить, какое число в массиве встречается чаще всего.

# a = [2,5,2,65,21,342,2,12,52,24,52]
#
# a_set = set(a)
#
# numbers = None
# qty_com = 0
#
# for i in a_set:
#     qty = a.count(i)
#     if qty > qty_com:
#         qty_com = qty
#         numbers = i
#
# print(numbers)

#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

# SIZE = 100
# array = [-30, 42, -5, 31, -37, 25, -50, -44, 17, -34, -33, -21, 48, 45, 15]
#
# maximum = - SIZE * SIZE
# for i in range(len(array)):
#     if array[i] < 0:
#         if array[i] > maximum:
#             maximum = array[i]
#             k = i
#
# print('Массив:', array)
# print('Максимальный отрицательны элемент в массиве:', maximum)
# print('Его позиция в массиве:', k)

#
# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

# string = 5 # строки
# column = 4 # столбец
# a = []
#
# for i in range(string):
#     b = []
#     s = 0
#     for j in range(column -1):
#         n = (int(input('Введите значения')))
#         s += n
#         b.append(n)
#     b.append(s)
#     a.append(b)
#
#
# for i in a:
#     print(i)


#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

#
# M = 10
# N = 5
# a = []
# for i in range(N):
#     b = []
#     for j in range(M):
#         n = int(random()*200)
#         b.append(n)
#         print('%4d' % n,end='')
#     a.append(b)
#     print()
#
# mx = -1
# for j in range(M):
#     mn = 200
#     for i in range(N):
#         if a[i][j] < mn:
#             mn = a[i][j]
#     if mn > mx:
#         mx = mn
#
# print("Максимальный среди минимальных: ", mx)



