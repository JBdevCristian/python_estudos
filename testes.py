import os
from datetime import datetime

# Função para criar a pasta de atualizações na área de trabalho
def criar_pasta_atualizacao():
    pasta = os.path.expanduser('~/Desktop/ATUALIZAÇÃO DE PRODUTOS')  # Caminho exato para a área de trabalho do cliente
    if not os.path.exists(pasta):
        os.makedirs(pasta)

# Função para carregar produtos do arquivo
def carregar_produtos(arquivo_produtos):
    produtos = {}
    try:
        with open(arquivo_produtos, 'r') as file:
            linhas = file.readlines()

        for linha in linhas:
            if "Produto: " in linha:
                partes = linha.strip().split('|')
                nome_produto = partes[1].split(":")[1].strip().lower()  # Converter para minúsculas
                preco = float(partes[2].split(":")[1].strip().replace('R$', '').replace(',', '.'))
                quantidade = int(partes[3].split(":")[1].strip())
                validade = partes[4].split(":")[1].strip()
                estoque = quantidade * 2
                produtos[nome_produto] = {
                    'preco': preco,
                    'quantidade': quantidade,
                    'validade': validade,
                    'estoque': estoque
                }
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado. Iniciando com um cadastro vazio.")
    return produtos

# Função para registrar a atualização do produto em um arquivo
def registrar(nome_produto, preco, quantidade, validade, vendas, arquivo_produtos):
    # Cria a pasta de atualizações caso não exista
    criar_pasta_atualizacao()

    # Define o caminho do arquivo
    caminho_arquivo = os.path.join(os.path.expanduser('~/Desktop/ATUALIZAÇÃO DE PRODUTOS'), arquivo_produtos)

    # Abre o arquivo em modo append para adicionar as atualizações
    with open(caminho_arquivo, "a") as arquivo:
        # Formata os dados para gravação
        data_atualizacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        linha = f"{data_atualizacao} | Produto: {nome_produto} | Preço: R${preco:.2f} | Quantidade: {quantidade} | Validade: {validade} | Vendas: {vendas}\n"
        arquivo.write(linha)

# Função para cadastrar produtos
def cadastrar_produto(produtos, arquivo_produtos):
    nome = input("Digite o nome do produto: ")

    # Entrada do preço com vírgula
    preco_input = input("Digite o preço do produto (use ',' para decimais): ")
    preco = float(preco_input.replace(',', '.'))  # Substitui a vírgula por ponto

    quantidade = int(input("Digite a quantidade do produto: "))

    # Cadastrando validade
    validade = input("Digite a validade do produto (formato DD/MM/AAAA): ")

    # Cadastrando o estoque com o dobro da quantidade
    estoque = quantidade * 2

    produtos[nome] = {
        'preco': preco,
        'quantidade': quantidade,
        'validade': validade,
        'estoque': estoque
    }

    registrar(nome, preco, quantidade, validade, 0, arquivo_produtos)
    print(f"Produto '{nome}' cadastrado com sucesso!\n")

# Função para listar produtos cadastrados
def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.\n")
        return
    print("\nProdutos cadastrados:")
    for nome, detalhes in produtos.items():
        preco_formatado = f"{detalhes['preco']:.2f}".replace('.', ',')
        print(f"Nome: {nome}, Preço: R${preco_formatado}, "
              f"Quantidade: {detalhes['quantidade']}, Estoque: {detalhes['estoque']}, Validade: {detalhes['validade']}")
    print()  # Linha em branco para separar

# Função para atualizar um produto
def atualizar_produto(produtos, arquivo_produtos):
    nome = input("Digite o nome do produto que deseja atualizar: ").strip().lower()  # Convertendo para minúsculas

    if nome in produtos:
        # Exibir as informações atuais do produto
        produto = produtos[nome]
        print(f"\nProduto encontrado: {nome.title()}")
        print(f"Preço: R${produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Validade: {produto['validade']}")

        # Solicitar os novos dados para o produto
        preco_input = input("\nDigite o novo preço do produto (use ',' para decimais): ")
        preco = float(preco_input.replace(',', '.'))

        quantidade = int(input("Digite a nova quantidade do produto: "))
        validade = input("Digite a nova validade do produto (formato DD/MM/AAAA): ")

        # Atualiza o estoque com o dobro da nova quantidade
        estoque = quantidade * 2

        # Atualiza os dados do produto
        produtos[nome] = {
            'preco': preco,
            'quantidade': quantidade,
            'validade': validade,
            'estoque': estoque
        }

        # Registra a atualização no arquivo
        registrar(nome, preco, quantidade, validade, 0, arquivo_produtos)
        print(f"\nProduto '{nome}' atualizado com sucesso!\n")
    else:
        print("Produto não encontrado.\n")

# Função para remover um produto
def remover_produto(produtos, arquivo_produtos):
    nome = input("Digite o nome do produto que deseja remover: ")
    if nome in produtos:
        del produtos[nome]
        # Regrava os produtos restantes no arquivo
        with open(arquivo_produtos, 'w') as file:
            for nome_produto, detalhes in produtos.items():
                registrar(nome_produto, detalhes['preco'], detalhes['quantidade'], detalhes['validade'], 0, arquivo_produtos)
        print(f"Produto '{nome}' removido com sucesso!\n")
    else:
        print("Produto não encontrado.\n")

# Função para vender um produto
def vender_produto(produtos, arquivo_produtos):
    nome = input("Digite o nome do produto que deseja vender: ")
    if nome in produtos:
        quantidade_vendida = int(input("Digite a quantidade vendida: "))

        # Verifica se há estoque suficiente
        if quantidade_vendida <= produtos[nome]['estoque']:
            produtos[nome]['estoque'] -= quantidade_vendida  # Atualiza o estoque
            produtos[nome]['quantidade'] -= quantidade_vendida  # Atualiza a quantidade disponível

            # Registrar a venda no arquivo de atualizações
            registrar(nome, produtos[nome]['preco'], produtos[nome]['quantidade'], produtos[nome]['validade'], quantidade_vendida, arquivo_produtos)

            print(f"Venda de {quantidade_vendida} unidades do produto '{nome}' registrada com sucesso!\n")
        else:
            print("Estoque insuficiente para completar a venda.\n")
    else:
        print("Produto não encontrado.\n")

# Função principal
def main():
    arquivo_produtos = os.path.join(os.path.expanduser('~/Desktop/ATUALIZAÇÃO DE PRODUTOS'), 'atualizacao_produtos.txt')
    produtos = carregar_produtos(arquivo_produtos)

    while True:
        print("=== Gerenciamento de Produtos da Padaria ===")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Atualizar produto")
        print("4. Remover produto")
        print("5. Vender produto")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_produto(produtos, arquivo_produtos)
        elif opcao == '2':
            listar_produtos(produtos)
        elif opcao == '3':
            atualizar_produto(produtos, arquivo_produtos)
        elif opcao == '4':
            remover_produto(produtos, arquivo_produtos)
        elif opcao == '5':
            vender_produto(produtos, arquivo_produtos)
        elif opcao == '6':
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
