### Sistema de Gestão Financeira Modular (Python)
Este é um protótipo funcional de um software para gerenciamento de finanças pessoais, desenvolvido como projeto acadêmico no Eniac. O objetivo principal foi criar uma aplicação de back-end robusta, utilizando persistência de dados, tratamento de erros e uma arquitetura modular
.
### Funcionalidades
Controle de Transações: Cadastro detalhado de receitas e despesas com descrição, valor, data, categoria e status
.
Dashboard em Tempo Real: Cálculo automático de saldo total, somatório de receitas e despesas
.
Persistência em JSON: Todos os dados são gravados no arquivo dados_financeiros.json, permitindo fechar e abrir o programa sem perder informações
.
Gestão Orçamentária: Sistema de configuração de limites por categoria. O software emite alertas caso um gasto ultrapasse o teto definido pelo usuário
.
Validação de Entradas: Uso de blocos try-except para garantir que o sistema não trave caso o usuário digite valores inválidos
.
Extrato Formatado: Visualização organizada das movimentações com separadores visuais para melhor experiência do usuário (UX).
### Tecnologias Utilizadas
Python 3.x
JSON (para armazenamento estruturado de dados)
Git/GitHub (para controle de versão e colaboração)
### Estrutura do Projeto
O código foi refatorado seguindo padrões profissionais de modularização
:
main.py: Ponto de entrada do sistema, contendo a lógica do menu interativo e interface com o usuário
.
operacoes.py: Módulo que concentra a lógica de negócio, funções de cálculo, e manipulação do arquivo JSON
.
dados_financeiros.json: Base de dados local do sistema
.
.gitignore: Configurado para manter o repositório limpo, ignorando arquivos de cache como __pycache__
.
📸 Demonstração do Terminal
## Menu Principal
![Menu Principal](menu.png)
---
## Exibição de Extrato Detalhado
![Exibição de Extrato](extrato.png)
---
## Alerta de Limite Ultrapassado
![Alerta de Limite Ultrapassado](limite.png)
## Minha Participação Específica
Como responsável pela lógica central e back-end, minhas principais contribuições técnicas foram:
Desenvolvimento da Arquitetura de Dados: Estruturei o fluxo de informações utilizando listas e dicionários integrados a um arquivo JSON para garantir a persistência dos dados
.
Implementação de Segurança: Criei os mecanismos de tratamento de exceções para validar entradas numéricas, impedindo falhas críticas no software
.
Refatoração para Módulos: Separei a interface da lógica de processamento (Modularização), facilitando a manutenção e futura escalabilidade para uma API
.
Lógica de Alertas: Desenvolvi a função de monitoramento de limites de gastos por categoria, uma funcionalidade essencial para gestão financeira real
.
Versionamento Profissional: Gerenciei o repositório utilizando Git, garantindo um histórico de commits organizado e a limpeza do ambiente via .gitignore
.
# Como executar o projeto
Clone o repositório:
Acesse a pasta:
Inicie o sistema: