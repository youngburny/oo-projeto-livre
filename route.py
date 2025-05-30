from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response

from app.models.sessao_agendada import SessaoAgendada


app = Bottle()
ctl = Application()


#-----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/helper')
def helper(info= None):
    return ctl.render('helper')


#-----------------------------------------------------------------------------
# Suas rotas aqui:

@app.route('/pagina', method=['GET'])
@app.route('/pagina/{parameter}', method=['GET'])
def acao_pagina(parameter=None):
    if not parameter:
        return ctl.render('pagina')
    else:
        return ctl.render('pagina',parameter)
    
# Rota para exibir o formulário de agendamento (GET)
@app.route('/agendar', method=['GET'])
def exibir_formulario_agendamento():
    """
    Renderiza o template HTML do formulário de agendamento.
    """
    print("Exibindo formulário de agendamento.")
    return ctl.render('agendar') # Renderiza agendar.tpl

# Rota para processar a submissão do formulário de agendamento (POST)
@app.route('/agendar', method=['POST'])
def processar_agendamento():
    """
    Recebe os dados do formulário de agendamento, cria um objeto SessaoAgendada
    e simula o armazenamento.
    """
    # Coletar dados do formulário usando request.forms
    # É importante usar os 'name' dos inputs do HTML
    nome_cliente = request.forms.get('nome_cliente')
    email_cliente = request.forms.get('email_cliente')
    telefone_cliente = request.forms.get('telefone_cliente')
    tipo_servico = request.forms.get('tipo_servico')
    data_sessao_str = request.forms.get('data_sessao')
    hora_inicio_str = request.forms.get('hora_inicio')
    duracao_horas_str = request.forms.get('duracao_horas')
    observacoes = request.forms.get('observacoes')

    # Validação básica e conversão de tipos
    try:
        # Converter string de data e hora para objetos datetime
        import datetime
        data_sessao = datetime.date.fromisoformat(data_sessao_str)
        hora_inicio = datetime.time.fromisoformat(hora_inicio_str)
        duracao_horas = int(duracao_horas_str)
    except (ValueError, TypeError) as e:
        print(f"Erro ao converter dados do formulário: {e}")
        return "Dados inválidos no formulário. Por favor, verifique." # Ou renderize uma página de erro

    # Criar um objeto SessaoAgendada
    nova_sessao = SessaoAgendada(
        nome_cliente=nome_cliente,
        email_cliente=email_cliente,
        telefone_cliente=telefone_cliente,
        tipo_servico=tipo_servico,
        data_sessao=data_sessao,
        hora_inicio=hora_inicio,
        duracao_horas=duracao_horas,
        observacoes=observacoes
    )

    print("\n--- Nova Sessão Agendada ---")
    print(nova_sessao) # Usa o método __str__ da classe
    print("--- Dados serializados para dicionário ---")
    print(nova_sessao.to_dict()) # Mostra como seria para serializar

    # *** Aqui você adicionaria a lógica para salvar a sessão no "banco de dados" ***
    # Por exemplo:
    # from package.data_manager import DataManager
    # DataManager.salvar_sessao(nova_sessao.to_dict()) # Assumindo um DataManager

    # Por enquanto, apenas redirecionamos para uma página de sucesso
    return redirect('/agendamento_sucesso')

# Rota para a página de sucesso do agendamento
@app.route('/agendamento_sucesso', method=['GET'])
def agendamento_sucesso():
    """
    Exibe uma mensagem de sucesso após o agendamento.
    """
    return "<h1>Sessão Agendada com Sucesso!</h1><p>Em breve entraremos em contato.</p><p><a href='/pagina'>Voltar para Home</a></p>"

#-----------------------------------------------------------------------------


if __name__ == '__main__':

    run(app, host='0.0.0.0', port=8080, debug=True, reloader=True)
