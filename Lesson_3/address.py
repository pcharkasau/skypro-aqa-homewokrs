# 1. В отдельном файле создайте класс `Address`.
# 2. Класс должен содержать в себе поля:
#     - «индекс»,
#     - «город»,
#     - «улица»,
#     - «дом»,
#     - «квартира».
# 3. В отдельном файле создайте класс `Mailing` (почтовое отправление).
# 4. В классе должно быть 4 поля:
#     - `to_address` (тип данных `Address`),
#     - `from_address` (тип данных `Address`),
#     - `cost` (тип данных `число`),
#     - `track` (тип данных строка).
# 5. Создайте файл `lesson_3_task_3.py`.
# 6. Импортируйте классы `Address` и `Mailing`.
# 7. В файле создайте экземпляр класса `Mailing`.
# 8. Заполните поля класса адресами (`to_address` и `from_address`), трек-номером (`track`) и стоимостью (`cost`).
# 9. Распечатайте в консоль отправление в формате: `Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в <индекс>, 
# <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей.`.
# Все данные должны получаться из экземпляра Mailing.

class Address:

    index = '000000'
    city = 'Неизвестен'
    street = 'Неопределен'
    house = '000'
    appartment = '000'

    def __init__(self, index, city, street, house, appartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.appartment = appartment