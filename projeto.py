import json
import os # Para verificar se o arquivo já existe

#1 lista global para guardar tudo
lista_receitas = []
lista_despesas = []

#2 funcao fora do while
def adicionar_receita():
    print("\n--- Cadastro de Receita ---")
    nome = input("Digite a descricao (ex: Salario): ")
    while True:
        try:
            valor = float(input("Valor: R$ "))
            break 
        except ValueError:
            print("❌ Erro: Digite apenas números (use ponto para centavos)!")

    data = input("Data (dd/mm/aaaa): ")
    categoria = input("Categoria (Ex:Renda extra, Bônus): ")
    status = input("Status (Recebido/Pendente): ")
    #3 Cria o "Pacote de dados (dicionario)"
    nova_receita = {
        "Descrição": nome, 
        "Valor": valor,
        "Data": data,
        "Categoria": categoria,
        "Status": status
        }

    #4 Guarda o pacote na lista
    lista_receitas.append(nova_receita)
    salvar_dados()#salva os dados no pc
    print(f"Receita '{nome}' guardada com sucesso!")

def adicionar_despesa():
    print("\n--- Cadastro de Despesa ---")
    nome = input("Digite a descricao (ex: Compras): ")
    # loop que só para quando o valor for válido
    while True:
        try:
            valor = float(input("Valor: R$ "))
            break  # Se chegou aqui sem erro, sai do loop do 'valor' e segue a função
        except ValueError:
            print("❌ Erro: Digite apenas números (use ponto para centavos)!")
            # Como não tem 'return' aqui, ele volta para o início do 'while True'
    
    # Após o loop garantir um valor correto, o restante da função continua...
    data = input("Data (dd/mm/aaaa): ")
    categoria = input("Categoria (ex: Moradia, Alimentação): ")
    status = input("Status (Pago/Pendente): ")

    nova_despesa = {
        "Descrição": nome, 
        "Valor": valor,
        "Data": data,
        "Categoria": categoria,
        "Status": status
        }

    lista_despesas.append(nova_despesa)
    salvar_dados()#salva os dados no pc
    print(f"Receita'{nome}' guardada com sucesso!")

def exibir_geral():
    total_receitas = sum(r["Valor R$"] for r in lista_receitas)
    total_despesas = sum(d["Valor R$"] for d in lista_despesas)
    saldo = total_receitas - total_despesas
    
    print("\n=== BALANÇO GERAL ===")
    print(f"Total de Entradas: R${total_receitas:.2f}")
    print(f"Total de Saídas:   R${total_despesas:.2f}")
    print(f"Saldo em Conta:    R${saldo:.2f}")

def carregar_dados():#funcao para puxar os dados já salvos.
    if os.path.exists("dados_financeiros.json"):
        with open("dados_financeiros.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            # Atualiza as listas globais com o que estava salvo
            lista_receitas.extend(dados.get("receitas", []))
            lista_despesas.extend(dados.get("despesas", []))
        print("\n✅ Dados carregados do disco!")

def salvar_dados():#funcao para salvar os dados dos clientes.
    dados = {
        "receitas": lista_receitas,
        "despesas": lista_despesas
    }
    with open("dados_financeiros.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    print("\n💾 Dados salvos com sucesso no arquivo!")

carregar_dados() #carrega os dados, já salvos!

#loop do menu
while True:

    print("\n--- SISTEMA FINANCEIRO ---")
    print("1 - Adicionar Receita")
    print("2 - Ver todas as Receitas")
    print("3 - Adicionar Despesas")
    print("4 - Ver todas as Despesas")
    print("5 - Ver o GERAL")
    print("sair - Encerrar programa")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        adicionar_receita() # Aqui chamamos a função!
    
    elif opcao == "2":
        print("\nLista de Receitas:")
        for r in lista_receitas:
            print(f"Descrição: {r['Descrição']} | Valor: R${r['Valor R$']:.2f}") # Mostra o que tem na lista
        
    elif opcao == "3":
        adicionar_despesa()

    elif opcao == "4":
        print("\nLista de Despesas")
        for r in lista_despesas:
            print(f"Descrição: {r['Descrição']} | Valor: R${r['Valor R$']:.2f}")

    elif opcao == "5":
        exibir_geral()

    elif opcao == "sair":
        print("Programa encerrado.")
        break # Sai do loop
    
    else:
        print("Opção inválida, tente novamente.")