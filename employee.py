class Employee:
    def __init__(self, user_name, _password, age, email, address, contact):
        self.user_name = user_name
        self._password = _password
        self.age = age
        self.email = email
        self.address = address
        self.contact = contact
        self.id_user = []
        
    def get_address(self):
        return self.address

    def get_contact(self):
        return self.contact

    def get_password(self):
        return self._password
    
    def set_password(self, password):
        self._password = password
    
    def set_address(self, address):
        self.address = address
    


