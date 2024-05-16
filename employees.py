from person import Person
class Employee(Person):
    def __init__(self, user_name, _password, user_id, email, role, address, date_of_birth, employee_id):
        super().__init__(user_name, _password, user_id, email, role, address, date_of_birth)
        self.employee_id = employee_id
        