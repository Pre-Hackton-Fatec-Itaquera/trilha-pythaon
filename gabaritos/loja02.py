decisao = input("Seja bem-vindo à Loja 02!\nDeseja ficar ou sair? Digite s ou n: ")

produtos = {
    "arroz": 25.00,
    "feijao": 8.00,
    "macarrao": 6.00,
    "leite": 5.50,
    "cafe": 12.00
}

carrinho = []

produtos_no_carrinho = set()

while True:

    if decisao == "s":
        print("\nAproveite a loja!")

        while True:
            print("\n--- PRODUTOS DISPONÍVEIS ---")

            for produto, preco in produtos.items():
                print(f"{produto} - R$ {preco:.2f}")

            escolha = input(
                "\nDigite o nome do produto para adicionar ao carrinho "
                "ou digite 'finalizar': "
            ).lower()

            if escolha == "finalizar":
                break

            if escolha in produtos:

                produto = (escolha, produtos[escolha])

                carrinho.append(produto)

                produtos_no_carrinho.add(escolha)

                print(f"{escolha} foi adicionado ao carrinho!")

            else:
                print("Produto não encontrado. Tente novamente.")

        print("\n--- SEU CARRINHO ---")

        if len(carrinho) == 0:
            print("Seu carrinho está vazio.")

        else:
            total = 0

            for produto in carrinho:
                nome, preco = produto
                print(f"{nome} - R$ {preco:.2f}")
                total += preco

            print(f"\nTotal da compra: R$ {total:.2f}")

            print("\nProdutos diferentes no carrinho:")
            print(produtos_no_carrinho)

        print("\nObrigado pela compra! Volte sempre!")
        break

    elif decisao == "n":
        print("Obrigado e tenha um ótimo descanso!")
        break

    else:
        print("Escolha uma das alternativas: s ou n")
        decisao = input("Deseja ficar ou sair? Digite s ou n: ").lower()
