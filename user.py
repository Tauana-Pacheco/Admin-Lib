from db import create_connection, close_connection
from sqlite3 import Error

class User:
    def __init__(self, id, user_name, _password, age, email, address, id_user, contact, ativo):
        self.id = id
        self.user_name = user_name
        self._password = _password
        self.age = age
        self.email = email
        self.address = address
        self.id_user = id_user
        self.contact = contact
        self.ativo = ativo
        self.loans = []
        self.users = []

    def save_to_db(self):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO User (name, age, email, address, id_user, contact, ativo) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (self.user_name,  self.age, self.email, self.address, self.id_user, self.contact, self.ativo)
            )
            connection.commit()
            cursor.close()
            close_connection(connection)
            print(f"Usuário {self.user_name} salvo no banco de dados.")

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

    def register(self, users):
        self.users.append(users)
    
    def remove_user(self):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                sql_command_remove = "DELETE FROM User WHERE id_user = ?"
                cursor.execute(sql_command_remove, (self.id_user,))
                connection.commit()
                print(f"Usuário com ID {self.id_user} removido do banco de dados.")
            except Error as e:
                print(f"Erro ao remover usuário do banco de dados: {e}")
            finally:
                cursor.close()
                close_connection(connection)


    @staticmethod
    def remove_user_from_list(users, user):
        if user in users:
            users.remove(user)
            print(f"Usuário {user.user_name} removido da lista.")
        else:
            print(f"Usuário {user.user_name} não encontrado na lista.")

    def update_info(self, new_user_name=None, new_password=None, new_age=None, new_email=None, new_address=None, new_contact=None, new_id_user=None, new_status=None):
        if new_user_name:
            self.user_name = new_user_name
        if new_password:
            self._password = new_password
        if new_age is not None:
            self.age = new_age
        if new_email:
            self.email = new_email
        if new_address:
            self.address = new_address
        if new_contact:
            self.contact = new_contact
        if new_id_user is not None:
            self.id_user = new_id_user
        if new_status is not None:
            self.ativo = new_status
        print(f"Informações do usuário {self.user_name} atualizadas com sucesso.")

    def login(self, user_name, password):
        if user_name == self.user_name and password == self._password:
            print("Login bem-sucedido.")
            return True
        else:
            print("Usuário ou senha incorretos. Tente novamente.")
            return False

    def reserve_book(self, borrow_instance, book):
        borrow_instance.reserve_book(book)

    def check_available(self, borrow_instance, book):
        borrow_instance.check_available(book)

    def returned_book(self, borrow_instance, returned_books):
        borrow_instance.returned_book(returned_books)


def main():
    while True:
        print("\n1. Criar usuário\n2. Atualizar usuário\n3. Login\n4. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            id = input("ID: ")
            user_name = input("Nome de usuário: ")
            password = input("Senha: ")
            age = int(input("Idade: "))
            email = input("Email: ")
            address = input("Endereço: ")
            id_user = input("ID do usuário: ")
            contact = input("Contato: ")
            ativo = input("Ativo (1 para sim, 0 para não): ")

            user = User(id, user_name, password, age, email, address, id_user, contact, ativo)
            user.save_to_db()

        elif choice == '2':
            id = input("ID do usuário a ser atualizado: ")
            user_name = input("Novo nome de usuário (deixe em branco para não alterar): ")
            password = input("Nova senha (deixe em branco para não alterar): ")
            age = input("Nova idade (deixe em branco para não alterar): ")
            email = input("Novo email (deixe em branco para não alterar): ")
            address = input("Novo endereço (deixe em branco para não alterar): ")
            id_user = input("Novo ID do usuário (deixe em branco para não alterar): ")
            contact = input("Novo contato (deixe em branco para não alterar): ")
            ativo = input("Novo status (1 para sim, 0 para não, deixe em branco para não alterar): ")

            user = User(id, user_name, password, int(age) if age else None, email, address, id_user, contact, int(ativo) if ativo else None)
            user.update_info(new_user_name=user_name, new_password=password, new_age=int(age) if age else None,
                             new_email=email, new_address=address, new_contact=contact,
                             new_id_user=id_user if id_user else None, new_status=int(ativo) if ativo else None)
        
        elif choice == '3':
            user_name = input("Nome de usuário: ")
            password = input("Senha: ")
            
            user = User(None, user_name, password, None, None, None, None, None, None)
            user.login(user_name, password)
        
        elif choice == '4':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
