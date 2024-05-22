
from sqlite3 import Error
from db import create_connection, close_connection
from user import User
from employee import Employee

class Adm(Employee):
    def __init__(self, name, _password, _age, _email, _address, _contact, id_admin):
        super().__init__(name, _password, _age, _email, _address, _contact, "Administradora")
        self.id_admin = id_admin
        self.user = []

    def _register_new_user(self, user):
        self.user.append(user)
        print(f"Usuário '{user.user_name}' registrado na biblioteca.")   
    
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

    def save_to_database(self):
        super().save_to_db()
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO Admin (id_admin) VALUES (?)", (self.id_admin,))
                
                for user in self.user:
                    cursor.execute("INSERT INTO User (name, age, email, address, id_user, contact, ativo) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                                (user.user_name, user.age, user.email, user.address, user.id_user, user.contact, user.ativo))
                    
                connection.commit()  
                print("Dados do administrador e dos usuários foram salvos no banco de dados.")
            except Error as e:
                print(f"Erro ao salvar dados no banco de dados: {e}")
            finally:
                cursor.close()
                close_connection(connection)

                                                                                                                              

