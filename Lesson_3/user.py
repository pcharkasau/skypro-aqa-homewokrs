# 1. Создайте файл `user.py`.
# 2. В файле объявите класс `User`.
# 3. Объявите в классе конструктор.
# Конструктор должен принимать на вход 2 параметра:
# 1. `first_name` — имя.
# 2. `last_name` — фамилия.
# Помните, что все методы класса, включая конструктор, принимают первым параметром `self`.
# 1. Создайте в классе 3 метода, которые печатают:
#    - имя,
#    - фамилию,
#    - имя и фамилию.

class User:
    
    def __init__(self, name, surname):
        self.first_name = name
        self.last_name = surname             
       
    def say_name(self):
        print("Моё имя: ", self.first_name)
    def say_surname(self):
        print("Моя фамилия: ", self.last_name)
    def say_name_surname(self):
        print("Меня зовут: ", self.first_name, self.last_name)