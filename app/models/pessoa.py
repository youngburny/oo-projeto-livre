class Pessoa():
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Pessoa(nome={self.nome}, idade={self.idade})'

    def __repr__(self):
        return f'Pessoa(nome={self.nome!r}, idade={self.idade!r})'
    