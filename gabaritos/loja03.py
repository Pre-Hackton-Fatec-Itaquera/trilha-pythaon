class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.carrinho = []
        self.produtos_no_carrinho = set()

    def pegar_compras(self, produtos_disponiveis):
        print(f"\nOlá, {self.nome}! Aproveite a loja!")

        while True:
            print("\n--- PRODUTOS DISPONÍVEIS ---")
            for produto, preco in produtos_disponiveis.items():
                print(f"{produto} - R$ {preco:.2f}")

            escolha = input(
                "\nDigite o nome do produto para adicionar ao carrinho "
                "ou digite 'finalizar': "
            ).lower()

            if escolha == "finalizar":
                break

            if escolha in produtos_disponiveis:
                produto = (escolha, produtos_disponiveis[escolha])
                self.carrinho.append(produto)
                self.produtos_no_carrinho.add(escolha)
                print(f"{escolha} foi adicionado ao carrinho!")
            else:
                print("Produto não encontrado. Tente novamente.")

    def pagar_compras(self):
        print("\n--- SEU CARRINHO ---")

        if len(self.carrinho) == 0:
            print("Seu carrinho está vazio.")
        else:
            total = 0
            for produto in self.carrinho:
                nome, preco = produto
                print(f"{nome} - R$ {preco:.2f}")
                total += preco

            print(f"\nTotal da compra: R$ {total:.2f}")
            print("\nProdutos diferentes no carrinho:")
            print(self.produtos_no_carrinho)

        print(f"\nObrigado pela compra, {self.nome}! Volte sempre!")


produtos = {
    "arroz": 25.00,
    "feijao": 8.00,
    "macarrao": 6.00,
    "leite": 5.50,
    "cafe": 12.00
}

decisao = input("Seja bem-vindo à Loja 03!\nDeseja ficar ou sair? Digite s ou n: ").lower()

while True:
    if decisao == "s":
        nome_usuario = input("Digite o seu nome para começar: ")
        cliente = Usuario(nome_usuario)
        
        cliente.pegar_compras(produtos)
        cliente.pagar_compras()
        break

    elif decisao == "n":
        print("Obrigado e tenha um ótimo descanso!")
        break

    else:
        print("Escolha uma das alternativas: s ou n")
        decisao = input("Deseja ficar ou sair? Digite s ou n: ").lower()