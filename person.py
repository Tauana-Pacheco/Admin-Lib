

class Person:
    def __init__(self, user_name, _password, user_id, email, role, address, date_of_birth, contact):
        self.user_id = user_id
        self.email = email
        self.user_name = user_name
        self._password = _password
        self.role = role
        self.address = address
        self.date_of_birth = date_of_birth
        self.contact = contact


    def can_perform_action(self, action):
        return action in self.role.permissions 

    def get_address(self):
        return self.address

    def get_date_of_birth(self):
        return self.date_of_birth
    
    def get_contact(self):
        return self.contact
    
    def set_address(self, address):
        self.address = address

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth
