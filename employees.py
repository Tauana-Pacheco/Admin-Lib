class Employee:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class LibraryManager(Employee):
    pass

class Receptionist(Employee):
    pass

class Cataloger(Employee):
    pass
