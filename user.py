from books import Book
from borrow import Borrow

class User():
    def __init__(self, user_name, _password,  age, email, address, contact, id_user, ativo):
        self.user_name = user_name
        self._password = _password
        self.age = age
        self.email = email
        self.address = address
        self.contact = contact
        self.matricula = id_user
        self.ativo = ativo
        self.loans = []
        self.users = []
      
    def get_user_name(self):
        return self.user_name

    def get_email(self):
        return self.email

    def get_address(self):
        return self.address

    def get_contact(self):
        return self.contact

    def get_password(self):
        return self._password

    def get_id_user(self):
        return self.id_user

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self._password = password
    
    def set_address(self, address):
        self.address = address

    def set_id_user(self, id_user):
        self.id_user = id_user    

    def register(self,users):
        self.users.append(users)
     
    def login(self, user_name, password):
        if user_name == self.user_name and password == self._password:
            print("Login bem-sucedido.")
            return True
        else:
            print("Usuário ou senha incorretos. Tente novamente.")
            return False
 
    # Reserva livro
    def reserve_book(self, borrow_instance, book):
        borrow_instance.reserve_book(book)

    # Verifica disponibilidade do livro
    def check_available(self, borrow_instance, book):
        borrow_instance.check_available(book)
    
    # Devolver o livro
    def returned_book(self, borrow_instance, returned_books):
        borrow_instance.returned_book(returned_books)

# # Criar usuário
user = User("Alice", "senha123", 25, "alice@example.com", "Rua piaui, 200", "555-1234", "12345", True)

book = Book(isbn="978-3-16-148410-0", title="Dom Quixote", author="Miguel de Cervantes", year_of_publication=1605, num_of_editions=1, num_of_copies=10, num_of_pages=200)
loan = Borrow("Ativo", "2024-05-20", "2024-06-20", "Alice", book)  # Suponha que você tenha uma instância válida de Book

livros_devolvidos = ["Senhor dos Aneis", "Bras Cubas"]
user.check_available(loan, book)
user.reserve_book(loan, book)
user.returned_book(loan, livros_devolvidos)


# Adicionar usuário
new_user = User("Joana", "senha123", 25, "joana@example.com", "Rua camargo, 50", "555-1234", "12345", True)
new_user.register(new_user)

# Login bem-sucedido
user1 = User("fulano", "senha123", 25, "fulano@example.com", "Rua X, Cidade Y", 58478,"123456789", True)
attempt_1 = user1.login("fulano", "senha123")  

 # Usuário ou senha incorretos
attempt_2 = user1.login("fulano", "senha_errada")
