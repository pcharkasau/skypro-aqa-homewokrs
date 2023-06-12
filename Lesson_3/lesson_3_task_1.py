# **Задание 4. FizzBuzz. Задачка с собеседования**
# 1. Создайте файл lesson_2_task_4.py.
# 2. Напишите функцию fizz_buzz, которая принимает один аргумент — n (число).
# 3. Функция должна печатать числа от 1 до n. При этом:
#   1. если число делится на 3, печатать `Fizz`;
#   2. если число делится на 5, печатать `Buzz`;
#   3. если число делится на 3 и на 5, печатать `FizzBuzz`.
n = int(input("Введите число: "))

def fizz_buzz(n):
    for i in range(1, n+1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i, end=" \n")   
fizz_buzz(n)