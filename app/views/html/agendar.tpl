<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Sonar Studio - Agendar Sessão</title>
    <link rel="stylesheet" href="/static/css/pagina.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
</head>
<body>
    <header>
        <h1><i class="fas fa-headphones-alt"></i> Sonar Studio</h1>
        <nav>
            <a href="/">Home</a>
            <a href="#">About</a>
            <a href="#">Portfolio</a>
            <a href="#">Contact</a>
            <a href="/agendar" class="active">Agendar Sessão</a>
        </nav>
    </header>

    <main class="agendamento">
        <h2><i class="fas fa-calendar-alt"></i> Agende Sua Sessão</h2>
        
        <form action="/agendar" method="POST">
            
            <div class="form-group">
                <label for="nome_cliente">Seu Nome Completo:</label>
                <input type="text" id="nome_cliente" name="nome_cliente" required />
            </div>

            <div class="form-group">
                <label for="email_cliente">Seu E-mail:</label>
                <input type="email" id="email_cliente" name="email_cliente" required />
            </div>
            
            <div class="form-group">
                <label for="tipo_servico">Tipo de Serviço:</label>
                <select id="tipo_servico" name="tipo_servico" required>
                    <option value="">Selecione um serviço para ver as opções</option>
                    <option value="gravacao">Gravação</option>
                    <option value="mixagem">Mixagem</option>
                    <option value="masterizacao">Masterização</option>
                </select>
            </div>
            
            <div id="detalhes_gravacao" class="detalhes-servico">
                <div class="form-group">
                    <label for="numero_canais"><i class="fas fa-microphone-alt"></i> Número de Canais (Gravação):</label>
                    <input type="number" id="numero_canais" name="numero_canais" min="1" value="4" />
                </div>
            </div>

            <div id="detalhes_mixagem" class="detalhes-servico">
                <div class="form-group">
                    <label for="numero_faixas"><i class="fas fa-sliders-h"></i> Número de Faixas (Mixagem):</label>
                    <input type="number" id="numero_faixas" name="numero_faixas" min="1" value="16" />
                </div>
            </div>
            
            <div class="form-group">
                <label for="data_sessao">Data da Sessão:</label>
                <input type="date" id="data_sessao" name="data_sessao" required />
            </div>

            <div class="form-group">
                <label for="hora_inicio">Hora de Início:</label>
                <input type="time" id="hora_inicio" name="hora_inicio" required />
            </div>

            <div class="form-group">
                <label for="duracao_horas">Duração Estimada (horas):</label>
                <input type="number" id="duracao_horas" name="duracao_horas" min="1" max="12" value="2" required />
            </div>

            <div class="form-actions">
                <button type="submit">Agendar Sessão</button>
            </div>
        </form>
    </main>

    <footer>
        <p>&copy; 2025 Sonar Studio - All rights reserved.</p>
    </footer>

    <script>
    document.addEventListener('DOMContentLoaded', function() {
        
        // Pega as referências dos elementos HTML que vamos manipular
        const tipoServicoSelect = document.getElementById('tipo_servico');
        const detalhesGravacao = document.getElementById('detalhes_gravacao');
        const detalhesMixagem = document.getElementById('detalhes_mixagem');
        // Se você tiver o de masterização, descomente a linha abaixo:
        // const detalhesMasterizacao = document.getElementById('detalhes_masterizacao');

        // Função que é executada toda vez que o menu de serviço muda
        function atualizarFormulario() {
            
            // --> PASSO 1: A PARTE MAIS IMPORTANTE E QUE PROVAVELMENTE ESTÁ ERRADA NO SEU CÓDIGO ATUAL <--
            // Antes de mostrar qualquer coisa, garantimos que TODAS as seções de detalhes
            // estão escondidas. Isso "limpa" o formulário a cada mudança.
            detalhesGravacao.classList.remove('visible');
            detalhesMixagem.classList.remove('visible');
            // Se tiver mais seções, adicione a linha para remover a classe 'visible' delas aqui também:
            // detalhesMasterizacao.classList.remove('visible');


            // --> PASSO 2: MOSTRAR APENAS A SEÇÃO CORRETA <--
            // Pega o valor da opção que o usuário acabou de selecionar (ex: 'gravacao')
            const servicoSelecionado = tipoServicoSelect.value;

            // Verifica qual serviço foi selecionado e mostra A-P-E-N-A-S o campo correspondente
            if (servicoSelecionado === 'gravacao') {
                detalhesGravacao.classList.add('visible');
            } 
            else if (servicoSelecionado === 'mixagem') {
                detalhesMixagem.classList.add('visible');
            }
            // else if (servicoSelecionado === 'masterizacao') {
            //     detalhesMasterizacao.classList.add('visible');
            // }
        }

        // Adiciona o "escutador de eventos" que chama a nossa função sempre que o usuário
        // muda a opção no menu de serviços.
        tipoServicoSelect.addEventListener('change', atualizarFormulario);
    });
</script>
</body>
</html>