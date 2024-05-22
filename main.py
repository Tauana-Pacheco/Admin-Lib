from db import  delete_table, drop_table, update_row,  delete_row, create_tables, create_connection, close_connection
from user import User
from books import PhysicalBook, DigitalBook
from borrow import Borrow
from admin import Adm
from employee import Employee
# from librarian import Librarian  V2 Implementar busca

#### EMPLOEEY ######
employee = Employee("Zenilda Ferreira", "senha(protegido)", 68, "zenilda@example.com", "Av. Brasil 2351", "1395623-7845", "Administradora")
employee1 = Employee("Gilda Amaral", "senha(protegido)", 88, "gilda@example.com", "Av. Angélica 2351", "13883-7845", "Biliotecaria")
employee.save_to_db()
employee1.save_to_db()

###### ADM ######
# Zenilda Ferreira", "", 68,  "zenilda@example.com", "Av. Brasil 2351", "1395623-7845", "Administradora"
admin = Adm("Paola Santana", "", 40,  "paola@example.com", "Av. Brasil 88", "139623-7845", "Administradora")
admin_new_user = User("ID", "Cecilia", "senha(protegido)", 24, "cecilia@example.com", "Rua das flores, 50", "ID_1473", "1135-4238", "True")
admin._register_new_user(admin_new_user)  
admin.save_to_database()

admin1 = Adm(" Tamara Salvador", "_password", 40,  "salvador@example.com", "Av. Salvador 97", "329623-4445", "Admin1istradora")
register_new_user1 = User("ID", "Yolanda", "_password", 24, "yolanda@example.com", "Rua camargo, 10", "ID_6673", "91135-7738", "True")
admin1._register_new_user(register_new_user1)  
admin1.save_to_database()

###### USER ######
user = User("ID", "Maria Lice", "senha(protegido)", 25, "alice@example.com", "Rua brasil, 01", "ID_3453", "11225-1234","False")
user1 = User("ID", "Iris", "senha(protegido)", 18, "iris@example.com", "Rua piaui, 200", "ID_4153", "11385-1234","True")
user2 = User("ID", "Lavinia", "senha(protegido)", 45, "lavnia@example.com", "Rua piaui, ", "ID_8453", "21885-1234","True")
user3 = User("ID", "Ines", "senha(protegido)", 65, "ines@example.com", "Rua araguaia, 30", "ID_8453", "31885-9975","False")
user4 = User("ID", "Maria Lice", "senha(protegido)", 17, "joao@example.com", "Rua sergipe, 100", "ID_8456", "11885-888","True")
user.save_to_db()
user1.save_to_db()
user2.save_to_db()
user3.save_to_db()
user4.save_to_db()

# ###### BOOKS ######
# # Criar um livro digital e salvar no banco de dados
digital_book = DigitalBook("40-0-430-21064-3", 'O Ateneu', 'Raul Pompeia', 1888, 3, 250, 200, '150mb', 'PDF')
digital_book2 = DigitalBook("13-1-637-91034-1", 'Anjos e Demonios', 'Carl Sagan', 1996, 2, 250, 270, '350mb', 'ePUB')
digital_book.save_to_db()
digital_book2.save_to_db()

# Criar um livro físico e salvar no banco de dados
physical_book = PhysicalBook("21-9-430-21033-1", "Kindred", "Octavia Butler", 1999, 1, 10, 200, 'Capa dura', 500)
physical_book.save_to_db()

# Atualizar o livro digital
digital_book.title = 'O Ateneu - Edição Especial'
digital_book.save_to_db()

# Atualizar o livro físico
physical_book.weight = 600
physical_book.save_to_db()

# ###### BORROW ######
# Realizar empréstimo
borrow = Borrow('RESERVADO', '2024-05-25', '2024-06-25',  user1.id_user,  physical_book.title)
borrow.reserve_book(physical_book)
borrow.save_to_db()

borrow2 = Borrow('RESERVADO', '2024-02-30', '2024-05-10',  user2.id_user,  digital_book2.title)
borrow2.reserve_book(digital_book2)
borrow2.save_to_db()

# Verifica se o livro está disponivel
borrow.check_available(digital_book)

########## Métodos que podem ser utilizados em qlqr tabela ##########
# DROP
# drop_table('User')
# DELETE TABLE
# delete_table('Borrow')
# DELETE ROW
#delete_row('User', 'id = 38')
# UPDATE
# update_row('User', {'address': 'Rua da Consolação, 2340', 'id_user': 'ID_7783'}, 'id = 16')
# delete_table('Admin')
# delete_table('Employee')
# delete_table('User')
# delete_table('Borrow')
# delete_table('Book')
# delete_table('PhysicalBook')
# delete_table('DigitalBook')
# delete_table('PhysicalBook')
# delete_table('DigitalBook')
# drop_table('Employee')

######################## MELHORIAS #################### :/
# Devolver o livro
# AJUSTAR
# borrow2.returned_book(physical_book)
# Salva os dados do administrador e do usuário no banco de dados
### checar
#admin._remove_user(admin_new_user)
