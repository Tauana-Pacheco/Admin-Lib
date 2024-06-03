from db import create_connection, close_connection
from sqlite3 import Error, IntegrityError
from datetime import datetime
from borrow import Borrow
from user import User
from books import Book

class Employee:
    def __init__(self, name, _age, _email, _address, _contact, type_position, id_=None):
        self.name = name
        self._age = _age
        self._email = _email
        self._address = _address
        self._contact = _contact
        self.type_position = type_position
        self.id = id_
    
    def save_to_db(self):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("INSERT INTO Employee (name, age, email, address, contact, type_position) VALUES (?, ?, ?, ?, ?, ?)",
                            (self.name, self._age, self._email, self._address, self._contact, self.type_position))
                employee_id = cursor.lastrowid
                
                if isinstance(self, Admin):
                    cursor.execute("INSERT INTO Admin (id, id_admin) VALUES (?, ?)",
                                    (employee_id, self.id_admin))
                elif isinstance(self, Librarian):
                    cursor.execute("INSERT INTO Bibliotecaria (id, id_librarian) VALUES (?, ?)",
                                    (employee_id, self.id_librarian))
                connection.commit()
                print(f"Funcionário {self.name} salvo no banco de dados.")
            except Exception as e:
                print(f"Erro ao salvar funcionário no banco de dados: {e}")
            finally:   
                cursor.close()
                close_connection(connection)
            
    @staticmethod
    def load_from_db(admin_id):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                sql_command = "SELECT * FROM Employee JOIN Admin ON Employee.id = Admin.id WHERE Admin.id_admin = ?"
                cursor.execute(sql_command, (admin_id,))
                row = cursor.fetchone()
                if row:
                    return Admin(row[1], row[2], row[3], row[4], row[5], row[6], row[0])
                else:
                    print(f"Admin with id {admin_id} not found.")
                    return None
            except Error as e:
                print(f"Erro ao carregar administrador do banco de dados: {e}")
                return None
            finally:
                cursor.close()
                close_connection(connection)
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

class Admin(Employee):
    def __init__(self, name, _age, _email, _address, _contact, id_admin, id_=None):
        super().__init__(name, _age, _email, _address, _contact, "Admin", id_)
        self.id_admin = id_admin
        self.user = []   
    
    def _remove_user(self, user):
        if not self.user:
            print("Erro: Não há usuários registrados no sistema.")
            return
        
        removed = False
        for stored_user in self.user:
            if stored_user.id == user.id:
                self.user.remove(stored_user)
                removed = True
                print(f"Usuário '{user.user_name}' foi removido do sistema.")
                break
        
        if not removed:
            print(f"Erro: Usuário '{user.user_name}' não encontrado no sistema.")

class Librarian(Employee):
    def __init__(self, name, _age, _email, _address, _contact, id_librarian, id_=None):
        super().__init__(name, _age, _email, _address, _contact, "Bibliotecaria", id_)
        self.id_librarian = id_librarian
        self.books = self.load_books_from_db()
    
    def borrow_books(self, book, user):
        if not book.available:
            print(f"O livro '{book.title}' não está disponível para empréstimo.")
            return None
        else:
            date_borrow = datetime.now().strftime("%Y-%m-%d")
            name = user.get_user_name()
            borrowed = Borrow("emprestado", date_borrow, None, name, book.title)
            book.available = False  # Mark the book as borrowed
            self.update_book_availability_in_db(book.isbn, False)
            print(f"Livro '{book.title}' foi emprestado para {name} em {date_borrow}.")
            return borrowed
    
    def get_books(self):
        return self.books
    
    def update_book_availability_in_db(self, isbn, available):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE Book SET available = ? WHERE isbn = ?", (available, isbn))
            connection.commit()
            cursor.close()
            close_connection(connection)

    def save_book_to_db(self, book):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            try:
               cursor.execute(
                 "INSERT INTO Book (isbn, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages, available, type_book) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                 (book.isbn, book.title, book.author, book.year_of_publication, book.num_of_editions, book.num_of_copies, book.num_of_pages, book.available, book.type_book)
            )
               connection.commit()
            except IntegrityError as e:
                 print(f"Erro ao salvar livro no banco de dados: {e}")
            finally:
               cursor.close()
               close_connection(connection)

    def _add_new_books(self, books):
        for book in books:
            self.books.append(book)
            self.save_book_to_db(book)
    
    def load_books_from_db(self):
        connection = create_connection()
        books = []
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT isbn, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages, available, type_book FROM Book")
            rows = cursor.fetchall()
            for row in rows:
                book = Book(row[0], row[1], row[2], row[3], row[4], row[5], row[6], bool(row[7]), row[8])
                books.append(book)
            cursor.close()
            close_connection(connection)
        return books

def main():
    print("Bem vindo ao sistema de funcionários!")
    while True:
        print("\nMenu:")
        print("1. Registrar funcionário") # ok
        print("2. Registar usuário") # ok 
        print("3. Remover usuário") # ajustar
        print("4. Visualizar livros disponíveis") # ok
        print("5. Emprestar livro") # ok
        print("6. Sair")
        choice = input("Escolha uma opção: ")
        type_position = input("Função (Administradora/Bibliotecaria): ")

        if choice == "1":
            name = input("Nome: ")
            _age = input("Idade: ")
            _email = input("Email: ")
            _address = input("Endereço: ")
            _contact = input("Telefone: ")

            if type_position == "Admin":
                id_admin = input("Adm ID: ")
                employee = Admin(name, _age, _email, _address, _contact, id_admin)
            elif type_position == "Bibliotecaria":
                id_librarian = input("Bibliotecaria ID: ")
                employee = Librarian(name, _age, _email, _address, _contact, id_librarian)
            else:
                print("Cargo inválido. Certifique-se sua escolha 'Admin' ou 'Bibliotecaria'.")
                continue

            employee.save_to_db()

        elif choice == "2":
            admin_id = input("Digite o ID do administrador: ")
            admin = Admin.load_from_db(admin_id)
            if admin:
                id = input("ID: ")
                user_name = input("Nome do Usuário: ")
                password = input("Senha: ")
                age = input("Idade do Usuário: ")
                email = input("Email do Usuário: ")
                address = input("Endereço do Usuário: ")
                id_user = input("ID do Usuário: ")
                contact = input("Telefone do Usuário: ")
                ativo = input("Ativo (True/False): ") == 'True'
                user = User(id, user_name, password, age, email, address, id_user, contact, ativo)

                user.save_to_db()
            else:
                print("Administrador não encontrado.")
        
        # ajustar
        elif choice == '3':
            admin_id = input("Digite o ID do administrador: ")
            admin = Admin.load_from_db(admin_id)
            if admin:
                id_user = input("ID do Usuário: ")
                user = User(None, None, None, None, None, None, id_user, None, None)
                user.remove_user_from_list([], user=id_user)
            else:
                print("Erro ao remover usuário.")
       
        elif choice == '4':
            librarian = Librarian("Milena Martins", 32, "milena@gmail.com", "Rua fontes, 22", "1197485-9945", "1")
            available_books = [book for book in librarian.get_books() if book.available]
            if available_books:
                print("Livros disponíveis:")
                for book in available_books:
                    print(f" - {book.title} por {book.author} (ISBN: {book.isbn})")
            else:
                print("Nenhum livro disponível no momento.")

        elif choice == '5':
            user_name = input("Nome de usuário: ")
            password = input("Senha: ")
            user = User(None, user_name, password, None, None, None, None, None, None)
            librarian = Librarian("Milena Martins", 32, "milena@gmail.com", "Rua fontes, 22", "1197485-9945", "1")
        
            if user.login(user_name, password):

                isbn = input("ISBN do livro para emprestar: ")
                books_to_borrow = [book for book in librarian.get_books() if book.isbn == isbn and book.available]
                if books_to_borrow:
                    borrowed_book = librarian.borrow_books(books_to_borrow[0], user)
                    if borrowed_book:
                        print(f"Livro com ISBN '{isbn}' emprestado com sucesso.")
                else:
                    print(f"Livro com ISBN '{isbn}' não está disponível.")

        elif choice == "6":
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
