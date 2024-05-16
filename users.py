from person import Person
from roles import Role
class User(Person):
    def __init__(self, user_name, _password, user_id, email, role, address, date_of_birth):
        super().__init__(user_name, _password, user_id, email, address, date_of_birth)
        self.user_id = user_id
        self.role = role