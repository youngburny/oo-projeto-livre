<!DOCTYPE html>
<html lang="en">
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
            <a href="/agendar">Agendar Sessão</a> </nav>
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
                <label for="telefone_cliente">Seu Telefone:</label>
                <input type="tel" id="telefone_cliente" name="telefone_cliente" placeholder="(XX) XXXXX-XXXX" />
            </div>

            <div class="form-group">
                <label for="tipo_servico">Tipo de Serviço:</label>
                <select id="tipo_servico" name="tipo_servico" required>
                    <option value="">Selecione um serviço</option>
                    <option value="gravacao">Gravação</option>
                    <option value="mixagem">Mixagem</option>
                    <option value="masterizacao">Masterização</option>
                    <option value="producao">Produção Musical</option>
                    <option value="outros">Outros (especifique nas observações)</option>
                </select>
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

            <div class="form-group">
                <label for="observacoes">Observações / Detalhes do Projeto:</label>
                <textarea id="observacoes" name="observacoes" rows="5" placeholder="Descreva brevemente seu projeto ou quaisquer requisitos especiais..."></textarea>
            </div>

            <div class="form-actions">
                <button type="submit">Agendar Sessão</button>
            </div>
        </form>
    </main>

    <footer>
        <p>&copy; 2025 Sonar Studio - All rights reserved.</p>
    </footer>
</body>
</html>