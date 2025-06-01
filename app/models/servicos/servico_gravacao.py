from app.models.servicos.servico import Servico

class ServicoGravacao(Servico):
    """Serviço de Gravação. O custo pode incluir um extra por canal."""
    def __init__(self, numero_canais):
        super().__init__(nome="Gravação", valor_base_hora=100)
        self.numero_canais = numero_canais
        self.taxa_por_canal = 10

    def calcular_custo(self, duracao_horas):
        custo_base = self.valor_base_hora * duracao_horas
        custo_extra_canais = self.numero_canais * self.taxa_por_canal
        print(f"Debug (Gravação): Custo base ({custo_base}) + Extra canais ({custo_extra_canais})")
        return custo_base + custo_extra_canais