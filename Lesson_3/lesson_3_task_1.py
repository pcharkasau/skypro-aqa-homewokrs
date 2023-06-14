# 5. Создайте файл `lesson_3_task_1.py`.
# 6. Импортируйте в него класс `user`.
# 7. Создайте новый экземпляр `User` и сохраните его в переменную `my_user`.
# 8. Вызовите все методы у объекта в переменной `my_user`.

from user import User

my_user = User("Peter", "Pan")

my_user.say_name()
my_user.say_surname()
my_user.say_name_surname()