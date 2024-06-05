import sys
from books import Book, DigitalBook, PhysicalBook
from borrow import Borrow
from employee import Librarian, Admin
from user import User

def interactive_cli():
    while True:
        print("\n\033[1m Bem-vindo ao sistema bibliotecário!\033[m")
        print("1. Usuário")
        print("2. Para todos") 
        print("3. Somente para funcionários")      
        print("5. Fechar sistema")

        role_choice = input("Digite o número da opção: ")

        if role_choice == '1':
            user_menu()

        if role_choice == '3':
            employee_menu()

        elif role_choice == '2':
            print("Bem vindo ao sistema de funcionários!")
            print("1. Consultar emprestimos")
            print("2. Serviço de Livros")
            print("3. Voltar")

            employee_choice = input("Digite o número da opção: ")

            if employee_choice == '1':
                borrow_menu()
            
            elif employee_choice == '2':
                book_menu()

            else:
                print("Opção inválida, tente novamente.")
     
        elif role_choice == '5':
           exit_program()

        else:
            print("Opção inválida, tente novamente.")

def user_menu():
    while True:
        print("\n1. Login\n2. Fazer Cadastro\n3. Atualizar cadastro\n4. Fazer empréstimo\n5. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            user_name = input("Nome de usuário: ")
            password = input("Senha: ")
            
            user = User(user_name, password, None, None, None, None, None, None)
            user.login(user_name, password)

        elif choice == '2':
            user_name = input("Nome de usuário: ")
            password = input("Senha: ")
            age = int(input("Idade: "))
            email = input("Email: ")
            address = input("Endereço: ")
            id_user = input("ID do usuário: ")
            contact = input("Contato: ")
            ativo = input("Ativo (1 para sim, 0 para não): ")

            user = User(user_name, password, age, email, address, id_user, contact, ativo)
            user.save_to_db()
   
        elif choice == '3':
            user_name = input("Nome de usuário: ")
            password = input("Senha: ")
            
            user = User(user_name, password, None, None, None, None, None, None)
            user.login(user_name, password)
            email = None
            address = None
            contact = None
            age = None
            id_user = None
            ativo = None
            user_name = input('Qual seu nome: ')
            if user_name == user.user_name:
                print('Qual dado você quer alterar? ')
                print("\n1. Nome de usuário:\n2. Senha:\n3. Idade:\n4. Email\n5. Endereço\n6. Contato.")
                options_choice = input("Digite o número da opção: ")
                if options_choice == '1':
                    user_name = input("Novo nome de usuário: ")
                if options_choice == '2':
                    password = input("Nova senha: ")
                if options_choice == '3':
                    age = input("Nova idade: ")      
                if options_choice == '4':     
                    email = input("Novo email: ")
                if options_choice == '5':
                     address = input("Novo endereço: ")
                if options_choice == '6':   
                    contact = input("Novo contato: ")
                user = User(user_name, password, int(age) if age else None, email, address, None, contact,None)
            
                user.update_info(new_user_name=user_name, new_password=password, new_age=int(age) if age else None,
                                new_email=email, new_address=address, new_contact=contact,
                                new_id_user=id_user if id_user else None, new_status=int(ativo) if ativo else None)        
        
        elif choice == '5':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

def employee_menu():
    while True:
        print("\nMenu:")
        print("1. Registrar funcionário") # ok
        print("2. Registar usuário") # ajustar 
        print("3. Remover usuário") # ajustar
        print("4. Sistema de Livros" )
        print("5. Sistema de Emprestimo")
        # print("6. Visualizar livros disponíveis") # ausyar
        # print("7. Emprestar livro") # ok
        print("8. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("Nome: ")
            _age = input("Idade: ")
            _email = input("Email: ")
            _address = input("Endereço: ")
            _contact = input("Telefone: ")

            type_position = input("Função (Administradora/Bibliotecaria): ")
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
            admin = Admin.load_from_db_admin(admin_id)
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
                user = User(user_name, password, age, email, address, id_user, contact, ativo)

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
       
       #("Milena Martins", 32, "milena@gmail.com", "Rua fontes, 22", "1197485-9945", "1")
        elif choice == '4':
            librarian_id = input("Digite o ID do bibliotecario: ")
            librarian = Librarian.load_from_db_librarin(librarian_id)
            book_menu()
        
        elif choice == '5':
            librarian_id = input("Digite o ID do bibliotecario: ")
            librarian = Librarian.load_from_db_librarin(librarian_id)
            borrow_menu()

        # elif choice == '5':
        #     user_name = input("Nome de usuário: ")
        #     password = input("Senha: ")
        #     user = User(user_name, password, None, None, None, None, None, None)
        #     librarian = Librarian("Milena Martins", 32, "milena@gmail.com", "Rua fontes, 22", "1197485-9945", "1")
        
        #     if user.login(user_name, password):

        #         isbn = input("ISBN do livro para emprestar: ")
        #         books_to_borrow = [book for book in librarian.get_books() if book.isbn == isbn and book.available]
        #         if books_to_borrow:
        #             borrowed_book = librarian.borrow_books(books_to_borrow[0], user)
        #             if borrowed_book:
        #                 print(f"Livro com ISBN '{isbn}' emprestado com sucesso.")
        #         else:
        #             print(f"Livro com ISBN '{isbn}' não está disponível.")

        elif choice == "6":
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

def borrow_menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Emprestar livro")
        print("2. Devolver livro")
        print("3. Reservar livro")
        print("4. Verificar disponibilidade do livro")
        print("5. Sair")

        choice = input("Digite o número da opção: ")

        if choice == '1':
            id_user = input("Digite o ID do usuário: ")
            id_book = input("Digite o ID do livro: ")
            start_date = input("Digite a data de início (AAAA-MM-DD): ")
            end_date = input("Digite a data de término (AAAA-MM-DD): ")
            borrow = Borrow('EMPRESTADO', start_date, end_date, id_user, id_book)
            borrow.save_to_db()

        elif choice == '2':
            isbn = None
            author = None
            title = None
            year_of_publication = None 
            num_of_editions = None
            num_of_copies = None
            num_of_pages = None
            available = None
            type_book = None
            id_book = input("Digite o ID do livro: ")
            book = Book(isbn, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages, available, type_book)
            borrow = Borrow(None, None, None, None, id_book)
            borrow.returned_book(book)

        elif choice == '3':
            author = None,
            year_of_publication = None 
            num_of_editions = None
            num_of_copies = None
            num_of_pages = None
            type_book = None
            id_user = input("Digite o ID do usuário: ")
            id_book = input("Digite o ID do livro: ")
            start_date = input("Digite a data de início (AAAA-MM-DD): ")
            end_date = input("Digite a data de término (AAAA-MM-DD): ")
            borrow = Borrow('RESERVADO', start_date, end_date, id_user, id_book)
            book = Book(author, year_of_publication, num_of_editions, num_of_copies, num_of_pages, type_book)
            borrow.reserve_book(book)

        elif choice == '4':
            id_book = input("Digite o ID do livro: ")
            isbn = None
            title = None
            author = None,
            year_of_publication = None 
            num_of_editions = None
            num_of_copies = None
            num_of_pages = None
            available = None
            type_book = None
            book = Book(isbn, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages, available, type_book)
            borrow = Borrow(None, None, None, None, id_book)
            borrow.check_available(book)

        elif choice == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

def book_menu():
    print("Bem-vindo ao serviço de livros")
    while True:
        print("\nMenu:")
        print("1. Adicionar livro")
        print("2. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            isbn = input("ISBN: ")
            title = input("Titulo: ")
            author = input("Autor: ")
            year_of_publication = input("Ano de publicação: ")
            num_of_editions = input("Número de edições: ")
            num_of_copies = input("Número de cópias: ")
            num_of_pages = input("Número de páginas: ")
            type_book = input("Tipo de Livro (PhysicalBook/DigitalBook): ")

            if type_book == "PhysicalBook":
                cover_type = input("Tipo de capa: ")
                weight = input("Peso: ")
                book = PhysicalBook(isbn, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages, cover_type, weight)
            elif type_book == "DigitalBook":
                file_size = input("Tamanho do arquivo: ")
                format = input("Formato: ")
                book = DigitalBook(isbn, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages, file_size, format)
            else:
                print("Tipo de livro inválido!")
                continue

            book.save_to_db()
            
        elif choice == "2":
            print("Saindo...")
            break

def exit_program():
    print("Fechando sistema...")
    sys.exit(0)

if __name__ == "__main__":
    interactive_cli()