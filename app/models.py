class Produto:
    def __init__(self, nome, categoria, preco, foto, descricao):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.foto = foto
        self.descricao = descricao

class Usuario:
    def __init__(self, nome, username, senha, email):
        self.nome = nome
        self.username = username
        self.senha = senha
        self.email = email