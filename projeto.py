#1 lista global para guardar tudo
lista_receitas = []
lista_despesas = []

#2 funcao fora do while
def adicionar_receita():
    print("\n--- Cadastro de Receita ---")
    nome = input("Digite a descricao (ex: Salario): ")
    valor = float(input("Digite o valor: R$"))

    #3 Cria o "Pacote de dados (dicionario)"
    nova_receita = {"Descrição": nome, "Valor R$": valor}

    #4 Guarda o pacote na lista
    lista_receitas.append(nova_receita)
    print(f"Receita '{nome}' guardada com sucesso!")

def adicionar_despesa():
    print("\n--- Cadastro de Despesa ---")
    nome = input("Digite a descricao (ex: Compras): ")
    valor = float(input("Digite o valor: R$"))

    nova_despesa = {"Descrição": nome, "Valor R$": valor}

    lista_despesas.append(nova_despesa)
    print(f"Receita'{nome}' guardada com sucesso!")

def exibir_geral():
    total_receitas = sum(r["Valor R$"] for r in lista_receitas)
    total_despesas = sum(d["Valor R$"] for d in lista_despesas)
    saldo = total_receitas - total_despesas
    
    print("\n=== BALANÇO GERAL ===")
    print(f"Total de Entradas: R${total_receitas:.2f}")
    print(f"Total de Saídas:   R${total_despesas:.2f}")
    print(f"Saldo em Conta:    R${saldo:.2f}")

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