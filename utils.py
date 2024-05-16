import random

#repassar dps
class Utils():
    
   # registar Usuários
    @staticmethod
    def register_users(user_name, password, address, date_of_birth, instance):
     if user_name and password:
        instance.user_name = user_name
        instance._password = password
        instance._address = address
        instance._date_of_birth = date_of_birth
        instance.user_id = random.randint(1000, 9999)

        print("Registrado com sucesso!")
     else:
        print("Ops, o registro falhou!")
   
   #remover Usuários
    @staticmethod
    def remove_users(user, users):
        if user in users:
            users.remove(user)
            print(f"Usuário '{user.user_name}' excluído com sucesso.")
        else:
            print("Usuário não encontrado.")
    
    # adicionar Funcionários
    # remover Funcionários
    
        
   
