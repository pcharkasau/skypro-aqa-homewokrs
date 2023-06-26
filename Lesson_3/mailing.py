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
from address import Address

class Mailing(Address):
   
    def __init__(self, index, city, street, house, appartment, track = '123456', cost = '100'):
        Address.__init__(self, index, city, street, house, appartment)
        self.track = track
        self.cost = cost

    def child_mail(self):
        print(f"Отправление № {self.track}")

    def child_from_address(self):
        print(f"из <индекс> {self.index}, <город> {self.city}, <улица> {self.street}, <дом> {self.house}, <квартира> {self.appartment}")

    def child_to_address(self):
        print(f"из <индекс> {self.index}, <город> {self.city}, <улица> {self.street}, <дом> {self.house}, <квартира> {self.appartment}")
        
    def child_pay(self):
        print(f"Стоимость {self.cost} рублей.")
