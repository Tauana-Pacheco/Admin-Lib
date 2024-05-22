from db import create_connection, close_connection
class Employee:
    def __init__(self, name, _password, _age, _email, _address, _contact, type_position):
        self.name = name
        self._password = _password
        self._age = _age
        self._email = _email
        self._address = _address
        self._contact = _contact
        self.type = type_position
    
    def save_to_db(self):
        connection = create_connection()
        if connection: 
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Employee (name, age, email, address, contact, type) VALUES (?, ?, ?, ?, ?, ?)",
            (self.name, self._age, self._email, self._address, self._contact, self.type))
            connection.commit()
            cursor.close()
            close_connection(connection)
            print(f"Funcionário {self.name} salvo no banco de dados.")
    
    # Getters
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self._age
    
    def get_email(self):
        return self._email

    def get_password(self):
        return self._password
    
    def get_address(self):
        return self._address

    def get_contact(self):
        return self._contact

    # Setters 
    def set_name(self, name):
        self.name = name 
        
    def set_age(self, age):
        self._age = age
    
    def set_email(self, email):
        self._email = email
    
    def set_password(self, password):
        self._password = password
    
    def set_address(self, address):
        self._address = address

    def set_contact(self, contact):
        self._contact = contact
        
    


