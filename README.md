# 🎧 Sonar Studio - Agendamento de Sessões

Este projeto é uma aplicação web para o agendamento de sessões em um estúdio de gravação, mixagem e masterização, desenvolvida como parte da disciplina de Orientação a Objetos. Utiliza o framework Python Bottle para o backend e foca em princípios de Orientação a Objetos, modelagem de dados e serialização.

## ✨ Funcionalidades

* Página inicial (Home) com informações sobre o estúdio.
* Formulário de agendamento de sessões com campos para detalhes do cliente e do serviço.
* **Em desenvolvimento:** Processamento e validação de dados do agendamento no backend.
* **Em desenvolvimento:** Persistência de dados de agendamento (serialização de objetos).

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar a aplicação localmente:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/youngburny/oo-projeto-livre
    cd oo-projeto-livre
    ```


2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```


4.  **Execute a aplicação:**
    ```bash
    python main.py
    ```

5.  **Acesse no navegador:**
    Abra seu navegador e acesse:
    * **Página Inicial:** `http://localhost:8080/` ou `http://localhost:8080/pagina`
    * **Agendar Sessão:** `http://localhost:8080/agendar`

---

**Desenvolvido por:** Bruno Souza Assis Furtado
**Disciplina:** Orientação a Objetos - Semestre 01/2025
**Professor:** Henrique Moura

# Observações

O projeto ainda está em desenvolvimento e não se encontra 100% completo. O repositório será enviado hoje (sexta-feira), mas o objetivo é finalizá-lo até o domingo solicitado.

**Status Atual**
As funcionalidades como o login/cadastro, verificação de sessões agendadas, e alguns itens interativos do site estão pendentes de implementação. 

**Próximos Passos**
Estou trabalhando para concluir as funcionalidades retratadas acima, e farei o upload das atualizações assim que estiverem prontas. A ideia é implementar as funções de login/cadastro, verificar as sessões agendadas, construir uma relação de herança, associações fracas e composição forte.