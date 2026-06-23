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
            valor = float(input("Valor: R$"))
            break 
        except ValueError:
            print("❌ Erro: Digite apenas números (use ponto para centavos)!")

    data = input("Data (dd/mm/aaaa): ")
    categoria = input("Categoria (Ex:Renda extra, Bônus): ")
    status = input("Status (Recebido/Pendente): ")
    #3 Cria o "Pacote de dados (dicionario)"
    nova_receita = {
        "descricao": nome, 
        "valor": valor,
        "data": data,
        "categoria": categoria,
        "status": status
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
        "descricao": nome, 
        "valor": valor,
        "data": data,
        "categoria": categoria,
        "status": status
        }

    lista_despesas.append(nova_despesa)
    salvar_dados()#salva os dados no pc
    print(f"Receita'{nome}' guardada com sucesso!")

def exibir_geral():
    total_receitas = sum(r["valor"] for r in lista_receitas)
    total_despesas = sum(d["valor"] for d in lista_despesas)
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

def limpar_dados():#funcao para limpar os dados salvos, vai sobrescrever o arquivo antigo, com um limpo por cima.
    confirmacao = input("⚠️ Tem certeza que deseja apagar TUDO? (s/n): ").lower()
    if confirmacao == 's':
        lista_receitas.clear()
        lista_despesas.clear()
        salvar_dados() # Isso sobrescreve o arquivo com as listas vazias
        print("\n🧹 Sistema resetado com sucesso!")
    else:
        print("\nAção cancelada.")