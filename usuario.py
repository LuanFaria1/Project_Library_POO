import sqlite3
from datetime import datetime

class Usuario:
    def __init__(self, nome, cpf, telefone, email, data_nascimento, login, senha):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.data_nascimento = data_nascimento
        self.data_emprestimo = None
        self.data_devolucao = None
        self.login = login
        self.senha = senha
        self.pendencias = []

    def efetuar_login(self, login, senha):
        if self.login == login and self.senha == senha:
            print("Login realizado com sucesso.")
            return True
        else:
            print("Login ou senha incorretos.")
            return False

    def efetuar_cadastro(self):
        print(f"Usuário {self.nome} cadastrado com sucesso.")

    def emprestimo(self, livro):
        self.data_emprestimo = datetime.now()
        self.data_devolucao = self.data_emprestimo + timedelta(days=14)
        print(f"Livro '{livro.titulo}' emprestado até {self.data_devolucao.strftime('%Y-%m-%d')}.")

    def adicionar_remover_livros(self, livro, acao):
        if acao == "adicionar":
            print(f"Livro '{livro.titulo}' adicionado ao catálogo.")
        elif acao == "remover":
            print(f"Livro '{livro.titulo}' removido do catálogo.")

    def deletar_conta(self):
        print(f"Conta do usuário {self.nome} deletada.")
