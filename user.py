from books import Book
from borrow import Borrow

class User():
    def __init__(self, user_name, _password,  age, email, address, contact, matricula, ativo):
        self.user_name = user_name
        self._password = _password
        self.age = age
        self.email = email
        self.address = address
        self.contact = contact
        self.matricula = matricula
        self.ativo = ativo
        self.loans = []
    
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

    def get_matricula(self):
        return self._matricula

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self._password = password
    
    def set_address(self, address):
        self.address = address

    def set_matricula(self, matricula):
        self.matricula = matricula    

    def register(self):
        # user_name = input("Digite um nome de usuário: ")
        # _password = input('senha123')
        # age = input("Digite a idade: ")
        # email = input('Digite o email: ')
        # contact = input("Telefone: ")
        # matricula = input("Digite a matrícula: ")
        # ativo = True
        # address = input("Endereço: ")
        # new_user = User(user_name, _password,  age, email, address, contact, matricula, ativo)
        # print("Usuário registrado com sucesso!")
        # return new_user
        pass
     
    def login(self, user_name, password):
        if user_name == self.user_name and password == self._password:
            print("Login bem-sucedido.")
            return True
        else:
            print("Usuário ou senha incorretos. Tente novamente.")
            return False
 
    # Solicitar emprestimo de livros
    def request_borrow(self,  books, user):
        borrowed = Borrow.borrow_books(self, books, user)
        return borrowed

    # Reserva livro
    def reserve_book(self, books):
        if Borrow.book in self.borrowed_books:
            print("O livro está indisponível no momento.")
        elif books in self.livros_reservados:
            print("O livro já está reservado por você.")
        else:
            if not books.available:
                print("O livro está indisponível no momento.")
            else:
                self.livros_reservados.append(books)
                print("Reserva realizada com sucesso.")
    
    # Visualizar quantidades de livros emprestados
    def view_quantity_books_loaned(self): 
        active_loans = [loan for loan in self.loans if loan.status == "Ativo"]
        return len(active_loans)
    

# # Criar usuário
user = User("Alice", "senha123", 25, "alice@example.com", "123 Main Street", "555-1234", "12345", True)

#  # Fazer empréstimo
book = Book(isbn="978-3-16-148410-0", title="Dom Quixote", author="Miguel de Cervantes", year_of_publication=1605, num_of_editions=1, num_of_copies=10, num_of_pages=200)
loan = Borrow("Ativo", "2024-05-20", "2024-06-20", "Alice", book)  # Suponha que você tenha uma instância válida de Book

# Visualizar quantidade de emprestimos de livros
print(user.view_quantity_books_loaned())

#  # user_name, _password,  age, email, address, contact, matricula, ativo
user1 = User("fulano", "senha123", 25, "fulano@example.com", "Rua X, Cidade Y", 58478,"123456789", True)
# user1.register_new_user()

#  # Tentativa de login
attempt_1 = user1.login("fulano", "senha123")  # Login bem-sucedido
attempt_2 = user1.login("fulano", "senha_errada")  # Usuário ou senha incorretos

###### refinar os metodos