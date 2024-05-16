class AdminMaster:
    def __init__(self):
        self.users = []
        self.employees = []
        self.books = []

    def add_user(self, user):
        self.users.append(user)

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_book(self, book):
        self.books.append(book)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"Usuário '{user.username}' excluído com sucesso.")
        else:
            print("Usuário não encontrado.")

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"Funcionário '{employee.username}' removido do sistema")
        else:
            print("Funcionário não encontrado.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Livro  '{book.title}' removido removido.")
        else:
            print("Livro não encontrado.")

    def get_all_users(self):
        return self.users

    def get_all_employees(self):
        return self.employees

    def get_all_books(self):
        return self.books

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

