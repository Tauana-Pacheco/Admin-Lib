class Role:
    def __init__(self, role, permissions):
        self.role = role
        self.permissions = permissions

general_permissions = ["ver_quantidade_livros", "ver_status_emprestimo", "ver_quantidade_usuarios"]
user_permissions = [general_permissions,'pegar_livros']
recepcionist_permissions = [general_permissions, 'emprestar_livros', 'cadastrar_usuarios', 'remover_usuarios']
cataloger_permissions = [general_permissions, 'adicionar_livros', 'remover_livros', 'contatar_editora', 'contatar_autores', ]
admin_permissions = [general_permissions, recepcionist_permissions, cataloger_permissions, "demitir_funcionario", "contratar_funcionario"]

all_library_employee = Role("Funcionários da biblioteca", general_permissions)
user_role = Role('Usuário', user_permissions)
recepcionist_role = Role('Recepcionista', recepcionist_permissions)
cataloger_role = Role('Catalogador', cataloger_permissions)
admin_role = Role("Admin", admin_permissions)
