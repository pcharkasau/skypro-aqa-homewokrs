# 5. В файле объявите переменную `catalog`.
# 6. Переменная хранит в себе список (`[]`).
# 7. Наполните список пятью разными экземплярами класса `Smartphone`.
# 8. Напишите цикл, который печатает весь каталог (список) в формате `<марка> - <модель>. <номер телефона>`.

from smartphone import Smartphone

# создаём переменные
catalog1 = Smartphone("Samsung", "Galaxy A73 5G", "+79280700001")
catalog2 = Smartphone("Samsung", "Galaxy A23", "79280700002")
catalog3 = Smartphone("Samsung", "Galaxy A53 5G", "+79280700003")
catalog4 = Smartphone("Samsung", "Galaxy A13", "+79280700004")
catalog5 = Smartphone("Samsung", "Galaxy S21 FE", "+79280700005")

catalog1.say_list() # просим напечатать каталог
catalog2.say_list()
catalog3.say_list()
catalog4.say_list()
catalog5.say_list()