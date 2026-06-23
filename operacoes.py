import json
import os # Para verificar se o arquivo já existe

#1 lista global para guardar tudo
lista_receitas = []
lista_despesas = [] #lista dicionarios, ele estica e adiciona mais uma.
limites_categorias = {} #Já esse ele pega o valor e substui e carrega do JSON.

def configurar_limites():
    print("\n--- CONFIGURAÇÃO DE LIMITES ---")
    categoria = input("Digite a categoria (ex: lazer, compras): ").lower()
    
    while True:
        try:
            valor_limite = float(input(f"Defina o limite mensal para {categoria}: R$ "))
            break
        except ValueError:
            print("❌ Erro: Digite um valor numérico válido!")
    
    # Atualiza o dicionário de limites
    limites_categorias[categoria] = valor_limite
    salvar_dados() # Salva a nova configuração no disco
    print(f"✅ Limite de R$ {valor_limite:.2f} definido para '{categoria}'!")

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
     # Lógica de aviso de orçamento
    categoria_atual = categoria.lower()
    if categoria_atual in limites_categorias:
        # Somamos tudo o que já gastamos nessa categoria específica
        total_gasto = sum(d['valor'] for d in lista_despesas if d['categoria'].lower() == categoria_atual)
        limite = limites_categorias[categoria_atual]

        if total_gasto > limite:
            print(f"\n⚠️ ATENÇÃO: Você ultrapassou o limite de {categoria_atual}!")
            print(f"Limite: R$ {limite:.2f} | Gasto Atual: R$ {total_gasto:.2f}")
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
            # 2. Carrega os limites (usando .update para dicionários)
            # O segundo parâmetro {} garante que, se não houver limites salvos, ele não dê erro
            limites_categorias.update(dados.get("limites", {}))
        print("\n✅ Dados carregados do disco!")

def salvar_dados():#funcao para salvar os dados dos clientes.
    dados = {
        "receitas": lista_receitas,
        "despesas": lista_despesas,
        "limites": limites_categorias
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