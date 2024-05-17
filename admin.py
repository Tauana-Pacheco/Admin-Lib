from person import Person
from user import User
from books import Book
class Role:
    def __init__(self, role, permissions):
        self.role = role
        self.permissions = permissions

    def __str__(self):
        return self.role

    @classmethod
    def from_predefined(cls, role_name):
        predefined_roles = {
            "all_library_employee": ["ver_quantidade_livros", "ver_status_emprestimo", "ver_quantidade_usuarios"],
            "Administrador": ["emprestar_livros", "cadastrar_usuarios", "remover_usuarios"],
            "Catalogador": ["adicionar_livros", "remover_livros"],
        }

        permissions = predefined_roles[role_name]
        return cls(role_name, permissions)

class Employee(Person):
    def __init__(self, user_name, _password, age, email, address, contact, employee_id, role):
        super().__init__(user_name, _password, age, email, address, contact)
        self.employee_id = employee_id
        self.role = Role.from_predefined("all_library_employee")

        if isinstance(role, Role):
            self.role = role
        else:
            raise ValueError("role must be an instance of Role class")
    
    # Função do funcionário
    def description(self):
        return f"Funcionário: {self.user_name} - ID: {self.employee_id} - Função: {self.role}"

    # Permissão do funcionário
    def have_permission(self, permission):
        return permission in self.role.permissions
    
    # todos os funcionários podem fazer ações de "ver_quantidade_livros", "ver_status_emprestimo", "ver_quantidade_usuarios
    def permissions_generic(self):
        general_permissions = {"ver_quantidade_livros", "ver_status_emprestimo", "ver_quantidade_usuarios"}
        if any(permission in self.role.permissions for permission in general_permissions):
            return "Você tem as permissões gerais no sistema"
        else:
            return "Você não está com as credenciais iniciais"
        
    # Cadastra novo usuário
    def register_new_user(self, user):
        if self.have_permission('cadastrar_usuarios'):
            if isinstance(user, User):
                self.id_user.append(user)
                print(f"Usuário '{user.user_name}' foi adicionado ao sistema.")
            else:
                raise ValueError("O objeto passado não é uma instância de User.")
        else:
            raise ValueError("Você não tem permissão para adicionar usuários.")

    # remove usuario do sistema   
    def remove_user(self, user_name):
        if self.have_permission('remover_usuarios'):
            user_found = None
            for user in self.id_user:
                if user.user_name == user_name:
                    user_found = user
                    break
            
            if user_found:
                self.id_user.remove(user_found)
                print(f"Usuário '{user_name}' foi removido do sistema.")
            else:
                print(f"O usuário '{user_name}' não existe no sistema.")
        else:
            raise ValueError("Você não tem permissão para remover usuários")

    def emprestar_livros(self, books):
        if self.have_permission("emprestar_livros"):
            if books.num_of_copies > 0:
                books.num_of_copies -= 1
                return f"{books.title} foi emprestado para {self.user_name}"
            else:
                return f"Não há cópias disponíveis de {books.title} para empréstimo"
        else:
            return "Você não tem permissão para emprestar livros"

# Criar instâncias de Role
admin_role = Role.from_predefined("Administrador")
cataloger_role = Role.from_predefined("Catalogador")

livro = Book(id=1, title="Dom Quixote", author="Miguel de Cervantes", year_of_publication=1605, num_of_editions=1, num_of_copies=10)
print(livro.num_of_copies)

# Criar instâncias de Employee
employee1 = Employee('Van', 's12345', 22, 'van@gmail.com', 'Rua Pindaíba, 33', '11874259631', 'V2343', admin_role)
employee2 = Employee('John', 'pass123', 30, 'john@example.com', '123 Main Street', '555-1234', 'J5678', cataloger_role)

# Descrição do funcionário
print(employee1.description())
print(employee2.description())

# Verificar permissões genéricas
print(employee1.permissions_generic())
print(employee2.permissions_generic())

# Empresta o livro
print(employee1.emprestar_livros(livro))

# Cria instância de Employee
employee = Employee("admin", "senha123", 30, "admin@example.com", "Endereço do Admin", "123456789", "EMP001", admin_role)

# Adiciona usuários à lista id_user
user1 = User("user1", "senha123", 25, "user1@example.com", "Endereço do User1", "987654321", "USR001", ativo=True)
user2 = User("user2", "senha456", 28, "user2@example.com", "Endereço do User2", "654387987", "USR002", ativo=True)
employee.id_user.extend([user1, user2])

# Remove usuário específico
employee.remove_user("user1")

# Adiciona novo usuário
new_user = User("novousuario", "novasenha", 25, "novousuario@example.com", "Endereço do Novo Usuário", "987654321", "USR003", ativo=True)
employee.register_new_user(new_user)

