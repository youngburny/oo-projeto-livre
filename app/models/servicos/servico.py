from abc import ABC, abstractmethod

class Servico(ABC):
    """
    Classe base Abstrata para todos os serviços oferecidos.
    Define a interface comum que todos os serviços devem ter.
    """
    def __init__(self, nome, valor_base_hora):
        self.nome = nome
        self.valor_base_hora = valor_base_hora

    @abstractmethod
    def calcular_custo(self, duracao_horas):
        """
        Método abstrato para calcular o custo.
        Cada subclasse DEVE implementar a sua própria lógica.
        """
        pass

    def __str__(self):
        return self.nome