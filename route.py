# Imports do Bottle e do seu Controller
from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file, template, redirect

# --- IMPORTS ATUALIZADOS ---
# Importamos a SessaoAgendada e também as nossas novas classes de serviço
from app.models.sessao_agendada import SessaoAgendada
# Supondo que você criou o pacote de serviços como discutimos:
from app.models.servicos.servico_gravacao import ServicoGravacao
from app.models.servicos.servico_mixagem import ServicoMixagem

import datetime


app = Bottle()
ctl = Application()


#-----------------------------------------------------------------------------
# Rotas estáticas (sem alterações)

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/helper')
def helper(info= None):
    return ctl.render('helper')

#-----------------------------------------------------------------------------
# LÓGICA PRINCIPAL

# --- A "FÁBRICA" DE SERVIÇOS ---
# Esta função é crucial. Ela traduz os dados do formulário HTML
# para os nossos objetos Python polimórficos.
def criar_servico_de_formulario(form_data):
    """Cria uma instância da subclasse de Servico apropriada."""
    tipo_servico = form_data.get('tipo_servico')

    if tipo_servico == 'gravacao':
        canais = int(form_data.get('numero_canais', 1))
        return ServicoGravacao(numero_canais=canais)
    
    elif tipo_servico == 'mixagem':
        faixas = int(form_data.get('numero_faixas', 8))
        return ServicoMixagem(numero_faixas=faixas)
    
    else:
        raise ValueError(f"Tipo de serviço desconhecido ou não implementado: '{tipo_servico}'")


@app.route('/pagina', method=['GET'])
@app.route('/pagina/{parameter}', method=['GET'])
def acao_pagina(parameter=None):
    if not parameter:
        return ctl.render('pagina')

# Rota para exibir o formulário de agendamento (GET)
@app.route('/agendar', method=['GET'])
def exibir_formulario_agendamento():
    """Renderiza o template HTML do formulário de agendamento."""
    return ctl.render('agendar')


# --- ROTA DE AGENDAMENTO (POST) - COMPLETAMENTE ATUALIZADA ---
# ROTA POST ATUALIZADA PARA SER MAIS SIMPLES
@app.route('/agendar', method=['POST'])
def processar_agendamento():
    try:
        # A criação dos objetos continua igual, pois você ainda pode querer
        # salvar esta informação no futuro.
        servico_obj = criar_servico_de_formulario(request.forms)
        data_sessao = datetime.date.fromisoformat(request.forms.get('data_sessao'))
        hora_inicio = datetime.time.fromisoformat(request.forms.get('hora_inicio'))
        duracao_horas = int(request.forms.get('duracao_horas'))
        
        nova_sessao = SessaoAgendada(
            nome_cliente=request.forms.get('nome_cliente'),
            email_cliente=request.forms.get('email_cliente'),
            servico_obj=servico_obj,
            data_sessao=data_sessao,
            hora_inicio=hora_inicio,
            duracao_horas=duracao_horas,
            observacoes=request.forms.get('observacoes')
        )

        # O cálculo do custo foi removido, pois não será mais exibido.
        # A lógica para salvar 'nova_sessao' num banco de dados viria aqui.
        print(f"Sessão para {nova_sessao.nome_cliente} criada com sucesso. Redirecionando...")

        # AÇÃO FINAL: Redirecionar para a página de sucesso estática.
        return redirect('/agendamento_sucesso')

    except (ValueError, TypeError) as e:
        print(f"Erro ao processar agendamento: {e}")
        return template('app/views/html/erro', mensagem_erro=str(e))


# ROTA GET PARA A PÁGINA DE SUCESSO ESTÁTICA
# Adicionamos esta rota de volta.
@app.route('/agendamento_sucesso')
def sucesso():
    """Apenas renderiza a página de confirmação estática."""
    return ctl.render('agendamento_sucesso')


if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080, debug=True, reloader=True)