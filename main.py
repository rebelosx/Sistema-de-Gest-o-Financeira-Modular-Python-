from operacoes import * # Isso "puxa" tudo o que tem no outro arquivo
carregar_dados() #carrega os dados, já salvos!

#loop do menu
while True:
    print("\n" + "="*30)
    print("   SISTEMA DE GESTÃO FINANCEIRA")
    print("="*30)
    print("1 - Adicionar Receita")
    print("2 - Adicionar Despesa")
    print("3 - Ver Extrato Detalhado")
    print("4 - Ver Balanço Geral (Dashboard)")
    print("5 - LIMPAR TODOS OS DADOS")
    print("6 - CONFIGURAR LIMITES POR CATEGORIA")
    print("sair - Encerrar")
    
    opcao = input("\nEscolha uma opção: ").lower().strip() # .lower transforma tudo em minusculo e.strip() remove espaços extras

    if opcao == "1":
        adicionar_receita()
    elif opcao == "2":
        adicionar_despesa()
    elif opcao == "3":
        print("\n" + "-"*40)
        print("         EXTRATO DETALHADO")
        print("-"*40)
        
        print("\n--- RECEITAS ---")
        if not lista_receitas:
            print("Nenhuma receita cadastrada.")
        for r in lista_receitas:
            # Usamos as chaves do dicionário para imprimir bonitinho
            print(f"Data: {r['data']} | {r['descricao']}: R$ {r['valor']:.2f} ({r['categoria']})")

        print("\n--- DESPESAS ---")
        if not lista_despesas:
            print("Nenhuma despesa cadastrada.")
        for d in lista_despesas:
            print(f"Data: {d['data']} | {d['descricao']}: R$ {d['valor']:.2f} ({d['categoria']})")
        print("-"*40)
    elif opcao == "4":
        exibir_geral()
    elif opcao == "5":
        limpar_dados() # Chama funcao de reset
    elif opcao == "6":
        configurar_limites()
    elif opcao == "sair":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida!")