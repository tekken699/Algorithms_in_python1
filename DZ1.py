from random import randint
from timeit import timeit

MAX_SIZE = 100
NUMBER_EXECUTIONS = 10_000


def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
                flag = False

        if flag == True:
            break
    return array


def bubble_sort_no_smart(array):
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]

    return array


numbers = [randint(-100, 100) for _ in range(MAX_SIZE)]
print(numbers)
print(bubble_sort(numbers))

time1 = timeit(f'bubble_sort({numbers})',
              setup='from __main__ import bubble_sort',
              number=NUMBER_EXECUTIONS)
time2 = timeit(f'bubble_sort_no_smart({numbers})',
              setup='from __main__ import bubble_sort_no_smart',
              number=NUMBER_EXECUTIONS)
print(time1)
print(time2)


'''2. Отсортируйте по возрастанию методом слияния одномерный вещественный
массив, заданный случайными числами на промежутке [0; 50). Выведите на экран
исходный и отсортированный массивы.'''

from random import randint

MAX_SIZE = 50

def merge_sort(array):

    if len(array) < 2:
        return array

    mid = len(array) // 2

    left_part = array[:mid]
    right_part = array[mid:]

    left_part = merge_sort(left_part)
    right_part = merge_sort(right_part)

    return merge_list(left_part, right_part)


def merge_list(list_1, list_2):
    result = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1

    result += list_1[i:]
    result += list_2[j:]
    return result


numbers = [randint(0, 50) for _ in range(MAX_SIZE)]

print(numbers)
print(merge_sort(numbers))



# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках.



def median(l, half):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return l[0]

    pivot = l[0]

    less = []
    more = []
    pivots = []
    for item in l:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            more.append(item)
        else:
            pivots.append(item)

    if len(less) > half:
        return median(less, half)
    elif len(less) + len(pivots) > half:
        return pivots[0]
    else:
        return median(more, half - len(more) - len(pivots))


n = 6
array = [random.randint(-100, 100) for _ in range(2 * n + 1)]
print(f'Исходный массив {array}')
print(f'Медиана {median(array, n)}')