# 1. Создайте файл `smartphone.py`.
# 2. В файле объявите класс `Smartphone`.
# 3. Объявите в классе конструктор.
# Конструктор должен принимать на вход следующие параметры:
# - марка телефона,
# - модель телефона,
# - абонентский номер (”+79…”).

class Smartphone:

    def __init__(self, brand, model, number):
        self.brand_phone = brand
        self.model_phone = model
        self.subscr_number = number

    def say_list(self):
        print("<",self.brand_phone, "> - <", self.model_phone, ">. <", self.subscr_number, ">")


# Напишите цикл, который печатает весь каталог (список) в формате `<марка> - <модель>. <номер телефона>`.