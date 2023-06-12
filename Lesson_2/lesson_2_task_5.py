# **Задание 5. Месяц — сезон**
# 1. Создайте файл lesson_2_task_5.py.
# 2. Напишите функцию month_to_season(), которая принимает 1 аргумент — номер месяца — и возвращает название сезона, к которому относится этот месяц.
# Например, передаем 2, на выходе получаем «Зима».

# лучшее решение
# a = int(input("Введите месяц: "))
# if a in [1, 2, 12]:
#     print("Зима")
# elif a in [3, 4, 5]:
#     print("Весна")
# elif a in [6, 7, 8]:
#     print("Лето")
# elif a in [9, 10, 11]:
#    print("Осень")
#______________________________________________________________________________________________________________________________

month = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
season = ["Зима", "Весна", "Лето", "Осень"]

mon = int(input("Введите номер месяца: "))
def month_to_season(mon):
    if mon == 1:
        print(season[0])
    if mon == 2:
        print(season[0])
    if mon == 3:
        print(season[1])
    if mon == 4:
        print(season[1])
    if mon == 5:
        print(season[1])
    if mon == 6:
        print(season[2])
    if mon == 7:
        print(season[2])
    if mon == 8:
        print(season[2])
    if mon == 9:
        print(season[3])
    if mon == 10:
        print(season[3])
    if mon == 11:
        print(season[3])
    if mon == 12:
        print(season[0])

month_to_season(mon)