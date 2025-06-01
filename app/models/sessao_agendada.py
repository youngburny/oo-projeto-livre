# sessao.py (o seu ficheiro, modificado)

import datetime

# Importamos as nossas novas classes de serviço
from app.models.servicos.servico import Servico
from app.models.servicos.servico_gravacao import ServicoGravacao
from app.models.servicos.servico_mixagem import ServicoMixagem

class SessaoAgendada:
    """
    Representa uma sessão agendada.
    Agora demonstra COMPOSIÇÃO com um objeto Servico polimórfico.
    """
    def __init__(self, nome_cliente, email_cliente, servico_obj: Servico, 
                 data_sessao, hora_inicio, duracao_horas, observacoes=None):
        
        # O atributo `tipo_servico` foi substituído por `servico` que é um objeto
        if not isinstance(servico_obj, Servico):
            raise TypeError("servico_obj deve ser uma instância de uma subclasse de Servico.")

        self.id_sessao = self._gerar_id_sessao()
        self.nome_cliente = nome_cliente
        self.email_cliente = email_cliente
        self.servico = servico_obj # Composição: A sessão TEM UM serviço
        self.data_sessao = data_sessao
        self.hora_inicio = hora_inicio
        self.duracao_horas = duracao_horas
        self.observacoes = observacoes
        self.data_agendamento = datetime.datetime.now()

    def _gerar_id_sessao(self):
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")

    def calcular_custo_total(self):
        """
        Delega o cálculo do custo para o objeto de serviço.
        Esta é a chamada polimórfica! Não precisamos saber qual é o tipo de serviço.
        """
        return self.servico.calcular_custo(self.duracao_horas)

    def __str__(self):
        # Agora usamos o objeto `servico` para obter o nome
        return (f"Sessão (ID: {self.id_sessao}) | "
                f"Cliente: {self.nome_cliente} | "
                f"Serviço: {self.servico.nome}")