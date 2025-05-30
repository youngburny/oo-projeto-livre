# package/models.py

import datetime

class SessaoAgendada:
    """
    Representa uma sessão agendada no Sonar Studio.

    Atributos:
        id_sessao (str): Identificador único para a sessão (pode ser gerado automaticamente).
        nome_cliente (str): Nome completo do cliente.
        email_cliente (str): Endereço de e-mail do cliente.
        telefone_cliente (str): Número de telefone do cliente (opcional).
        tipo_servico (str): Tipo de serviço agendado (ex: 'gravacao', 'mixagem').
        data_sessao (datetime.date): Data da sessão.
        hora_inicio (datetime.time): Hora de início da sessão.
        duracao_horas (int): Duração estimada da sessão em horas.
        observacoes (str): Quaisquer observações ou detalhes adicionais do cliente (opcional).
        data_agendamento (datetime.datetime): Data e hora em que a sessão foi agendada.
    """

    def __init__(self, nome_cliente, email_cliente, tipo_servico, data_sessao, hora_inicio,
                 duracao_horas, telefone_cliente=None, observacoes=None):
        self.id_sessao = self._gerar_id_sessao() # Método para gerar um ID único
        self.nome_cliente = nome_cliente
        self.email_cliente = email_cliente
        self.telefone_cliente = telefone_cliente
        self.tipo_servico = tipo_servico
        self.data_sessao = data_sessao
        self.hora_inicio = hora_inicio
        self.duracao_horas = duracao_horas
        self.observacoes = observacoes
        self.data_agendamento = datetime.datetime.now()

    def _gerar_id_sessao(self):
        """Método auxiliar para gerar um ID único para a sessão.
           Em um projeto real, isso seria mais robusto (ex: UUID).
        """
        # Para fins de exemplo, um ID simples baseado em timestamp
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")

    def __str__(self):
        """Representação em string do objeto SessaoAgendada."""
        return (f"Sessão Agendada (ID: {self.id_sessao})\n"
                f"Cliente: {self.nome_cliente} ({self.email_cliente})\n"
                f"Serviço: {self.tipo_servico}\n"
                f"Data/Hora: {self.data_sessao.strftime('%d/%m/%Y')} às {self.hora_inicio.strftime('%H:%M')}\n"
                f"Duração: {self.duracao_horas} horas")

    def to_dict(self):
        """Converte o objeto SessaoAgendada para um dicionário, útil para serialização."""
        return {
            "id_sessao": self.id_sessao,
            "nome_cliente": self.nome_cliente,
            "email_cliente": self.email_cliente,
            "telefone_cliente": self.telefone_cliente,
            "tipo_servico": self.tipo_servico,
            "data_sessao": self.data_sessao.isoformat(), # Converte para string ISO 8601
            "hora_inicio": self.hora_inicio.isoformat(), # Converte para string ISO 8601
            "duracao_horas": self.duracao_horas,
            "observacoes": self.observacoes,
            "data_agendamento": self.data_agendamento.isoformat()
        }

    @staticmethod
    def from_dict(data_dict):
        """Cria um objeto SessaoAgendada a partir de um dicionário, útil para deserialização."""
        return SessaoAgendada(
            nome_cliente=data_dict["nome_cliente"],
            email_cliente=data_dict["email_cliente"],
            telefone_cliente=data_dict.get("telefone_cliente"), # Usar .get para opcionais
            tipo_servico=data_dict["tipo_servico"],
            data_sessao=datetime.date.fromisoformat(data_dict["data_sessao"]),
            hora_inicio=datetime.time.fromisoformat(data_dict["hora_inicio"]),
            duracao_horas=data_dict["duracao_horas"],
            observacoes=data_dict.get("observacoes")
        )