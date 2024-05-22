from db import  delete_table, create_tables, create_connection, close_connection
from user import User
from books import PhysicalBook, DigitalBook
from borrow import Borrow

# delete_table('User')
# create_tables()

# delete_table('PhysicalBook')
# delete_table('DigitalBook')
# Definir as informações do empréstimo
status = 'INDISPONÍVEL'  # Assumindo que o livro está emprestado
start_date = '2024-05-25'  # Data de início do empréstimo
end_date = '2024-06-25'  # Data de término do empréstimo

# Obter o ID do usuário com base no nome
user = User.get_id_user('ID_4153')
if user:
    id_user = 'ID_4153'
else:
    # Lidar com o caso em que o usuário não é encontrado
    print("Usuário não encontrado.")
    id_user = None

# Obter o ID do livro
digital_book = DigitalBook.get_title('O Ateneu')  # Supondo que você tenha um método semelhante para buscar o livro pelo título
if digital_book:
    id_book = digital_book
else:
    # Lidar com o caso em que o livro não é encontrado
    print("Livro não encontrado.")
    id_book = None

# Salvar o empréstimo no banco de dados se o usuário e o livro forem encontrados
if id_user and id_book:
    borrow = Borrow(status, start_date, end_date, id_user, id_book)
    borrow.save_to_db()


# Criar um objeto de empréstimo
# status = 'INDISPONÍVEL'  # Assumindo que o livro está emprestado
# start_date = '2024-05-25'  # Data de início do empréstimo
# end_date = '2024-06-25'  # Data de término do empréstimo
# id_user = User.get_user_name('Iris')  # ID do usuário que está realizando o empréstimo
# id_book = DigitalBook.id  # ID do livro digital que está sendo emprestado

# # Salvar o empréstimo no banco de dados
# borrow = Borrow(status, start_date, end_date, id_user, id_book)
# borrow.save_to_db()

###### USER ######
# user = User("ID", "Maria Lice", "senha(protegido)", 25, "alice@example.com", "Rua brasil, 01", "ID_3453", "11225-1234","False")
# user1 = User("ID", "Iris", "senha(protegido)", 18, "iris@example.com", "Rua piaui, 200", "ID_4153", "11385-1234","True")
# user2 = User("ID", "Lavinia", "senha(protegido)", 45, "lavnia@example.com", "Rua piaui, ", "ID_8453", "21885-1234","True")
# user3 = User("ID", "Ines", "senha(protegido)", 65, "ines@example.com", "Rua araguaia, 30", "ID_8453", "31885-9975","False")
# user4 = User("ID", "Maria Lice", "senha(protegido)", 17, "joao@example.com", "Rua sergipe, 100", "ID_8456", "11885-888","True")
# user.save_to_db()
# user1.save_to_db()
# user2.save_to_db()
# user3.save_to_db()
# user4.save_to_db()


# ##### BOOKS ######
# # Criar um livro digital e salvar no banco de dados
# digital_book = DigitalBook("40-0-430-21064-3", 'O Ateneu', 'Raul Pompeia', 1888, 3, 250, 200, '150mb', 'PDF')
# digital_book2 = DigitalBook("13-1-637-91034-1", 'Anjos e Demonios', 'Carl Sagan', 1996, 2, 250, 270, '350mb', 'ePUB')
# digital_book.save_to_db()
# digital_book2.save_to_db()

# # Criar um livro físico e salvar no banco de dados
# physical_book = PhysicalBook("21-9-430-21033-1", "Kindred", "Octavia Butler", 1999, 1, 10, 200, 'Capa dura', 500)
# physical_book.save_to_db()

# # Atualizar o livro digital
# digital_book.title = 'O Ateneu - Edição Especial'
# digital_book.save_to_db()

# # Atualizar o livro físico
# physical_book.weight = 600
# physical_book.save_to_db()

