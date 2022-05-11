# Задание 9 урок 3
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# python -m timeit -n 100 -s "import random" "x = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]" "import task_1" "task_1.matrix_func(x)"

# 100 loops, best of 5: 73.6 usec per loop          3 X 3
# 100 loops, best of 5: 177 usec per loop           5 X 5
# 100 loops, best of 5: 375 usec per loop           5 X 10
# 100 loops, best of 5: 338 usec per loop           10 X 5
# 100 loops, best of 5: 657 usec per loop           10 X 10