# **Задание 7.  Сумма элементов списка**
# 1. Создайте файл lesson_2_task_7.py.
# 2. Дан список lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20].
# 3. Выведите сумму всех элементов списка.

lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

sum_of_list = 0

for num in lst:
    sum_of_list += num

print("Сумма чисел в списке: ", sum_of_list)

# альтернативный вариант решения
# list = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# sum_of_list = sum(list)
# print(sum_of_list)