# **Задание 8. Range**
# 1. Изучите статью: https://pythonchik.ru/osnovy/python-range.
# 2. Создайте файл lesson_2_task_8.py.
# 3. Создайте список [ 18, 14, 10, 6, 2 ] с помощью функции range() и выведите его на экран.

# version 1___________________________
# import numpy as np
# arr = np.arange(18, 1, -4)
# print(arr)

# version 2___________________________
# array_1 = [i for i in range(18, 1, -4)]
# print(array_1)

# version 3___________________________
array_2 = []
for i in range(18, 1, -4):
    array_2.append(i)
print(array_2)