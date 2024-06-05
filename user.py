from db import create_connection, close_connection
from sqlite3 import Error

class User:
    def __init__(self, user_name, _password, age, email, address, id_user, contact, ativo):
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
                "INSERT INTO User (name, password, age, email, address, id_user, contact, ativo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (self.user_name, self._password, self.age, self.email, self.address, self.id_user, self.contact, self.ativo)
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
                print(f"Usuário com id {self.id_user} removido do banco de dados.")
            except Error as e:
                print(f"Erro ao remover usuário do banco de dados: {e}")
            finally:
                cursor.close()
                close_connection(connection)

    def update_info(self, new_user_name=None, new_password=None, new_age=None, new_email=None, new_address=None,
                    new_id_user=None, new_contact=None, new_status=None):
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
        if new_id_user:
            self.id_user = new_id_user
        if new_contact:
            self.contact = new_contact
        if new_status is not None:
            self.ativo = new_status

        # Update the database
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute('''UPDATE User SET name=?, password=?, age=?, email=?, address=?, id_user=?, contact=?, ativo=? WHERE id_user=?''',
                            (self.user_name, self._password, self.age, self.email, self.address, self.id_user, self.contact, self.ativo))
            connection.commit()
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
        if new_status is not None:
            self.ativo = new_status
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute('''UPDATE User SET name=?, password=?, age=?, email=?, address=?, contact=?, ativo=? WHERE id_user=?''',
                            (self.user_name, self._password, self.age, self.email, self.address, self.contact, self.id_user, self.ativo))
            connection.commit()
            cursor.close()
            close_connection(connection)

    def login(self, user_name, password):
       connection = create_connection()
       if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT password FROM User WHERE name = ?", (user_name,))
            result = cursor.fetchone()

            if result:
                stored_password = result[0]
                if password == stored_password:
                    print("Login bem-sucedido.")
                    cursor.close()
                    close_connection(connection)
                    return True
                else:
                    print("Usuário ou senha incorretos. Tente novamente.")
                    cursor.close()
                    close_connection(connection)
                    return False
            else:
                print("Usuário não encontrado. Tente novamente.")
                cursor.close()
                close_connection(connection)
                return False

    def reserve_book(self, borrow_instance, book):
        borrow_instance.reserve_book(book)

    def check_available(self, borrow_instance, book):
        borrow_instance.check_available(book)

    def returned_book(self, borrow_instance, returned_books):
        borrow_instance.returned_book(returned_books)
