def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print("")
    if n % (m + 1) == 0 and m < n:
        print("Computador começa!")
        computador_escolhe_jogada(n,m)
    else:
        if n % (m+1) != 0 and m < n:
            print("Você começa!")
            usuario_escolhe_jogada(n,m)
        else:
            if m >= n or n <= 0:
                print("valores inválidos! tente novamente")
                partida()