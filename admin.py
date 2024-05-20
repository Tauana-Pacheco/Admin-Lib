
from user import User
from employee import Employee

class Adm(Employee):
    def __init__(self, user_name, _password, age, email, address, contact, employee_id):
        super().__init__(user_name, _password, age, email, address, contact)
        self.employee_id = employee_id
        self.user = []

    # Cadastra novo usuário
    def register_new_user(self, user):
        self.user.append(user)
        print(f"Usuário '{user.user_name}' registrado na biblioteca.")   
    
    # remove usuario do sistema   
    def remove_user(self, user):
        if len(self.user) == 0:
            print(f"Erro: Não há usuários registrados no sistema.")
            return
        
        user_to_remove = None
        for user in self.user:
            if user.user_name == user.user_name:
                user_to_remove = user
                break
        
        if user_to_remove:
            self.user.remove(user_to_remove)
            print(f"Usuário '{user.user_name}' foi removido do sistema.")
        else:
            print(f"Erro: Usuário '{user.user_name}' não encontrado no sistema.")

# # Criar instâncias de adm
adm = Adm('Van', 's12345', 22, 'van@gmail.com', 'Rua Pindaíba, 33', '11874259631', 'V2343')

# # Adiciona novo usuário
new_user = User("novousuario", "novasenha", 25, "novousuario@example.com", "Endereço do Novo Usuário", "987654321", "USR003", ativo=True)
adm.register_new_user(new_user)

# Remove usuário
adm.remove_user(new_user) 
                                                                                                                              

