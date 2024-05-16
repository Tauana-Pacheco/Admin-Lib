import random 

class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._address = None
        self._date_of_birth = None
        self._user_id = None

    def get_password(self):
        return self._password

    def get_address(self):
        return self._address

    def get_date_of_birth(self):
        return self._date_of_birth
    
    def get_user_id(self):
        return self._user_id

    def register(self, new_username, new_password, new_address=None, date_of_birth=None):
        if new_username and new_password:
            self._username = new_username
            self._password = new_password
            self._address = new_address
            self._date_of_birth = date_of_birth
            self._user_id = random.randint(1000, 9999)

            print("Registratado com sucesso!")
        else:
            print("Ops, o registro falhou!")


    def login(self, username, password):
        if username == self._username and password == self._password:
            print("Login efetuado com sucesso! :)")
        else:
            print("Ops, login falhou! :(")

