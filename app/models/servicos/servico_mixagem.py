from app.models.servicos.servico import Servico

class ServicoMixagem(Servico):
    """Serviço de Mixagem. O custo pode variar com o número de faixas."""
    def __init__(self, numero_faixas):
        super().__init__(nome="Mixagem", valor_base_hora=120)
        self.numero_faixas = numero_faixas

    def calcular_custo(self, duracao_horas):
        custo_base = self.valor_base_hora * duracao_horas
        # Lógica de exemplo: bónus se a mixagem for longa e tiver muitas faixas
        bonus_complexidade = 0
        if duracao_horas > 4 and self.numero_faixas > 24:
            bonus_complexidade = 150
        
        print(f"Debug (Mixagem): Custo base ({custo_base}) + Bónus complexidade ({bonus_complexidade})")
        return custo_base + bonus_complexidade