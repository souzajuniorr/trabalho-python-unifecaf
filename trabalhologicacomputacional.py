# --- TRABALHO DE LÓGICA COMPUTACIONAL - UNIFECAF ---
# Sistema de Estoque para Loja de Eletrônicos

# Criando o dicionário vazio para guardar os produtos
estoque = {}

while True:
    # Menu simples e claro
    print("\n--- MENU DA LOJA ---")
    print("1 - Adicionar Produto")
    print("2 - Atualizar Produto")
    print("3 - Excluir Produto")
    print("4 - Visualizar Estoque")
    print("5 - Sair")
    
    opcao = input("Escolha o que deseja fazer: ")

    # 1. ADICIONAR PRODUTO
    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        
        # Verificando se o campo está vazio (exigência do professor)
        if nome == "":
            print("Erro: Você não digitou o nome!")
        else:
            preco = float(input("Digite o preço: R$ "))
            quantidade = int(input("Digite a quantidade: "))
            
            # Guarda no dicionário
            estoque[nome] = [preco, quantidade]
            print("Produto cadastrado com sucesso!")

    # 2. ATUALIZAR PRODUTO
    elif opcao == "2":
        nome_busca = input("Qual o nome do produto para atualizar? ")
        
        if nome_busca in estoque:
            novo_preco = float(input("Novo preço: R$ "))
            nova_qtd = int(input("Nova quantidade: "))
            
            # Atualiza os dados
            estoque[nome_busca] = [novo_preco, nova_qtd]
            print("Produto atualizado!")
        else:
            print("Aviso: Produto não encontrado.")

    # 3. EXCLUIR PRODUTO
    elif opcao == "3":
        nome_apagar = input("Digite o nome do produto para excluir: ")
        
        if nome_apagar in estoque:
            del estoque[nome_apagar]
            print("Produto removido!")
        else:
            print("Erro: Esse produto não existe.")

    # 4. VISUALIZAR ESTOQUE
    elif opcao == "4":
        print("\n--- LISTA DE PRODUTOS NO ESTOQUE ---")
        
        if estoque == {}:
            print("O estoque está vazio no momento.")
        else:
            # Usando o loop FOR para mostrar os itens (exigência do professor)
            for produto in estoque:
                detalhes = estoque[produto]
                print("Nome:", produto, "- Preço: R$", detalhes[0], "- Qtd:", detalhes[1])

    # 5. SAIR
    elif opcao == "5":
        print("Saindo do programa...")
        break # Para o loop while

    else:
        print("Opção inválida, tente de 1 a 5.")
        