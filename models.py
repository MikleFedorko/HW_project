class User:
    def __init__(self,
                 login,
                 password):
        self.__login = login
        self.__password = password

    @property
    def login(self):
        return self.__login

    def check_auth(self,
                   login,
                   password):
        if self.__login == login and self.__password == password:
            return True
        else:
            return False

class Author(User):
    pass

class Subscriber(User):
    pass

class Admin(User):
    pass
