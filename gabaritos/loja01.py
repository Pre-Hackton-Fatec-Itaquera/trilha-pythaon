decisao = input("Seja bem-vindo à loja 01!\nDeseja ficar ou sair? Digite s ou n: ")

while True:
    if decisao == "s":
        print("Aproveite a loja!")
        break

    elif decisao == "n":
        print("Obrigado e tenha um ótimo descanso!")
        break

    else:
        print("Escolha uma das alternativas: s ou n")
        decisao = input("Deseja ficar ou sair? Digite s ou n: ")
