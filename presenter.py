from file_models import users

from models import (Author,
                    Subscriber,
                    Admin)

user_types = {"author":Author,
             "subscriber":Subscriber,
             "admin":Admin}

def registration(user_type):
    user_login = input("login:")
    user_password = input("password:")
    if user_login not in [user.login for user in users]:
        user_class = user_types[user_type]
        user = user_class(user_login,user_password)
        users.append(user)
        print ("Ви зареєструвались!")
        
def login():
    user_login = input("login:")
    user_password = input("password:")
    for user in users:
        if user.check_auth(user_login, user_password):
            return user

def auth_menu(user_type):
    while True:
        choise = input("1 registration, 2 login, 9 exit:")
        if choise == "1":
            registration(user_type)
        if choise == "2":
            user = login()
            if user:
                print (user)
        if choise == "9":
            break
