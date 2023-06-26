from models import User

from presenter import (login,
                       registration,
                       auth_menu)

choises = {"1":"admin",
          "2":"author",
          "3":"subscriber"}

while True:
    choise = input("1 Admin, 2 Author, 3 Subscriber, 9 exit:")
    if choise in choises:
        user_type = choises.get(choise)
        auth_menu(user_type)
    if choise == "9":
        break
