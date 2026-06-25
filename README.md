#  ModularFinance: Gestão Financeira Modular (Python)

Este é um protótipo funcional de um software para gerenciamento de finanças pessoais, desenvolvido como projeto acadêmico no **Eniac**. O objetivo principal foi criar uma aplicação de back-end robusta, utilizando persistência de dados, tratamento de erros e uma arquitetura modular.

##  Funcionalidades

*   **Controle de Transações:** Cadastro detalhado de receitas e despesas com descrição, valor, data, categoria e status.
*   **Dashboard em Tempo Real:** Cálculo automático de saldo total, somatório de receitas e somatório de despesas.
*   **Persistência em JSON:** Todos os dados são gravados no arquivo `dados_financeiros.json`, permitindo fechar e abrir o programa sem perder informações.
*   **Gestão Orçamentária:** Sistema de configuração de limites por categoria. O software emite alertas caso um gasto ultrapasse o teto definido pelo usuário.
*   **Validação de Entradas:** Uso de blocos `try-except` para garantir que o sistema não trave caso o usuário digite valores inválidos (como letras em campos de valor).
*   **Extrato Formatado:** Visualização organizada das movimentações com separadores visuais para melhor experiência do usuário (UX).

##  Tecnologias Utilizadas

*   **Python 3.x**
*   **JSON** (Estrutura de banco de dados local)
*   **Git/GitHub** (Versionamento e colaboração)

##  Estrutura do Projeto

O código segue padrões profissionais de **modularização**:

*   `main.py`: Ponto de entrada do sistema, contendo a lógica do menu interativo e interface com o usuário.
*   `operacoes.py`: Módulo que concentra a lógica de negócio, funções de cálculo e manipulação do arquivo JSON.
*   `dados_financeiros.json`: Base de dados local do sistema.
*   `.gitignore`: Configurado para ignorar arquivos de cache como `__pycache__`, mantendo o repositório limpo.

---

##  Demonstração do Terminal

### 1. Menu Principal
![Menu Principal](img/menu.png)

---

### 2. Exibição de Extrato Detalhado
![Exibição de Extrato](img/extrato.png)

---

### 3. Alerta de Limite Ultrapassado
![Alerta de Limite Ultrapassado](img/limite.png)

---

##  Minha Participação Específica

Como responsável pela **lógica central e back-end**, minhas principais contribuições técnicas foram:

1.  **Arquitetura de Dados:** Estruturei o fluxo de informações utilizando listas e dicionários integrados a um arquivo JSON para persistência permanente.
2.  **Mecanismos de Segurança:** Implementei o tratamento de exceções para validar entradas numéricas, impedindo falhas críticas no software.
3.  **Modularização:** Separei a interface (UI) da lógica de processamento, facilitando a manutenção e futura escalabilidade para uma API (como FastAPI).
4.  **Lógica de Monitoramento:** Desenvolvi a função de alerta de limites, cruzando dados de despesas com o orçamento definido pelo usuário.
5.  **Governança de Código:** Gerenciei o repositório via Git, garantindo um histórico de commits organizado e um ambiente de desenvolvimento limpo.

##  Como executar o projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/rebelosx/projeto.git
Acesse a pasta:
Inicie o sistema:

---