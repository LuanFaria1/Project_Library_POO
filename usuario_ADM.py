from Usuario import Usuario

class UsuarioADM(Usuario):
    def __init__(self, nome, cpf, telefone, email, data_nascimento, login, senha):
        super().__init__(nome, cpf, telefone, email, data_nascimento, login, senha)

    def adicionar_livro(self, livro, biblioteca):
        biblioteca.adicionar_livros(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def remover_livro(self, livro, biblioteca):
        biblioteca.remover_livros(livro)
        print(f"Livro '{livro.titulo}' removido da biblioteca.")

    def adicionar_usuario(self, usuario, biblioteca):
        biblioteca.registrar_usuario(usuario)
        print(f"Usuário '{usuario.nome}' adicionado à biblioteca.")

    def remover_usuario(self, usuario, biblioteca):
        biblioteca.remover_usuario(usuario)
        print(f"Usuário '{usuario.nome}' removido da biblioteca.")
