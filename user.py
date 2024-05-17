from person import Person
from books import Book

class User(Person):
    def __init__(self, user_name, _password,  age, email, address, contact, matricula, ativo):
        super().__init__(user_name, _password, age, email, address, contact)
        self.matricula = matricula
        self.ativo = ativo
        self.loans = []

    def register_new_user(self):
        user_name = input("Digite um nome de usuário: ")
        _password = input('senha123')
        age = input("Digite a idade: ")
        email = input('Digite o email: ')
        contact = input("Telefone: ")
        matricula = input("Digite a matrícula: ")
        ativo = True
        address = input("Endereço: ")
        new_user = User(user_name, _password,  age, email, address, contact, matricula, ativo)
        print("Usuário registrado com sucesso!")
        return new_user

    def login(self, user_name, password):
        if user_name == self.user_name and password == self._password:
            print("Login bem-sucedido.")
            return True
        else:
            print("Usuário ou senha incorretos. Tente novamente.")
            return False
 
    # Faz emprestimo
    def add_loan(self, loan):
        self.loans.append(loan)

    # Reserva livro
    def reservar(self, livro):
        if livro in self.livros_emprestados:
            print("O livro está indisponível no momento.")
        elif livro in self.livros_reservados:
            print("O livro já está reservado por você.")
        else:
            self.livros_reservados.append(livro)
            print("Reserva realizada com sucesso.")

    # Visualizar o status do empréstimo
    def view_loan_status(self):
        if self.loans:
            print("Status dos empréstimos:")
            for loan in self.loans:
                print(f"Status: {loan.status}, Livro: {loan.book.title}, Data de início: {loan.start_date}, Data de término: {loan.end_date}")
        else:
            print("Você não tem empréstimos ativos.")
    
    # Visualizar quantidades de livros emprestados
    def view_quantity_books_loaned(self): 
        active_loans = [loan for loan in self.loans if loan.status == "Ativo"]
        return len(active_loans)
    
    # Devolver livro
    def return_books(self, livros_devolvidos):
        for book in livros_devolvidos:
            if book in self.livros_emprestados:
                self.livros_emprestados.remove(book)
                print(f"O livro '{book}' foi devolvido com sucesso.")
            else:
                print(f"O livro '{book}' não está emprestado pelo usuário.")

    # Verifica disponibilidade do livro
    def verificar_disponibilidade(self, livro):
        if livro in self.livros_emprestados:
            print("O livro está indisponível no momento.")
        elif livro in self.livros_reservados:
            print("O livro já está reservado por você.")
        else:
            print("O livro está disponível para empréstimo.")

class Loan: 
    def __init__(self, status, start_date, end_date, user_name, book):
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.user_name = user_name
        self.book = book


# Criar um usuário
user = User("Alice", "senha123", 25, "alice@example.com", "123 Main Street", "555-1234", "12345", True)

 # Criar um empréstimo
book = Book(id=1, title="Dom Quixote", author="Miguel de Cervantes", year_of_publication=1605, num_of_editions=1, num_of_copies=10)
loan = Loan("Ativo", "2024-05-20", "2024-06-20", "Alice", book)  # Suponha que você tenha uma instância válida de Book

 # Adicionar o empréstimo ao usuário
user.add_loan(loan)

 # Visualizar o status do empréstimo
user.view_loan_status()

 # Visualizar quantidade de livros
print(user.view_quantity_books_loaned())

 # user_name, _password,  age, email, address, contact, matricula, ativo
user1 = User("fulano", "senha123", 25, "fulano@example.com", "Rua X, Cidade Y", 58478,"123456789", True)
user1.register_new_user()

 # Tentativa de login
attempt_1 = user1.login("fulano", "senha123")  # Login bem-sucedido
attempt_2 = user1.login("fulano", "senha_errada")  # Usuário ou senha incorretos