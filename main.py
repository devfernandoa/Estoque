import json

import sys, os

limpar = lambda: os.system('cls')

with open("estoque.json", "r") as json_file:
    estoque = json.load(json_file)

while True:
    print("\n")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Alterar produto")
    print("4 - Listar produtos")
    print("5 - Sair")
    print("\n")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        limpar()
        produto = input("Digite o nome do produto: ")
        if produto in estoque:
            print("Produto já em estoque")
            continue 
        quantidade = int(input("Digite a quantidade do produto: "))
        preco = float(input("Digite o preço do produto: "))
        estoque[produto] = {"quantidade": quantidade, "preco": preco}
        with open("estoque.json", "w") as json_file:
            json.dump(estoque, json_file)
    elif opcao == 2:
        limpar()
        produto = input("Digite o nome do produto: ")
        if produto not in estoque:
            print("Produto não encontrado")
            continue 
        del estoque[produto]
        with open("estoque.json", "w") as json_file:
            json.dump(estoque, json_file)
    elif opcao == 3:
        limpar()
        produto = input("Digite o nome do produto: ")
        if produto not in estoque:
            print("Produto não encontrado")
            continue 
        quantidade = int(input("Digite a quantidade que foi adicionada ou reduzida: "))
        preco = float(input("Digite o preço do produto: "))
        estoque[produto]["quantidade"] += quantidade
        estoque[produto]["preco"] = preco
        with open("estoque.json", "w") as json_file:
            json.dump(estoque, json_file)
            
    elif opcao == 4:
        limpar()
        for produto in estoque:
            print("\n")
            print(produto)
            print("Quantidade: ", estoque[produto]["quantidade"])
            print("Preço: R$", estoque[produto]["preco"])
    elif opcao == 5:
        limpar()
        break